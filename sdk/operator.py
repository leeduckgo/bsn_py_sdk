import requests
from sdk.common.loggers import logger
from sdk.common import myecdsa256
import json
import configparser

class Operator:
    '''
        init.
    '''
    def __init__(self, userCode, appCode, chainCode, url, cert_path):
        self.userCode = userCode
        self.appCode = appCode
        self.chainCode = chainCode
        self.url = url
        self.cert_path = cert_path

    '''
        public functions.
    '''
    def get_data(self, baseKey):
        funcName = "get"

        return self.__handle_with_key(self.userCode, self.appCode,
        self.chainCode, self.url, 
        self.cert_path, funcName, baseKey)
    
    def delete_data(self, baseKey):
        funcName = "delete"
        
        return self.__handle_with_key(self.userCode, self.appCode,
        self.chainCode, self.url, 
        self.cert_path, funcName, baseKey)
    
    def get_history(self, baseKey):
        funcName = "getHistory"

        return self.__handle_with_key(self.userCode, self.appCode,
        self.chainCode, self.url, 
        self.cert_path, funcName, baseKey)

    def save_data(self, baseKey, baseInfo):
        funcName = "set"

        return self.__handle_with_key_and_value(self.userCode, self.appCode,
        self.chainCode, self.url, self.cert_path, 
        funcName, baseKey, baseInfo)        

    def update_data(self, baseKey, baseInfo):
        funcName = "update"

        return self.__handle_with_key_and_value(self.userCode, self.appCode,
        self.chainCode, self.url, self.cert_path,
        funcName, baseKey, baseInfo)
       
    '''
        private functions.
    '''
    def __handle_with_key(self, userCode, appCode, chainCode, url, cert_path, funcName, baseKey):
        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        else:
            payload = userCode + appCode + chainCode + funcName + baseKey
            logger.info('baseKey: %s', baseKey)
            logger.info('string waited to sign: %s', payload)

            mac = myecdsa256.ecdsa_sign(payload, cert_path + '/private_key.pem').decode()
            logger.info('mac in base64: %s', mac)

            data = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                    "body": {"chainCode": chainCode, "funcName": funcName, "args": [baseKey]},
                    "mac": mac}
            headers = {'content-type': 'application/json'}
            res = requests.post(url, headers=headers, json=data, verify= cert_path + '/bsn_https.pem')
            return res.json()

    def __handle_with_key_and_value(self, userCode, appCode, chainCode, url, cert_path, funcName, baseKey, baseInfo):
        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        elif len(baseInfo.strip()) == 0:
            logger.error("baseInfo can not be null")
        else:
            logger.info('baseKey: %s', baseKey)
            logger.info('baseInfo: %s', baseInfo)
            list = {"baseKey": baseKey, "baseValue": baseInfo}
            list = json.dumps(list)
            payload = userCode + appCode + chainCode + funcName + list
            logger.info('string waited to sign: %s', payload)

            mac = myecdsa256.ecdsa_sign(payload, cert_path + '/private_key.pem').decode()
            logger.info('mac in base64: %s', mac)

            data = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                    "body": {"chainCode": chainCode, "funcName": funcName, "args": [list]},
                    "mac": mac}
            headers = {'content-type': 'application/json'}
            res = requests.post(url, headers=headers, json=data, verify= cert_path + '/bsn_https.pem')
            return res.json()
