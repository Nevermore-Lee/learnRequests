import re

s2 = 'asdfafxxIxx123xxlovexxdafsafdsafsaxxyouxxsdfa'
f = re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
f2 = re.findall('xx(.*?)xx123xx(.*?)xx',s2)
f3 = re.findall('xx(.*?)xx',s2,re.S)
print(f)
print(f2[0][1])
print(f3)
s = '123rrrr123'
output = re.sub('123(.*?)123','123%d123'%789,s)
print(output)

s1 = 'asdfasf1234567989dafa555555sf'
number = re.findall('(\d+)',s1)
# number = re.findall('{[a-z]}(.*?){[a-z]}',s1,re.S)
print(number)