from django.shortcuts import get_object_or_404, render,redirect

from .forms import checkoutForm
from . models import products,category,cartitem,cart,checkout
from django.contrib import messages
from django.contrib.auth.models import User,auth





# Create your views here.
def home(request,cate_id=None):
    if cate_id is not None:
        cate=category.objects.get(id=cate_id)
        obj=products.objects.filter(cate=cate_id,available=True)
    else:
         obj=products.objects.filter(available=True)
    cate=category.objects.all()
    return render(request,'fashion.html',{"obj":obj,"cate":cate})
def details(request,pro_id):
    product1=products.objects.get(id=pro_id)
    return render(request,'details.html',{'product':product1})

def addtocart(request,product_id):
    user=User.objects.get(id=request.user.id)
    product=products.objects.get(id=product_id)
    if cart.objects.filter(user=user).exists():
        print('here')
        # cart=cartitem.objects.create(cart=cartitem.objects.get(user=User),product=products.objects.get(id=products))
        # cart.save()
        cartid = cart.objects.get(user=user)
        
        item=cartitem.objects.create(product=product,cartid=cartid)
        item.save()
    else:
            print('hello')
            Cart=cart.objects.create(user=user)
            Cart.save()

            item=cartitem.objects.create(product=product,cartid=Cart)
            item.save()

    messages.info(request, "product added to cart sucessfully")
    return redirect('home')
def cartview(request):
     user=User.objects.get(id=request.user.id)
     cart1=cart.objects.get(user=user)
     cartview=cartitem.objects.filter(cartid=cart1)
    #  if request.method=='POST':
    #       value=request.POST.get
          
     return render(request,'cartdetails.html',{"cartview":cartview})
def increment(request,itemad_id):
     if request.method=="POST":
          
        print("this place increment")
        item=get_object_or_404(cartitem, id=itemad_id)
        item.quantity += 1
        item.save()
        
        return redirect('cartview')
def decrement(request,itemde_id):
     if request.method=="POST":
        print("this place here decrement")
        item=get_object_or_404(cartitem,id=itemde_id )
        if item.quantity > 1 :
            item.quantity -= 1 
            item.save()
        else:
            item.delete()
        return redirect('cartview')
def delete(request,itemre_id):
     if request.method=="POST":
        item=get_object_or_404(cartitem,id=itemre_id)
        item.delete()
        # messages.info(request,'deleted')
        return redirect('/')
def create_order(request):
    user=User.objects.get(id=request.user.id)
    cart1=cart.objects.get(user=user)
    cartview=cartitem.objects.filter(cartid=cart1)
    total=0
    for i in cartview:
        total += i.product.price * i.quantity
    if request.method == "POST":
        Name = request.POST.get("firstName")
        print(Name)
        Email = request.POST.get("email")
        Address = request.POST.get("address")
        Paymenttype = request.POST.get("paymentMethod")

        if Paymenttype == "credit":
            payment = 1
        elif Paymenttype == "debit":
            payment = 2
        else:
            payment = 3  # Assume Paymenttype == "paypal"

        Order1 = checkout.objects.create(name=Name, email=Email, address=Address, paymenttype=payment)
        Order1.save()  
        return render(request, "sucess.html")   
    return render(request, 'chekout.html',{'cartview':cartview,'total':total})
    
    
# def order(request):
    
   
    
    # return render(request, "chekout.html")


# form=checkoutForm(request.post)
# if form.is_valid():
#             form.save()
        
# else:
#         form=checkoutForm()
# return redirect("/")
