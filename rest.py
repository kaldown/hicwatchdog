#! -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from json import (dumps as json_dumps,
                  loads as json_loads)

import requests

from main import send_message

app = Flask(__name__)
api = Api(app)

#parser = reqparse.RequestParser()
#parser.add_argument('/ping', type=str, help='Assume you\'ve sent PING')

#class Ping(Resource):
#    def post(self):
#        parsed_args = parser.parse_args()
#
#        print(parsed_args, end='\n')
#
#        if args.get('/ping') is not None:
#            # place sendMessage
#            print('PONG')
#            return 'PONG'
#        return 'Wrong command, {args}'.format(args=args)

# {'update_id': 420493647, 'message': {'date': 1481467703, 'text': '/ping',
# 'message_id': 17, 'entities': [{'type': 'bot_command', 'offset': 0, 'length':
# 5}], 'from': {'id': 64509064, 'username': 'kAldown', 'first_name': 'kAldown'},
# 'chat': {'type': 'private', 'id': 64509064, 'username': 'kAldown',
# 'first_name': 'kAldown'}}}

class Ping(Resource):
    def post(self):
        args = request.get_json()

        message = args.get('message', {})
        text = message.get('text', {})
        from_user = message.get('from', {})
        chat = message.get('chat', {})

        if isinstance(text, str):
            if text.startswith('/ping'):
                fetched_message = {
                    'chat_id': chat.get('id'),
                    'text': u'ты че епт {user}'\
                        .format(user=from_user.get('username', 'Хз кто такой'))
                }
                print(fetched_message)
                send_message(**fetched_message)
                return None, 200
        return 'Wrong command, {args}'.format(args=args)

api.add_resource(Ping, '/hicwatchdog_hook/')

if __name__ == '__main__':
    app.run(debug=True)
