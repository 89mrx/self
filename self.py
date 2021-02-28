try:
    import requests
    import uuid
    import time
    # import pyfiglet module
    import pyfiglet
except Exception as e:
    print(e)
print("\033[1;32;40m")
result = pyfiglet.figlet_format("9gyxi")
print(result)
print("---------------------------- \033[1;31;40m")
print("Follow Instagram:@9gyxi")
print("---------------------------- \033[2;37;40m")
user = input('Enter username: ')
password = input('Enter password: ')
print("---------------------------- \033[1;32;40m")
target = str(input(("Target:")))
sle = int(input("Enter sleep: "))
print("---------------------------- \033[1;30;40m")
def login():
    global target
    r = requests.Session()

    uid = str(uuid.uuid4())

    url = "https://i.instagram.com/api/v1/accounts/login/"

    headers = {
        'User-Agent': 'Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; >
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com'
    }

    data = {
        '_uuid': uid,
        'username': user,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:239490550:{}'.format(password),
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_count': '0'
    }

    loginreq = r.post(url, data=data, headers=headers, allow_redirects=True)
    print(loginreq.text)


    if loginreq.text.find("is_private") >= 0:
        done = 0
        print("DONE LOGIN")
        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
        url_id = "https://www.instagram.com/{}/?__a=1".format(target)
        url_get_user_id = r.get(url_id).json()
        print(url_get_user_id)
        while True:
            user_id = str(url_get_user_id["logging_page_id"])
            your_user_id = str(user_id.split("_")[1])# 4231341234
            urlRep = "https://i.instagram.com/users/" + your_user_id + "/report/"
            datas = {
                    'source_name': '', 'reason_id': 2, 'frx_context': ''  #  Suicide self-injury or >
                }
            req_SessionID = r.post(urlRep, data=datas)
            done += 1
            print("---------------------------- \033[1;32;40m")
            print(f"Done spam -> 9gyxi : {done}")
            time.sleep(sle)
    else:
        print("LOGIN FAILED CHECK YOUR INFO!")
login()
