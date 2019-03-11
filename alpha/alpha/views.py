from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm, LoginForm

class HomePageView(TemplateView):
	template_name = 'home.html'

class ContactPageView(FormView):
	template_name = 'contact/contact.html'
	form_class = ContactForm
	success_url = '/thanks/'

	def form_valid(self, form):
		return super().form_valid(form)

class LoginPageView(FormView):
	template_name = 'auth/login.html'
	form_class = LoginForm
	success_url = '/logged/'

	def form_valid(self, form):
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

		return super().form_valid(form) 