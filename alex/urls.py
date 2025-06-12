from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index1'),
    path('education/', views.education_view, name='education'),
    path('experience/', views.experience_view, name='experience'),
    path('certifications/', views.certification_view, name='certifications'),
    path('certificate/', views.certifications_view, name='viewcertification'),
    path('aboutme/', views.aboutMe, name='aboutme'),

]