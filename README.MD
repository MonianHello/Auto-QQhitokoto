Auto-QQhitokoto
--------------
 MonianHello
 2020.07.08
--------------
(代码写的和屎一样，在线等pr)

**所需前置：** 
 1. 酷Q Air 
 2. CQHTTP
 3. Python 3.x

**使用帮助:**

- 默认酷Q HTTP端口为5700，有需要自行修改api_url
- encode仅供调试使用

| 参数 | 说明 | 
| -----| ---- |
| text | 返回纯洁文本 | 
| json | 返回格式化后的 JSON 文本 | 
| js |返回指定选择器的同步调用函数。默认选择器为：.hitokot|
| 其他 |返回格式化后的 JSON 文本 |

- maintype后的参数类型
   + `1` 将对象设置为群，id处填写群号
   + `2` 将对象设置为个人，id处填写对方QQ号
   + `3` 将对象设置为讨论组，id处填写讨论组号
   + 设置为其他数字会报错

- delay为发送延时，单位是秒(s)

- num为发送次数，发送失败也会计算次数