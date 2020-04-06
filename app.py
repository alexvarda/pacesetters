from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''
app.config['MYSQL_USER'] = 'ps_user'
app.config['MYSQL_PASSWORD'] = 'Pacesetters2019!'
app.config['MYSQL_HOST'] = '142.93.8.21' 
#app.congif['MYSQL_PORT'] = '3306'
app.config['MYSQL_DB'] = 'pacesetters'
#app.config['MYSQL_CURSORCLASS'] =  data type of the stuff thats returned (tuples by defalut)
db = SQLAlchemy(app)
db.app = app


class table2(db.Model):
    companyName = db.Column(db.String, primary_key=True)
    address = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)

    def __init__(self, name, address, latitude, longitude):
        self.companyName = name
        self.address = district
        self.latitude = latitude
        self.longitude = longitude
    
    def __repr__(self):
        return "<Company: %d / Coordinates Lat: %s , Long: %s>" % (self.companyName, self.latitude, self.longitude)
'''
@app.route('/', methods=['GET', 'POST'])

def map():
    
    #cur = mysql.connection.cursor()
    #cur.execute(''' SELECT * FROM table2 limit 10 ''') 
    #a = cur.fetchall()

    return  render_template("map.html")






if __name__ == '__main__':
    app.run(debug=True)