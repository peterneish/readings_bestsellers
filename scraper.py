# bestsellers from readings.com.au

import scraperwiki           
import lxml.html
import time
html = scraperwiki.scrape("http://www.readings.com.au/collection/bestselling-books")
root = lxml.html.fromstring(html)

pos = 0

for el in root.cssselect("div.shelf-grid__products a"):
    title   = el.cssselect("h4.shelf-grid-product__title")[0].text_content()
    author  = el.cssselect("p.shelf-grid-product__author")[0].text_content()
    link    = el.attrib['href']
    isbn    = link.split("/")[2]
    pos += 1

    print title
    #print author
    #print link
    print isbn
    link = "http://www.readings.com.au" + link
    

    record = {"title"  : title,
              "author" : author,
              "isbn"   : isbn,
              "link"   : link,
              "pos"    : pos,
              "sdate"  : time.strftime( "%Y-%m-%d" )
             }
    scraperwiki.sqlite.save(unique_keys=["isbn", "sdate"], data=record)


    
