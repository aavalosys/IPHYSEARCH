from flask import Flask, jsonify, request
import ping3
from lam_connection_lib import *







app = Flask(__name__)

@app.route('/api/ping/', methods=['POST'])
def ping():
    ip = request.get_json()
    response_time = ping3.ping(ip, timeout=1, unit="ms")
    if response_time is None:
        value = "Down"
    else:
        value = "Up"
    return jsonify(ip, value)



#print (check_int("fy2023w48","10.123.45.6", "GigabitEthernet 0/2/24"))


@app.route('/api/getinterface/', methods=['POST'])
def getinterface():
    ip = request.get_json()
    print (ip)
    value = (check_int(ip[0], ip[1], ip[2]))
    return jsonify(ip, value)


@app.route('/api/getpingvrf/', methods=['POST'])
def getpingvrf():
    ip = request.get_json()
    print (ip)
    value = (check_pingvrf(ip[0], ip[1], ip[2], ip[3]))
    return jsonify(ip, value)

@app.route('/api/getbackup/', methods=['POST'])
def getbackup():
    ip = request.get_json()
    print (ip)
    value = (check_backup(ip[0], ip[1]))
    return jsonify(ip, value)




if __name__ == '__main__':
    app.run(host="10.10.26.4",debug=True)