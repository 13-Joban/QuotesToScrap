# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# extracted data -> pipeline -> db
import sqlite3

class QuoteprojectPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_table""")
        self.curr.execute("""CREATE TABLE quotes_table(
                title text,
                author text,
                tag text)""")

    def process_item(self, item, spider):

        self.store_table(item)
        print("Pipeline "+ item['title'])
        return item

    def store_table(self, item):
        self.curr.execute("""
            INSERT INTO quotes_table (title, author, tag) 
            VALUES (?, ?, ?)""",
                          (item['title'], item['author'], ', '.join(item['tags'])))
        self.conn.commit()

