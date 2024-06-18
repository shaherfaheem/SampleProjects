from django.urls import path, include
from . import views, guestorder,utils,admin
urlpatterns = [
    path("", views.store, name = "store"),
    path("store/search/", views.search, name = "search"),
    path("store/login/", views.login, name = "login"),
    path("store/register/", views.register, name = "register"),
    path("store/registered/", views.Registration, name = "registered"),
    path("store/loggedin/", views.LoggingIn, name = "loggedin"),
    path("store/loggedout/", views.signout, name = "logout"),
    path("cart/", views.cart, name = "cart"),
    path("checkout/", views.checkout, name = "checkout"),
    path("updateitem/", views.updateItem, name = "updateitem"),
    path("processorder/", views.processOrder, name = "processorder"),
]
   