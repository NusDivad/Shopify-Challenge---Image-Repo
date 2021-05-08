'''
David Sun
Image Repository for Shopify Intern Challenge
Created 5/4/21
'''
from keras.preprocessing.image import load_img
import tag_prediction as tagger
import pickle

class myImage:
	#An image class containing the image bitmap and metadata
	#The identifier for images is the filename, must be unique
	def __init__(self, metadata, filename):
		self.metadata = metadata
		self.id = filename
		self.image = load_img(filename)
		self.tags = tagger.tag(filename)
		#full_tags = tagger.tag(filename)
		#self.tags = full_tags

	def manual_tag(self, tags):
		self.tags = tags

	@property
	def serial_image(self):
		return pickle.dumps(self.image)
		
	@staticmethod
	def serial_to_image(obj):
		return pickle.loads(obj)

	@property
	def sql_dict(self):
		values = {"metadata": self.metadata,
					"id" : self.id,
					"image": self.serial_image}
		return values
	
