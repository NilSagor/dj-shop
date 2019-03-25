from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product
from http import Http404





# Create your views here.
class ProductListView(ListView):
	model = Product
	template_name = 'products/product_list.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

class ProductDetailView(DetailView):
	model = Product
	template_name = 'products/product_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context