from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/refresh", methods = ["GET"])
def refresh():

    res = {
        'error' : True,
        'success' : False,
        'server_list' : {}
    }
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

    print(server_list)
    return render_template("server_list.html", response=res, server_list=server_list)

if __name__ == "__main__":
    app.run(debug = True)