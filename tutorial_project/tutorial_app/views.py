from django.shortcuts import render
from django.http import HttpResponse
from models import Category, Page
from forms import CategoryForm, PageForm
from forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login 
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

def index(request):
	context_dict = {}
	request.session.set_test_cookie()
	if request.session.test_cookie_worked():
		print ">>> TEST COOKIE WORKED"
		request.session.delete_test_cookie()

	category_list = Category.objects.order_by('-likes')[:5]

	context_dict['categories'] = category_list  
	page_list = Page.objects.order_by('-views')[:5]
	context_dict['pages'] = page_list

	#visits = int(request.COOKIES.get('visits','1'))
	visits = request.session.get('visits')

	if not visits:
		visits = 1

	reset_last_visit_time = False

	#if 'last_visit' in request.COOKIES:
	#	last_visit = request.COOKIES['last_visit']
	last_visit =  request.session.get('last_visit_time')
	if last_visit:
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

		if (datetime.now()-last_visit_time).days>0:
			visits = visits +1
			reset_last_visit_time = True

	else:
		reset_last_visit_time = True

	
	response = render(request , 'index.html', context_dict)

	if reset_last_visit_time:
		#response.set_cookie('last_visit', datetime.now())
		#response.set_cookie('visits', visits)
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = visits

	context_dict['visits'] = visits	
	return response


def about(request):

	if request.session.get('visits'):
		count = request.session.get('visit')
	else: count = 0

	count = +1
	context_dict['visits']= count

	return render (request,'about.html',context_dict)
	
	#delete bottom line
def about(request):
    return HttpResponse("About Us")

def category(request, category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category)

		context_dict['category'] = category
		context_dict['pages'] = pages

	except Category.DoesNotExist:
		pass

	return render(request, 'category.html', context_dict)


def add_category(request):
		if request.method == 'POST':
			form = CategoryForm(request.POST)
			if form.is_valid():
					form.save(commit=True)
					return index(request)
			else:
					print form.errors
		else:
			form = CategoryForm()

		return render(request,'add_category.html', {'form':form})				


def add_page(request, category_name_slug):
	try:
			cat = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
			cat = None

	if request.method =='POST':
		form = PageForm(request.POST)

		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.catgeory = cat
				page.views = 0 
   			  	page.save()
				return category(request, category_name_slug)
			else:
				print form.errors
		else:
			print form.errors
	else:
		form = PageForm()

		context_dict = {'form':form, 'category':cat, 'slug':category_name_slug}
	return render(request, 'add_page.html', context_dict)

def register(request):
	registered = False
	if request.method == 'POST':
		#Attempt to grab information from the raw form information.
		#Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfile(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid:
			# Save the user's form data to the database.
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit = False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True

		else:
			print user_form.erros, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username' )
		password = request.POST.get (usetname=username, password=password)
		if user:
			if user.is_active:
				login(request, user_form)
				return HttpResponseReDirect('/')
			else: 
					return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details: {0},{1}". format (username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render (request,'login.html',{})

def user_logout(request):
	logout(request)
	
	return HttpResponseRedirect('/')



