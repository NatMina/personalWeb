from django.shortcuts import render
from django.shortcuts import redirect
from django.templatetags.static import static
from .models import Experience, Education, Certification

# Create your views here.


def index(request):
    return render(request, 'index1.html')


def education_view(request):
    education_data = Education.objects.all().order_by('-end_date')
    return render(request, 'education.html', {'education_data': education_data})


def experience_view(request):
    experience_data = Experience.objects.all().order_by('-end_date')
    return render(request, 'experience.html', {'experience_data': experience_data})

def certification_view(request):
    certification_data = Certification.objects.all().order_by('-date')
    return render(request, 'certification.html', {'certification_data': certification_data})

def certifications_view(request):
    cert_images = [
        'AlexCertImage/cert1.jpg',
        'AlexCertImage/cert2.jpg',
        'AlexCertImage/cert3.jpg',
        'AlexCertImage/cert4.jpg',
        'AlexCertImage/cert5.jpg',
        'AlexCertImage/cert6.jpg',
        'AlexCertImage/cert7.jpg',

    ]
    return render(request, 'viewcertificates.html', {'cert_images': cert_images})

def aboutMe(request):
    return render(request, 'aboutme.html')
