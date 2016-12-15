from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

def index(request):
	# if not 'first_name' in request.session:
	# 	request.session['first_name'] = ""

	return render(request, "login/index.html")

def success(request):
	# if request.session['first_name'] == "":

	if not 'first_name' in request.session :
		return redirect('/')
	else:
		first_name = request.session['first_name']
		return render(request, "login/success.html",)
	 
def logout(request)	:
	del request.session['first_name']
	return redirect ('/')	

def register_process(request):
	
	if request.method == "POST":
		result = User.userMgr.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'])
	
		if result[0]==True:
			request.session['first_name'] = result[1].first_name
			print result, "*******************************************************"
			# request.session.pop('errors')
			return redirect('/success')
		else:

			# request.session['errors'] = result[1]
			messages.add_message(request, messages.WARNING, result[1][0])

			print result[1], "^^^^^^^^^^^^^^^^^^^^"
			return redirect('/')
	else:

		return redirect ('/')

def login_process(request):
	print "------------ POST ----------------\n", request.POST
	result = User.userMgr.login(request.POST['email'],request.POST['password'])

	if result[0] == True:
		request.session['first_name'] = result[1][0].first_name
		# We have result[1][0] this refers to the results of the query (user query returned) and index of zero which is what we just unwrapped.
		return redirect('/success')
	else:
		messages.add_message(request, messages.WARNING, result[1][0])

		# request.session['errors'] = result[1]
		return redirect('/')


