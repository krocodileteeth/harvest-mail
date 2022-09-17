from flask import Flask, request
import database
import time
class Mail():
    def __init__(self, id, sender, receiver, subject, content, next_id=-1, prev_id=-1, read=False):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content
        self.read = read
        self.next_id = next_id
        self.prev_id = prev_id
        self.timestamp = time.time()

class MailHandler():
    def __init__(self, db_file):
        self.db_file = db_file
        self.db = database.create_connection(db_file)

    def handle_reply(self, mail):
        pass

    def handle_new_sent(self, mail):
        pass

    def get_new_id(self):
        return 0

    def get_status(self):
        return "Status"

    def read_mail(self):
        id = request.args.get('id')
        return id

    def send_mail(self):
        mail = Mail(self.get_new_id(), read=True, **request.args)

        if 'prev_id' in request.args:
            mail.prev_id = request.args.get('prev_id')
            self.handle_reply(mail)
        else:
            self.handle_new_sent(mail)

        return self.get_status()
    