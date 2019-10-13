import urllib.request as urllib2
import re
import base64
import socket
import os, glob

class VPNServersList:

    def __init__(self):

        self.base_url = 'http://www.vpngate.net/api/iphone/'
        self.server_details = {
            'error' : None,
            'success' : None
        }
    
    def tcp_port_is_open(self, ip, port) :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        r = s.connect_ex((ip, port))
        if r == 0 :
            s.close()
            return True
        else :
            return False
    
    def get_server_list(self):

        ua = urllib2.Request(self.base_url)
        ua.add_header('User-agent', 'Mozilla/5.0')
        res = urllib2.urlopen(ua)

        if res.getcode() == 200 :
            result = {}
            p = re.compile('^\w+')
            i = 0
            while True :
                if i >= 10:
                    break
                else:
                    i += 1

                svr_line = res.readline()
                if svr_line:
                    svr_line = svr_line.decode('utf-8')
                    if p.match(svr_line):
                        c = re.compile(',').split(svr_line)
                        ip = c[1]
                        country = c[6]
                        config_base64 = c[-1]
                        config = base64.b64decode(config_base64)

                        # get tcp port from config_file
                        p_tcp = re.compile('^proto tcp', re.MULTILINE)
                        p_port = re.compile('^remote [.|\d]+ (\d+)', re.MULTILINE)
                        config = config.decode('utf-8')
                        if p_tcp.search(config) :
                            m_port = p_port.search(config)
                            if m_port :
                                port = int(m_port.group(1))
                                if self.tcp_port_is_open(ip, port) :
                                    print("GOOD: ", country, ip, port)
                                    if country not in result :
                                        result[country] = []
                                    else :
                                        result[country].append({'ip':ip, 'config':config})
                                        self.server_details[ip] = {
                                            'host_name' : c[0],
                                            'ip' : ip,
                                            'score': c[2],
                                            'ping': c[3],
                                            'speed' : c[4],
                                            'country_long' : c[5],
                                            'country_short' : c[6],
                                            'sessions' : c[7],
                                            'uptime' : c[8],
                                            'total_users' : c[9],
                                            'total_traffic' : c[10],
                                            'operator' : c[12]
                                        }
                                else :
                                    print("TIMEOUT: ", country, ip, port)
                else :
                    break

            config_path = './config_files'
            os.chdir(config_path)
            
            for country in result :
                for server in result[country] :
                    file_name = '_'.join(['vpngate', country, server['ip']]) + '.ovpn'
                    print(file_name)
                    f = open(file_name, 'w')
                    f.write(server['config'])
                    f.close()
        else :
            print(res.getcode())
        
        if len(self.server_details) > 2:
            error = False
            success = True
        else:
            error = True
            success = False
        
        return self.server_details, error, success

# Uncomment to test above class functions
# obj = VPNServersList()
# obj.get_server_list()