from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request,'welcome.html')

def get_started(request):
    return render(request, 'get_started2.html')


def login_cust(request):
    cust_login = CustLogin()
    if request.method == 'POST':
        cust_login = CustLogin(request.POST)
        # print("1")
        # email = cust_login.cleaned_data['email']
        # pswd = cust_login.cleaned_data['pswd']
        if cust_login.is_valid():
            # print("2")
            email = cust_login.cleaned_data['email']
            pswd = cust_login.cleaned_data['pswd']
            user = authenticate(username=email, password=pswd)
            # print("3")
            # if user is not None:
            #     print("4")
            #     login(request, user)
            return redirect('/uhome/') #hard coded for now
            # else:
            #     messages.error(request, "Invalid username or password")
    
    context = {'cust_login':cust_login}
    return render(request, 'cust_login.html', context)

def login_seller(request):
    sell_login = SellerLogin()
    if request.method == 'POST':
        sell_login = SellerLogin(request.POST)
        if sell_login.is_valid():
            email = sell_login.cleaned_data['email']
            pswd = sell_login.cleaned_data['pswd']
            user = authenticate(username=email, password=pswd)
            # print("1")
            # if user is not None:
            #     login(request, user)
            return redirect('/seller/') #hard coded for now
            # else:
            #     messages.error(request, "Invalid username or password")
    
    context = {'sell_login':sell_login}
    return render(request, 'sell_login.html', context)

def cust_reg(request):
    c_reg = CustRegister()
    if request.method =='POST':
        c_reg = CustRegister(request.POST)
        if c_reg.is_valid():
            fname = c_reg.cleaned_data['fname']
            lname = c_reg.cleaned_data['lname']
            email = c_reg.cleaned_data['email']
            mob = c_reg.cleaned_data['u_phone']
            pswd = c_reg.cleaned_data['pswd']
            conf_pswd = c_reg.cleaned_data['conf_pswd']
            c = Customer(fname=fname, lname=lname, email=email, u_phone=mob, pswd=pswd, conf_pswd=conf_pswd)
            c.save()
            messages.success(request,"Your profile has been updated Succesfully")
            return redirect('/home/get_started/')
    context = {'c_reg':c_reg}
    return render(request, 'cust_reg.html', context)

def seller_reg(request):
    s_reg = SellRegister()
    if request.method =='POST':
        s_reg = SellRegister(request.POST)
        if s_reg.is_valid():
            fname = s_reg.cleaned_data['fname']
            lname = s_reg.cleaned_data['lname']
            email = s_reg.cleaned_data['email']
            mob = s_reg.cleaned_data['s_phone']
            company = s_reg.cleaned_data['company']
            address = s_reg.cleaned_data['address']
            locality = s_reg.cleaned_data['locality']
            descr = s_reg.cleaned_data['description']
            pswd = s_reg.cleaned_data['pswd']
            conf_pswd = s_reg.cleaned_data['conf_pswd']
            s = Seller(fname=fname, lname=lname, email=email, s_phone=mob, company=company, address=address, locality=locality, description=descr, pswd=pswd, conf_pswd=conf_pswd)
            s.save()
            messages.success(request,"Your profile has been updated Succesfully")
            return redirect('/home/get_started/')
    context = {'s_reg':s_reg}
    return render(request, 'owner_reg.html', context)

def test1(request):
    # seller= Seller.objects.get(id=s_pk)
    if request.user.is_authenticated:
        seller = request.user.seller

    customer= Customer.objects.all()
    orders=seller.order_set.all()
    customer_names=orders.values('customer').distinct()
    c_name=[]
    for c in customer_names:
        c_name.append(customer.get(id=c['customer']))
    orders_count=orders.count()
    pending_orders_count = orders.filter(status="Pending").count()
    status = StatusUpdate()
    if request.method=='POST':
        status = StatusUpdate()
        if status.is_valid():
            status.save()
            return redirect('/seller/'+str(seller.id))
    context ={'seller':seller,'orders':orders,'orders_count':orders_count,'c_name':c_name,'customer':customer, 'pending_orders_count':pending_orders_count, 'status':status}
    return render(request,'seller.html',context)

