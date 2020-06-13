import pdfkit 
from bs4 import BeautifulSoup
import requests
import sys
import threading
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QWidget, QComboBox, QVBoxLayout, QLineEdit ,QTextEdit, QSystemTrayIcon,QMenu,QAction
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore



def class web2pdf(object):
    def __init__(self):
        url = ""
        depth = 0
        tag = ""
        file_path = ""
        search_by = ""
        nxtBtnTxt = ""
        elem_class = None
    
    def getBaseUrl():
        li = self.url.split("/")
        return li[0]+"//"+li[2]

    def webtopdf():
        # get the links
        links = getNextLinks(elem_class)

        #save pdf from links
        for idx,link in enumerate(links):
            savePDF(link, "page"+str(idx)+".pdf")
        submit_btn.setEnabled(True)

    # need to make this function dynamic to fit various search criteria-----------------------------------
    def getNextLinks(elem_class):
        links =[]
        for i in range(self.depth):
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
            nextPage = soup.find(class_=elem_class)
            link = nextPage.find('a')
            nxt_link = getBaseUrl(self.url)+link['href']
            links.append(nxt_link)
            start_url = nxt_link
        return links

    def smartFindNextLink():
        links =[]
        for i in range(self.depth):
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content,'html.parser')
            for link in soup.findAll('a' ,{'href':True}):
                if(link.text.strip() == self.nxtBtnTxt):
                    links.append(link['href'])


