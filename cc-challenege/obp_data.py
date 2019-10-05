import constants as CONSTANTS

import requests as req
import constants as CONSTANTS

ObpResponse = req.request("GET", CONSTANTS.urlObpAPI, data=CONSTANTS.payload, headers=CONSTANTS.headers)

print(ObpResponse.text)