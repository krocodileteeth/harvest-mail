from flask import Flask, request, jsonify
from database import MailDatabase
import time
class Mail():
    def __init__(self, id, sender, receiver, subject, content, next_id=-1, prev_id=-1, read=False, timestamp=None):
        self.id = int(id)
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content
        self.read = read
        self.next_id = int(next_id)
        self.prev_id = int(prev_id)
        if timestamp is None:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp

    def toJSON(self):
        return self.__dict__

class MailHandler():
    def __init__(self, db_file):
        self.db = MailDatabase(db_file)
        self.curr_id = -1

    def handle_reply(self, mail):
        prev_id = mail.prev_id
        self.db.add_mail(mail)
        self.db.update_mail_by_id(prev_id, 'next_id', mail.id)
        prev_mail = self.db.get_mail_by_id(prev_id)

        return prev_id

    def handle_new_sent(self, mail):
        self.db.add_mail(mail)

    def search(self, chain, all_mail):
        while True:
            curr = chain[-1]
            if curr['next_id'] == -1:
                return chain
            
            chain.append(all_mail[curr['next_id']])

    def get_status(self):
        all_mail = self.db.get_all_mail()
        all_mail_mapped = list(map(lambda x : Mail(*x).toJSON(), all_mail))

        chains = []

        for m in all_mail_mapped:
            if m['prev_id'] == -1:
                new_chain = [m]
                chains.append(self.search(new_chain, all_mail_mapped))

        return jsonify(chains)

    def receive_mail(self, sender, receiver, subject, content, prev_id=-1):
        mail = Mail(self.db.get_new_id(), sender, receiver, subject, content, prev_id=prev_id)
        self.db.add_mail(mail)

    def read_mail(self):
        id = request.args.get('id')
        self.db.update_mail_by_id(id, 'read', True)
        return id

    def send_mail(self):
        mail = Mail(self.db.get_new_id(), read=True, **request.args)

        if 'prev_id' in request.args:
            self.handle_reply(mail)
        else:
            self.handle_new_sent(mail)

        return self.get_status()
    