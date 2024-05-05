from django.shortcuts import render

# Create your views here.
def templates(request):
    return render(request,'template_app/index.html',{'name':'Prathyush'})