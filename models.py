from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

# Users Model
class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone =  db.Column(db.String(14), nullable=False)
    username = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(14), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False)
    register_date = db.Column(db.DateTime)

    def __init__(self, firstname, lastname, email, phone, username, password, register_date):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password
        self.register_date = register_date

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'firstname', 'lastname', 'email', 'phone', 'username', 'role_id', 'register_date')
        exclude = ('password')

# Init Schema
User_schema = UserSchema()
Users_schema = UserSchema(many=True)