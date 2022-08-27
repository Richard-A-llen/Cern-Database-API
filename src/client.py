import random
import os
import shutil
import requests
import ssl

current_dir = os.path.dirname(__file__)
server_crt_file = os.path.dirname(__file__) + r'./flask_cert.pem'

def test_index():
    response = requests.get(r'http://127.0.0.1:8080')
    print(f'response = {response}')
    print(f'response.content = {response.content}')


def task():
    sleep = random.randint(5, 10)
    response = requests.get(f'http://127.0.0.1:8080/task/do_some?name=test&taks=eating')
    print(f'response = {response}')
    print(f'response.content = {response.content}')


def upload_file():
    # you can change file and save_name to test
    # save_name used to save file with the name on the remote server side
    file = r"D:\MyPrograms\MicroserviceWithFlask\client\A Man Without Love.mp3"
    if (not os.path.exists(file)):
        print("the file doesn't exist.")
        return
    save_name = r"demo.mp3"
    url = f'http://127.0.0.1:8080/upload/upload?user=test&file_name={save_name}'
    response = requests.post(url, files={'file': open(file, 'rb')})
    print(f'response = {response}')
    print(f'response.content = {response.content}')


def download_file():
    with requests.get(f'https://127.0.0.1:8080/request/download?name=test&file=test', stream=True, verify=server_crt_file) as f:
        with open(r'D:\MyPrograms\MicroserviceWithFlask\misc\test', 'wb') as w:
            shutil.copyfileobj(f.raw, w)
    print(f'response = {f.status_code}')


def login(name, passwd):
    response = requests.get(f'http://127.0.0.1:8080/login/?user={name}&passwd={passwd}')
    print(f'response = {response}')
    print(f'response.content = {response.content}')


def task_login(name, passwd):
    response = requests.get(f'https://127.0.0.1:8080/request/login?user={name}&passwd={passwd}', verify=server_crt_file)
    print(f'response = {response}')
    print(f'response.content = {response.content}')


if __name__ == '__main__':
    # task_login("test", 3333)
    download_file()
    # login("test", 1234)
    # test_index()
    # task()
    # upload_file()
    # download_file()