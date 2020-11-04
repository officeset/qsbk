# python

## 库函数

需要下载 qrcode ，PIL  ，Image，pillow，numpy，MyQR，imageio。

下载方式：在cmd中输入pip  install  xxx（库函数名）

## 纯文本二维码

简单制作方法

```python
import qrcode
data="www.baidu.com"
img = qrcode.make(data)
img.save('test.png')
#文件默认与py文件存在一个路径下
```

配置二维码的参数

```python
import qrcode
qr = qrcode.QRCode(
        version = 1, #二维码的实际大小级别(1 - 40)
        error_correction = qrcode.constants.ERROR_CORRECT_L, #二维码的容错级别(L,M(默认),Q,H)
        box_size = 10, #整张二维码图片的大小
        border = 5, #二维码背景边框宽度
    )
data = raw_input() #输入需要转换的数据
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image()
img.save('test.png') #将图片保存为png(注意其他格式可能会出现问题)

```

二维码带logo

```python
from PIL import Image
import qrcode//引入库函数

qr = qrcode.QRCode(//配置二维码参数
    version=5, 
    error_correction=qrcode.constants.ERROR_CORRECT_H,
     box_size=8, 
     border=4)

qr.add_data("http://www.jason-niu.com")//数据
qr.make(fit=True)
img = qr.make_image()
img = img.convert("RGBA")//保证logo的图像色彩两句相同代码缺一不可
# logo="D:/favicon.jpg"
icon = Image.open("素材.gif")
img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
#确认logo在二维码上的具体位置
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon) //图片粘贴（图标，（w，h），图标） 
# img.show()
img.save('二维码logo.png')//保存图片

```

## 动态二维码

```python
from MyQR import myqr
myqr.run(
    words='www.baidu.com',
    # 扫描二维码后，显示的内容，或是跳转的链接
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='1.jpg',  # 图片所在目录，可以是gif，png，pig等格式
    colorized=True,  # 黑白(False)还是彩色(True)
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name='Python.gif',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )
```

## 二维码识别

下载pyzbar库

```python
import os
import qrcode
from PIL import Image
from pyzbar import pyzbar

def decode_qr_code(code_img_path):
    if not os.path.exists(code_img_path)://判断该路径是否存在
        raise FileExistsError(code_img_path)

    # Here, set only recognize QR Code and ignore other type of code
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])

result=decode_qr_code("test.png")
if len(result):
	print(result[0].data.decode("utf-8"))

```

## 多线程

直接使用threading.Thread进行多线程实现，其中target为要执行的方法或函数，args为参数列表（方法或函数需要的值），结尾加，因为是元组。

```python
def pa(n):
    for i in range(10):
        time.sleep(2)
        print("这是线程"+str(n))

def pa2(n):
    for i in range(10):
        time.sleep(1)
        print("这是线程"+str(n))

import threading,time
def run(n):
    print("task  ",n)
    time.sleep(2)

start_time=time.time()
t1=threading.Thread(target=pa,args=(1,))
t2=threading.Thread(target=pa2,args=(3,))

t1.start()
t2.start()
```

使用多线程继承threading.Thread创建类示例

```python
import threading
import time


def hello():
    print("hello")


class Mythread(threading.Thread):
    def __init__(self, n, name, hello):
        super(Mythread, self).__init__()
        self.n = n
        self.name = name
        self.hello = hello

    def run(self):
        for i in range(10):
            self.hello()
            time.sleep(self.n)
            print("这是第" + str(self.n) + "个线程,名称为" + self.name)


t1 = Mythread(1, "前进", hello)
t2 = Mythread(2, "长城", hello)

t1.start()
t2.start()

```

## 正则匹配

