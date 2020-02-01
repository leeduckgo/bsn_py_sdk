# -*- coding:utf-8 -*-


from flask import (
    request,make_response, render_template, flash)
from app import app
import json
from functools import wraps
from blockchain import Blockchain

blockchain = Blockchain()

#===init plugins====
'''此处是插件'''
"""
    api follow the RESTFUL: http://www.ruanyifeng.com/blog/2014/05/restful_api.html
"""

# === api ===

@app.route('/api/get_data', methods=['get'])
def get_data():


@app.route('/api/get_history', methods=['get'])
def get_history():



@app.route('/api/delete_data', methods=['get'])
def delete_data():



@app.route('/api/save_data', methods=['post'])
def save_data():

@app.route('/api/update_data', methods=['post'])
def update_data():

#===cross_domain====
'''这个是允许跨域的代码'''

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun

#===   pages    ===
'''此处是各个页面'''
@app.route('/page_name',methods=['POST'])
@allow_cross_domain
def the_function():
    id=msg_translate_from_front(request)['id'] #与前端交互
    example=msg_translate_from_front(request)['example']

    # print("body:")
    # print(trans(request.get_data())) #body
    #
    # print("headers:")
    # print(request.headers) #header
    #
    # print("args:")
    # print(request.args) #args
    #
    # return json.dumps({"result":"success"})
    # #=======获取信息=========
    #
    # #从数据库获取所有记录
    # all_data=Father.query.all()
    #
    # #根据从前端获得的信息筛选出信息
    # a_data=Father.query.filter_by(id=id,example=example).all()
    #
    # #筛选出第一个匹配项
    # a_data=Father.query.filter_by(id=id,example=example).all()[0]
    #
    # #第一个匹配项中的某个属性
    # an_attribute=Father.query.filter_by(id=id,example=example).all()[0].example
    #
    # #获取一列
    # the_col=abstract_col(Father.query.all(),"id")
    # #=======获取信息=========
    #
    # #=====修改数据库信息======
    #
    # #修改某条信息
    # Father.query.filter_by(id=id).update({Father.id:id,\
    #                                                     Father.example:Father.example})
    # db.session.commit()
    #
    # #新增某条信息
    #
    # #=====修改数据库信息======
    # an_item=Father()
    # an_item.id = id
    # an_item.example="this_is an example"
    # db.session.add(an_item)
    # db.session.commit()

    return msg_traslate_to_front(all_data)


@app.route('/', methods=['get', 'post'])
def index():
    return "HELLO"
    # if request.method == 'POST':
    #     name = request.form.get('user_name')
    #     password = request.form.get('password')

    #     try:
    #         money = float(request.form.get('money'))
    #     except:
    #         return json.dumps({"result": "money_error"})

    #     if name == "suibe" and password == "123":
    #         return "aha"
    #     else:
    #         return json.dumps({"result": "name_or_password_error"})

    # return render_template('index.html')


@app.route('/query', methods=['post'])
def query():
    name = request.form.get('user_name')
    password = request.form.get('password')

    if name == "suibe" and password == "123":
        res = "balance is: " + str(query_addr("0x0199deC6E8e00112fb596Af541803d1b9593AbBd"))+\
            "<br>url: <a href='https://ropsten.etherscan.io/address/0x769699506f972a992fc8950c766f0c7256df601f'>https://ropsten.etherscan.io/address/0x769699506f972a992fc8950c766f0c7256df601f</a>"
        return res
    else:
        return json.dumps({"result": "name_or_password_error"})


@app.route('/pay', methods=['post'])
def pay():
    name = request.form.get('user_name')
    password = request.form.get('password')

    try:
        money = float(request.form.get('money'))
    except:
        return json.dumps({"result": "money_error"})

    if name == "suibe" and password == "123":
        url = "https://ropsten.etherscan.io/tx/" + str(transfer('0xbB3092922EC650281d5A95BC67Fa932CC19ceE01', int(money)*100))
        return "链上交易:  " + "<a href='" + url + "'>" + url + "</a>"
    else:
        return json.dumps({"result": "name_or_password_error"})

def query_addr(addr):
    my_provider = Web3.HTTPProvider('https://ropsten.infura.io/v3/2b5bd86dfba2472d9b3b9e65bcf3c350')
    w3 = Web3(my_provider)
    with open('erc20.json', 'r') as abi_definition:
        abi = json.load(abi_definition)
    contract = w3.eth.contract(abi=abi, address="0xAcCD5Abb2398A262D8F4848dCA6371C30ecb63ed")
    result = contract.functions.balanceOf("0x0199deC6E8e00112fb596Af541803d1b9593AbBd").call() /100
    return result


def transfer(to_addr, value):
    key = "9BDA4542DB17297AE7858B31274081B7E2704000201F57F13A86B4D659C98658"
    return do_transfer(key, to_addr, value)


def do_transfer(key, to_addr, value):
    my_provider = Web3.HTTPProvider('https://ropsten.infura.io/v3/2b5bd86dfba2472d9b3b9e65bcf3c350')
    w3 = Web3(my_provider)
    w3.eth.defaultAccount = "0x0199deC6E8e00112fb596Af541803d1b9593AbBd"
    with open('erc20.json', 'r') as abi_definition:
        abi = json.load(abi_definition)
    contract = w3.eth.contract(abi=abi, address="0xAcCD5Abb2398A262D8F4848dCA6371C30ecb63ed")
    print("正在交易，请耐心等待")
    account_address= Web3.toChecksumAddress("0x0199deC6E8e00112fb596Af541803d1b9593AbBd")
    tx = contract.functions.transfer(to_addr, value).buildTransaction({'nonce': w3.eth.getTransactionCount(account_address)})
    signed_tx = w3.eth.account.signTransaction(tx, key)
    tx_hash= w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.eth.waitForTransactionReceipt(tx_hash)['transactionHash'].hex()

#=== black code ===

'''Python格式=>前端数据'''
def msg_traslate_to_front(msg_all):
    try:
        msg_after_trans={msg_all[0].class_name:[]}

        for every_msg in msg_all:
            a_msg={}

            for every_vary in every_msg.class_varies:
                a_msg[every_vary]=every_msg.get_vary(every_vary)

            msg_after_trans[msg_all[0].class_name].append(a_msg)

        json_data=json.dumps(msg_after_trans)
        print("translate_to_front is {0}".format(json_data))
        #data format:{posts:[{a:b,c:d},{a:e,c:f}...]}
        return json_data
    except:
        return None

'''pretty json '''
def trans(payload):
    try:
        return json.loads(str(payload, "utf-8"))
        # return json.dumps(a_json, sort_keys=True, indent=4, separators=(',', ':'))
    except:
        print("not json")
        return payload


'''前端数据=>Python格式'''
def msg_translate_from_front(request):
    msg_data_old=request.form.to_dict()
    for i in msg_data_old:
        msg_data_new= json.loads(i)
    print("translate_from_front is {0}".format(msg_data_new))
    return msg_data_new

'''提取数据库中的列'''
def abstract_col(data, col_name):
    col = []
    for item in data:
        col.append(eval("item."+col_name))
    return col

