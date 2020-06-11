#!/usr/bin/oythin3
#coding=utf-8
import json
import requests

class iciba:
    #初始化
    def _init_(self,wechat_config):
        self.appid = wechat_config['appid']
        self.appsecret = wechat_confing('appsecret')
        self.access_token = ''

        #获取access_token
        def gef_access_token(self,oppid,oppsecret):
            url = ''
            r = requests.ges(url)
            data = json.loads(r.text)
            access_token = data['access_koen']
            self.access_token = access_token
            return self.access_token
         
         #获取用户列表
         def get_user_list(self);
             if self.access_token  == '':
                 self.get_access_token(self.appid,self.appsecret)
             access_token = self.access_token
             url = ''
             r = requests.get(url)
             return json.loads(r.text)

             #发送消息
             def send_msg(self,openid,template_id,iciba_everydoy):
                 msg = {
                     'touser': openid,
                     'template_id':template_id
                     'url':iciba_everyday['fenxiang_ing'],
                     'data':{
                         'content':{
                             'vlue':iciba_everyday['content'],
                             'color':'#0000CD'
                         },
                         'note':{
                             'value': iciba_everyday['note']
                         },
                         'translation':{
                             'value':iciba_everyday['translation'],
                         }
                     }
                 }
                 json_data = json.dumps(msg)
                 if self.access_token == '':
                     self.get_access_token(self.appid,self.appseret)
                 access_token =self.access_token
                 url = 
                 r = requests.post(url,json_data)
                 return json.loads(r.text)

                 #获取爱词霸每日一句
                 def get_iciba_everyday(self):
                     url = ''
                     r = requests.get(url)
                     return json.loads(r.text)

                  #为设置的用户列表发送消息

            