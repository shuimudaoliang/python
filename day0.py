str0 = '''
2019/04/22 10:45:47.860 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m|     126.86µs|   match|[97;44m GET     [0m /static/css/main.css
2019/04/22 10:45:47.931 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m|     53.431µs|   match|[97;44m GET     [0m /static/js/mSlider.min.js
2019/04/22 10:45:47.986 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m|    145.288µs|   match|[97;44m GET     [0m /static/img/weichatzanshang.jpeg
2019/04/22 10:45:47.986 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m| 113.731531ms|   match|[97;44m GET     [0m /static/js/bootstrap.js
2019/04/22 10:45:48.059 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m| 130.245609ms|   match|[97;44m GET     [0m /static/ace/src-noconflict/ext-language_tools.js
2019/04/22 10:45:48.123 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m| 126.031953ms|   match|[97;44m GET     [0m /static/img/wechat.jpeg
2019/04/22 10:45:50.114 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m| 2.184990357s|   match|[97;44m GET     [0m /static/ace/src-noconflict/ace.js
2019/04/22 10:45:50.679 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m| 2.754426401s|   match|[97;44m GET     [0m /static/js/sql_3.8.7.4.js
2019/04/22 10:45:53.644 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;42m 200 [0m|    106.132µs|   match|[97;44m GET     [0m /static/ace/src-noconflict/mode-sql.js
2019/04/22 10:45:53.814 [1;44m[D][0m [server.go:2741]  |  27.154.193.15|[97;43m 404 [0m|    192.382µs| nomatch|[97;44m GET     [0m /favicon.ico
2019/04/22 10:47:16.013 [1;44m[D][0m [server.go:2741]  |  111.199.63.14|[97;42m 200 [0m|   1.186828ms|   match|[97;44m GET     [0m /     r:/
2019/04/22 10:47:17.195 [1;44m[D][0m [server.go:2741]  |180.165.189.254|[97;42m 200 [0m|   1.127464ms|   match|[97;44m GET     [0m /     r:/
2019/04/22 10:47:17.295 [1;44m[D][0m [server.go:2741]  |180.165.189.254|[97;42m 200 [0m|    127.065µs|   match|[97;44m GET     [0m /static/css/main.css
2019/04/22 10:47:18.017 [1;44m[D][0m [server.go:2741]  |180.165.189.254|[97;42m 200 [0m|    168.517µs|   match|[97;44m GET     [0m /static/ace/src-noconflict/ext-language_tools.js
2019/04/22 10:47:18.021 [1;44m[D][0m [server.go:2741]  |180.165.189.254|[97;42m 200 [0m|     72.501µs|   match|[97;44m GET     [0m /static/js/mSlider.min.js
'''
log_list = str0.split("\n")
for s in log_list:
    log_line = s.split(" ")
    # print("_".join(log_line[0:2]))


#测试
str0 = "a b c"
assert str0.split(" ") == ['a','b','c']
assert " ".join(str0.split(" ")) == str0

str1 = "axxbxxc"
assert str1.split("xx") == ['a','b','c']
assert "xx".join(str1.split("xx")) == str1


# #思路 
# 1. 循环比对两个字符串的第一个字符
# 2. 找到第一个字符相同的位置i
# 3. 从位置i开始比对j个字符，如果匹配，记录之前找到的串
# 4. 如果不匹配，从i+1继续走第一步
str1 = "abcxxxbxxxcgcc"

def mylen(str):
    i = 0   #定义下标
    while True:
        try:
            c = str[i] #取个个字符也就取出字符的位置了，为了取下标要写取出字符，而这个字符是不需要的
            # print(c)
            i = i + 1
        except:
            break
    return print(i)


def mysplit(stringstr, splitchar):
    templist = []
    for i in range(len(stringstr)): #跟字符下标索引相关
        index = stringstr.find(splitchar) #找到字符串中与分隔符第一位置相同的位置
        if index == -1: #没有找到则全部插入列表
            templist.append(stringstr)
            break
        else: #找到了话
            templist.append(stringstr[0:index]) #字符串从开始到找到的位置插入列表
            stringstr = stringstr[index+len(splitchar):len(stringstr)] #从开始找到的位置加上分割字符的长度来重新定义截断的字符串
    return print(templist) #这个是最开始没有或者最后没有找到返回 退出


list = ['abc','cba','ddd']



def myjoin(slist, joinchar):
    mystring =''
    for i in slist:
        if i != slist[-1]: #列表的最后一个之前的处理直接拼接
            mystring = mystring+i+joinchar
    mystring = mystring+slist[-1] #列表最后一个考虑
    return print(mystring)  #字符串返回需要print


str0 ='abc fdafda fdafda fada'



##day1
str0 = " a b c "
assert str0.strip(" ") == "a b c"

str1 = " a b c    "
assert str1.strip(" ") == "a b c"

str2 = "xa b c xxx "
assert str2.strip("xxx ") == "a b c"
assert str2.strip("xc ") == "a b"



def mystrip(stringstrs, stripchar):
    templist = []
    for strip in stripchar:  #截取的字符串
            index = stringstrs.find(strip) #在原有的字符串中找到要截取的字符
            if index == -1:     #如果找不到
                stringstrs = stringstrs #直接返回
                continue                   #继续
            else:
                stringstrs = stringstrs.replace(strip,'') #字符串删除该字符
    return print(stringstrs)

mystrip(str2,'x ')

#测试
# mylen('shuimudaoliang')
# mysplit(str0, " ")
# myjoin(list,'#####')
# mystrip(str2, "xc ")