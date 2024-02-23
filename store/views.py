from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating, ProductGallery
from category.models import Category, Sub_Category
from brand.models import Brand
from carts.models import CartItem
from django.db.models import Q

from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct

# Create your views here.
from .forms import PriceRangeForm


def store(request, category_slug=None, brand_slug=None, sub_category_slug=None):

    categories = None
    sub_categories = None
    brands = None
    products = None
    
    paged_products = None

    product_count = 0
    price_form = PriceRangeForm(request.GET)
    all_brands = Brand.objects.filter(product__is_available=True).distinct()

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug) 
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
        brands = Brand.objects.filter(product__category=categories).distinct()

    elif sub_category_slug is not None:
        sub_categories = get_object_or_404(Sub_Category, subslug=sub_category_slug)
        products = Product.objects.filter(sub_category=sub_categories, is_available=True)
        product_count = products.count()
        brands = Brand.objects.filter(product__sub_category=sub_categories).distinct()

    elif brand_slug is not None:
        brand_instance = get_object_or_404(Brand, brandslug=brand_slug) 
        products = Product.objects.filter(brand=brand_instance, is_available=True)
        product_count = products.count()
        brands = Brand.objects.filter(pk=brand_instance.pk)  # Ensure brands is always a queryset or a list


    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()


    if price_form.is_valid():
        min_price = price_form.cleaned_data['min_price']
        max_price = price_form.cleaned_data['max_price']

        # Handle the case when the form fields are not filled or are empty strings
        if min_price:
            products = products.filter(Discount_price__gte=min_price)
        if max_price:
            products = products.filter(Discount_price__lte=max_price)

        product_count = products.count()

    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    
    context = {
        'products': paged_products,
        'product_count': product_count,
        'price_form': price_form,
        'brands': brands,  # Ensure brands is always a queryset or a list
        'all_brands': all_brands,
    }
    return render(request, 'store/store.html', context)




from django.http import HttpResponseServerError


# views.py
from django.shortcuts import render, get_object_or_404
from wishlist.models import  Wishlist

def product_detail(request, category_slug, product_slug):
    try:
        single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

        orderproduct = None
        if request.user.is_authenticated:
            orderproduct = OrderProduct.objects.filter(user=request.user, product=single_product).exists()

        reviews = ReviewRating.objects.filter(product=single_product, status=True)
        related_products = single_product.related_products.all()
        product_gallery = ProductGallery.objects.filter(product=single_product)
        
        context = {
            'single_product': single_product,
            'in_cart': in_cart,
            'orderproduct': orderproduct,
            'reviews': reviews,
            'product_gallery': product_gallery,
            'related_products': related_products,
        }

        if request.method == 'POST' and request.user.is_authenticated:
            # Add product to wishlist
            user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
            user_wishlist.products.add(single_product)

        return render(request, 'store/product_detail.html', context)

    except Product.DoesNotExist:
        return HttpResponseServerError("Product not found.")





def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
            context = {
                'products':products,
                'product_count':product_count,
            }

    return render(request, 'store/store.html',context)



def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
            

