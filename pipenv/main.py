import os

print(os.environ["NAME"])

print("\nPython path:\n{}".format("\n".join(os.sys.path)))

import requests

response = requests.get("https://httpbin.org/ip")
print("Your IP is {0}".format(response.json()["origin"]))
