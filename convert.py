#!/usr/bin/env python
from wand.image import Image
import os


pwd = os.getcwd()
books = os.listdir('%s/my_shelf'%(pwd))
books_available = os.listdir('%s//hold' %(pwd))

for book in books:
	book_name = book[:-4]
	
	# try:
	# 	os.mkdir('%s//hold//%s'%(pwd,b))
	# 	break
	# except OSError, e:
	# 	if e.errno !=17:	
	# 		raise
	# 	pass

	if book_name in books_available:
		continue
	else:
		os.mkdir('%s//hold//%s'%(pwd,book_name))		


	with Image(filename = '%s//my_shelf//%s' %(pwd,book), resolution=200) as image:
	   image.compression_quality = 99
	   image.save(filename='%s//hold//%s//|.jpg' %(pwd,book_name))



