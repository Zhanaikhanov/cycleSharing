from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# 
from django.contrib.auth import authenticate, login as ll_login, logout as ll_logout
from django.views import View
from .forms import LoginForm,SignForm
from django.contrib.auth.models import User
from bicycle.models import Bicycle, BicycleRent
from bicycle.forms import PostForm

# 



class IndexView(View):
	initial = {'key':'value'}
	form_class = PostForm
	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		context = {'bicycle_list': Bicycle.objects.all()
		,'post_form':form}
		return render(request,'main/index.html',context)
	

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# some actions
			type_b = form.cleaned_data['type_b']
			style = form.cleaned_data['style']
			image = form.cleaned_data['image']
			cost = form.cleaned_data['cost']
			stars = form.cleaned_data['stars']
			
			print("posted")
			# ==============
			# fs = form.save(commit=False)
			bicycle = Bicycle.objects.create(
				type_b=type_b,
				style=style,
				image = image,
				cost=cost,
				stars=stars,
				owner=request.user
				)
			bicycle.save()

			context = {
			'form':form,
			'success':'bicyclebicycle have been succesfully registered.'
			}
			return render(request,'main/index.html',context)

		else:
			context = {'form':form}
			return render(request,'main/index.html',context)



class SignView(View):
	form_class = SignForm
	initial = {'key':'value'}
	template_name = 'registration/registration.html'


	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# some actions
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			print(username,password)
			# ==============
			# fs = form.save(commit=False)
			try:
				user = User.objects.get(username=username)
				context = {
					'form':form,
					'error':"this username already exists."
					}
				return render(request, self.template_name, context)
			except User.DoesNotExist:
				user = User.objects.create_user(
					username=username,
					password=password
					)
				user.save()
				ll_login(request,user)

				context = {
				'form':form,
				'success':'user have been succesfully registered.'
				}
				return render(request,self.template_name,context)

		else:
			context = {'form':form}
			return render(request,self.template_name,context)

			# ==============


		# 	user = authenticate(request, username=username, password=password)
		# 	if user is not None:
		# 		ll_login(request,user)
		# 		return HttpResponse("logged in malades")
		# 	else:
		# 		return HttpResponse("ee naebwik")


		# else:
		# 	return HttpResponse("tebe pizda")

class LogoutView(View):
	initial = {'key','value'}
	template_name = 'login/logout.html'

	def get(self, request, *args, **kwargs):
		ll_logout(request)
		return render(request, self.template_name)




class LoginView(View):
	form_class = LoginForm
	initial = {'key':'value'}
	template_name = 'login/login.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# some actions
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			print("sign in:",username,password)
			
			user = authenticate(request, username=username, password=password)
			if user is not None:
				ll_login(request,user)
				return HttpResponse("logged in malades")
			else:
				return HttpResponse("ee not logged in")


		else:
			return HttpResponse("not valid")
