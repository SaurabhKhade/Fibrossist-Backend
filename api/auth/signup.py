from datetime import datetime
import random
import smtplib
from flask import request, abort
from functions.validation import invalid_signup
from database.db import db
import json
from functions.otp_mail import mail
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def signup():

    try:
        if request.method == 'OPTIONS':
            return {"status": 200, "message": "OK"}, 200
        if request.method == 'GET':
            return {"status": 200, "message": "Expected request structure",
                    "data": {
                        "email": "string",
                        "password": "string",
                        "name": "string",
                        "surname": "string",
                        "age": "number",
                        "gender": "string (M, F or O)"
                    }}, 200
        data = request.data

        # handling invalid data
        if len(data) == 0:
            return {"status": 400, "message": "No data provided"}, 400

        data = json.loads(data.decode('utf-8'))
        users = db["auth"]

        if invalid_signup(data):
            return {"status": 400, "message": invalid_signup(data)}, 400

        # if user already exists, convey so, if not create user
        user = users.find_one({"email": data["email"]})

        if user:
            return {"status": 409, "message": "User with this email already exists"}, 409
        else:
            send_otp(data)
            return {"status": 200, "message": "Please verify your email to continue."}, 200

    except Exception as e:
        print("\n\n", str(e), "\n\n")
        if ("duplicate key error" in str(e) and "FibrossistCluster.otp" in str(e)):
            return {"status": 200, "message": "OTP sent already. Please verify your email."}, 200
        abort(500)


def send_otp(data):
    otp = db["otp"]
    random_otp = random.randint(100000, 999999)
    otp.insert_one({"email": data["email"], "otp": random_otp,
                   "createdAt": datetime.utcnow(), "data": json.dumps(data)})

    # smtp = smtplib.SMTP('send.smtp.mailtrap.io', 587)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    # smtp.login("api", "b2d9d201511ed5c45dd7bdf0e22da8f7")
    sender = os.environ.get("MAIL_USER")
    receiver = data["email"]
    password = os.environ.get("MAIL_PASS")
    smtp.login(sender, password)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Verify your email to start using Fibrossist"
    msg['From'] = os.environ.get("MAIL_USER")
    msg['To'] = receiver

    body = MIMEText(mail(data, random_otp, os.environ.get("HOST")), 'html')
    msg.attach(body)

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
