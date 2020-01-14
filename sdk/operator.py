
import requests
from common.loggers import logger
from common import myecdsa256

class Operator:
    # 获取链上数据
    def get_data(self, baseKey, url):
            userCode = "reddate"
            appCode = "CL1851016378620191011150518"
            chainCode = "cc_base"
            funcName = "get"

            if len(baseKey.strip()) == 0:
                logger.error("baseKey can not be null")
            else:
                return self.__do_get_data(userCode, appCode, chainCode, funcName, baseKey, url)
    def __do_get_data(self, userCode, appCode, chainCode, funcName, baseKey, url):
        payload = userCode + appCode + chainCode + funcName + baseKey
        logger.info('拼接待签名的字符串：%s', payload)

        mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
        logger.info('base64格式mac值：%s', mac)

        data = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                    "body": {"chainCode": chainCode, "funcName": funcName, "args": [baseKey]},
                    "mac": mac}
        headers = {'content-type': 'application/json'}
        res = requests.post(url, headers=headers, json=data, verify='./certificate/bsn_https.pem')
        return res.json()
            
    # # 存储链上数据
    # def save_data():
    #     print("save")
    # # 查询块
    # def get_block_info(txId, url):
    #     userCode = "reddate"
    #     appCode = "CL1851016378620191011150518"
    #     return do_get_data2(userCode,appCode, txId, url)
        
    # def do_get_data2(userCode, appCode, txId, url):
    #     payload = userCode + appCode + txId
    #     logger.info('拼接待签名的字符串：%s', payload)

    #     mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
    #     logger.info('base64格式mac值：%s', mac)

    #     data = {"header": {"userCode": userCode, "appCode": appCode},
    #                 "body": {"txId": txId},
    #                 "mac": mac}
    #     headers = {'content-type': 'application/json'}
    #     r = requests.post(url, headers=headers, json=data, verify='./certificate/bsn_https.pem')
    #     return r