import requests
url = 'https://www.capgemini.com/'
r = requests.get(url)
print(r)
print(r.url)
print(r.status_code)
print(r.headers)
print(r.request.headers)
print(r.request.body)
header = r.headers
print(header)
print("Date is: \t", header['date'], "\n\nType of Content is: \t", header['Content-Type'])
print(r.encoding)
print(r.text)
print(r.text[:100])



#//  MODIFY URL USING GET:  changes in URL, no changes in body
url = 'http://httpbin.org/get'
payload = {'Name': 'Sonali', 'ID': 123}
r1 = requests.get(url, params=payload)
print(r1)
print(r1.headers)
print(r1.url)
print(r1.json())
print(r1.request.body)


#//  POST REQUEST METHOD:  no changes in URL, changes in body
url_post = 'http://httpbin.org/post'
payload = {'Name': 'Sonali', 'ID': 123}
r_post = requests.post(url_post, data=payload)
print(r_post)
print(r_post.headers)
print(r_post.url)
print(r_post.json())
print(r_post.request.body)
