import requests
from .common.loggers import logger
from .common import myecdsa256
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
            return {"success": False, "payload": "incorrect basekey"}
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
            return  self.__handle_res(res.json(), funcName)

    def __handle_with_key_and_value(self, userCode, appCode, chainCode, url, cert_path, funcName, baseKey, baseInfo):
        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
            return {"success": False, "payload": "incorrect basekey"}
        elif len(baseInfo.strip()) == 0:
            logger.error("baseInfo can not be null")
            return {"success": False, "payload": "incorrect baseInfo"}
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
            return  self.__handle_res(res.json(), funcName)

    def __handle_res(self, payloadDicted, funcName):
        try:
            if payloadDicted['header']['code'] == 0:
                txId = payloadDicted['body']['blockInfo']['txId']
                context = self.__handle_payload(payloadDicted['body']['ccRes']['ccData'], funcName)
                return {"success": True,"payload": {"txId": txId, "context": context}}
            else:
                error_msg = payloadDicted["header"]
                logger.error('error when req from node: %s', error_msg)
                return {"success": False, "payload": error_msg}
        except:
            logger.error('error when req from node: %s', payloadDicted)
            return {"success": False, "payload": "unknow error"}
    def __handle_payload(self, payload, funcName):
        if funcName in ["save", "get", "delete", "update"]:
            return payload
        elif funcName == "getHistory":
            return json.loads(payload)
        

