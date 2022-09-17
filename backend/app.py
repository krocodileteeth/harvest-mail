from flask import Flask
from flask_cors import CORS
from game import GameHandler
from mail import MailHandler, Mail
from dotenv import load_dotenv

load_dotenv()

MAIL_DATABASE = 'mail.db'
GAME_DATABASE = 'game.db'

app = Flask(__name__)
CORS(app)

game = GameHandler(GAME_DATABASE)
game = GameHandler(':memory:')
mail = MailHandler(MAIL_DATABASE, game)
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

@app.route('/game/status')
def game_status():
    return game.get_status(mail.get_all_mail())

@app.route('/test/phase/0')
def test_phase_0():
    mail0 = {"id": mail.db.get_new_id(), "sender": "sender", "receiver": "receiver", "subject": "s1", "content": "hello", "next_id":-1, "prev_id":-1}
    mail1 = {"id": mail.db.get_new_id(), "sender": "sender", "receiver": "receiver", "subject": "re: s1", "content": "hi", "next_id":-1, "prev_id": 0}
    mail2 = {"id": mail.db.get_new_id(), "sender": "sender", "receiver": "receiver", "subject": "re: re: s1", "content": "bye", "next_id":-1, "prev_id": 1}
    mail3 = {"id": mail.db.get_new_id(), "sender": "sender", "receiver": "receiver", "subject": "s2", "content": "heh", "next_id":-1, "prev_id": -1}

    mail.handle_new_sent(Mail(**mail0))
    mail.handle_reply(Mail(**mail1))
    mail.handle_reply(Mail(**mail2))
    mail.handle_new_sent(Mail(**mail3))

    return "phase 0"

@app.route('/test/phase/1')
def test_phase_1():
    mail.receive_mail('outsider', 'user', 'sub', 'hi')

    mail5 = {"id": mail.db.get_new_id(), "sender": "user", "receiver": "outside", "subject": "re: sub", "content": "heh", "next_id":-1, "prev_id": 4}
    mail.handle_reply(Mail(**mail5))
    return "phase 1"

@app.route('/test/phase/2')
def test_phase_2():
    mail.receive_mail('outsider', 'user', 're: re: sub', 'hello', prev_id=5)
    mail7 = {"id": mail.db.get_new_id(), "sender": "user", "receiver": "outside", "subject": "re: re: re: sub", "content": "heh heh", "next_id":-1, "prev_id": 6}
    mail.handle_reply(Mail(**mail7))
    return "phase 2"

game.reset_database()
