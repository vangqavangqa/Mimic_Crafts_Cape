from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product_Details, Categories, posted_jobs, job_post_status, Order, bennar, contact_table, Subcategory, Discount_Coupon, blog_post, Blogs_Comments, Brands, Custom_Project, catalog, newsletter_table
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
import random
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .models import EmailConfirmed
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def get_catalog(request):
    last_catalog = catalog.objects.last()
    url_catalog = last_catalog.catalog_url
    return HttpResponse(url_catalog)


def index(request):
    Product_Details_all = Product_Details.objects.all().order_by('-id')
    all_category = Categories.objects.all().order_by('-id')
    # pagination
    p = Paginator(all_category, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    #show list of pages
    number_of_pages_1 = p.num_pages+1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    # Search_with_price_all = Search_with_price.objects.all()
    # print(Search_with_price_all)

    # query jobs
    all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
    p_jobs = Paginator(all_jobs, 4)
    page2 = p_jobs.page(1)

    # if not price2:
    #     price2 = Add_prod.objects.aggregate(Max('price'))['price__max']
    #
    # my_products = Add_prod.objects.filter(price__range=(price1, price2))


    bennar_first = bennar.objects.first()

    if bennar_first:
        get_id_benner=bennar_first.id
        bennar_all = bennar.objects.all().exclude(id=get_id_benner)
    else:
        bennar_all = None
    all_latest_pst = blog_post.objects.order_by('-time')[:6]
    context2 = {'cats':page, 'Categories_all':Categories_all, 'list':list, 'all_jobs':page2, 'page_num':page_num, 'bennar_all':bennar_all, 'bennar_first':bennar_first, 'page_num':page_num, 'all_latest_pst':all_latest_pst}
    return render(request, 'index.html', context2)


def all_brands(request):
    all_brands = Brands.objects.all().order_by('-id')
    # pagination
    p = Paginator(all_brands, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    #show list of pages
    number_of_pages_1 = p.num_pages+1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    context2 = {'brands':page, 'Categories_all':Categories_all, 'list1':list, 'page_num':page_num, 'page_num':page_num}
    return render(request, 'brand_list.html', context2)




def subcats_of_cat(request, pk):
    get_category = Categories.objects.get(id=pk)
    all_subcat  = Subcategory.objects.filter(Category = get_category)
    # pagination
    qty_all_subcat = all_subcat.count()
    p = Paginator(all_subcat, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    #show list of pages
    number_of_pages_1 = p.num_pages+1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    # query jobs
    all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
    p_jobs = Paginator(all_jobs, 4)
    page2 = p_jobs.page(1)

    context2 = {'cats':page, 'Categories_all':Categories_all, 'list1':list, 'all_jobs':page2, 'page_num':page_num, 'page_num':page_num, 'qty_all_subcat':qty_all_subcat, 'get_category':get_category}

    return render(request, 'index2.html', context2)



def brands_list_subcat(request, pk):
    get_Subcategory = Subcategory.objects.get(id=pk)
    all_prd = Product_Details.objects.filter(subcategory=get_Subcategory).order_by('-id')
    qty_brn = 0
    lst_brnd = []
    for i in all_prd:
        if i in lst_brnd:
            pass
        else:
            qty_brn = qty_brn+1
            print(i.Brands)
            lst_brnd.append(i.Brands)

    print(lst_brnd)

    # pagination
    p = Paginator(lst_brnd, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    context = {'all_prd':page, 'Categories_all':Categories_all, 'list':list, 'page_num':page_num, 'get_Subcategory':get_Subcategory, 'qty_brn':qty_brn}
    return render(request, 'products_page2.html', context)





def products_subcats_brands(request):
    # brand= request.GET.get('brand')
    subcategory= request.GET.get('subcategory')

    # print('brand, subcategory')
    # print(brand, subcategory)

    get_Subcategory = Subcategory.objects.get(id=subcategory)
    # get_brand = Brands.objects.get(id=brand)

    get_prod_brand_cat = Product_Details.objects.filter(subcategory=get_Subcategory).order_by('-id')

    get_prod_brand_cat_qty = get_prod_brand_cat.count()


    # pagination
    p = Paginator(get_prod_brand_cat, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    context = {'all_prd':page, 'Categories_all':Categories_all, 'list':list, 'page_num':page_num, 'get_prod_brand_cat_qty':get_prod_brand_cat_qty, 'get_Subcategory':get_Subcategory}
    return render(request, 'products_page3.html', context)




def products_page(request):
    all_prd = Product_Details.objects.all().order_by('-id')

    Product_Details_all = Product_Details.objects.all().order_by('-id')

    # pagination
    p = Paginator(Product_Details_all, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    context = {'all_prd':page, 'Categories_all':Categories_all, 'list':list, 'page_num':page_num}
    return render(request, 'products_page.html', context)




def brand_products(request, pk):
    get_brnd = Brands.objects.get(id=pk)
    products_of_brand = Product_Details.objects.filter(Brands=get_brnd).order_by('-id')
    # pagination
    p = Paginator(products_of_brand, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages
    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)
    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    Categories_all = Categories.objects.all()
    context = {'all_prd':page, 'Categories_all':Categories_all, 'list':list, 'page_num':page_num}
    return render(request, 'products_page5.html', context)



def profile(request):
    Categories_all = Categories.objects.all()
    context22= {'Categories_all':Categories_all}
    return render(request, 'profile.html', context22)


def gp_jobs(request):
    if request.method == "POST":
        job_title = request.POST.get('job_title')
        job_location = request.POST.get('job_location')
        job_type = request.POST.get('job_type')
        # print(job_title, job_location, job_type)


        # search_jobs_form = posted_jobs.objects.filter(Q(job_title__icontains=job_title) | Q(job_details__icontains=job_title) | Q(job_location__icontains=job_location) | Q(job_type__icontains=job_type)).order_by('-id')

        search_jobs_form = posted_jobs.objects.filter(Q(job_title__icontains=job_title) | Q(job_details__icontains=job_title)).filter(job_post_status='2').order_by('-id')

        search_jobs_count = posted_jobs.objects.filter(Q(job_title__icontains=job_title) | Q(job_details__icontains=job_title)).filter(job_post_status='2').order_by('-id').count()

        Categories_all = Categories.objects.all()

        context13 = {'search_jobs_form':search_jobs_form, 'job_title':job_title, 'job_location':job_location, 'job_type':job_type, 'search_jobs_count':search_jobs_count, 'Categories_all':Categories_all}
        return render(request, 'gp_jobs.html', context13)
    else:
        all_job_post = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
        Categories_all = Categories.objects.all()
        context12 = {'all_job_post':all_job_post, 'Categories_all':Categories_all}
        return render(request, 'gp_jobs.html', context12)


def contact(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')

    save_contact_table=contact_table(name=name, email=email, message=message)
    save_contact_table.save()

    messages.success(request, name+' Your Message Successfully Deliver to Manager. Our manager will get back to you soon. Thank You !!')
    return redirect('/')



def about(request):
    Categories_all = Categories.objects.all()
    context22 = {'Categories_all': Categories_all}
    return render(request, 'about.html', context22)


def see_my_post(request):
    user = request.user
    mypost = posted_jobs.objects.filter(user=user).order_by('-id')

    # pagination
    p = Paginator(mypost, 10)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    context11 = {'mypost':page, 'list':list, 'Categories_all':Categories_all}
    return render(request, 'see_my_post.html', context11)


def job_post_details(request, pk):
    get_posted_jobs_id = posted_jobs.objects.get(id=pk)
    Categories_all = Categories.objects.all()

    context11 = {'get_posted_jobs_id':get_posted_jobs_id, 'Categories_all':Categories_all}
    return render(request, 'job_post_details.html', context11)

def post_job(request):
    if request.method=="POST":
        post_job_title1 = request.POST.get('post_job_title', '')
        # a=post_job_title.capitalize()
        post_job_title=post_job_title1.upper()
        post_job_details = request.POST.get('post_job_details', '')
        post_job_location1 = request.POST.get('post_job_location', '')
        post_job_location = post_job_location1.upper()
        post_job_type = request.POST.get('post_job_type', '')
        jobs_salary = request.POST.get('jobs_salary', '')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        company_name = request.POST.get('company_name', '')
        qualification = request.POST.get('qualification', '')

        job_p_status = request.POST.get('job_p_status')
        # print(job_p_status)

        het_job_pst_sttus = job_post_status.objects.get(job_post_status=job_p_status)

        user = request.user
        # print(user)

        save_job_post = posted_jobs(user=user, job_title=post_job_title, company_name=company_name, job_details=post_job_details, qualification=qualification, job_location=post_job_location, job_type=post_job_type, salary=jobs_salary, phone_number=phone_number, job_post_status=het_job_pst_sttus, email=email)
        save_job_post.save()

        messages.success(request, 'Your Job Post is Under Review !! If Every Thing Alright, Your post will be Arrived in 48 hours !!')

        return redirect('gp_jobs')
    else:
        get_status = job_post_status.objects.filter(id='1')
        Categories_all = Categories.objects.all()

        context10 = {'get_status': get_status, 'Categories_all':Categories_all}
        return render(request, 'post_job.html', context10)


def custom_project(request):
    if request.method=="POST":
        your_name = request.POST.get('your_name', '')
        company_name = request.POST.get('company_name', '')
        emal_add = request.POST.get('emal_add', '')
        phone_number = request.POST.get('phone_number', '')
        project_name = request.POST.get('project_name', '')
        project_details = request.POST.get('project_details')
        attach_file = request.FILES.get('attach_file')

        save_Custom_Project = Custom_Project(Name=your_name, Company_Name=company_name, Email_Adress=emal_add, Phone_Number=phone_number, Project_Name=project_name, Details=project_details, Attach_File=attach_file)
        save_Custom_Project.save()

        email_for_buy = render_to_string(
            'custom_project_for_customer.html',
            {
                'your_name': your_name,
                'company_name': company_name,
                'emal_add': emal_add,
                'phone_number': phone_number,
                'project_name': project_name,
            }
        )

        send_mail(
            'Custom Project - Thank You For Sending Us',  # subject
            email_for_buy,  # massage
            '',  # from email
            [emal_add],  # to email
            fail_silently=True,
        )

        email_for_buy = render_to_string(
            'custom_project_for_admin.html',
            {
                'your_name': your_name,
                'company_name': company_name,
                'emal_add': emal_add,
                'phone_number': phone_number,
                'project_name': project_name,
            }
        )

        send_mail(
            'Custom Project',  # subject
            email_for_buy,  # massage
            '',  # from email
            [emal_add],  # to email
            fail_silently=True,
        )

        messages.success(request, 'Your Custom Project Details Has been Submitted Our Manager will Contact You soon !!')

        return redirect('index')
    else:
        get_status = job_post_status.objects.filter(id='1')
        Categories_all = Categories.objects.all()

        context10 = {'get_status': get_status, 'Categories_all':Categories_all}
        return render(request, 'custom_project.html', context10)


def newsletter(request):
    newsletter_email = request.POST.get('newsletter_email')
    newsletter_table_save = newsletter_table(email_address=newsletter_email)
    newsletter_table_save.save()
    messages.success(request, 'Thank You For Subscribe Us !')
    return redirect('index')

def product_search(request):
    search_product  = request.GET.get('search_product')

    # prod_search = Product_Details.objects.filter(product_name__icontains = search_product)
    # prod_search_des = Product_Details.objects.filter(description__icontains = search_product)
    #
    # search_result = prod_search.union(prod_search_des)

    if search_product:
        search_result = Product_Details.objects.filter(Q(product_name__icontains = search_product) | Q(description__icontains = search_product)).order_by('-id')

        search_result_count = Product_Details.objects.filter(Q(product_name__icontains = search_product) | Q(description__icontains = search_product)).count()

    # pagination
    p = Paginator(search_result, 1)

    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages in template
    number_of_pages_1 = p.num_pages + 1
    list1 = []
    for i in range(1, number_of_pages_1):
        list1.append(i)

    page_num = request.GET.get('page', 1)
    print(page_num)
    page_num = int(page_num)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()
    # Search_with_price_all = Search_with_price.objects.all()

    # query jobs
    all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
    p_jobs = Paginator(all_jobs, 4)
    page2 = p_jobs.page(1)

    all_latest_pst = blog_post.objects.order_by('-time')[:6]
    context5 = {'all_prd':page, 'search_product':search_product, 'Categories_all':Categories_all, 'search_result_count':search_result_count, 'list':list1, 'all_jobs':page2, 'page_num':page_num, 'all_latest_pst':all_latest_pst}
    return render(request, 'products_page4.html', context5)


def category_search_by_user(request, pk):
    get_all_prod_by_cat = Product_Details.objects.filter(category=pk).order_by('-id')

    # pagination
    p = Paginator(get_all_prod_by_cat, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    Categories_all = Categories.objects.all()

    # query jobs
    all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
    p_jobs = Paginator(all_jobs, 4)
    page2 = p_jobs.page(1)
    all_latest_pst = blog_post.objects.order_by('-time')[:6]
    context={'Product_Details_all':page, 'list1':list, 'Categories_all':Categories_all, 'all_jobs':page2, 'page_num':page_num, 'all_latest_pst':all_latest_pst}
    return render(request, 'index.html', context)



def subcategory_search_by_user(request, pk):
    subcat = Subcategory.objects.get(id=pk)
    get_all_prod_by_cat = Product_Details.objects.filter(subcategory=pk).order_by('-id')
    # pagination
    p = Paginator(get_all_prod_by_cat, 15)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    Categories_all = Categories.objects.all()
    # query jobs
    all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
    p_jobs = Paginator(all_jobs, 4)
    page2 = p_jobs.page(1)
    all_latest_pst = blog_post.objects.order_by('-time')[:6]
    context={'Product_Details_all':page, 'list1':list, 'Categories_all':Categories_all, 'all_jobs':page2, 'page_num':page_num, 'all_latest_pst':all_latest_pst}
    return render(request, 'index.html', context)




#
# def category_search(request):
#     checkbox_cat_seach = request.GET.get('checkbox_cat_seach')
#     price_search_check = request.GET.get('price_search_check')
#
#     if checkbox_cat_seach and price_search_check:
#         cat_details_get = Categories.objects.get(id=checkbox_cat_seach)
#         # price_details_get = Search_with_price.objects.get(id=price_search_check)
#
#         get_minmum_price = price_details_get.minimum_price
#         get_maximum_price=price_details_get.maximum_price
#
#         get_all_prod_by_cat = Product_Details.objects.filter(category=cat_details_get).order_by('-id').filter(price__gte=get_minmum_price).filter(price__lte=get_maximum_price)
#         # print(get_all_prod_by_cat)
#
#         get_all_prod_by_cat2 = Product_Details.objects.filter(category=cat_details_get).order_by('-id').filter(
#             price__gte=get_minmum_price).filter(price__lte=get_maximum_price).count()
#
#         # pagination
#         p = Paginator(get_all_prod_by_cat, 15)
#
#         # print(p.num_pages)
#         number_of_pages = p.num_pages
#
#         # show list of pages in template
#         number_of_pages_1 = p.num_pages + 1
#         list2 = []
#         for i in range(1, number_of_pages_1):
#             list2.append(i)
#
#         page_num = request.GET.get('page', 1)
#         try:
#             page = p.page(page_num)
#         except EmptyPage:
#             page = p.page(1)
#
#         Categories_all = Categories.objects.all()
#         Search_with_price_all = Search_with_price.objects.all()
#
#         # query jobs
#         all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
#         p_jobs = Paginator(all_jobs, 10)
#         page2 = p_jobs.page(1)
#
#         context8 = {'Categories_all': Categories_all, 'Product_Details_all': page, 'get_all_prod_by_cat2': get_all_prod_by_cat2, 'cat_details_get': cat_details_get, 'Search_with_price_all':Search_with_price_all, 'price_details_get':price_details_get, 'list2':list2, 'all_jobs':page2}
#
#         return render(request, 'index.html', context8)
#
#     elif checkbox_cat_seach:
#         cat_details_get = Categories.objects.get(id=checkbox_cat_seach)
#         # print(checkbox_cat_seach)
#         get_all_prod_by_cat = Product_Details.objects.filter(category=cat_details_get).order_by('-id')
#         get_all_prod_by_cat2 = Product_Details.objects.filter(category=cat_details_get).count()
#         # print(get_all_prod_by_cat)
#
#         # pagination
#         p = Paginator(get_all_prod_by_cat, 15)
#
#         # print(p.num_pages)
#         number_of_pages = p.num_pages
#
#         # show list of pages in template
#         number_of_pages_1 = p.num_pages + 1
#         list2 = []
#         for i in range(1, number_of_pages_1):
#             list2.append(i)
#
#         page_num = request.GET.get('page', 1)
#         try:
#             page = p.page(page_num)
#         except EmptyPage:
#             page = p.page(1)
#
#
#         Categories_all = Categories.objects.all()
#         Search_with_price_all = Search_with_price.objects.all()
#
#         # query jobs
#         all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
#         p_jobs = Paginator(all_jobs, 10)
#         page2 = p_jobs.page(1)
#
#
#         context5 = {'Categories_all': Categories_all, 'Product_Details_all': page,
#                             'get_all_prod_by_cat2': get_all_prod_by_cat2, 'cat_details_get': cat_details_get, 'Search_with_price_all':Search_with_price_all, 'list2':list2, 'all_jobs':page2}
#         return render(request, 'index.html', context5)
#
#     elif price_search_check:
#         price_details_get = Search_with_price.objects.get(id=price_search_check)
#         # print(checkbox_cat_seach)
#
#         get_minmum_price = price_details_get.minimum_price
#         get_maximum_price = price_details_get.maximum_price
#         # print(get_minmum_price, get_maximum_price)
#
#         # price_searching = Product_Details.objects.filter(price__gte=get_minmum_price).filter(
#         #     price__lte=get_maximum_price)
#         # print(price_searching)
#
#         get_all_prod_by_cat = Product_Details.objects.filter(price__gte=get_minmum_price).filter(
#             price__lte=get_maximum_price)
#         get_all_prod_by_cat2 = Product_Details.objects.filter(price__gte=get_minmum_price).filter(
#             price__lte=get_maximum_price).count()
#
#         # pagination
#         p = Paginator(get_all_prod_by_cat, 15)
#
#         # print(p.num_pages)
#         number_of_pages = p.num_pages
#
#         # show list of pages in template
#         number_of_pages_1 = p.num_pages + 1
#         list2 = []
#         for i in range(1, number_of_pages_1):
#             list2.append(i)
#
#         page_num = request.GET.get('page', 1)
#         try:
#             page = p.page(page_num)
#         except EmptyPage:
#             page = p.page(1)
#
#         Categories_all = Categories.objects.all()
#         Search_with_price_all = Search_with_price.objects.all()
#
#         # query jobs
#         all_jobs = posted_jobs.objects.filter(job_post_status='2').order_by('-id')
#         p_jobs = Paginator(all_jobs, 10)
#         page2 = p_jobs.page(1)
#
#         context6 = {'Categories_all':Categories_all, 'Search_with_price_all':Search_with_price_all, 'Product_Details_all':page, 'get_all_prod_by_cat2':get_all_prod_by_cat2, 'price_details_get':price_details_get, 'list2':list2, 'all_jobs':page2}
#         return render(request, 'index.html', context6)
#
#     else:
#         return redirect('/')


def account(request):
    if request.method=='POST':

        #check the post peramiters
        sign_username=request.POST['sign_username']
        sign_email=request.POST['sign_email']
        sign_password=request.POST['sign_password']
        confirm_sign_password=request.POST['confirm_sign_password']
        sign_first_name=request.POST['sign_first_name']
        sign_last_name=request.POST['sign_last_name']




        #chech the error inputs

        user_username_info = User.objects.filter(username=sign_username)
        user_email_info = User.objects.filter(email=sign_email)

        erorr_message= ""

        if user_username_info:
            # messages.error(request, "Username Already Exist")
            erorr_message = "Username Already Exist"

        elif user_email_info:
            # messages.error(request, "Email Already Exist")
            erorr_message = "Email Already Exist"

        elif sign_password != confirm_sign_password:
            # messages.error(request, "Passwords are not match")
            erorr_message = "Passwords are not match"

        elif len(sign_password)<7:
            # messages.error(request, "Passwords Must be Al least 7 Digits")
            erorr_message = "Passwords Must be Al least 7 Digits"

        if not erorr_message:

            # create user
            myuser = User.objects.create_user(sign_username, sign_email, sign_password)
            myuser.first_name=sign_first_name
            myuser.last_name=sign_last_name
            myuser.is_active = False
            myuser.save()


            # send mail
            user = EmailConfirmed.objects.get(user=myuser)
            site = get_current_site(request)
            email = myuser.email
            first_name = myuser.first_name
            last_name = myuser.last_name

            sub_of_email = "Activation Email From Mimic Crafts Cape."
            email_body = render_to_string(
                'verify_email.html',
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'domain': site.domain,
                    'activation_key': user.activation_key
                }
            )

            send_mail(
                sub_of_email,  # Subject of message
                email_body,  # Message
                '',  # From Email
                [email],  # To Email

                fail_silently=True
            )

            messages.success(request, 'Check Your Email for Activate Your Account !!!')

            return redirect('/')

        else:
            Categories_all = Categories.objects.all()

            value_dic = {'sign_username': sign_username, 'sign_email': sign_email, 'sign_first_name': sign_first_name,
                         'sign_last_name': sign_last_name, 'erorr_message':erorr_message, 'Categories_all':Categories_all}
            return render(request, 'account.html', value_dic)

    else:
        usr = request.user
        # print(usr)
        user_username = User.objects.filter(username=usr)
        # print(user_username)
        if user_username:
            return redirect('/')
        else:
            Categories_all = Categories.objects.all()
            condict = {'Categories_all':Categories_all}
            return render(request, 'account.html', condict)



def email_confirm(request, activation_key):
    user= get_object_or_404(EmailConfirmed, activation_key=activation_key)
    if user is not None:
        user.email_confirmed=True
        user.save()

        myuser=User.objects.get(email=user)
        myuser.is_active=True
        myuser.save()

        Categories_all = Categories.objects.all()
        condict = {'Categories_all': Categories_all}
        return render(request, 'registration_complete.html', condict)





def login_func(request):
    if request.method == 'POST':
        log_username = request.POST['log_username']
        log_password = request.POST['log_password']
        # this is for authenticate username and password for login
        user = authenticate(username=log_username, password=log_password)

        erorr_message_2 = ""

        if user is not None:
            login(request, user)
            # messages.success(request, "Successfully Logged In !!")
            return redirect('index')
        else:
            erorr_message_2 ="Invalid Credentials, Please Try Again !!"

            Categories_all = Categories.objects.all()

            value_func2 = {'erorr_message_2':erorr_message_2, 'log_username':log_username, 'Categories_all':Categories_all}
            # messages.error(request, "Invalid Credentials, Please Try Again !!")
            return render(request, 'account.html', value_func2)


def func_logout(request):
    # this is for logout from user id
    logout(request)
    return redirect('index')


def details_products(request, pk):
    Product_Details_details= Product_Details.objects.get(id=pk)
    # print(Product_Details_details.category)

    Product_Details_details_category=Product_Details_details.category

    Product_Details_by_cate = Product_Details.objects.filter(category=Product_Details_details_category).order_by('-id')

    Categories_all = Categories.objects.all()

    context3 = {'Product_Details_details':Product_Details_details, 'Product_Details_by_cate':Product_Details_by_cate, 'Categories_all':Categories_all}
    return render(request, 'products_details.html', context3)


@csrf_exempt
def check_coupon(request):
    vcoupon_input = request.POST.get('vcoupon_input')
    print(vcoupon_input)

    check_code = Discount_Coupon.objects.filter(code = vcoupon_input)
    if check_code:
        get_row_coupon = Discount_Coupon.objects.get(code=vcoupon_input)
        if get_row_coupon.active_status:
            print('active')
            return HttpResponse(get_row_coupon.discount_percentage)
            # return JsonResponse(get_cat_seri, safe=False)
        else:
            print('not active')
            return HttpResponse(False)
    else:
        print('coupon does not exist!')
        return HttpResponse(False)




def cart(request):
    if request.method =="POST":
        items_json=request.POST.get('items_json')
        all_prod=request.POST.get('all_prod')
        all_prod_price=request.POST.get('all_prod_price')
        all_prod_qty=request.POST.get('all_prod_qty')

        coupon_code=request.POST.get('coupon_code')
        if coupon_code:
            coupon_code = Discount_Coupon.objects.get(code=coupon_code)
        else:
            coupon_code = None
        prod_details=request.POST.get('prod_details')
        print('prod_details')
        print(prod_details)
        # prod_details = json.loads(prod_details)

        # total_bill=request.POST.get('total_bill')
        # total_bill =json.loads(total_bill)


        # currency_type1222=request.POST.get('currency_type1222')
        # currency_type1222 =json.loads(currency_type1222)



        company_name=request.POST.get('company_name')
        full_address=request.POST.get('full_address')
        city=request.POST.get('city')
        postal_code=request.POST.get('postal_code')
        country=request.POST.get('country')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        # print(full_address, city, postal_code, country, phone)

        #make random order ID
        random_num = random.randint(2345678909800, 9923456789000)
        uniqe_confirm = Order.objects.filter(order_id=random_num)
        # print(random_num)

        while uniqe_confirm:
            random_num = random.randint(234567890980000, 992345678900000)
            if not Order.objects.filter(order_id=random_num):
                break
        # print(random_num)
        user = request.user

        post_order = Order(user=user, order_id=random_num, items_json=prod_details, company_name=company_name, full_address=full_address, city=city, postal_code=postal_code, country=country, phone=phone, email=email, Discount_Coupon=coupon_code)
        post_order.save()
        order_id = post_order.order_id
        # print(order_id)


        email_for_buy = render_to_string(
            'email_for_buy.html',
            {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'prod_details': prod_details,
                'full_address' :full_address,
                'city' : city,
                'postal_code' :postal_code,
                'country' : country,
                'phone' : phone,
                'email' : email,
            }
        )

        send_mail(
            'Purchase Order',  # subject
            email_for_buy,  # massage
            '',  # from email
            [email],  # to email

            fail_silently=True,
        )

        email_for_admin = render_to_string(
            'email_for_admin.html',
            {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'prod_details': prod_details,
                'full_address': full_address,
                'city': city,
                'postal_code': postal_code,
                'country': country,
                'phone': phone,
                'email': email,
            }
        )

        send_mail(
            'Received a Order',  # subject
            email_for_admin,  # massage
            '',  # from email
            [''],  # to email

            fail_silently=True,
        )
        # print("come")

        Thank = True
        Categories_all = Categories.objects.all()
        return render(request, 'cart.html', {'Thank':Thank, 'order_id':order_id, 'Categories_all':Categories_all})

    Categories_all = Categories.objects.all()
    dict={'Categories_all':Categories_all}
    return render(request, 'cart.html', dict)

def my_order(request):
    user = request.user

    # print(usr)
    user_username = User.objects.filter(username=user)
    # print(user_username)
    if user_username:
        myorder_filter = Order.objects.filter(user=user).order_by('-id')
        Categories_all = Categories.objects.all()
        context13 = {'myorder_filter': myorder_filter, 'Categories_all':Categories_all}
        return render(request, 'my_order.html', context13)
    else:
        return redirect('/')




def order_details(request):
    if request.method=="POST":
        user = request.user
        order_id=request.POST.get('order_id')
        print(order_id, user)
        myorder_details = Order.objects.get(id=order_id)

        dict1=myorder_details.items_json


        # using zip()
        # list1, list2 = list(zip(*dict1.items()))

        # list1=[]
        # list2=[]
        #
        # #using items()
        # for i in dict1.items():
        #     list1.append(i[0]), list2.append(i(1))
        #
        # print(dict1)

        Categories_all = Categories.objects.all()

        context13 = {'myorder_details':myorder_details, 'Categories_all':Categories_all}
        return render(request, 'order_details.html', context13)
    else:
        return redirect('/')



def all_blogs(request, template='all_blogs.html', page_template='all_blogs_new.html'):
    all_latest_pst = blog_post.objects.order_by('-time')
    Categories_all = Categories.objects.all()
    context = {'all_latest_pst': all_latest_pst, 'page_template': page_template,'Categories_all':Categories_all}
    if request.is_ajax():
        template = page_template
    return render(request, template, context)



def blog_details(request, pk):
    all_latest_pst = blog_post.objects.order_by('-time')[:6]
    gett_pst = blog_post.objects.get(id=pk)
    print(gett_pst)

    all_comments = Blogs_Comments.objects.filter(Blog=gett_pst)
    all_commnt_count = all_comments.count()

    context = {'gett_pst': gett_pst, 'all_latest_pst':all_latest_pst, 'all_commnt_count':all_commnt_count, 'all_comments':all_comments}
    return render(request, 'blog_details.html', context)





def submit_comments(request):
    if request.user.is_authenticated:
        subject = request.POST.get('text_comments')
        text_comments = request.POST.get('text_comments')
        post_id = request.POST.get('post_id')

        b_p = blog_post.objects.get(id=post_id)

        sav_commnt =Blogs_Comments(User=request.user, Blog=b_p, comment_subject=subject, comment_text=text_comments)
        sav_commnt.save()
        messages.success(request, "Your Comment Is Posted !!")
        return redirect('blog_details', post_id)
    else:
        messages.success(request, "You Have to Login for submitting Comments !!")
        return redirect('signup_login')
