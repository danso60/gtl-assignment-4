from flask import Flask, render_template
import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy as sql
from flask_migrate import Migrate

b_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(b_dir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = sql(app)

Migrate(app,db)

class CountryHealthReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.Text)
    totalcase = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)
    activecase = db.Column(db.Integer)
    totaldeaths = db.Column(db.Integer)

    def __init__(self,country,totalcase,recoveries,activecase,totaldeaths):
        self.country = country
        self.totalcase = totalcase
        self.recoveries = recoveries
        self.activecase = activecase
        self.totaldeaths = totaldeaths

    def __repr__(self):
        return f'{self.totalcase}'

@app.route('/')

def Index():
    HealthState = CountryHealthReport.query.all()
    return render_template('index.html',HealthState=HealthState)

if __name__=='__main__':
    app.run()

# import sqlite3
# from flask import g

# DATABASE = '/path/to/database.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


