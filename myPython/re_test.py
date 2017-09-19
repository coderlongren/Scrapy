# _*_ coding:utf-8 _*_
#引入正则表达式的包
import re

#创建一个正则表达式对象
# 1.12  3.14 123
pattern = re.compile('\d+\.\d+')
#提供要匹配的字符串
src = "3.14, 123456,123.123,asdfsd,156.2"
result = pattern.findall(src)
print(src)
print(result)
