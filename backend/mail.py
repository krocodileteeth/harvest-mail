from flask import Flask, request
from flask_restful import Api, Resource, reqparse
class Mail():
    def __init__(self, id, sender, receiver, subject, content, next_id=-1, prev_id=-1, read=False):
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

    if 'prev_id' in request.args:
        mail.prev_id = request.args.get('prev_id')
        handle_reply(mail)
    else:
        handle_new_sent(mail)

    return get_status()
    