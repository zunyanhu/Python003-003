from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from .models import T1
from django.db.models import Q
from django.contrib import messages


def film_review(request):
    shorts = T1.objects.filter(n_star__gt=3)

    return render(request, 'film_review.html', locals())


def search(request):
    q = request.GET.get('q')
    error_msg = '请输入关键词'

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'search_error.html', {'error_msg': error_msg})

    short_results = T1.objects.filter(short__contains=q)
    return render(request, 'search_results.html', {'error_msg': error_msg,
                                            'short_results': short_results})
