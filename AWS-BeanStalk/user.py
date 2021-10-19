# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash


# class User(UserMixin):

#     def __init__(self, id,password):
#         self.id = id
#         self.password = generate_password_hash(password)
        

#     def set_password(self, password):
#         self.password = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password, password)

#     def __repr__(self):
#         return '<User {}>'.format(self.id)

# users = []
# user=User()
# def get_user(id):
#     for user in users:
#         if user.id == id:
#             return user
#     return None