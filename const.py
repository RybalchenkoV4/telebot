TOKEN = "5940354494:AAGLSM4FpV9V7hTlQaP26HpbyIWhsLItYMo"

URL = "https://api.telegram.org/bot{token}/{method}"

UPDATE_METH = "getUpdates"
SEND_METH = "sendMessage"

MY_ID = 419884280

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    UPDATE_ID = file.readline()

WEATHER_TOKEN = '89b88106fcd11e0856da3904c61667a1'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'