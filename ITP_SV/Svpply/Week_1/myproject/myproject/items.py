from scrapy.item import Item, Field

class ProductItem(Item):
     product_name = Field()
     status = Field()
     price = Field()
     currency = Field()
