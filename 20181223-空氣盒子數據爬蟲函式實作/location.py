def main(county,site):

	import requests,json
	import urllib3
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

	opendata = 'https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json'
	res = requests.get(opendata, headers=headers,verify=False)
	data = json.loads(res.text)

	for kh in data:
		if kh['county'] == county and kh['Site'] == site:
			print(county, site, ": PM2.5="+kh['PM25'])
main('高雄市','前鎮')