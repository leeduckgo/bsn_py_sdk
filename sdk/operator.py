import requests
from common.loggers import logger
from common import myecdsa256
import json


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
        logger.info('输入的baseKey：%s', baseKey)

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

    def save_data(self, baseKey, baseInfo, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "set"

        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        elif len(baseInfo.strip()) == 0:
            logger.error("baseInfo can not be null")
        else:
            return self.__do_save_data(userCode, appCode, chainCode, funcName, baseKey, baseInfo, url)

        logger.info('用户输入baseKey：%s', baseKey)
        logger.info('用户输入baseInfo：%s', baseInfo)

    def __do_save_data(self, userCode, appCode, chainCode, funcName, baseKey, baseInfo, url):
        list = {"baseKey": baseKey, "baseValue": baseInfo}
        list = json.dumps(list)
        payload = userCode + appCode + chainCode + funcName + list
        logger.info('拼接待签名的字符串：%s', payload)

        mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
        logger.info('base64格式mac值：%s', mac)

        datas = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                 "body": {"chainCode": chainCode, "funcName": funcName, "args": [list]},
                 "mac": mac}
        logger.info('save_data请求传参：%s', datas)
        headers = {'content-type': 'application/json'}
        res = requests.post(url, headers=headers, json=datas, verify='./certificate/bsn_https.pem')
        return res.json()

    def update_data(self, baseKey, baseInfo, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "update"

        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        elif len(baseInfo.strip()) == 0:
            logger.error("baseInfo can not be null")
        else:
            return self.__do_update_data(userCode, appCode, chainCode, funcName, baseKey, baseInfo, url)

        logger.info('用户输入baseKey：%s', baseKey)
        logger.info('用户输入baseInfo：%s', baseInfo)

    def __do_update_data(self, userCode, appCode, chainCode, funcName, baseKey, baseInfo, url):
        list = {"baseKey": baseKey, "baseValue": baseInfo}
        list = json.dumps(list)
        payload = userCode + appCode + chainCode + funcName + list
        logger.info('拼接待签名的字符串：%s', payload)

        mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
        logger.info('base64格式mac值：%s', mac)

        datas = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                 "body": {"chainCode": chainCode, "funcName": funcName, "args": [list]},
                 "mac": mac}
        logger.info('update_data请求传参：%s', datas)
        headers = {'content-type': 'application/json'}
        res = requests.post(url, headers=headers, json=datas, verify='./certificate/bsn_https.pem')
        return res.json()

    def delete_data(self, baseKey, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "delete"

        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        else:
            return self.__do_delete_data(userCode, appCode, chainCode, funcName, baseKey, url)
        logger.info('输入的baseKey：%s', baseKey)

    def __do_delete_data(self, userCode, appCode, chainCode, funcName, baseKey, url):
        payload = userCode + appCode + chainCode + funcName + baseKey
        logger.info('拼接待签名的字符串：%s', payload)

        mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
        logger.info('base64格式mac值：%s', mac)

        data = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                "body": {"chainCode": chainCode, "funcName": funcName, "args": [baseKey]},
                "mac": mac}
        logger.info("delete_data传参：%s", data)
        headers = {'content-type': 'application/json'}
        res = requests.post(url, headers=headers, json=data, verify='./certificate/bsn_https.pem')
        return res.json()

    def get_history(self, baseKey, url):
        userCode = "reddate"
        appCode = "CL1851016378620191011150518"
        chainCode = "cc_base"
        funcName = "getHistory"

        if len(baseKey.strip()) == 0:
            logger.error("baseKey can not be null")
        else:
            return self.__do_get_history(userCode, appCode, chainCode, funcName, baseKey, url)
        logger.info('输入的baseKey：%s', baseKey)

    def __do_get_history(self, userCode, appCode, chainCode, funcName, baseKey, url):
        payload = userCode + appCode + chainCode + funcName + baseKey
        logger.info('拼接待签名的字符串：%s', payload)

        mac = myecdsa256.ecdsa_sign(payload, './certificate/private_key.pem').decode()
        logger.info('base64格式mac值：%s', mac)

        data = {"header": {"userCode": userCode, "appCode": appCode, "tId": "dc1d6010b7ff421dae0146f193dded09"},
                "body": {"chainCode": chainCode, "funcName": funcName, "args": [baseKey]},
                "mac": mac}
        logger.info("delete_data传参：%s", data)
        headers = {'content-type': 'application/json'}
        res = requests.post(url, headers=headers, json=data, verify='./certificate/bsn_https.pem')
        return res.json()
