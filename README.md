# smos-api-wrapper
API wrapper for Simplemining OS (SMOS) written in python3

API documentation: https://api.simplemining.net/docs.html

## Usage

```
import smos
from smos import SMOS
import secrets
from pprint import pprint as pp

#creating an object
smos = SMOS(secrets.api_key)

# Getting rig list
pp(smos.getRigList())
# or
query={'status': 'off', 'itemsPerPage': '10'}
pp(smos.getRigList(query))

# Getting deposit address
payload = {'currency': 'eth'}
address = smos.getDepositAddress(payload)

# Getting deposit history
payload = {'page': 1, 'itemsPerPage': '100', 'order[amountUsd]': 'asc'}
deposits = smos.getDepositList(payload)

# rebooting rig(s) by their ID or group ID or whatever
rigs = '{"rigIds": [761897,111111,222222,987654]}'
reboot = smos.executeReboot(rigs)
pp(reboot) 
# delete and patch commands return status code
# >200

```

## TODO
1. error handling?
2. ?
