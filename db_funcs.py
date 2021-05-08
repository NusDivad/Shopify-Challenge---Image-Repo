'''
David Sun
Image Repository for Shopify Intern Challenge
Created 5/4/21
'''

# img = Image.open("haha.jpg")
# img = img.tobitmap()

#Add top comment for created, owner, etc.
#Yolo model trained on MSCOCO dataset
import io
import os
import sqlite3
from myImage import myImage

conn = sqlite3.connect('image_repo.db')
c = conn.cursor()

def add_image(new_image):
	#Adds to both overall table and tag specific table
	with conn:
		#If filename (id) is not unique, will throw an error and not mess up the tags table
		try:
			c.execute("INSERT INTO images VALUES (:metadata, :id, :image)", new_image.sql_dict)
			for tag in new_image.tags:
				c.execute("INSERT INTO tags VALUES (:tag, :id)", {"tag":tag, "id":new_image.id})
		except Exception as e:
			print(e)
			pass

# To Implement
# def add_all_images_in_filesystem(path, metadata):
# 	pass

def remove_image_by_id(id):
	with conn:
		c.execute("DELETE from images WHERE id = :id", {"id": id})
		c.execute("DELETE from tags WHERE id = :id", {"id": id})

def get_image_from_id(id):
	c.execute("SELECT image FROM images WHERE id = :id", {"id": id})
	return myImage.serial_to_image(c.fetchone()[0])

def search_images_by_tag(tag):
	c.execute("SELECT id from tags WHERE tag = :tag", {"tag": tag})
	return c.fetchall()