from django.shortcuts import render
import pyrebase
# Create your views here.

firebaseConfig={
    'apiKey': "AIzaSyBnByXDSg3vSCLtLZd0HLoJRBiZOQLzS-o",
    'authDomain': "musicapp-2e4ed.firebaseapp.com",
    'projectId': "musicapp-2e4ed",
    'storageBucket': "musicapp-2e4ed.appspot.com",
    'messagingSenderId': "212672843199",
    'appId': "1:212672843199:web:d807d5e1368a6f4e0e650a"
}

firebase=pyrebase.initialize_app(firebaseConfig)

# db=firebase.database()
auth=firebase.auth()
# storage=firebase.storage()

# login
email=input("enter your email")
password=input("enter your password")
auth.sign_in_with_email_and_password(email, password)

