'''
David Sun
Image Repository for Shopify Intern Challenge
Created 5/4/21
'''
import tag_prediction
import db_funcs as db

def tag_test():
	x = tag_prediction.tag("test images/apple.png")
	assert(x == ['apple'])

def sql_tests():
	apple = db.myImage("author: me", "test images/apple.png")
	apple.manual_tag(["apple"])
	db.add_image(apple)
	print(db.get_image_from_id("test images/apple.png"))
	assert(db.search_images_by_tag("apple") == [('test images/apple.png',)])
	print(db.search_images_by_tag("apple"))
	db.remove_image_by_id("test images/apple.png")
	assert(db.search_images_by_tag("apple") == [])
	print(db.search_images_by_tag("apple")

if __name__ == "__main__":
	sql_tests()
	tag_test()