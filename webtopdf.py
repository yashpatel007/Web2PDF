import pdfkit 
from bs4 import BeautifulSoup
import requests


base_url = input("please enter base_url: ")
elem_class = input("please enter elem class: ")
full_url = input("enter url to first page: ")
depth = input("how many pages: ")


def savePDF(url, fname):
    pdfkit.from_url(url,fname)
    

def getNextLinks(start_url, depth):
    links =[]
    for i in range(depth):
        page = requests.get(start_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        nextPage = soup.find(class_=elem_class)
        link = nextPage.find('a')
        nxt_link = base_url+link['href']
        links.append(nxt_link)
        start_url = nxt_link
    return links



def webtopdf():
    links = getNextLinks(full_url,int(depth))
    for idx,link in enumerate(links):
        savePDF(link, "page"+str(idx)+".pdf") 

print(getNextLinks("https://www.tutorialspoint.com/cplusplus/index.htm",3))
webtopdf()


#pdfkit.from_url('https://www.tutorialspoint.com/cplusplus/index.htm','cpp.pdf') 