def test2(request,c_pk):
    customer= Customer.objects.get(id=c_pk)
    orders=customer.order_set.all()
    orders_count=orders.count()
    context ={'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'cus_details.html',context)

def orderUpdate(request,pk):
    order=Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/seller/'+str(order.seller.id))
    context = {'form':form}
    return render(request,'order_update.html',context)

def userHome(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        cart,created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
        cartitems = cart.get_cart_items

    else:
        items=[]
        order = {'get_cart_total':0,'get_cart_items':0}

    #******************************************************************************
    # customer=Customer.objects.get(id=pk)
    customer=request.user.customer
    food=Product.objects.filter(category="Food")
    art=Product.objects.filter(category="Art")
    bites=Product.objects.filter(category="Quick Bites")
    seller=Seller.objects.all()
    order=customer.order_set.all()
    context={'user':customer,'seller':seller,'order':order,'food':food,'art':art,'bites':bites,'cartitems':cartitems}
    return render(request,'userhome.html', context)

def userProfile(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        cart,created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
        cartitems = cart.get_cart_items

    else:
        items=[]
        order = {'get_cart_total':0,'get_cart_items':0}

    #******************************************************************************


    # user=Customer.objects.get(id=pk)
    customer=request.user.customer
    u_update=UserUpdate(instance=customer)
    order= customer.order_set.all()
    orders_count=order.count()
    context={'user':customer,'orders_count':orders_count,'u_form':u_update,'cartitems':cartitems}
    if request.method =='POST':
        u_update=UserUpdate(request.POST,request.FILES,instance=customer)
        if u_update.is_valid():
            u_update.save()
            messages.success(request,"Your profile has been updated Succesfully")
            return redirect('/uprofile/'+str(customer.id))
            # return redirect('/uprofile/')
    return render(request,'userprofile.html',context)

def order(request,pk):
    if request.user.is_authenticated:
        customer=request.user.customer
        cart,created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
        cartitems = cart.get_cart_items

    else:
        items=[]
        order = {'get_cart_total':0,'get_cart_items':0}

    #******************************************************************************


    seller=Seller.objects.get(id=pk)
    products=Product.objects.filter(seller=seller)
    orders=seller.order_set.all()
    orders_count=orders.count()
    context={'seller':seller,'orders':orders,'orders_count':orders_count,'products':products,'cartitems':cartitems}
    return render(request,'sellerpage.html',context)


def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        cart,created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
        cartitems = cart.get_cart_items

    else:
        items=[]
        order = {'get_cart_total':0,'get_cart_items':0}
    #******************************************************************************
    d_form = Shipping( )
    if request.method == 'POST':
        d_form = Shipping(request.POST)
        if d_form.is_valid():
            messages.success(request,"Order has been Sucessfully Placed")
            new_order = Order(customer=customer,seller=cart.seller,status="Pending")
            new_order.save()
            for i in items:
                new_item=OrderItem(product=i.product,order=new_order,quantity=i.quantity)
                new_item.save()
                i.delete()
            d_form.save()
            d_mod = Delivery.objects.filter(dno=d_form.data['dno'],street=d_form.data['street'],locality=d_form.data['locality']).first()
            d_mod.order= new_order
            d_mod.save()
            cart.delete()            
            return redirect('/orders/')

    context={'items':items,'cart':cart,'cartitems':cartitems,'d_form':d_form}
    return render(request,'usercart.html',context)

def vieworders(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        cart,created = Cart.objects.get_or_create(customer=customer)
        items = cart.cartitem_set.all()
        cartitems = cart.get_cart_items

    else:
        items=[]
        order = {'get_cart_total':0,'get_cart_items':0}


    customer=request.user.customer
    orders= Order.objects.filter(customer=customer).order_by('-date_created')
    context={'orders':orders,'cartitems':cartitems}
    return render(request,'orders.html',context)



def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order= Cart.objects.filter(customer=customer).first()
    order.seller= product.seller
    order.save()
    orderitem,created = CartItem.objects.get_or_create(product=product,order=order)
    if action =='add':
        orderitem.quantity = orderitem.quantity+1
    #add an elif later for removing
    elif action == 'remove':
        orderitem.quantity = orderitem.quantity-1

    orderitem.save()
    if orderitem.quantity<=0:
        orderitem.delete()
    if order.get_cart_items == 0:
        Cart.objects.filter(customer=customer).delete()

    print(productId,action)
    return JsonResponse('Item was added', safe=False)

def sellerProfile(request,pk):
    if request.user.is_authenticated:
        seller = request.user.seller
    # seller=Seller.objects.get(id=pk)
    s_update=SellerUpdate(instance=seller)
    # order=user.order_set.all()
    # orders_count=order.count()
    # context={'user':user,'orders_count':orders_count,'u_form':u_update}
    context={'seller':seller, 's_form':s_update}
    if request.method =='POST':
        s_update=SellerUpdate(request.POST,request.FILES,instance=seller)
        if s_update.is_valid():
            s_update.save()
            messages.success(request,"Your profile has been updated Succesfully")
            return redirect('/sprofile/'+str(seller.id))
    return render(request,'sellerprofile.html',context)

def viewProducts(request):
    # if request.user.is_authenticated:
    #     seller = request.user.seller
    
    # # customer= Customer.objects.all()
    # orders=seller.order_set.all()
    # order_names=orders.values('name').distinct()
    # o_name=[]
    # for o in order_names:
    #     o_name.append(.get(id=c['customer']))
    # orders_count=orders.count()
    # pending_orders_count = orders.filter(status="Pending").count()
    
    return render(request, 'viewProducts.html')
def productsAdd(request):
    # seller_obj = Seller.objects.get(id=pk)
    if request.user.is_authenticated:
        seller = request.user.seller
    # order = 
    p_form = ProductForm()
    if request.method =='POST':
        p_form = ProductForm(request.POST)
        if p_form.is_valid():
            name = p_form.cleaned_data['name']
            price = p_form.cleaned_data['price']
            # s = p_form.cleaned_data['seller']
            category = p_form.cleaned_data['category']
            descr = p_form.cleaned_data['description']
            p = Product(name=name, price=price, category=category, description=descr)
            p.save()
            messages.success(request,"Your profile has been updated Succesfully")
            return redirect('/products/'+str(seller.id))
    context = {'user':seller, 'p_form':p_form}
    return render(request, 'products.html', context)

def productsUpdate(request):
    if request.user.is_authenticated:
        seller=request.user.seller

    # else:
    #     items=[]
    #     order = {'get_cart_total':0,'get_cart_items':0}

    #******************************************************************************


    # user=Customer.objects.get(id=pk)
    seller=request.user.seller
    p_update=ProductUpdateForm(instance=seller)
    # order= customer.order_set.all()
    # orders_count=order.count()
    # context={'user':customer,'orders_count':orders_count,'u_form':u_update,'cartitems':cartitems}
    context = {'user':seller, 'p_update':p_update}
    if request.method =='POST':
        p_update=ProductUpdateForm(request.POST,instance=seller)
        if p_update.is_valid():
            p_update.save()
            messages.success(request,"Your profile has been updated Succesfully")
            return redirect('/products/'+str(seller.id))
            # return redirect('/uprofile/')
    return render(request,'productsUpdate.html',context)