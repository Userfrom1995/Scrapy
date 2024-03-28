# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyTutorialPipeline:
    def process_item(self, item, spider):
        return item


import mysql.connector

# class SaveToMySQLPipeline:
#
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='User1995',  # add your password here if you have one set
#             database='scrappy'
#         )
#         self.cur = self.conn.cursor()
#
#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS books(
#             id int NOT NULL auto_increment,
#             author_title VARCHAR(255),
#             born_date VARCHAR(255),
#             born_location VARCHAR(255),
#             description text,
#             PRIMARY KEY (id)
#         )
#         """)
#
#     def process_item(self, item, spider):
#         self.cur.execute("""
#         INSERT INTO books (
#             author_title,
#             born_date,
#             born_location,
#             description
#             ) VALUES (%s, %s, %s, %s)
#         """, (
#             item.get("author_title"),
#             item.get("born_date"),
#             item.get("born_location"),
#             item.get("description")
#         ))
#         self.conn.commit()
#         return item
#
#     def close_spider(self, spider):
#         self.cur.close()
#         self.conn.close()
