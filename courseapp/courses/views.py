from datetime import date, datetime
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Course, Category

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
            "imageUrl": "1.webp",
            "slug": "javascript-kursu",
            "date": datetime.now,
            "isActive": True,
            "isUpdated": True
        },
        {
            "title": "python kursu",
            "description": "python kurs açıklaması",
            "imageUrl": "2.webp",
            "slug": "python-kursu",
            "date": date(2022,10,10),
            "isActive": False,
            "isUpdated": True

        },
        {
            "title": "web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl": "3.webp",
            "slug": "web-gelistirme-kursu",
            "date": date(2022,10,10),
            "isActive": True,
            "isUpdated": False

        }
    ],
    "categories": [
        {"id":1, "name": "programlama", "slug": "programlama"},
        {"id":2, "name": "web geliştirme", "slug":"web-gelistirme" },
        {"id":3, "name": "mobil uygulamalar", "slug":"mobil-uygulamalar"},
        ]
}

def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar
    })

def details(request, kurs_id):
    try:
        course= Course.objects.get(pk=kurs_id)
    except:
        raise Http404()
    
    context = {
        'course': course 
    }
    return render(request, 'courses/details.html', context)


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
