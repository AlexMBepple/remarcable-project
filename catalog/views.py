from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Category, Tag


def home(request):
    return render(request, 'catalog/index.html')


def categories_api(request):
    categories = Category.objects.all().order_by('name')
    return JsonResponse({
        'categories': [{'id': c.id, 'name': c.name} for c in categories]
    })


def tags_api(request):
    category_id = request.GET.get('category', '')
    query = request.GET.get('q', '').strip()

    filters = Q()
    if category_id:
        filters &= Q(category_id=category_id)
    if query:
        filters &= (Q(name__icontains=query) | Q(description__icontains=query))

    tags = (
        Tag.objects
        .filter(products__in=Product.objects.filter(filters))
        .distinct()
        .order_by('name')
    )
    return JsonResponse({
        'tags': [{'id': t.id, 'name': t.name} for t in tags]
    })


def products_api(request):
    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '')
    tag_ids = request.GET.getlist('tags')
    page_number = request.GET.get('page', '1')

    filters = Q()
    if query:
        filters &= (Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        filters &= Q(category_id=category_id)
    if tag_ids:
        filters &= Q(tags__id__in=tag_ids)

    products = (
        Product.objects
        .select_related('category')
        .prefetch_related('tags')
        .filter(filters)
    )

    if tag_ids:
        products = products.distinct()

    products = products.order_by('name', 'id')

    paginator = Paginator(products, settings.CATALOG_PAGE_SIZE)
    page = paginator.get_page(page_number)

    data = [{
        'id': str(p.id),
        'name': p.name,
        'description': p.description,
        'category': p.category.name if p.category else None,
        'tags': [t.name for t in p.tags.all()],
    } for p in page]

    return JsonResponse({
        'products': data,
        'page': page.number,
        'has_next': page.has_next(),
        'total_pages': paginator.num_pages,
        'count': paginator.count,
    })