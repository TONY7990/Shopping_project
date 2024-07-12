from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('filter/<int:cate_id>',views.home,name='filter'),
    path('details/<int:pro_id>',views.details,name='details'),
    path('addtocart/<int:product_id>',views.addtocart,name='addtocart'),
    path('cartview',views.cartview,name='cartview'),
    path('increment/<int:itemad_id>',views.increment,name='increment'),
    path('decrement/<int:itemde_id>',views.decrement,name='decrement'),
    path('delete/<int:itemre_id>',views.delete,name='delete'),
    path('checkout',views.create_order,name='checkout'),
    # path('order',views.order,name='order')

]
