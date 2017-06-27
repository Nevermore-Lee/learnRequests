import requests
import  re
html = requests.get('http://www.toutiao.com/i6417563885221446146/')
title = re.search('<title>(.*?)</title>',html.text,re.S).group(1)
links = re.findall(' href="(.*?)"',html.text,re.S)
print(html.text)
print(html.encoding)
print(title)
for each in links:
    print(each)
# print(links)