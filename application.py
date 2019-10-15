from flask import Flask,render_template,request
import requests
import os

app = Flask(__name__)

# Render Index Page
@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")

# Get the list of configuration files
@app.route("/config_list", methods = ["GET"])
def config_list():

    res = {
        'error' : True,
        'success' : False
    }
    
    try:
        list_config_files = os.listdir("C:\\Program Files\\OpenVPN\\config")
        res['error'] = False
        res['succss'] = True
    except FileNotFoundError:
        res['error'] = 'No Config Files Available'
    except Exception as error:
        res['error'] = error
    
    return { 'list' : list_config_files }

#  Refresh list of available connections
@app.route("/refresh", methods = ["GET"])
def refresh():

    res = {
        'error' : True,
        'success' : False,
        'server_list' : {}
    }
    server_dict = {}
    try:
        from bin.server_list import VPNServersList
        obj = VPNServersList()
        server_details, error, success  = obj.get_server_list()

        res = {
            'error' : error,
            'success' : success,
        }
        server_dict = server_details

    except ImportError:
        err = 'Fetching files are missing !'
        res['error'] = err
    except Exception as error:
        # error = 'Cannot fetch server list at the moment. Please try again later !'
        res['error'] = error

    server_list = []
    for server in server_dict.keys():
        server_list.append(server_dict[server])    
    
    flag = False
    if server_list and server_dict:
        flag = True

    return render_template("server_list.html", response=res, server_list=server_list, refresh_flag=flag)

# Randomize connection
@app.route("/stealth_mode_randomize", methods = ["GET"])
def stealth_mode_randomize():

    res = {
        'error' : True,
        'success' : False
    }
    try:
        dis_command = '"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --command disconnect_all'
        os.system(dis_command)
    except Exception as error:
        pass

    try:
        import random
        list_config_files = os.listdir("C:\\Program Files\\OpenVPN\\config")
        config_connect = random.choice(list_config_files)
        command = '"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe" --connect ' + config_connect
        os.system(command)

        res['error'] = False
        res['success'] = True
    except Exception as error:
        res['error'] = error
    print(res)
    return render_template('connected.html', status=res)

if __name__ == "__main__":
    app.run(debug = True)