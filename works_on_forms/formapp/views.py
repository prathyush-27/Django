
from django.shortcuts import redirect,render
from django.urls import reverse

def show_form(request):
    return render(request,'formapp/form.html')


def submit_form(request):
    if request.method=='POST':
        request.session['fname'] = request.POST.get('fname')
        request.session['lname'] = request.POST.get('lname')
        request.session['email'] = request.POST.get('email')
        request.session['gitlink'] = request.POST.get('gitlink')
        return redirect('display_data')
    else:
        return redirect('show_form')

def display_data(request):
     fname = request.session.get('fname', 'Unknown')
     lname = request.session.get('lname', 'Unknown')
     email = request.session.get('email', 'Unknown@example.com')
     gitlink = request.session.get('gitlink', 'No Link Provided')

     context={
         'fname':fname,
         'lname':lname,
         'email':email,
         'gitlink':gitlink
     }
     return render(request,'formapp/display_data.html',context)