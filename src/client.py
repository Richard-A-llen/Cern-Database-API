import os
import shutil
import requests

current_dir = os.path.dirname(__file__)
server_crt_file = os.path.dirname(__file__) + r'./flask_cert.pem'
request_successful = 200


def login(user, passwd):
    response = requests.get(
        f'https://127.0.0.1:8080/request/login?user={name}&passwd={passwd}', verify=server_crt_file)
    print(f'response = {response}')
    print(f'response.content = {response.content}')
    if response.status_code == request_successful:
        return response.content # receive session
    print("login failed.")
    return None

def download(session, file):
    with requests.get(f'https://127.0.0.1:8080/request/download?session={session}&file=test', stream=True, verify=server_crt_file) as f:
        if f.status_code != request_successful:
            print(f"{f.content}")
            return
        with open(r'D:\MyPrograms\MicroserviceWithFlask\misc\test', 'wb') as w:
            shutil.copyfileobj(f.raw, w)
            print(r"download successful")

def upload(session, local_file):
    # you can change file and save_name to test
    # save_name used to save file with the name on the remote server side
    if not (os.path.exists(local_file) and os.path.isfile(local_file)):
        print("the file doesn't exist.")
        return
    file_name = os.path.basename(local_file)
    url = f'https://127.0.0.1:8080/upload/upload?session={session}&file_name={file_name}'
    response = requests.post(url, files={'file': open(local_file, 'rb')})
    if response.status_code == request_successful:
        print("upload successful")
    else:
        print("upload failed.")
    print(f"{response.content}")

def user_demo():
    user = "test"
    password = "4f@d64E0c!0"
    session = login(user, password)
    download(session, "test.txt")
    upload(session, "local_file.txt")


if __name__ == '__main__':
    user_demo()
