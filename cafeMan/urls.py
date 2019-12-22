from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.location, name="location"),
    path('products/',views.product, name="products"),
    path('order/<int:food_id>',views.order,name='order'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('order/add_item_to_order/',views.add_item_to_order,name='add_item_to_order'),
    path("otp/", views.otp, name="otp"),
    path('admin_dash/otpVerify/',views.otpVerify,name='otpVerify'),
    path('send_pdf/',views.send_pdf,name='send_pdf')
]