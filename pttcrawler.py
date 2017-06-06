# -*- coding: utf-8 -*-
#!/usr/bin/env python

import re
import requests
from bs4 import BeautifulSoup  
from requests.models import Response

import sys
import os



count=0
TITLE = sys.argv[1]

	
Graph_text_file1 = open("/user/wangchenyu/Desktop/pttdata.txt","w")
Graph_text_file1.write("jj %s\n"%(TITLE))
Graph_text_file1.write("jj\n%s\n"%(sys.path))


reload(sys);
exec("sys.setdefaultencoding('utf-8')");
assert sys.getdefaultencoding().lower() == "utf-8";

def parseGos(link):
	resp = requests.get(url=str(link),cookies={"over18":"1"})
	soup = BeautifulSoup(resp.text)
	
	#print(resp)
	#print (resp.status_code)
	if (resp.status_code)==404:
		print ("PAGE NOT FOUND")

	else:
		# author
		author  = soup.find(id="main-container").contents[1].contents[0].contents[1].string.replace(' ', '')
		# title
		title = soup.find(id="main-container").contents[1].contents[2].contents[1].string.replace(' ', '')
		Graph_text_file_title.write("%s"%(title))
		#print (title)
		# date
		date = soup.find(id="main-container").contents[1].contents[3].contents[1].string
		month={"Jan":"1","Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}
		#print date
		if "  " in str(date):
			#print "hello"
			date = str(date).replace("  "," ")
			
		year = str(date.split(" ")[4])
		#print year
		second= str(date.split(" ")[3]).split(":")[2]
		#print (month[date.split(" ")[1]])
		date_str=str(date.split(" ")[4])+"/"+str(month[date.split(" ")[1]])+"/"+str(date.split(" ")[2])+" "+str(date.split(" ")[3])
		#print date_str
		# ip
		try:
			ip = soup.find(text=re.compile("※ 發信站:"))
			ip = re.search("[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*",str(ip)).group()
		except:
			ip = "ip is not find"
		# content
		a = str(soup.find(id="main-container").contents[1])
		a = a.split("</div>")
		a = a[4].split("<span class=\"f2\">※ 發信站: 批踢踢實業坊(ptt.cc),")
		content = a[0].replace(' ', '').replace('\n', '').replace('\t', '')
		# message
		#num , all , g , b , n ,message = 0,0,0,0,0,{}
		#print author
		#print title
	
		Graph_text_file_author_time_title.write("%s\t%s\t%s"%(author,title,date_str))
		Graph_text_file_content.write("%s\n"%(content))
	
		for tag in soup.find_all("div","push"):
			#print (tag)
			try:			
				#num += 1
				push_tag = tag.find("span","push-tag").string.replace(' ', '')
				push_userid = tag.find("span","push-userid").string.replace(' ', '')
				push_content = tag.find("span","push-content").string.replace(' ', '').replace('\n', '').replace('\t', '')
				push_ipdatetime = tag.find("span","push-ipdatetime").string.replace('\n', '')
				#message[num]={"狀態":push_tag,"留言者":push_userid,"留言內容":push_content,"留言時間":push_ipdatetime}
		
			except:
				push_tag = tag.find("span","push-tag").string.replace(' ', '')
				push_userid = tag.find("span","push-userid").string.replace(' ', '')
				#push_content = tag.find("span","push-content").string.replace(' ', '').replace('\n', '').replace('\t', '')
				push_content=":http"
				push_ipdatetime = tag.find("span","push-ipdatetime").string.replace('\n', '')
				pass
				#print ("hello")
			#messageNum = {"g":g,"b":b,"n":n,"all":num}
			# json-data
			#d={"b_作者":author , "c_標題":title , "d_日期":date , "e_ip":ip , "f_內文":content , "g_推文":message}

			push_ipdatetime=push_ipdatetime.strip()
			Graph_text_file_pushcontent.write("%s\t%s\t%s\t%s/%s:%s\n"%(push_tag,push_userid,push_content,year,push_ipdatetime,second))
	
	
#url="https://www.ptt.cc/bbs/MobileComm/M.144645.A.D12.html"

url="https://www.ptt.cc/bbs/MobileComm/M.1441039633.A.CFD.html"
url = sys.argv[1]

Graph_text_file_author_time_title = open("C:/wamp/www/new_author_title_date.txt","w")
Graph_text_file_title = open("C:/wamp/www/new_title.txt","w")
Graph_text_file_content= open("C:/wamp/www/new_content.txt","w")
Graph_text_file_pushcontent= open("C:/wamp/www/new_push_content.txt","w")

parseGos(url)

#print "check"
#utf8_check()
#os.system('python utf8_check.py new_push_content')
