#!/usr/bin/env python
import requests
import time
import json

if __name__ == '__main__':
    port_number = 7201
    ip_address = "127.0.0.1"
    url = "http://" + ip_address + ":" + str(port_number) + "/api/robot/status"
    print("Requesting from " + url)
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            print("Status: " + str(response.status_code))
            print(json.dumps(response.json()))
        except requests.exceptions.HTTPError as errh:
            print("Status: " + str(response.status_code))
            print(json.dumps(response.json()))
        except requests.exceptions.ConnectionError as errc:
            print('{"Message": "Connection Error"}')
        except requests.exceptions.Timeout as errt:
            print('{"Message": "Request Timeout"}')
        except requests.exceptions.RequestException as err:
            print('{"Message": "Request Exception"}')
        time.sleep(1)
