from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def voter_image_view(request): 
  
    if request.method == 'POST': 
        form = VoterForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect(success) 
    else: 
        form = VoterForm() 
    return render(request, 'upload_page.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('Successfully Uploaded') 