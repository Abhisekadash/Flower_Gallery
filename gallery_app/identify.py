import io,os
from google.cloud import vision



def identification(filename):
	os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r"My Project 97253-9b2100576a43.json"
	client=vision.ImageAnnotatorClient()
	#with open('checking/flower.jpeg', 'wb+') as destination:
	#	for chunk in filename.chunks():
	#		destination.write(chunk)
	for  content in filename.chunks():
		
		#with io.open(filename,'rb') as image_file:
				#	content=image_file.read()
		image=vision.types.Image(content=content)
		response= client.object_localization(image=image).localized_object_annotations
		for res in response:
			if res.name=='Flower':
				return True
			else:
				return False