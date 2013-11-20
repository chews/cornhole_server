# -*- coding: utf-8 -*-


from flask.ext.restful import reqparse, abort, Resource
from datetime import datetime
from models import PlantData

parser = reqparse.RequestParser()
parser.add_argument('imei', type=str, required=False)
parser.add_argument('ph', type=float, required=False)
parser.add_argument('n', type=int, required=False)
parser.add_argument('p', type=int, required=False)
parser.add_argument('k', type=int, required=False)
parser.add_argument('temp', type=float, required=False)
parser.add_argument('moisture', type=int, required=False)
parser.add_argument('lat', type=float, required=False)
parser.add_argument('lon', type=float, required=False)



class EventResourceCreator(Resource):
    def post(self):
        now = datetime.now() # Timezone!!
        args = parser.parse_args()
        event = PlantData(imei=args['imei'])
        event.ph = args['ph']
        event.n = args['n']
        event.p = args['p']
        event.k = args['k']
        event.temp = args['temp']
        event.moisture = args['moisture']
        event.lat = args['lat']
        event.lon = args['lon']
        event.created_at = datetime(now.year, now.month, now.day, 8)
        event.save()
        return event.to_json(), 201

class EventEcho(Resource):

    def get(self):
        return "echo", 201

class EventResourceMutator(Resource):

    def get(self, event_id):
        return "Awesome", 200

    def put(self, event_id):
        event = FooEvent.objects(id=event_id)


    def delete(self, event_id):
        pass
