import json
import requests


class Course:

    def __init__(self):
        self.url = "https://www.cbr-xml-daily.ru/daily_json.js"

    def get(self):
        result = ''
        response = requests.get(self.url)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            json_obj = json.loads(response.text)
            if 'Valute' in json_obj:
                if 'CNY' in json_obj['Valute']:
                    result = json_obj['Valute']['CNY']['Value']

        return result
