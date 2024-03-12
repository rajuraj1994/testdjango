from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages

# Create your views here.
def index(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'products/products.html',context)

def show_category(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'products/showcategory.html',context)

def post_product(request):
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product added')
            return redirect('/products/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'failed to add product')
            return render(request,'products/addproduct.html',{'forms':form})
    context={
        'forms':ProductForm
    }
    return render(request,'products/addproduct.html',context)

def post_category(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added')
            return redirect('/products/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'failed to add category')
            return render(request,'products/addcategory.html',{'forms':form})
    context={
        'forms':CategoryForm
    }
    return render(request,'products/addcategory.html',context)

def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'product deleted')
    return redirect('/products')

def delete_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'category deleted')
    return redirect('/products/categorylist')

def update_product(request,product_id):
    instance=Product.objects.get(id=product_id)
    if request.method == 'POST':
        form=ProductForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'product updated')
            return redirect('/products')
        else:
            messages.add_message(request,messages.ERROR,'failed to update product')
            return render(request,'products/updateproduct.html',{'forms':form})

    context={
        'forms':ProductForm(instance=instance)
    }
    return render(request,'products/updateproduct.html',context)

def update_category(request,category_id):
    instance=Category.objects.get(id=category_id)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category updated')
            return redirect('/products/categorylist')
        else:
            messages.add_message(request,messages.ERROR,'failed to update category')
            return render(request,'products/updatecategory.html',{'forms':form})

    context={
        'forms':CategoryForm(instance=instance)
    }
    return render(request,'products/updatecategory.html',context)
