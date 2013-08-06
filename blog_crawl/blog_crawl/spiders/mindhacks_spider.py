from scrapy.spider import BaseSpider
class MindhacksSpider(BaseSpider): 
    domain_name = "mindhacks.cn" 
    start_urls = ["http://mindhacks.cn/"]
    
    def parse(self, response): 
        items = []
        hxs = HtmlXPathSelector(response)
        posts = hxs.x('//h1/a/@href').extract()
        items.extend([self.make_requests_from_url(url).replace(callback=self.parse_post)        for url in posts])
        page_links = hxs.x('//div[@class="wp-pagenavi"]/a[not(@title)]') 
        for link in page_links:
            if link.x('text()').extract()[0] == u'\xbb':
                url = link.x('@href').extract()[0]
                items.append(self.make_requests_from_url(url))
            return items
        return []
￼
    def parse_post(self, response):
        item = BlogCrawlItem()
        item.url = unicode(response.url)
        item.raw = response.body_as_unicode()
    return [item]
    
SPIDER = MindhacksSpider()