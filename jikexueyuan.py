import re
import requests
import sys

class spider(object):
    def __init__(self):
        print('开始爬取内容...')

    def getsource(self,url):
        html = requests.get(url)
        html.encoding='utf-8'
        print(html.encoding)
        return html.text

    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,total_page+1):
            link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
            page_group.append(link)
        return page_group

    def geteveryclass(self,source):
        everyclass = re.findall('(li id=".*?</li>)',source,re.S)
        return everyclass

    def getinfo(self,eachclass):
        info={}
        info['content'] = re.search('style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachclass,re.S).group(1)
        info['title'] = re.search('class="lessonimg" title="(.*?)">', eachclass, re.S).group(1)
        info['classtime'] = re.search('<em>(.*?)</em>', eachclass, re.S).group(1)
        # info['title'] = re.search('title="(.*?)"alt=', eachclass, re.S).group(1)
        return info
    def saveinfo(self,classinfo):
        #写入文件编码确定为utf-8否则会出现乱码
        f = open('info.txt','w',encoding='utf-8')
        for each in classinfo:
            f.writelines(('content:'+each['content']+'\n'))
            f.writelines('title:'+each['title']+'\n')
            f.writelines('classtime:'+each['classtime']+'\n')
        f.close()
if __name__=="__main__":
    class_info = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=2'
    jikespider = spider()
    all_links = jikespider.changepage(url,3)
    for link in all_links:
        print("正在处理页面.."+link)
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            info = jikespider.getinfo(each)
            class_info.append(info)
        jikespider.saveinfo(class_info)

