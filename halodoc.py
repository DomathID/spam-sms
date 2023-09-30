import requests
from fake_useragent import UserAgent

url = "https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests"

ua = UserAgent()
user_agent = ua.random

headers = {
    "Host": "magneto.api.halodoc.com",
    "Connection": "keep-alive",
    "Content-Length": "72",
    "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": "\"Android\"",
    "X-XSRF-TOKEN": "D12D611B234C4FAE3392DFAB88777FFFEFCA75A57B5B7434B7CA9170D05FAF618BC66315885DAA261B5C88FD3A0638955A80",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": user_agent,
    "Content-Type": "application/json",
    "Origin": "https://www.halodoc.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6",
    "Cookie": "_gcl_au=1.1.1204589061.1695237135; XSRF-TOKEN=D12D611B234C4FAE3392DFAB88777FFFEFCA75A57B5B7434B7CA9170D05FAF618BC66315885DAA261B5C88FD3A0638955A80; _ga=GA1.1.777862174.1695237137; amp_394863=5CaF2jO-2aQqLCo1VNawMl...1haq03o0c.1haq03oek.2.1.3; _ga_02NBJNEKVH=GS1.1.1695237136.1.0.1695237136.60.0.0; afUserId=ad18d7a5-9e5b-4b17-8c0e-cb28958984d4-o; AF_SYNC=1695237138441"
}

data = {
    "phone_number": "+62",
    "channel": "sms",
    "otp_resent": False
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

