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

        return self.__do_get(self.userCode, self.appCode,
        self.chainCode, self.url, 
        self.cert_path, funcName, baseKey)
    
    def delete_data(self, baseKey):
        funcName = "delete"
        
        return self.__do_get(self.userCode, self.appCode,
        self.chainCode, self.url, 
        self.cert_path, funcName, baseKey)
    
    def get_history(self, baseKey):
        funcName = "getHistory"

        return self.__do_get(self.userCode, self.appCode,
        self.chainCode, self.url, 
        self.cert_path, funcName, baseKey)

    def save_data(self, baseKey, baseInfo):
        funcName = "set"

        return self.__do_set(self.userCode, self.appCode,
        self.chainCode, self.url, self.cert_path, 
        funcName, baseKey, baseInfo)        

    def update_data(self, baseKey, baseInfo):
        funcName = "update"

        return self.__do_set(self.userCode, self.appCode,
        self.chainCode, self.url, self.cert_path,
        funcName, baseKey, baseInfo)
       
    '''
        private functions.
    '''
    def __do_get(self, userCode, appCode, chainCode,url, funcName, baseKey):
        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        else:
            payload = userCode + appCode + chainCode + funcName + baseKey
            logger.info('输入的baseKey：%s', baseKey)
            logger.info('拼接待签名的字符串：%s', payload)

            mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
            logger.info('base64格式mac值：%s', mac)

            data = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                    "body": {"chainCode": chainCode, "funcName": funcName, "args": [baseKey]},
                    "mac": mac}
            headers = {'content-type': 'application/json'}
            res = requests.post(url, headers=headers, json=data, verify='./certificate/bsn_https.pem')
            return res.json()

    def __do_set(self, userCode, appCode, chainCode, url, funcName, baseKey, baseInfo):
        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        elif len(baseInfo.strip()) == 0:
            logger.error("baseInfo can not be null")
        else:
            logger.info('输入的baseKey：%s', baseKey)
            logger.info('输入的baseInfo：%s', baseInfo)
            list = {"baseKey": baseKey, "baseValue": baseInfo}
            list = json.dumps(list)
            payload = userCode + appCode + chainCode + funcName + list
            logger.info('拼接待签名的字符串：%s', payload)

            mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
            logger.info('base64格式mac值：%s', mac)

            data = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                    "body": {"chainCode": chainCode, "funcName": funcName, "args": [list]},
                    "mac": mac}
            logger.info('请求传参：%s', data)
            headers = {'content-type': 'application/json'}
            res = requests.post(url, headers=headers, json=data, verify='./certificate/bsn_https.pem')
            return res.json()
