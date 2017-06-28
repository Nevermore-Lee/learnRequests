import requests
import  re
html = requests.get('http://www.toutiao.com/i6417563885221446146/')
title = re.search('<title>(.*?)</title>',html.text,re.S).group(1)
#爬起链接
links = re.findall(' href="(.*?)"',html.text,re.S)
#爬去部分文字，先大后小
text_field = re.findall('<div>(.*?)</div>',html.text,re.S)[0]
print(text_field)
the_text = re.findall('">(.*?)</a>',text_field,re.S)
for each in the_text:
    print(each)
# print(html.text)
# print(html.encoding)
# print(title)
# for each in links:
#     print(each)
# print(links)
