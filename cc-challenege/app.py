import requests as req
import constants as CONSTANTS


urlObp = "https://citizensbank.openbankproject.com/obp/v4.0.0/banks/citizens.0201.us-b.cb/accounts/03392032-7904-45d0-8609-5302a47b5d75/owner/transactions"

payload = "{\n\t\"email\": \"fanonxr@gmail.com\",\n\t\"password\": \"hello1234\",\n\t\"confirmPassword\": \"hello1234\",\n\t\"handle\": \"user\"\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': 'DirectLogin token="eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.lNsosH2hcbsTkxEgg83jYFpuK8RKj9m1xeGLgadikWs"',
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "7a6c2306-646b-4888-b874-28cb08b30677,cab7911d-4f47-4505-808d-8b2b0677beac",
    'Host': "citizensbank.openbankproject.com",
    'cookie': "JSESSIONID=1s579di2fv0vzhyupfbap8z0v",
    'accept-encoding': "gzip, deflate",
    'content-length': "111",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

obpResponse = req.request("GET", urlObp, data=payload, headers=headers)

def search_for_transactions():
    transactions = obpResponse['transactions']['transactions']

# print(ObpResponse.text)
