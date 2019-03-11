from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm

class HomePageView(TemplateView):
	template_name = 'home.html'

class ContactPageView(FormView):
	template_name = 'contact/view.html'
	form_class = ContactForm
	success_url = '/thanks/'

	def form_valid(self, form):
		return super().form_valid(form)