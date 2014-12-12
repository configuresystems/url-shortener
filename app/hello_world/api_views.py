from app import api

from flask import abort
from flask.ext.restful import Resource, reqparse, fields, marshal

messages = [
        ]

message_fields = {
        'id': fields.Integer,
        'message': fields.String,
        'uri': fields.Url('message')
        }


class HelloWorldListApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message',
                                    type=str,
                                    required=True,
                                    help="Provide a message",
                                    location='json'
                                    )
        super(HelloWorldListApi, self).__init__()

    def get(self):
        return { 'messages': map(lambda m: marshal(m, message_fields), messages) }

    def post(self):
        args = self.reqparse.parse_args()
        id = 1
        if len(messages) > 0:
            id = messages[-1]['id'] + 1
        message = {
                'id': id,
                'message': args['message'],
                }
        messages.append(message)
        return { 'message': marshal(message, message_fields) }, 201

class HelloWorldApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message',
                                    type=str,
                                    required=True,
                                    help="Provide a message",
                                    location='json'
                                    )
        super(HelloWorldApi, self).__init__()

    def get(self, id):
        message = filter(lambda m: m['id'] == id, messages)
        if len(message) == 0:
            abort(404)
        return { 'message': marshal(message[0], message_fields) }

    def put(self, id):
        message = filter(lambda m: m['id'] == id, messages)
        if len(message) == 0:
            abort(404)
        message = message[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                message[k] = v
        return { 'message': marshal(message, message_fields) }

    def delete(self, id):
        message = filter(lambda m: m['id'] == id, messages)
        if len(message) == 0:
            abort(404)
        messages.remove(message[0])
        return { 'result': True }

