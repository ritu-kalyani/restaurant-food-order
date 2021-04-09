from django.shortcuts import redirect, render
from .models import Product,Contact,Orders,OrderUpdate, UserData
from math import ceil
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import sqlite3
from django.db.utils import IntegrityError

# import logging library
# import logging

# logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    # products= Product.objects.all()
    # print(products)
    # n= len(products)
    # nSlides =n//4 +ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    # allProds =[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    allProds=[]
    catprods =Product.objects.values('category','id')
    cats ={item['category'] for item in catprods}
    for cat in cats:
        prod =Product.objects.filter(category=cat)
        n =len(prod)
        nSlides =n//4 +ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])

    params={'allProds':allProds}
    return render(request,"index2.html",params)

def searchMatch(query, item):
    # '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request,'search.html', params)


def about(request):
    return render(request,"about.html")

@login_required(login_url='/shop/login')
def contact(request):
    thank = False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True
    
    userData = UserData.objects.get(username=request.user.username)
    context = {'user': userData, 'thank': thank}

    return render(request,"contact.html",context)        

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    if request.user.is_authenticated:
        userData = UserData.objects.get(username=request.user.username)
        context={'orders': list(Orders.objects.filter(user_id=userData))}
        return render(request, 'tracker.html', context)
    else:
        return render(request, 'tracker.html')

def productview(request,id):
    #fetch the products using id 
     product =Product.objects.filter(id=id)
     return render(request,"prodview.html",{'product':product[0]})

@login_required(login_url='/shop/login')
@csrf_protect
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, user_id=UserData.objects.get(username=request.user.username))
        order.save()
        update = OrderUpdate(order_id = order.order_id,update_desc ="Your Order Has Been Placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})

    userData = UserData.objects.get(username=request.user.username)
    context = {'user': userData}
    return render(request, 'checkout.html', context)

def faq(request):
    return render(request,'faq.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
        try:
            data = request.POST
            user = UserData(username=data['username'],fullname=data['full-name'], email=data['email-address'], address=data['present_address'], city=data['city'], state=data['state'], zip_code=data['zip'], phone=data['phone_number'])
            user.save()
            userData = User.objects.create_user(username=data['username'], password=data['full-password'], email=data['email-address'])
            userData.save()
        except sqlite3.IntegrityError as e:
            return HttpResponse('409: Given User already exists', status=409)
        
        except IntegrityError as e:
            return HttpResponse('409: Given User already exists', status=409)
    return render(request,'register.html')

@csrf_protect
def login(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        
        if user is not None:
            auth_login(request, user)

            return redirect('/shop/')
        
        else:
            return HttpResponse('401 Unauthorized', status=401)
    return render(request,'login.html')

@login_required(login_url='/shop/login')
def logout(request):
    auth_logout(request)
    return redirect('/shop/')
     