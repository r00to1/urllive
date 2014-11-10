#coding=utf-8
import sys 
import urllib2
url_notok=sys.argv[1]
url_ok=sys.argv[2]
result = list()
f = open(url_notok, 'r')                   #以读方式打开文件
for line in f.readlines(): 
    #print line                         #依次读取每行
    line = line.strip()
    #print line                             #去掉每行头尾空白
    if  len(line) !=0:      
        if line[0:7]=='http://' or line[0:8]=='https://':
            pass
        else:
            line='http://'+line
        print line
    try:
        response = urllib2.urlopen(line,timeout=4)
        print response
        result.append(line)                             #保存
        result.sort()                                       #排序结果
        open(url_ok, 'w').write('%s' % '\n'.join(result)) #保存入结果文件
    except urllib2.HTTPError, e:
        print e.code
    except:
        print "error"


    
    
    