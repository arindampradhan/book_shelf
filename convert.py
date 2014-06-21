from wand.image import Image
import os

pwd = os.getcwd()
books = os.listdir('%s/my_shelf'%(pwd))
books_available = os.listdir('%s/img'%(pwd))

for book in books:
	b = book[:-4]
	
	# try:
	# 	os.mkdir('%s//img//%s'%(pwd,b))
	# 	break
	# except OSError, e:
	# 	if e.errno !=17:	
	# 		raise
	# 	pass

	if b in books_available:
		continue
	else:
		os.mkdir('%s//img//%s'%(pwd,b))		


	with Image(filename = '%s//my_shelf//%s' %(pwd,book), resolution=200) as image:
	   image.compression_quality = 99
	   image.save(filename='%s//img//%s//page.jpg' %(pwd,b))

