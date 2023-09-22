from django.urls import path
from . import views

app_name = 'swj'

urlpatterns = [
    # members views
    path('', views.main_page, name='main_page'),
    path('<int:id>/', views.member_detail, name='member_detail'),
    path('', views.homepage, name='homepage'),
    path('contributors', views.contributors, name='contributors'),
    path('members', views.members, name='members'),
    path('references', views.references, name='references'),
]