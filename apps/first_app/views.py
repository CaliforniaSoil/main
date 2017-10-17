from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
def blog(request):
    response = "blogblog"
    return HttpResponse(response)
def new(request):
    response = "plasceholder to display a new form to create"
    return HttpResponse(response)
def create(request):
    return redirect('/')
def show(request, number):
    response = ("placeholder to display blog" + number)
    return HttpResponse(response)
def edit(request, number):
    print number
    response = "place holder to edit blog" + number
    return HttpResponse(response)
def delete(request, number):
    return redirect('/')
