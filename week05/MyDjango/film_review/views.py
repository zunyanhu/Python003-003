from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import T1


def film_review(request):
    shorts = T1.objects.filter(n_star__gt=3)

    return render(request, 'index.html', locals())


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'errors.html', {'error_msg': error_msg})

    post_list = T1.objects.filter(title__icontains=q)
    return render(request, 'results.html', {'error_msg': error_msg,
                                            'post_list': post_list})