from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    data = {}
    data['ip'] = request.remote_addr
    return render_template('index.html', data=data)
#def index():
#    user = {'username': 'Miguel'}
#    return render_template('index.html', title='Home', user=user)

from flask import jsonify

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