```python
"""
### 常用元字符 ###
1 .:匹配任何一个字符;
2 ^:匹配除去所列首个字符外的所有字符; ^\d表示必须以数字开头。
3 $:匹配字符串的尾部字符  \d$表示必须以数字结束
4 []:由一对方括号括起来的字符，表明一个字符集合，能够匹配包含在其中的任意一个字符。’-‘ 减号来指定一个字符集合的范围。例子：[a-zA-Z][^a-zA-Z]
5 | 将两个规则并列起来，注意是匹配两边所有的规则 
    要匹配 ‘I have a dog’或’I have a cat’，需要写成r’I have a (?:dog|cat)’ ，而不能写成 r’I have a dog|cat’
5 (?: )  如果想限定它的有效范围，必需使用一个无捕获组 ‘(?: )’包起来
6 \d  匹配数字,这是一个以’\’开头的转义字符，’\d’表示匹配一个数字，即等价于[0-9]
7 \D 匹配非数字 这个是上面的反集，即匹配一个非数字的字符，等价于[^0-9]。注意它们的大小写
   下面我们还将看到Python的正则规则中很多转义字符的大小写形式，代表互补的关系。
8 \w 匹配字母和数字 匹配所有的英文字母和数字，即等价于[a-zA-Z0-9]。 \W  等价 [^a-zA-Z0-9]
9 \s 匹配间隔符  即匹配空格符、制表符、回车符等表示分隔意义的字符，它等价于[ \t\r\n\f\v]。（注意最前面有个空格)  补集：  \S 
10 \A 匹配字符串开头  匹配字符串的开头。它和’^’的区别是，’\A’只匹配整个字符串的开头，即使在’M’模式下，它也不会匹配其它行的行首。
11 \Z 匹配字符串结尾  匹配字符串的结尾。它和’$’的区别是，’\Z’只匹配整个字符串的结尾，即使在’M’模式下，它也不会匹配其它各行的行尾。
12 \b’ 匹配单词边界  它匹配一个单词的边界，比如空格等，不过它是一个‘0’长度字符，它匹配完的字符串不会包括那个分界的字符。
       而如果用’\s’来匹配的话，则匹配出的字符串中会包含那个分界符
13 \B 匹配非边界 它同样是个0长度字符。re.findall( r’\Bbc\w+’ , s )     #匹配包含’bc’但不以’bc’为开头的单词
    ['bcde']  #成功匹配了’abcde’中的’bcde’，而没有匹配’bcd’
14 (?# ) 注释 Python允许你在正则表达式中写入注释
### 重复 规则 ###
15 *   0或多次匹配  
16 +  1次或多次匹配  表示匹配前面的规则至少1次，可以多次匹配
17 ?  0或1次匹配 只匹配前面的规则0次或1次
### 精确匹配和最小匹配  ###
18 {m}    精确匹配m次
   {m,n}  匹配最少m次，最多n次。(n>m)  指定最少3次：{3,}  最大为5次：{,5}
    例子： re.findall( r’\b\d{3}\b’ , s )            # 寻找3位数
19 ‘*?’ ‘+?’ ‘??’ 最小匹配
   ‘*’ ‘+’ ‘?’通常都是尽可能多的匹配字符（贪婪匹配）。有时候我们希望它尽可能少的匹配。
   #例子 re.match(r'^(\d+)(0*)$', '102300').groups()  #('102300', '') 
   #     re.match(r'^(\d+?)(0*)$', '102300').groups() #('1023', '00')
   
### 前向界定与后向界定 ###
20 (?<=…) 前向界定  括号中’…’代表你希望匹配的字符串的前面应该出现的字符串。
    前向界定括号中的表达式必须是常值，也即你不可以在前向界定的括号里写正则式
    re.findall( r’(?<=[a-z]+)\d+(?=[a-z]+)' , s )          # 错误的用法
21 (?=…)  后向界定
   不过如果你只要找出后面接着有字母的数字，你可以在后向界定写正则式：
   re.findall( r’\d+(?=[a-z]+)’, s )
22 (?<!...) 前向非界定
只有当你希望的字符串前面不是’…’的内容时才匹配
23 (?!...) 后向非界定
只有当你希望的字符串后面不跟着’…’内容时才匹配。
### 使用组 ###
24  ()    包含在’()’中的内容，而虽然前面和后面的内容都匹配成功了，却并不包含在结果中,
    用group()或group(0)返回匹配的所有结果，用 group(1)，(2)...返回第1，2...个()里面的内容
25  (?(id/name)yes-pattern|no-pattern) 判断指定组是否已匹配，执行相应的规则
    这个规则的含义是，如果id/name指定的组在前面匹配成功了，则执行yes-pattern的正则式，否则执行no-pattern的正则式。
    
### 注意 ### 
碰到字符串里面有以上的符号的或者像是 _ - 等字符  要加转义符 \
"""
import re
 
p1 = '.+'
p2 = '[^bc]'
p3 = '[ab$]'
p4 = '[a-z]'
string = 'abc'
m = re.match(p1,string)
n = re.match(p2,string)
l = re.match(p3,string) #?
o = re.match(p4,string)
#m.group() #abc 
#n.group() # a
#l.group() # a
o.group() # a
 
 
s= '12 34\n56 78\n90'
print(re.findall( r'^\d+' , s , re.M ))        #匹配位于行首的数字
print(re.findall( r'\A\d+', s , re.M ))        #匹配位于字符串开头的数字
print(re.findall( r'\d+$' , s , re.M ))          #匹配位于行尾的数字
print(re.findall( r'\d+\Z', s , re.M ))       #匹配位于字符串尾的数字
 
s1 =  'abc abcde bc bcd'
print(re.findall( r'\bbc\b', s1 ))      #匹配一个单独的单词 ‘bc’ ，而当它是其它单词的一部分的时候不匹配
 
 
### 综合例子  ###
 
s2 = 'aaa bbb111 cc22cc 33dd'
re.findall( r'\b[a-z]+\d*\b' , s2 )      # ['aaa', 'bbb111']       #必须至少1个字母开头，以连续数字结尾或没有数字，并且首尾为边界符
 
s3 =  '123 10e3 20e4e4 30ee5'
re.findall( r'\b\d+[eE]?\d*\b' , s )  # ['123', '10e3']   这样就可以把科学计数法记录的数字也拿出来了
 
s4  = '/* part 1 */ code /* part 2 */' # 找出 C++注释
re.findall(r'/\*.*?\*/',s4)   # ['/* part 1 */', '/* part 2 */']   #  .*?  表示匹配任意一个字符0次或多次，加？表示尽可能少匹配,要加转义符 \
 
 
re.findall( r'(?<=/\*).+?(?=\*/)',s4)                                   # 不希望匹配的结果把’/*’和’*/’也包括进来
 
s5 =  'aaa111aaa , bbb222 , 333ccc'
#re.findall( r'(?<=[a-z]+)\d+(?=[a-z]+)' , s5 )   # 前向错误 ，后向可以  # 要匹配包夹在字母中间的数字 
            
re.findall (r'[a-z]+(\d+)[a-z]+' , s5 )          # 使用group
 
# 下面使用组！#
s6 = 'aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'
re.findall( r'([a-z]+)\d+([a-z]+)' , s6 )           # [('aaa', 'aaa'), ('fff', 'ggg')]  # 找出中间夹有数字的字母
 
#(?P<name>…)’ 命名组  ,‘(?P=name)’ 调用已匹配的命名组
re.findall( r'(?P<g1>[a-z]+)\d+(?P=g1)' , s6 )  # ['aaa']   # 找出被中间夹有数字的前后同样的字母 fff777ggg不满足
 
# \number       通过序号调用已匹配的组  ，上面的也可以写为
re.findall( r'([a-z]+)\d+\1' , s6 )   #['aaa'] 
 
s7 = '111aaa222aaa111 , 333bbb444bb33'
re.findall( r'(\d+)([a-z]+)(\d+)(\2)(\1)' , s7 )   #[('111', 'aaa', '222', 'aaa', '111')] #找出完全对称的 数字－字母－数字－字母－数字 中的数字和字母
 
# (?(id/name)yes-pattern|no-pattern)’ 判断指定组是否已匹配，执行相应的规则
s8 = '<usr1@mail1>  usr2@maill2'  #要匹配一些形如 usr@mail 的邮箱地址，有的写成< usr@mail >有的没有，要匹配这两种情况
re.findall( r'(<)?\s*(\w+@\w+)\s*(?(1)>)' , s8 )  #[('<', 'usr1@mail1'), ('', 'usr2@maill2')] 
```

