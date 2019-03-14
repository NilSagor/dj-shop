from django.shortcuts import render
from django.view.generic import ListView

from .models import Product



# Create your views here.
class ProductListView(ListView):
	model = Product
	template_name = 'products/product_list.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context