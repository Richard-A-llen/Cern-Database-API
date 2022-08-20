import random
import os
import shutil
import requests

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
    url = f'http://127.0.0.1:8080/upload/upload?file_name={save_name}'
    response = requests.post(url, files={'file': open(file, 'rb')})
    print(f'response = {response}')
    print(f'response.content = {response.content}')


def download_file():
    with requests.get(f'http://127.0.0.1:8080/download/file?name=test', stream=True) as f:
        with open(r'D:\MyPrograms\MicroserviceWithFlask\client\song', 'wb') as w:
            shutil.copyfileobj(f.raw, w)
    print(f'response = {f.status_code}')


def login(name, passwd):
    response = requests.get(f'http://127.0.0.1:8080/login/?user={name}&passwd={passwd}')
    print(f'response = {response}')
    print(f'response.content = {response.content}')


def task_login(name, passwd):
    response = requests.get(f'http://127.0.0.1:8080/task/login?user={name}&passwd={passwd}')
    print(f'response = {response}')
    print(f'response.content = {response.content}')


if __name__ == '__main__':
    task_login("test", 3333)
    # login("test", 1234)
    # test_index()
    # task()
    # upload_file()
    # download_file()