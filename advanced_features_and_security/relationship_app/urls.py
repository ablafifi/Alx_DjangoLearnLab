from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books



urlpatterns = [
    path('C:\Users\lafif\Documents\alx\Alx_DjangoLearnLab\django-models\relationship_app\books', views.list_books, name='list_books'),
    path('C:\Users\lafif\Documents\alx\Alx_DjangoLearnLab\django-models\relationship_app\library/<int:pk>', views.LibraryDetailView.as_view(), name='library_detail'),

    path('C:\Users\lafif\Documents\alx\Alx_DjangoLearnLab\django-models\relationship_app\login', LoginView.as_view(template_name='login.html'), name='login'),
    path('C:\Users\lafif\Documents\alx\Alx_DjangoLearnLab\django-models\relationship_app\logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('C:\Users\lafif\Documents\alx\Alx_DjangoLearnLab\django-models\relationship_app\register', views.register, name='register'),
]
