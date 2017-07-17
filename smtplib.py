from flask import Flask, url_for, render_template, redirect, current_app
from email.mime.text import MIMEText
import smtplib
from itsdangerous import URLSafeTimedSerializer


def send_email(email):
	from_email = current_app.config['FROM_EMAIL']
	from_password = current_app.config['FROM_PASSWORD']
	to_email = email
	s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

	subject="Hello"
	token = s.dumps(to_email)
	confirm_url = url_for(
		'confirm_email',
		token=token,
		_external=True)

	message = render_template(
		'email/hello.html',
		confirm_url=confirm_url)

	msg=MIMEText(message, 'html')
	msg['Subject']=subject
	msg['To']=to_email
	msg['From']= 'Hello'

	gmail=smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.send_message(msg)
