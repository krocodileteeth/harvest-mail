from flask import Flask
from flask_cors import CORS
import game
from mail import MailHandler
import stats

MAIL_DATABASE = 'mail.db'

app = Flask(__name__)
CORS(app)
mail = MailHandler('mail.db')
# mail = MailHandler(':memory:')

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
