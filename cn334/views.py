from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def index(request):
  return render(request, 'home.html')


def test(request):
  dt = date.today()
  data = {
      'numbers': [1, 2, 3],
      'dept': {
          'ece': 'Electrical',
          'ie': 'Industrial'
      },
      'date': dt,
  }
  return render(request, 'test.html', data)


def home(request):
  return render(request, 'home.html')


def category(request):
  return render(request, 'category.html')


def product(request):
  return render(request, 'product.html')


def checkout(request):
  return render(request, 'checkout.html')


def contact(request):
  return render(request, 'contact.html')
