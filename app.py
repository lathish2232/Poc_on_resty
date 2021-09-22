import os 
from flask_cors import CORS
from flask import Flask

from settings import database,logger

app = Flask(__name__, static_url_path='/static/')
app.secret_key = 'ItShouldBeAnythingButSecret05L21a0546' 
app.config['CORS_HEADERS'] = 'Content-Type'
Cors = CORS(app)

from flask_restx import reqparse, Api, Resource, fields

api = Api(app)


@api.route('/test')
@api.response(200, 'Successful')

class Atms(Resource):
    def get(self):
        print('---------------i am in')
        resp={"code":200,"message":"This is a test url"}
        return resp

api.add_resource(Atms, '/test', methods=['GET'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7197))
    logger.info(port)
    logger.info("runing ...")
    app.run(debug=True)