from flask import Flask
from datetime import datetime

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

        print(diff.days)

    def handle_send(self):
        if self.send_points >= self.SEND_LIMIT:
            return

        self.send_points += self.SEND_POINTS

    def handle_penalty(self, timestamp):
        pass

    def reset_limits(self):
        self.reply_points = 0
        self.send_points = 0

