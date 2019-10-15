import re
import json
import pandas as pd
import urllib.request as urllib2

class geoip:

    def __init__(self, ip_address):

        self.url = 'http://ipinfo.io/' + ip_address + '/json'

    def get_response(self):

        response = urllib2.urlopen(self.url)
        data = json.load(response)
        return data
    
    def get_ip_details(self):

        data = self.get_response()

        IP=data['ip']
        org=data['org']
        city = data['city']
        country=data['country']
        region=data['region']

        res = {
            'ip' : IP,
            'org' : org,
            'city' : city,
            'country' : country,
            'region' : region
        }

        return res
    
    def update_connections(self):

        res = {
            'success': False,
            'error' : True
        }
        try:
            ip_details = self.get_ip_details()
            df = pd.read_csv('connection_list.csv', index_col=0)
            row = pd.DataFrame({
                'ip_address':ip_details['ip'],
                'organisation':ip_details['org'],
                'city':ip_details['city'],
                'country':ip_details['country'],
                'region':ip_details['region']
                }, index=[0])
            df = pd.concat([row, df[:]]).reset_index(drop = True)
            df.to_csv('connection_list.csv', sep=',')
            res['success'] = True
            res['error'] = False
        except Exception as error:
            res['error'] = error
        
        return res

# Uncomment below lines to test above class
# obj = geoip("220.94.70.87")
# obj.update_connections()