from django.shortcuts import render
from store.models import Product, ReviewRating
from carousels.models import Carousel
from store.models import ProdDeal
from brand.models import Brand
from django.db.models import Count


def get_deal():
    # Your logic to retrieve a deal goes here
    # For example, you might query the database or perform some other computation
    return "Some deal"

def home(request):
    deal = get_deal()

    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    carousel_list = Carousel.objects.all().order_by('-id')

    reviews_list = []  # Initialize an empty list to store reviews for all products

    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        reviews_list.extend(reviews)  # Add reviews for the current product to the list
        deal = ProdDeal.objects.first()
        
        all_brands = Brand.objects.filter(product__is_available=True).annotate(product_count=Count('product')).distinct()


    context = {
        'products': products,
        'carousel_list': carousel_list,
        'reviews': reviews_list,  # Use the list of all reviews in the context
        'deal': deal,
        'all_brands': all_brands,
    }
    return render(request, 'home.html', context)
