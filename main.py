from netmiko import ConnectHandler

from flask import Flask, jsonify, render_template, request

radius_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.18.192',
    'username': 'admin',
    'password': '30NO1982',
    'port': '22',
    'secret': 'secret',
}

app = Flask (__name__)

@app.route('/', methods=['GET'])
def createRadiusUser ():  

    net_connect = ConnectHandler(**radius_mikrotik)
    config_commands =['/tool user-manager user add username= password= copy-from="Usuario Matrix" customer=admin']
    output = net_connect.send_config_set(config_commands)
    return jsonify(output)


if __name__ == '__main__': 
  app.run(debug=True)