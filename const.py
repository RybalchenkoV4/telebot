TOKEN = "your token"

URL = "https://api.telegram.org/bot{token}/{method}"

UPDATE_METH = "getUpdates"
SEND_METH = "sendMessage"

MY_ID = 419884280

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    UPDATE_ID = file.readline()

WEATHER_TOKEN = 'your weather token'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
