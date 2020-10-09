from django.shortcuts import render

# Create your views here.
def view_info(request):
    return render(request, "info_page.html")
