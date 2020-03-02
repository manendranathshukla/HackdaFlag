import requests

url="https://hackdaflag.pythonanywhere.com"



cookies={'login':'false'}
rr=requests.cookies.RequestsCookieJar()
rr.set("vtu","10547",domain="hackdaflag.pythonanywhere.com",path="/site3")
r3=requests.get(url,cookies=rr)
print(r3)
