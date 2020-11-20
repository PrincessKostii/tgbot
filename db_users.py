from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)

db = client['tgbot']


def check_and_add_user(message):
        new_user = {
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'user_id': message.from_user.id,
            'message': message.text,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        db.users.insert_one(new_user)