# ! Not tested yet

import requests
import time
from stem import Signal
from stem.control import Controller


def get_current_ip():
    session = requests.session()

    # TO Request URL with SOCKS over TOR
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:8118'
    session.proxies['https']='socks5h://localhost:8118'

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as error:
        print(str(error))
    else:
        return r.text


def renew_tor_ip():
    with Controller.from_port(port = 8118) as controller:

        try:
            print('is alive BEFORE ? ')
            print(controller.is_alive())
            controller.authenticate(password="MyStr0n9P#D")
        except:
            print('error')
        finally:
            print('authenticated')

        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    for i in range(5):
        print(get_current_ip())
        renew_tor_ip()
        print('renewed')
        time.sleep(5)