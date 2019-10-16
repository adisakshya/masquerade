from flask import Flask,render_template,request
import requests
import os
import pandas as pd

app = Flask(__name__)

# Render Index Page
@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")

# Get the list of configuration files
@app.route("/config_list/<country_code>", methods = ["GET"])
def config_list(country_code):

    res = {
        'error' : True,
        'success' : False
    }

    connection_list = {}
    country_list = []
    try:
        df = pd.read_csv('./bin/connection_list.csv', index_col=0)
        for index, row in df.iterrows():
            
            country = row['country']
            if country not in country_list:
                country_list.append(country)
            
            if country_code != 'all':
                if country != country_code:
                    continue

            ip_address = row['ip_address']
            organisation = row['organisation']
            city = row['city']
            region = row['region']

            if type(city) != str:
                city = 'Unknown'
            if type(region) != str:
                region = 'Unknown'
            
            if country not in connection_list.keys():
                connection_list[country] = []
            
            connection_list[country].append({
                    'ip_address':ip_address,
                    'organisation':organisation,
                    'country':country,
                    'city':city,
                    'region':region
                })

        res['error'] = False
        res['success'] = True
    except FileNotFoundError:
        res['error'] = 'Connection List File Not Found !'
    except Exception as error:
        res['error'] = error
    
    refresh_flag = False
    if connection_list:
        refresh_flag = True
    
    print(connection_list)
    return render_template('server_list.html', country_list = country_list, server_list = connection_list, response = res, refresh_flag = refresh_flag )

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