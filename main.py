# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/10/23 12:37:06
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
'''

# here put the import lib
import requests as rq
from hashlib import md5
import time

class TB(object):
    def __init__(self, appkey, appsecret):
        self.root_url = "https://eco.taobao.com/router/rest"
        self.appkey = appkey
        self.appsecret = appsecret

    def public_data(self, method=None, sign=None, session=None):
        datas = {
            "app_key": self.appkey,
            "timestamp": self.__time_now__(),
            "format": "json",
            "v": "2.0",
            "sign_method": "md5"
        }
        if session:
            datas.update({"session": session})
        if method:
            datas.update({"method": method})
        if sign:
            datas.update({"sign": sign})
        return datas

    def __time_now__(self):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return now_time

    def sign(self, data):
        parameters = "%s%s%s" % (self.appsecret,str().join('%s%s' %(key, data[key]) for key in sorted(data.keys())),self.appsecret)
        sign = md5(parameters.encode('utf-8')).hexdigest().upper()
        return sign

    def get_time(self):
        methods = "taobao.time.get"
        pub_data = self.public_data(method=methods)
        sign_strs = self.sign(pub_data)
        pub_data.update({"sign": sign_strs})
        print("post data", pub_data)
        sigm_get = rq.post(self.root_url, data=pub_data)
        print(sigm_get.json())

    def tbk_kouling_jiexi(self, kouling: str):
        methods = "taobao.wireless.share.tpwd.query"
        pub_data = self.public_data(method=methods)
        pub_data.update({"password_content": kouling})
        sign_strs = self.sign(pub_data)
        pub_data.update({"sign": sign_strs})
        data_get = rq.post(self.root_url, data=pub_data)
        print(data_get.json())

    def tbk_tuiguangquan(self, item_id: int = None, activity_id: str = None):
        methods = "taobao.tbk.coupon.get"
        pub_data = self.public_data(method=methods)
        if item_id:
            pub_data.update({"item_id": item_id})
        if activity_id:
            pub_data.update({"activity_id": activity_id})
        sign_strs = self.sign(pub_data)
        pub_data.update({"sign": sign_strs})
        print(pub_data)
        data_get = rq.post(self.root_url, data=pub_data)
        print(data_get.json())

    def tbk_kouling_create(self, user_id: str = None, text: str = None, url: str = None, logo: str = None):
        methods = "taobao.tbk.tpwd.create"
        pub_data = self.public_data(method=methods)
        if user_id:
            pub_data.update({"user_id": user_id})
        if text:
            pub_data.update({"text": text})
        if url:
            pub_data.update({"url": url})
        if logo:
            pub_data.update({"logo": user_id})
        sign_strs = self.sign(pub_data)
        pub_data.update({"sign": sign_strs})
        data_get = rq.post(self.root_url, data=pub_data)
        print(data_get.json())

    def tbk_item_info(self,num_iids:str,platform:int=None,ip:str=None):
        methods = "taobao.tbk.item.info.get"
        pub_data = self.public_data(method=methods)
        pub_data.update({"num_iids":num_iids})
        if platform:
            pub_data.update({"platform": platform})
        if ip:
            pub_data.update({"logo": ip})
        sign_strs = self.sign(pub_data)
        pub_data.update({"sign": sign_strs})
        data_get = rq.post(self.root_url, data=pub_data)
        print(data_get.json())
