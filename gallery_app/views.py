from django.shortcuts import render,redirect
from .forms import ImageForm
from django.http import HttpResponse
from .models import Picture_model
from .identify import identification
from django.forms import modelformset_factory
import os
#from connect import identify

# Create your views here.
def main_flower(request):
	form=ImageForm()
	try:
		file=Picture_model.objects.filter(name='Tulip')
	except Exception as e:
		raise e
	name='Tulip'
	return render(request,'gallery_app/main.html',{'form':form,'file':file,'name':name})

def main(request,name):
	form=ImageForm()
	try:
		file=Picture_model.objects.filter(name=name)
	except Exception as e:
		raise e
	return render(request,'gallery_app/main.html',{'form':form,'file':file,'name':name})

def upload(request,name):
	if request.method =='POST':
		form = ImageForm(request.POST,request.FILES)
		file=Picture_model.objects.filter(name=name)
		if form.is_valid():
			try:
				if identification(request.FILES['image'])==True:
					form.save()
				else:
					context={'form':form,'file':file,'name':name,'error':"Sorry It's not a image of Flower."}
					return render(request,'gallery_app/main.html', context)
			except Exception as e:
				raise e

			name=form['name'].value()
		return redirect('/main/'+name)
	else:
		form=ImageForm()
		file=Picture_model.objects.filter(name=name)
		context={'form':form,'file':file,'name':name,'error':'Unmatched image upload'}
		return render(request,'gallery_app/main.html', context)

def remove(request,images_id,name):
	b=Picture_model.objects.get(pk=images_id)
	b1=(str(b.image.url)).split('/')
	try:
		os.remove(os.path.join('static',b1[1],b1[2],b1[3]))
		b.delete()
	except Exception as e:
		raise e
	
	name1='/main/'+name
	return redirect(name1)

def fullimage(request,images_id):
	try:
		b=Picture_model.objects.get(pk=images_id)
	except Exception as e:
		raise e
	return render(request,'gallery_app/image.html',{'images':b})