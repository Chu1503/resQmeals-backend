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

def fetchFood():
    restaurants_dict = db.child('restaurants').get().val()
    restaurants = []

    if restaurants_dict is not None:
        for restaurant_name, restaurant_data in restaurants_dict.items():
            if 'posts' in restaurant_data:
                for post_id, post_data in restaurant_data['posts'].items():
                    food_item = post_data.get('food')
                    claimer = post_data.get('claimer')
                    if food_item and isinstance(food_item, dict):
                        food_type = food_item.get('name', '')
                        quantity = food_item.get('quantity', '')
                        restaurant_details = {
                            'restaurant_name': restaurant_name,
                            'food_type': food_type,
                            'quantity': quantity,
                            'claimer': claimer
                        }
                        restaurants.append(restaurant_details)

    return restaurants
