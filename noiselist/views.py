from django.template import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django import forms
from noiselist.models import *

class TodoForm(forms.Form):
  name = forms.CharField(max_length=1000, widget=forms.Textarea)

def index(request):
  todos = TodoItem.objects.all()

  return render_to_response('index.html', { 'todos' : todos }, context_instance=RequestContext(request))

def add_todo(request):

  if request.method == 'POST':
    form = TodoForm(request.POST)

    if( form.is_valid() == True ):
      item = TodoItem()
      item.name = form.cleaned_data['name']
      item.save()
      # All saved so return the user to the frontpage
      return redirect('/')
    else:
      return render_to_response('add_todo.html', { 'form' : form}, context_instance=RequestContext(request))
  else:
    form = TodoForm()
  
  return render_to_response('add_todo.html', { 'form' : form}, context_instance=RequestContext(request))
