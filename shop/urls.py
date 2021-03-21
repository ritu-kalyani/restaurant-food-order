from django.urls import path
from shop import views

urlpatterns = [
    path("", views.index,name="ShopHome"),
    path("about/", views.about,name="AboutUs"),
    path("contact/", views.contact,name="ContactUs"),
    path("tracker/", views.tracker,name="TrackingStatus"),
    path("search/", views.search,name="search"),
    path("products/<int:id>", views.productview,name="ProductView"),
    path("checkout/", views.checkout,name="Checkout"),    
    path("faq/",views.faq,name="faq"),
]
