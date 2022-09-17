from flask import Flask
import game
import mail
import stats

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is a server!'

@app.get('/mail/status')
def mail_status():
    return mail.get_status()

@app.post('/mail/read')
def read_mail():
    return mail.read_mail()

@app.post('/mail/send')
def send_mail():
    return mail.send_mail()