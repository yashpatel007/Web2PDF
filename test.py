def getBaseUrl(url):
    li = url.split("/")
    print(li[0]+"//"+li[2])

getBaseUrl('http://www.google.com/hello/some.html')