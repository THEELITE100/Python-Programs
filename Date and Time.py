#time
import time
print(time.time())
print(time.ctime(257.752))
print(time.localtime())
print(help(time.time))
print(help(time.ctime))
print(help(time.localtime))
a = time.localtime()
b = time.mktime(a)
print(b)
c = time.asctime(a)
print(c)
x = time.strftime("%d/%m/%Y")
print(x)
#datetime
import datetime
print(datetime.datetime(2017,5,2,2,5,7))
v = datetime.datetime.now()
print(v.year)
print(v.month)
print(v.hour)