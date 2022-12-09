from flask import request, abort
from database.db import db
from datetime import datetime
import smtplib
import random
from functions.otp_mail import otp_mail as mail
import os
import json
from functions.crypto import hash

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_otp():
    try:
        if request.method == 'OPTIONS':
            return {"status": 200, "message": "OK"}, 200
        email = json.loads(request.data.decode('utf-8'))["email"]
        otp = random.randint(100000, 999999)
        opt_db = db["otp"]
        users = db["auth"]
        user = users.find_one({"email": email})
        if user:
            opt_db.insert_one({"email": email, "otp": otp,
                              "createdAt": datetime.utcnow()})
            send_mail(email, otp)
            return {"status": 200, "message": "OTP sent successfully"}, 200
        else:
            return {"status": 404, "message": "User not found"}, 404

    except Exception as e:
        print(e)
        if ("duplicate key error" in str(e) and "FibrossistCluster.otp" in str(e)):
            return {"status": 200, "message": "OTP sent successfully"}, 200
        abort(500)


def verify_otp():
    try:
        if request.method == 'OPTIONS':
            return {"status": 200, "message": "OK"}, 200
        data = json.loads(request.data.decode('utf-8'))
        otp = db["otp"]
        users = db["auth"]

        otp_in_db = otp.find_one(
            {"email": data["email"], "otp": int(data["otp"])}
        )
        if (otp_in_db):
            otp.delete_one({"email": data["email"]})
            password = hash(data["password"])
            users.update_one({"email": data["email"]}, {
                             "$set": {"password": password}})
            return {"status": 200, "message": "Password changed successfully"}, 200
        else:
            return {"status": 400, "message": "Invalid OTP"}, 400

    except Exception as e:
        print(e)
        abort(500)


def send_mail(email, otp):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    sender = os.environ.get("MAIL_USER")
    password = os.environ.get("MAIL_PASS")
    receiver = email
    smtp.login(sender, password)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Verify your email to recover your account"
    msg['From'] = os.environ.get("MAIL_USER")
    msg['To'] = receiver

    body = MIMEText(mail(otp), 'html')
    msg.attach(body)

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
