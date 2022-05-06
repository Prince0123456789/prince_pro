from django.http import Http404, HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from shop import models


def login(request):
    res = render(request, 'login/login.html')
    return res
def signup(request):
    res = render (request, 'signup/signup.html')
    return res

def saveuser(request):
    ternusers= models.users()
    ternusers.uno=request.POST['uno']
    ternusers.uname=request.POST['uname']
    ternusers.upass=request.POST['upass']
    ternusers.uemail=request.POST['uemail']
    ternusers.umob=request.POST['umob'] 
    ternusers.save()
    return HttpResponseRedirect('http://localhost:8000/users/')

def newuser(request):
    err_msg = 'username already taken'
    d={}
    try:
        if int(request.GET['err'])==1:
            d['err_msg']=err_msg
    except:
        pass
    return render(request, 'signup/signup.html', d)

# delete exsting user

def del_user(request):
     ternusers=models.users.objects.get(id=int(request.GET['id']))
     ternusers.delete()
     return HttpResponseRedirect('http://localhost:8000/users/') 

def users(request):
    ternusers=models.users.objects.all()
    res = render(request,'shop/users.html', {'users':ternusers})
    return res

# SESSION


def deco_login(f1):
    def mod_f1(request):
        if 'username' in request.session.keys():
            print(request.session)
            return f1(request)
        else:
            raise Http404
    return mod_f1



def loginvalidate(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        ternusers=models.users.objects.get(uname=username,upass=password)
        request.session['username']=username
        s='http://localhost:8000/?user_login='+ternusers.uname
    except:
        s='http://localhost:8000/login/'
        print('hello')

    return HttpResponseRedirect(s)

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect("http://localhost:8000/account/login")



# shop 
@deco_login
def index(request):
    hj={}
    try:
        hj['user']=request.GET['user_login']
    except:
        pass
    return render(request, 'shop/index.html', hj)
def product(request):
    return render(request, 'shop/product.html')