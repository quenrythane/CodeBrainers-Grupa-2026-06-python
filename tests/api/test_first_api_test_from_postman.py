import requests

def test_health_from_postman():
    url = "http://127.0.0.1:8000/health"

    payload = {}
    headers = {
    'sec-ch-ua-platform': '"Windows"',
  'Referer': 'http://127.0.0.1:8000/docs',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
  'accept': 'application/json',
  'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
  'sec-ch-ua-mobile': '?0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
