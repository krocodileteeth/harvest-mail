from flask import Flask, request
from flask_restful import Api, Resource, reqparse

class Mail():
    def __init__(self, id, sender, receiver, subject, content, read=False):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content
        self.read = read

def handle_reply(mail):
    pass

def handle_new_sent(mail):
    pass

def get_new_id():
    return 0

def get_status():
    return "Status"

def read_mail():
    id = request.args.get('id')
    return id

def send_mail():
    mail = Mail(get_new_id(), read=True, **request.args)
    mail.reply_id = -1

    if 'reply_id' in request.args:
        mail.reply_id = request.args.get('reply_id')

    if mail.reply_id >= 0:
        handle_reply(mail)
    else:
        handle_new_sent(mail)

    return get_status()
    