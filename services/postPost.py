import pyrebase
import os
from dotenv import load_dotenv
import datetime
import uuid

load_dotenv()

firebaseConfig = {
    'apiKey': os.getenv('FIREBASE_API_KEY'),
    'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
    'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    'appId': os.getenv('FIREBASE_APP_ID'),
    'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID')
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


def postPost(restaurant_id, food_name, item_quantity, claimer, status):
    unique_id = str(uuid.uuid4())
    post_id = f"{restaurant_id}_{unique_id}"

    data = {
        'food': {
            'name': food_name,
            'quantity': item_quantity
        },
        'claimer': claimer,
        'status': status
    }

    db.child('restaurants').child(restaurant_id).child('posts').child(post_id).update(data)

    return post_id


# def claim_post(restaurant_id, post_id, claimer):
#     db.child('restaurants').child(restaurant_id).child('posts').child(post_id).update({'claimer': claimer})

#     return "Post claimed successfully"


# def update_status(restaurant_id, post_id, status):
#     db.child('restaurants').child(restaurant_id).child('posts').child(post_id).update({'status': status})

#     return "Status updated successfully"