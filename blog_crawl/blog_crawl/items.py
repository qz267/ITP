# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import ScrapedItem
class BlogCrawlItem(ScrapedItem): 
    
    def __init__(self):
        ScrapedItem.__init__(self)
        self.url = ''
        
￼   def __str__(self):
        return 'BlogCrawlItem(url: %s)' % self.url