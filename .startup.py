import configparser
from sdk import Operator
config = configparser.ConfigParser()
config.read('config.ini')
config_dicted = dict(config['bsn_info'])
op = Operator(config_dicted["user_code"], config_dicted["app_code"],
        config_dicted["chain_code"], config_dicted["url"],
        config_dicted["cert_path"])
