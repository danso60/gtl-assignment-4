import flask
from flask import request, jsonify
from flask_cors import CORS 

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

covidcases = [
    {'id': 0,
     'country': 'Ghana',
     'total_cases': '11,118',
     'recoveries': '3979',
     'active_cases': '7000',
     'total_deaths': '48'
     },
    {'id': 1,
     'country': 'Nigeria',
     'total_cases': '17,218',
     'recoveries': '15,008',
     'active_cases': '2,000',
     'total_deaths': '210'
     },
   {'id': 2,
     'country': 'Egypt',
     'total_cases': '20,000',
     'recoveries': '18,001',
     'active_cases': '1,900',
     'total_deaths': '99'
     }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Covid tracker</h1>
<p>covid application api to track their cases created successfully... </p>'''


# A route to return all of the available entries.
@app.route('/app/v1/resources/covid/all', methods=['GET'])
def api():
    return jsonify(covidcases)

app.run()