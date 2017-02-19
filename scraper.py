# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
import scraperwiki
import urllib2, lxml.etree
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
url = 'http://usda.mannlib.cornell.edu/usda/current/BeeColonies/BeeColonies-05-12-2016.pdf'
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
pdfdata = urllib2.urlopen(url).read()
xmldata = scraperwiki.pdftoxml(pdfdata)
root = lxml.etree.fromstring(xmldata)

# # To print all of the pdf in xml:
# print lxml.etree.tostring(root, pretty_print=True)

# # To print a page of the pdf in xml:


pages = list(root)
print "There are",len(pages),"pages"

scraperwiki.sqlite.

# # For each page in the document and for each element in a page
for page in pages[3:4]:
  for el in page:
    # # If the element is tagged as text, print our that text and its attribute
    if el.tag == "text":
      if int(el.attrib['left']) == 56: data = { 'State': el.text }
      elif int(el.attrib['left']) < 238 & int(el.attrib['left']) > 210: data['Colonies_start'] = el.text 
      elif int(el.attrib['left']) < 355 & int(el.attrib['left']) > 320: data['Colonies_max'] = el.text
      elif int(el.attrib['left']) < 450 & int(el.attrib['left']) > 420: data['Colonies_lost'] = el.text
      elif int(el.attrib['left']) < 550 & int(el.attrib['left']) > 540: data['Percent_lost'] = el.text
      elif int(el.attrib['left']) < 645 & int(el.attrib['left']) > 610: data['Colonies_added'] = el.text
      elif int(el.attrib['left']) < 755 & int(el.attrib['left']) > 710: data['Colonies_renov'] = el.text
      elif int(el.attrib['left']) < 850 & int(el.attrib['left']) > 840: data['Percent_renov'] = el.text

      
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=[],table_name = 'Colonies_2015_Jan_Mar', data=data)

# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
