import json

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.urls import reverse

from .models import UserCreate,Product,Shoping

def register_view(request:HttpRequest)->HttpResponse:
    if request.method == 'GET':
        return render(request=request,template_name = 'register.html')
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode())
            username = data['username']
            password = data['password']
        except Exception:
            username = request.POST.get('username')
            password = request.POST.get('password')

        if UserCreate.objects.filter(username = username).exists():
            return HttpResponse(
                content='User alredy exsists',status = 404
            )
      
        UserCreate(username = username,password = password).save()

        return redirect(to='shop:login_page')


def login_view(request:HttpRequest)->HttpResponse:
    if request.method == 'GET':
        return render(request=request,template_name = 'login.html')
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode())
            username = data['username']
            password = data['password']
        except Exception:
            username = request.POST.get('username')
            password = request.POST.get('password')

        if UserCreate.objects.filter(username = username,password = password).exists():
            return render(request=request,template_name='product.html')
        else:
            return HttpResponse(
                content='User Not Found',status = 404
            )
        

def get_product_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'product.html')

    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode())
            username = data['username']
            name = data['name']
            quantity = int(data['quantity'])
            category = data['category']
        except Exception:
            username = request.POST.get('username')
            name = request.POST.get('name')
            quantity = int(request.POST.get('quantity', 0))
            category = request.POST.get('category')

        if not UserCreate.objects.filter(username=username).exists():
            return HttpResponse('User not found', status=400)

        product = Product.objects.filter(name=name, category=category).first()
        if not product:
            return HttpResponse('Product not found', status=400)

        if product.quantity < quantity:
            return HttpResponse(f'Buncha {name} mavjud emas!', status=400)

        total_price = product.price * quantity

        Shoping.objects.create(
            username=username,
            name=name,
            total_price=total_price,
            quantity=quantity
        )

        shoping_list = Shoping.objects.filter(username=username)
        return render(request, 'basket.html', {'data': shoping_list})

def all_product(request:HttpRequest)->HttpResponse:
    data = Product.objects.all()
    return render(request,'all_product.html',context={
        'data':data
    })

def basket_view(request:HttpRequest)->HttpResponse:
    data = Product.objects.all()
    return render(request,'basket.html',context={
        'data':data
    })

def add_product(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request,template_name='add_product.html')
    if request.method == 'POST':
        try:
            for data in json.loads(request.body.decode()):
                Product(
                name = data['name'],
                category = data['category'],
                price = data['price'],
                quantity = data['quantity']
                ).save()  
        except Exception:
            Product(
                name = request.POST.get('name'),
                category = request.POST.get('category'),
                price = request.POST.get('price'),
                quantity = request.POST.get('quantity') 
            ).save()  

        return redirect(to=reverse('shop:all_product'))