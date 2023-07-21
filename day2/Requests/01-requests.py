import requests
import secrets

# API 불러오기
def main():
    """response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={secrets.API_KEY}")
    # 401 error -> append Key
    """
    payload = {"access_key":secrets.API_KEY}
    response = requests.get("http://api.exchangeratesapi.io/v1/latest",
                             params=payload)
    
    if response.status_code != 200:
        print("Error occured!")

    print(response.status_code)
    # print(response.text)
    # print(secrets.API_KEY)
    
    print(response.headers['Content-Type'])
    # application/json

    print(type(response.text))
    # str

    # str to dictionary
    response_dictionary = response.json()

    success = response_dictionary['success']
    timestamp = response_dictionary['timestamp']
    base = response_dictionary['base']
    date = response_dictionary['date']
    
    KRW = response_dictionary['rates']['KRW']
    AUD = response_dictionary['rates']['AUD']
    USD = response_dictionary['rates']['USD']
    
    print(f"성공코드 : {success}")
    print(f"timestamp : {timestamp}")
    print(f"base : {base}")
    print(f"date : {date}")
    print(f"KRW : {KRW} AUD : {AUD} USD : {USD}")
    
    
    """
    받은 response를 dictionary화 해서
    success는 ~
    timestamp는 ~
    base KRW 기준으로 달러는 얼마인지 받아오기
    """



if __name__ == "__main__":
    main()

