from datetime import date
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
}

db = {
    "courses": [
        {
            "title": "javascript kursu",
            "description": "javascript kurs açıklaması",
            "imageUrl": "https://bairesdev.mo.cloudinary.net/blog/2023/08/What-Is-JavaScript-Used-For.jpg?tx=w_1920,q_auto",
            "slug": "javascript-kursu",
            "date": date(2022,10,10),
            "is-active": True
        },
        {
            "title": "python kursu",
            "description": "python kurs açıklaması",
            "imageUrl": "",
            "slug": "python-kursu",
            "date": date(2022,10,10),
            "is-active": False
        },
        {
            "title": "web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl": "",
            "slug": "web-gelistirme-kursu",
            "date": date(2022,10,10),
            "is-active": True
        }
    ],
    "categories": ["programlama","web geliştirme","mobil uygulama"]
}

def index(request):
    category_list = list(data.keys())
    
    return render(request, 'courses/index.html',{
        'categories': category_list
    })

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/kurslar.html', {
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("yanlıs kategori seçimi")
    
def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1]
    
    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)
