from flask import Flask
import game
import mail
import stats

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is a server!'

@app.route('/mail/status')
def mail_status():
    return mail.get_status()

@app.route('/mail/read')
def read_mail():
    return mail.read_mail()

@app.route('/mail/send')
def send_mail():
    return mail.send_mail()