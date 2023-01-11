import requests
import json
import const
import time
from pprint import pprint

def answer_user_bot(data):
    pass

def get_parse_weather_data(data):
    pass

def get_weather(location):
    url = const.WEATHER_URL.format(city=location,token=const.WEATHER_TOKEN)
    response = requests.get(url)
    pprint(response.content)

def get_message(data):
    return data['message']['text']
    

def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    return True


def main():
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH)

        content = requests.get(url).text

        data  = json.loads(content)
        result = data['result'][::-1]
        needed_part = None

        for elem in result:
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                break
        
        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            get_weather(message)
            save_update_id(needed_part)


        
        

        break
        time.sleep(5)



if __name__ == '__main__':
    main()

