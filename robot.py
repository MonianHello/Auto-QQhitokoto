import requests
import time
encode = "text"
maintype = 2
id = 2860421919
delay = 2
num = 10
###############
# MonianHello
# 2020.07.08
#
#
# 默认酷Q HTTP端口为5700，有需要自行修改api_url
#
# encode仅供调试使用
#   参数	    说明
#   text	返回纯洁文本
#   json	返回格式化后的 JSON 文本
#   js	    返回指定选择器的同步调用函数。默认选择器为：.hitokoto
#   其他	    返回格式化后的 JSON 文本
#
# maintype后的参数类型
#   1 将对象设置为群，id处填写群号
#   2 将对象设置为个人，id处填写对方QQ号
#   3 将对象设置为讨论组，id处填写讨论组号
#   设置为其他数字会报错
#
# delay为发送延时，单位是秒(s)
#
# num为发送次数，发送失败也会计算次数
###############
hitokotoAPI = "https://v1.hitokoto.cn/?encode="+encode
for i in range(num):
    if i == num:
        break
    if maintype == 1:
                yiyan = requests.get(hitokotoAPI)
                says = yiyan.text
                QQtype = "send_group_msg"
                sendtype = 'group_id'
                api_url = 'http://127.0.0.1:5700/' + QQtype
                data = {
                    sendtype: id,
                    'message': says,
                    'auto_escape': False
                }
                r = requests.post(api_url, data=data)
                if "ok" in r.text:
                    print("[info][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]已成功发送: " + says)
                    time.sleep(delay)
                else:
                    print("[error][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]发送失败")
                    time.sleep(delay)
    if maintype == 2:
                yiyan = requests.get(hitokotoAPI)
                says = yiyan.text
                QQtype = "send_private_msg"
                sendtype = 'user_id'
                api_url = 'http://127.0.0.1:5700/' + QQtype
                data = {
                    sendtype: id,
                    'message': says,
                    'auto_escape': False
                }
                r = requests.post(api_url, data=data)
                if "ok" in r.text:
                    print("[info][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]已成功发送: " + says)
                    time.sleep(delay)
                else:
                    print("[error][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]发送失败")
                    time.sleep(delay)
    if maintype == 3:
                yiyan = requests.get(hitokotoAPI)
                says = yiyan.text
                QQtype = "send_discuss_msg"
                sendtype = 'discuss_id'
                api_url = 'http://127.0.0.1:5700/' + QQtype
                data = {
                    sendtype: id,
                    'message': says,
                    'auto_escape': False
                }
                r = requests.post(api_url, data=data)
                if "ok" in r.text:
                    print("[info][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]已成功发送: " + says)
                    time.sleep(delay)
                else:
                    print("[error][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]发送失败")
                    time.sleep(delay)
                #print("[error][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]参数错误，程序退出")
                #quit()
num = str(num)
print("[info][" + time.strftime("%Y-%m-%d %H:%M:%S") + "]达到循环次数"+ num +"次，程序退出")






