#!/usr/bin/env python3

from urllib import parse
import json
import time
import requests

# 变量
urlid = "i56CzmH"
urlid = "wjQAD1wYPbz07wwOrgdc5g"


# 提交密码返回结果
def submit(pwd):
    datamod['pwd'] = pwd
    res = s.post(url, data=datamod)
    print(f'{pwd}:{res.json()}')


# 新建会话
s = requests.Session()
# 设置请求headers伪装浏览器操作
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/65.0.3325.146 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': f'https://pan.baidu.com/share/init?surl={urlid}',
})
# 发送GET请求设置cookies
res = s.get("https://pan.baidu.com/share/init?surl=i56CzmH")

# 初始化请求URL
urlmode = {
    "surl": urlid,
    "t": int(time.time()),
    "channel": "chunlei",
    "web": 1,
    "app_id": "250528",
    "bdstoken": "null",
    "logid": "MTUyNTE0OTMzODIwMzAuMzc2MTM5ODg1ODg3ODc5OTQ",
    "clienttype": 0,
}
# 对请求URL编码和拼接
urlmode = parse.urlencode(urlmode)
url = f'https://pan.baidu.com/share/verify?{urlmode}'
# 提交密码的Form表单
datamod = {
    "pwd": "0000",
    "vcode": "",
    "vcode_str": "",
}

# 提交密码
submit("qwy1")
submit("1311")
submit("dZ23")

