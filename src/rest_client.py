"""
rest_client.py
Created on: Jul 31, 2021 16:50
Description: REST API Client
Copyright (c) 2021 Pin Loon Lee (pllee4)
"""
#!/usr/bin/env python
import time
import json
import argparse
import requests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="REST Client")
    parser.add_argument(
        "port_number", nargs="?", default="7201", type=int, help="port number"
    )
    parser.add_argument(
        "ip_address",
        nargs="?",
        default="127.0.0.1",
        help="ip_address for server",
    )
    margs = parser.parse_args()
    port_number = margs.port_number
    ip_address = margs.ip_address
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
