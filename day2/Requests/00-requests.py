"""
가상환경(venv) 설정
python -m venv venv # venv라는 폴더가 생성됨

source venv/Scripts/activate # venv 실행


"""


# pip install requests

import requests

def main():
    response = requests.get("http://www.google.com/fgdgsdfg")
    print(response)
    print(response.status_code)
    print(response.headers['Content-Type']) # text / html
    print("Content: ", response.text)

if __name__ == "__main__":
    main()
