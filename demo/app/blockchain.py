# -*- coding:utf-8 -*-
from bsn_sdk import Operator
import configparser

class Blockchain():
    def __init__(self):
        self.config = self.get_config()
        self.operator = Operator(self.config["user_code"], self.config["app_code"], 
        self.config["chain_code"], self.config["url"], self.config["cert_path"])
    def get_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return dict(config['bsn_info'])
    def get_data(self, key):
        return self.operator.get_data(key)
    def save_data(self, value):
        return self.operator.save_data(value)
    def update_data(self, key, value):
        return self.operator.update_data(key, value)
    def delete_data(self, key):
        return self.operator.delete_data(key)
    def get_history(self, key):
        return self.operator.get_history(key)