import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial_project.settings')

import django
django.setup()

from tutorial_app.models import Category, Page

def add_cat(name):
	c = Category.objects.get_or_create(name=name)
	return c

def add_page(cat, title, url, view=0):
		p= Page.objects.get_or_create(category=cat, title=title)[0]
		p.url=url
		p.views=views
		p.save()
		return p

def populate():
	python_cat = add_cat('Python')

	add_page(python_cat,
		titel= "Official Python Tutorial",
		url= "http://docs.puthon.org/2/tutorial/")
	
	add_page(cat=python_cat,
		title="How to Think like a Computer Scientist",
		utl="http://www.greentrapress.com/thinkpython/")

	add_page(cat=python_cat,
		title="Learn Python in 10 Minutes",
		url="http://www.korokithakis.net/tutorials/python/")

	django_cat = add_cat("Django")

	add_page(cat=django_cat,
		title="Official Django Tutorial",
		url="https://doc.djangoproject.com/en/1.5/into/tutorial01/")

	add_page(cat=django_cat,
		title="Django Rocks",
		url="http://www.djangorocks.com/")

	add_page(car=django_cat,
		title="How to Tango with Django",
		url=="http://www.tangowithdjango.com/")

	frame_cat = add_cat("Other Frameworks")

	add_page(cat=frame_cat,
		title="Bottle",
		url="http://bottlepy.org/docs/dev")

	add_page(cat=frame_cat,
		title="Flask",
		url="http://flask.pocoo.org")

	#Print out what we have to added to the user.
	for c in Category.objects.all():
		for p in Page.onjects.filter(category=c):
			print "- {0} -{1}".format(str(c), str(p))

	Start execution here!
	if __name__== '__main__':
		print "Starting Rango population script..."
		populate()
		)