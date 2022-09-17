from flask import Flask
from datetime import datetime
import time
import os

class GameHandler():
    def __init__(self):
        self.BASE_POINTS = 10
        self.BONUS_POINTS = 1
        self.PENALTY_POINTS = -2
        self.SEND_POINTS = 3
        self.REPLY_LIMIT = 200
        self.SEND_LIMIT = 20
        self.reply_points = 0
        self.send_points = 0

    def handle_reply(self, prev_timestamp, curr_timestamp):
        prev_datetime = datetime.fromtimestamp(prev_timestamp)
        curr_datetime = datetime.fromtimestamp(curr_timestamp)

        diff = curr_datetime - prev_datetime

        hours = diff.seconds / 3600

        if self.reply_points >= self.REPLY_LIMIT and hours <= 48:
            return

        if hours <= 12:
            self.reply_points += self.BASE_POINTS + round(12 - hours) * self.BONUS_POINTS
        elif hours <= 24:
            self.reply_points += self.BASE_POINTS

    def handle_send(self):
        if self.send_points >= self.SEND_LIMIT:
            return

        self.send_points += self.SEND_POINTS

    def handle_penalty(self, days):
        penalty = self.PENALTY_POINTS

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

        return str(self.send_points + self.reply_points)

    def reset_limits(self):
        self.reply_points = 0
        self.send_points = 0

