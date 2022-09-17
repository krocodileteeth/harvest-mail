from flask import Flask, request
from flask_restful import Api, Resource, reqparse

def get_status():
    pass

def read_mail():
    id = request.args.get('id')
    return id

def send_mail():
    
    pass