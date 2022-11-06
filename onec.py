import requests
import json
from config import *
import log
from const import LOGIN, PASS

logger = log.get()

class Http1C():
    '''Connector http-service 1c:enterprise'''

    def __init__(self):
        self.url = f'http://{HOST}:{PORT}/{BASE}/hs/{URL}/'
    
        response = self.ping()
        if response.status_code != 200:
            print(f"Error ping-test: code {response.status_code}")
            raise Exception("1C:service connection error")

    def __str__(self) -> str:
        description = 'Траслятор в http-service 1C ' + self.url
        return description

    def ping(self):
        '''Test online status'''
        
        logger.debug(f'Ping 1C: url={self.url}')
    
        response = requests.get(self.url,
            headers= {'Authorization': 'Basic'},
            auth=(LOGIN, PASS))

        return response

    def send(self, hook_data: dict):
        
        id_log = hook_data["id"][0] if len(hook_data["id"]) == 1 else hook_data["id"] 
        logger.debug(f'Send 1C: url={self.url}; event={hook_data["event"]}; ID={id_log}')

        response = requests.post(self.url,
            headers= {'Authorization': 'Basic'},
            auth=(LOGIN, PASS),
            data=json.dumps(hook_data))

        log_messange = f'Send 1C: ID={id_log}, status={response.status_code}'
        if response.status_code == 200:
            logger.debug(log_messange)
        else:
           logger.error(log_messange + f', error={response.text}')

        return response
