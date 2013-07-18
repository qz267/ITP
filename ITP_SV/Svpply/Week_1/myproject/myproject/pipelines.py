
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DorpItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors


class MySQLStorePipeline(object):
      def _init_(self):
          self.dbpool = adbapi.ConnectionPool(
              'MySALdb',
               db = 'test',
              user = 'user'
              passwd = '******',
              cursorclass = MySQLdb.cursors.DictCursor,
              charset = 'utf8'
              use_unicode = False
              )

      def process_item(self,item,spider):
         query = self.dbpool.runInteraction(self_conditional_insert,item)
         query.addErrback(self.handle_error)
         return item

      def_conditional_insert(self,tx,item):
          if item.get('name'):
              tx.execute(\
                  "insert into product (name, status)\values(%s,%s)",
                  (item['name'], item['status'])
                  )

        
 
