import os
# Constants to request to the api

CONSUMER_KEY = "1DoG8m37zYEkfeRcXFosEKiTe"
CONSUMER_SECRET = "nbnt0QT6kWNGJvNDHvo8zvI8yX9PIW9grxkdgbvq35nKyn0oqC"
ACCESS_KEY = "1008178143528718336-jv7RtsQhUx4z1rNK3fZgjSijsKjYhQ"
ACCESS_SECRET = "LGr9Znc3nwf0cyuy01YbAvC0m6oCI7Lk1sIT0WoUfi440"

py_dir = os.getcwd()
base_dir = os.path.normpath(os.getcwd() + os.sep + os.pardir)

urlObpAPI = "https://citizensbank.openbankproject.com/obp/v4.0.0/banks/citizens.0201.us-b.cb/accounts/03392032-7904-45d0-8609-5302a47b5d75/owner/transactions"

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