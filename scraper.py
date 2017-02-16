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

print etree.tostring(root, pretty_print=True)
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
