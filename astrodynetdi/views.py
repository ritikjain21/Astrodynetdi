from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from home.models import ProductDetailPage, ApplicationDetailPage


def PageNotFound(request):
    return render(request, 'home/404.html')


def product_detail_page(request, slug):
    page = ProductDetailPage.objects.get(slug=slug)
    products = page.products.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    drop_down = ProductDetailPage.objects.live().public().order_by('-id')
    application_drop_down = ApplicationDetailPage.objects.live().public().order_by('-id')
    return render(request, 'home/product_detail_page.html', {'page': page, 'products': products,
                                                             'dropdown_product': drop_down,
                                                             'dropdown_application': application_drop_down})