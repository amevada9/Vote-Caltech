from django.shortcuts import render

# Create your views here.
def voter_info_view(request): 
    return render(request, 'voter_info.html')
