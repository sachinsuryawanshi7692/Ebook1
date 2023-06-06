from django.shortcuts import render,redirect
from django.http import HttpResponse
from ebookapp.models import Product
from django.db.models import Q
from ebookapp.forms import EmpForm,ProductModelForm,UserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def home(request):
    #data=Product.objects.all()  #select * from ebookshop_product;(fetch all data)
    #print(data)
    data=Product.objects.filter(status=1)
    content={}
    content['products']=data
    return render(request,'index.html',content)

#def register(request):
 #   return render(request,'register.html')

#def login(request):
 #   return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')
                

def reuse(request):
    return render(request,'base1.html')

#sort price

def sort(request,sv):
    if sv == '0':
        param="price"
    else:
        param="-price"

    data=Product.objects.order_by(param).filter(status=1)
    content={}
    content['products']=data
    return render(request,'index.html',content)

def catfilter(request,catv):
    q1=Q(cat=catv)
    q2=Q(status=1)
    data=Product.objects.filter(q1 & q2)
    content={}
    content['products']=data
    return render(request,'index.html',content)

def pricerange(request):

    low=request.GET['min']
    high=request.GET['max']
    q1=Q(status=1)
    q2=Q(price__gte=low)
    q3=Q(price__lte=high)
    content={}
    data=Product.objects.filter(q1 & q2 & q3)
    content['products']=data
    return render(request,'index.html',content)


def product_details(request,pid):
    data=Product.objects.filter(id=pid)
    content={}
    content['products']=data
    return render(request,'product_details.html',content)

def addbook(request):
    #print("Method is:",request.method)
    if request.method=="POST":
        #print("insert in database")
        #fetch data from request POST
        n=request.POST['pname']
        c=request.POST['pcat']
        amt=request.POST['pprice']
        d=request.POST['bdate']
        s=request.POST['status']
        #print(n)
        #print(cat)
        #print(amt)
        #print(s)
        p=Product.objects.create(name=n,cat=c,price=amt,date=d,status=s)
        #print(p)
        p.save()
        return redirect('/addbook')

    else:
       #print("Insert in else part") 
       p=Product.objects.all()
       content={}
       content['products']=p   
       return render(request,'addbook.html',content)


def delbook(request,rid):
    #print("Delete id:",rid)
    #fetch record to be deleted
    p=Product.objects.filter(id=rid)
    p.delete()
    return redirect('/addbook')


def editbook(request,rid):
     
    if request.method=="POST":
       uname=request.POST['pname']
       ucat=request.POST['pcat']
       uprice=request.POST['pprice']
       udate=request.POST['bdate']
       ustatus=request.POST['status']
       p=Product.objects.filter(id=rid)
       p.update(name=uname,cat=ucat,price=uprice,date=udate,status=ustatus)
       return redirect('/addbook')
    else:
        p=Product.objects.filter(id=rid)
        content={}
        content['products']=p
        return render(request,'editbook.html',content)

def djangoform(request):
    if request.method=="POST":
       ename=request.POST['name']
       dept=request.POST['dept']
       email=request.POST['email']
       sal=request.POST['salary']
    
    else:
        obj=EmpForm()
        content={}
        content['forms']=obj
        return render(request,'djangoform.html',content)

def modelform(request):
    if request.method=="POST":
        pass
    else:
        pobj=ProductModelForm()
        #print(pobj)
        content={}
        content['mform']=pobj
        return render(request,'modelform.html',content)


def user_register(request):
    content={}
    regobj=UserForm()
    content['uform']=regobj

    if request.method =="POST":
       regobj=UserForm(request.POST)
       print(regobj)

       if regobj.is_valid():
          regobj.save()
          content['success']="User Created Successfully"
          return render(request,'user_register.html',content)
    
    else:
        regobj=UserForm()
        return render(request,'user_register.html',content)
        #regobj=UserCreationForm()
        #print(regobj)

def user_login(request):
    
    if request.method=="POST":
       logobj=AuthenticationForm(request=request,data=request.POST)
       #print(logobj)
       if logobj.is_valid():
          uname=logobj.cleaned_data['username']
          upass=logobj.cleaned_data['password']
          #print("username:",uname)
          #print("PASSWORD:",upass)
          u=authenticate(username=uname,password=upass)
          #print(u)
          if u:
            print("In Login function if block")
            login(request,u)
            return HttpResponse("User is successsfully logged in")

    else:
        logobj=AuthenticationForm()
        content={}
        content['loginform']=logobj
        return render(request,'user_login.html',content)


def setsession(request):

    request.session['name']= 'Krushna'
    return render(request,'setsession.html' )

def getsession(request):

    content={}
    content['data']=request.session['name']
    return render(request,'getsession.html',content)

def addtocart(request):
    uid=request.user.id
    print("id of the user:",uid)
    return HttpResponse("IN addtocart section")

def user_logout(request):
    logout(request)
    return redirect('/login')
    



    







