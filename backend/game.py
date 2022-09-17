from flask import jsonify
from datetime import datetime
from database import GameDatabase
import time
import os

class GameStats():
    def __init__(self, user_id, points, emails_sent, emails_received, fastest_response):
        self.user_id = user_id
        self.points = points
        self.emails_sent = emails_sent
        self.emails_received = emails_received
        self.fastest_response = fastest_response

class GameHandler():
    def __init__(self, db_file):
        self.db = GameDatabase(db_file)
        self.BASE_POINTS = 10
        self.BONUS_POINTS = 1
        self.PENALTY_POINTS = -2
        self.SEND_POINTS = 3
        self.REPLY_LIMIT = 200
        self.SEND_LIMIT = 20
        self.reply_points = 0
        self.send_points = 0
        self.penalty_points = 0

    def reset_database(self):
        self.db.set_stats(0, 0, 0, 0, 2048)

    def update_stats(self):
        self.db.update_points(self.reply_points + self.send_points + self.penalty_points)

    def handle_reply(self, prev_timestamp, curr_timestamp):
        prev_datetime = datetime.fromtimestamp(prev_timestamp)
        curr_datetime = datetime.fromtimestamp(curr_timestamp)

        diff = curr_datetime - prev_datetime

        hours = diff.seconds / 3600

        stats = GameStats(*self.db.get_stats())
        new_email_sent_count = stats.emails_sent + 1
        new_fastest = min(stats.fastest_response, diff.seconds / 60)

        self.db.update_emails_sent(new_email_sent_count)
        self.db.update_fastest_response(new_fastest)

        if self.reply_points >= self.REPLY_LIMIT and hours <= 48:
            return

        if hours <= 12:
            self.reply_points += self.BASE_POINTS + round(12 - hours) * self.BONUS_POINTS
        elif hours <= 24:
            self.reply_points += self.BASE_POINTS

    def handle_receive(self):
        stats = GameStats(*self.db.get_stats())
        new_email_receive_count = stats.emails_received + 1

        self.db.update_emails_received(new_email_receive_count)

    def handle_send(self):
        stats = GameStats(*self.db.get_stats())
        new_email_sent_count = stats.emails_sent + 1

        self.db.update_emails_sent(new_email_sent_count)

        if self.send_points >= self.SEND_LIMIT:
            return

        self.send_points += self.SEND_POINTS

    def handle_penalty(self, days):
        self.penalty_points -= self.PENALTY_POINTS

    def get_status(self, all_mail=None):
        curr_date = datetime.fromtimestamp(time.time())
        
        if all_mail is not None:
            for m in all_mail:
                if m.next_id == -1 and m.sender != os.environ.get("USER"):
                    m_date = datetime.fromtimestamp(m.timestamp)
                    diff = curr_date - m_date

                    hours = diff.seconds / 3600

                    if hours > 48:
                        self.handle_penalty(round(hours / 24))

        self.update_stats()
        stats = GameStats(*self.db.get_stats())

        return jsonify(stats.__dict__)

    def reset_limits(self):
        self.reply_points = 0
        self.send_points = 0

