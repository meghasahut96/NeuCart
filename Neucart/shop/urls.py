from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="index"),
    path('contact/', views.contact,name="contact"),
    path('tracker/', views.tracker,name="tracker"),
    path('productView/<int:id>', views.productView,name="productView"),
    path('search/', views.search,name="search"),
    path('checkout/', views.checkout,name="checkout"),
    path('about/', views.about,name="about"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)