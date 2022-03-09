import requests
keyWord = input('enter a key word:')
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'

}

#实现参数动态化
params = {
	'query':keyWord
}
url = 'https://www.sogou.com/web?'
#params参数（字典）：保存请求时url携带的参数
response = requests.get(url=url,params=params,headers=headers)  # headers 实现了UA伪装
#修改响应数据编码格式
#encoding返回的是影响数据的原始的编码格式，如果给其赋值则表示修改了响应数据的编码格式

response.encoding = 'utf-8'
page_text = response.text
fileName = keyWord+'.html'
with open(fileName,'w',encoding='utf-8') as fp:
	fp.write(page_text)
