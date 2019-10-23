#!/usr/bin/python
#codded by dz0ne all rights reserved thanks sami_zaidi
import requests, sys, re, os, time, random

Tsumi=0
#
if Tsumi==1:
    may="special=1/"
else:
    may=''
if not os.path.isdir('logz'):
    os.mkdir('logz')
else:
    pass
try:
 defacer = sys.argv[1]
 zhe = sys.argv[2]
 phpsessid = sys.argv[3]
except:
    print "Usage python %s defacer zhe phpsessid"%(sys.argv[0])
    exit()
page = 1
nb=1
while True :
    lnk = 'http://zone-h.org/archive/%snotifier=%s/page=%s'%(may,defacer,str(page))
    cookaa= {'ZHE' : zhe ,'PHPSESSID' : phpsessid}
    con = requests.session().get(lnk, cookies=cookaa, timeout=10)
    king = re.findall('<td>(.*)\n							</td>', con.content)
    for oo in king:
        nb+=1;
        with open('logz/%s_zoneh.txt'%defacer, 'a') as rr:
            rr.write(oo.split('/')[0] + '\n')
    page += 1
    #to defend zone's Ban
    if page >69:
        exit()
    if nb==1:
        print " You Have One Of This Problems :\n * Error Connection\n * The Defacer Name Not Avaible Or He ve 0 Deface\n * Your Cookies Was Changed\n * You Take Ban"
        exit()
    print "[%s] Sites Saveed In logz/%s_zoneh.txt"%(nb ,defacer)

#fb.com/dzone
