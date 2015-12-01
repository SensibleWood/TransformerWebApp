#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask.ext.restplus import Api, Resource, fields
from uuid import uuid4

app = Flask(__name__)
api = Api(app,
          version="1.0",
          title="API Transformer demonstration",
          description="API created to demonstrate the functionality offered by the API Transformer Convertron")
demo_ns = api.namespace('demo', description='Demo operations')


@demo_ns.route('')
class Demo(Resource):
    @api.doc(description='A demo HTTP GET',
             responses={400: ("Bad request", api.model('Error', {"message": fields.String})),
                        500: "Unhandled exception (captured in server logs)"})
    def get(self):
        return 'This is a demo!', 200

    @api.expect(api.model('Demo Request', {"data": fields.String(required=True)}))
    @api.doc(description='A demo HTTP POST',
             responses={400: ("Bad request", api.model('Error', {"message": fields.String})),
                        500: "Unhandled exception (captured in server logs)"})
    @api.marshal_with(api.model(
        'Demo Response',
        {"id": fields.String(required=True), "data": fields.String(required=True)}), code=201)
    def post(self):
        return {'id': uuid4().hex, 'data': 'Created new demo resource'}, 201

if __name__ == '__main__':
    app.run()
