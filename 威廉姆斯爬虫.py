import requests
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

tb = [	'census-lgbt-demographics-studies', 
		'economic-impact-reports',
		'marriage-and-couples-rights',
		'parenting',
		'discrimination',
		'transgender-issues',
		'race-ethnicity',
		'safe-schools-and-youth',
		'health-and-hiv-aids',
		'violence-crime',
		'immigration',
		'military-related',
		'international']

for cate in tb:
	pg = 1
	print(cate)
	num = 0
	
	while pg != 0:
		url = 'https://williamsinstitute.law.ucla.edu/category/research/'+ cate + '/page/' + str(pg)
		html = requests.get(url)
		html.encoding = 'utf-8'
		if re.search(r'<title>Page not found', html.text) == None:
			print(url)			
			rep_urls = re.findall(r'<h2><a href="https://(.*?)" title', html.text)
			for rep_url in rep_urls:
				rep_url = 'https://' + rep_url
				rep_html = requests.get(rep_url)
				rep_html.encoding = 'utf-8'
				rep = []
				rep.extend(re.findall(r'<h1>(.*?)</h1>', rep_html.text))
				rep.extend(re.findall(r'<p><strong>By (.*?)</strong><br />', rep_html.text))
				rep.extend(re.findall(r'<strong>(.*?)</strong></p>', rep_html.text))
				file_name = cate+'.txt'

				with open(file_name, 'a') as file:
					for ele in rep:
						file.write(ele+'	')

				pdf_list = re.findall(r'<a href="(.*?).pdf"', rep_html.text)
				for pdf_url in pdf_list:
					pdf_url = pdf_url + '.pdf'
					pdf_name = pdf_url.split('/')[-1]
					try:
						pdf_html = requests.get(pdf_url)
						with open(pdf_name, 'wb') as code:
							code.write(pdf_html.content)
						with open(file_name, 'a') as file:
							file.write(pdf_url + '//downloaded	')
					except:
						with open(file_name, 'a') as file:
							file.write(pdf_url + '//downloadfail	')
					with open(file_name, 'a') as file:
						file.write('\n')
				num = num + 1
				print(str(num))
			pg = pg + 1
		else:
			pg = 0
			
	print(cate + 'finished!')