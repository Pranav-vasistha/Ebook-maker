import bs4 , time , re , requests
from selenium import webdriver
from ebooklib import epub
#https://www.wnmtl.org/chapter/63261

browser = webdriver.Firefox()
browser.get('https://www.wnmtl.org/chapter/63261')
time.sleep(10)

#extract

title1 = browser.find_element('css selector', '#chapterContentTitle').text
content = browser.find_element('css selector','#chapterContent').text
content1 = re.sub('\n', '<br>', content)




def main():
    i=1
    while i<3 :
        nxtbtn = browser.find_element('css selector','#nextBtn')
        nxtbtn.click()
        time.sleep(5)
        title1 = browser.find_element('css selector', '#chapterContentTitle').text
        content = browser.find_element('css selector','#chapterContent').text
        content1 = re.sub('\n', '<br>', content)
        ebook()
        i += 1

def ebook():
    book = epub.EpubBook()

    #metadata
    book.set_identifier('1')
    book.set_title('RMJI')
    book.set_language('en')
    book.add_author('Wang Yu')

    #chapters
    c1=epub.EpubHtml(title = title1, file_name='chap_01.xhtml', lang='hr')
    c1.content= u'<h1>{}</h1><p>{}</p>'.format(title1, content1)

    #add chapter
    book.add_item(c1)

    #tabel of content
    book.toc = (epub.Link('chap_01.xhtml','introduction','intro'),
                (epub.Section('immortal arc'),(c1, )))

    # add default NCX and NAV file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    #define css
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid='style_nav' ,
                            file_name='style/nav.css',
                            media_type='text/css',
                            content=style)

    #add css file
    book.add_item(nav_css)

    #basic spine
    book.spine = ['nav',c1]

    #write to file
    epub.write_epub('test8.epub',book,{})


ebook()
