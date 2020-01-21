import requests
from common.loggers import logger
from common import myecdsa256
import json


class Operator:
    '''
        public functions.
    '''
    def get_data(self, baseKey, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "get"

        return self.__do_get(userCode, appCode, chainCode, funcName, baseKey, url)

    def save_data(self, baseKey, baseInfo, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "set"

        return self.__do_set(userCode, appCode, chainCode, funcName, baseKey, baseInfo, url)        

    def update_data(self, baseKey, baseInfo, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "update"

        return self.__do_set(userCode, appCode, chainCode, funcName, baseKey, baseInfo, url)
    
    def delete_data(self, baseKey, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "delete"
        
        return self.__do_get(userCode, appCode, chainCode, funcName, baseKey, url)
    
    def get_history(self, baseKey, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "getHistory"

        return self.__do_get(userCode, appCode, chainCode, funcName, baseKey, url)
       
    '''
        private functions.
    '''
    def __do_get(self, userCode, appCode, chainCode, funcName, baseKey, url):
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

    def __do_set(self, userCode, appCode, chainCode, funcName, baseKey, baseInfo, url):
        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        elif len(baseInfo.strip()) == 0:
            logger.error("baseInfo can not be null")
        else:
            logger.info('输入的baseKey：%s', baseKey)
            logger.info('输入的baseKey：%s', baseKey)
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
