import bs4 , time , re , requests
from selenium import webdriver
import pandas as pd

#https://www.wnmtl.org/chapter/63261 (website name)

browser = webdriver.Firefox()
browser.get('https://novelhi.com/s/A-Record-of-a-Mortals-Journey-to-Immortality-%E2%80%93-Immortal-World-Arc/1')
time.sleep(10)
title1 = []

def context() :
    title1.append({browser.find_element('css selector', '.book_title > h1:nth-child(1)').text})
    content = browser.find_element('css selector','#showReading').text
    content = re.sub('\n','<br>',content)
    content = re.sub('\'','',content)
    title1.append({content})

def main() :
    i=1
    while i < 1406 : #1406 = number of pages
        nxtbtn = browser.find_element('css selector','.next')
        nxtbtn.click()
        context()
        i += 1

context()
main()
csv1 = {'title':title1}

df = pd.DataFrame(csv1)
df.to_csv('rmj4.csv', index = False )

CSV= pd.read_csv('rmj4.csv')
CSV.to_html('RMJI-immortal world arc.html')
