from django.contrib.auth import authenticate, login,  get_user_model 
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView



from .forms import ContactForm, LoginForm, RegisterForm

class HomePageView(TemplateView):
	template_name = 'home.html'

class ContactPageView(FormView):
	template_name = 'contact/contact.html'
	form_class = ContactForm
	success_url = '/thanks/'

	def form_valid(self, form):
		return super().form_valid(form)

# class LoginPageView(FormView):
# 	template_name = 'auth/login.html'
# 	form_class = LoginForm
# 	success_url = '/logged/'

# 	def form_valid(self, form):
# 		username = form.cleaned_data.get("username")
# 		password = form.cleaned_data.get("password")
# 		user = authenticate(useranem=username, password=password)
# 		print(user.is_authenticated())
# 		if user is not None:
# 			login(user)
# 		else:
# 			print("Error")

# 		return super().form_valid(form) 

def loginPageView(request):
	form_class = LoginForm(request.POST or None)
	context = {
		'form' : form_class
	}
	print("user logged in")
	#print(request.user.is_authenticated)
	if form_class.is_valid():
		print(form_class.cleaned_data)
		username = form_class.cleaned_data.get("username")
		password = form_class.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect("/login")
		else:
			print("Error")
	return render(request, "auth/login.html", context)



User = get_user_model()
def RegisterPageView(request):
	form_class = RegisterForm(request.POST or None)
	context = {
		'form' : form_class
	}
	if form_class.is_valid():
		print(form_class.cleaned_data)
		username = form_class.cleaned_data.get("username")
		email = form_class.cleaned_data.get("email")
		password = form_class.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	return render(request, "auth/register.html", context)
