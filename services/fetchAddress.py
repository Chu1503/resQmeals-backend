import pyrebase
import os
from dotenv import load_dotenv
import datetime

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

def fetchAddress(claimer):
    address_pairs = []

    restaurants = db.child('restaurants').get().val()
    if restaurants:
        for restaurant_id, restaurant_details in restaurants.items():
            seller_address = restaurant_details.get('address')

            if claimer:
                user_details = db.child('users').child(claimer).get().val()
                buyer_address = user_details.get('buyer_address')
            else:
                buyer_address = None

            address_pairs.append({'seller_address': seller_address, 'buyer_address': buyer_address})

    return address_pairs

