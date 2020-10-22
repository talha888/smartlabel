from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://talha:ali@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =  SQLAlchemy(app)

class User(db.Model):
   UserID = db.Column(db.Integer, primary_key = True)
   Email= db.Column(db.String(80))
   Password =  db.Column(db.String(255))
   MemberShipRole =  db.Column(db.Boolean)
   
def token_required(f):
   @wraps(f)
   def decorated(*args, **kwargs):
      token = None

      if 'x-access-token' in request.headers:
         token = request.headers['x-access-token']
      
      if not token:
         return jsonify({'message':'Token is missing'}), 401

      try:
         data = jwt.decode(token, app.config['SECRET_KEY'])
         current_user = User.query.filter_by(UserID=data['UserID']).first()
      except:
         return jsonify({'message':'Token is missing'}), 401
      
      return f(current_user, *args, **kwargs)
   
   return decorated


@app.route('/user', methods=['GET'])
@token_required
def get_all_user(current_user):

   if not current_user.MemberShipRole:
      return jsonify({'message': 'cannot perform that function, only admin allowed'})
   users = User.query.all()

   output = []
   for user in users:
      user_data = {}
      user_data['UserID'] = user.UserID
      user_data['Email'] = user.Email
      user_data['Password'] = user.Password
      user_data['MemberShipRole'] = user.MemberShipRole
      output.append(user_data)

   return jsonify({'user': output})


@app.route('/user/<UserID>', methods=['GET'])
@token_required
def get_one_user(current_user,UserID):

   if not current_user.MemberShipRole:
      return jsonify({'message': 'cannot perform that function, only admin allowed'})

   user = User.query.filter_by(UserID=UserID).first()

   if not user:
         return jsonify({'message':'No user Found'})

   user_data = {}
   user_data['UserID'] = user.UserID
   user_data['Email'] = user.Email
   user_data['Password'] = user.Password
   user_data['MemberShipRole'] = user.MemberShipRole

   return jsonify({'user': user_data})


@app.route('/user', methods=['POST'])
@token_required
def create_user(current_user):

   if not current_user.MemberShipRole:
      return jsonify({'message': 'cannot perform that function, only admin allowed'})

   data = request.get_json()
   
   user = User.query.filter_by(Email=data['Email']).first()

   if user:
      return jsonify({'message': 'user already exist'})

   hashed_password = generate_password_hash(data['Password'],method='md5')

   new_user = User(Email=data['Email'], Password=hashed_password, MemberShipRole = True)
   db.session.add(new_user)
   db.session.commit()
   
   return jsonify({'message':'new user created!'})


@app.route('/user/<UserID>', methods=['PUT'])
@token_required
def promote_user(current_user, UserID):

   if not current_user.MemberShipRole:
      return jsonify({'message': 'cannot perform that function, only admin allowed'})

   user = User.query.filter_by(UserID=UserID).first()

   if not user:
         return jsonify({'message':'No user Found'})
   user.MemberShipRole = True
   db.session.commit()

   return jsonify({'message': 'User has been promoted'})


@app.route('/user/<UserID>', methods=['DELETE'])
@token_required
def delete_user(current_user, UserID):

   if not current_user.MemberShipRole:
      return jsonify({'message': 'cannot perform that function, only admin allowed'})
   
   user = User.query.filter_by(UserID=UserID).first()

   if not user:
         return jsonify({'message':'No user Found'})
 
   db.session.delete(user)
   db.session.commit()

   return jsonify({'message': 'User has been Deleted'})


@app.route('/login')
def login():
   auth = request.authorization
   
   if not auth or not auth.username or not auth.password:
      return make_response('Could not verify ', 401 , {'WWW-Authenticate':'Basic realm = "Login required"'})

   user = User.query.filter_by(Email=auth.username).first()

   if not user:
      return make_response('Could not verify ', 401 , {'WWW-Authenticate':'Basic realm = "Login required"'})

   if check_password_hash(user.Password, auth.password):
      token =jwt.encode({'UserID': user.UserID,'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

      return jsonify({'token': token.decode('UTF-8')})
   
   return make_response('Could not verify ', 401 , {'WWW-Authenticate':'Basic realm = "Login required"'})

if __name__ ==  '__main__':
   app.run(debug=True)