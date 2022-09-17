from flask import Flask
from flask_cors import CORS
from game import GameHandler
from mail import MailHandler, Mail
import stats

MAIL_DATABASE = 'mail.db'

app = Flask(__name__)
CORS(app)

game = GameHandler()
mail = MailHandler('mail.db', game)
mail = MailHandler(':memory:', game)

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

def add_fake_date():
    mail0 = {"id": mail.db.get_new_id(), "sender": "s", "receiver": "r", "subject": "s", "content": "c", "next_id":-1, "prev_id":-1}
    mail1 = {"id": mail.db.get_new_id(), "sender": "s", "receiver": "r", "subject": "s", "content": "c", "next_id":-1, "prev_id": 0}
    mail2 = {"id": mail.db.get_new_id(), "sender": "s", "receiver": "r", "subject": "s", "content": "c", "next_id":-1, "prev_id": 1}
    mail3 = {"id": mail.db.get_new_id(), "sender": "s", "receiver": "r", "subject": "s", "content": "c", "next_id":-1, "prev_id": -1}

    mail.handle_new_sent(Mail(**mail0))
    mail.handle_reply(Mail(**mail1))
    mail.handle_reply(Mail(**mail2))
    mail.handle_new_sent(Mail(**mail3))

add_fake_date()