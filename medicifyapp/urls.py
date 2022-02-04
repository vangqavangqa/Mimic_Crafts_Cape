from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get_catalog', views.get_catalog, name='get_catalog'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('all_brands', views.all_brands, name='all_brands'),
    path('brand_products/<int:pk>', views.brand_products, name='brand_products'),
    path('subcats_of_cat/<int:pk>', views.subcats_of_cat, name='subcats_of_cat'),
    # path('products_subcat/<int:pk>', views.products_subcat, name='products_subcat'),
    path('brands_list_subcat/<int:pk>', views.brands_list_subcat, name='brands_list_subcat'),
    path('products_subcats_brands', views.products_subcats_brands, name='products_subcats_brands'),
    path('custom_project', views.custom_project, name='custom_project'),
    path('products_page', views.products_page, name='products_page'),
    path('gp_jobs', views.gp_jobs, name='gp_jobs'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('all_blogs', views.all_blogs, name='all_blogs'),
    path('blog_details/<int:pk>', views.blog_details, name="blog_details"),
    path('submit_comments', views.submit_comments, name='submit_comments'),
    path('profile', views.profile, name='profile'),
    path('my_order', views.my_order, name='my_order'),
    path('order_details', views.order_details, name='order_details'),
    path('post_job', views.post_job, name='post_job'),
    path('see_my_post', views.see_my_post, name='see_my_post'),
    path('job_post_details/<int:pk>', views.job_post_details, name='job_post_details'),
    path('product_search', views.product_search, name='product_search'),
    # path('category_search', views.category_search, name='category_search'),
    path('category_search_by_user/<int:pk>', views.category_search_by_user, name='category_search_by_user'),
    path('subcategory_search_by_user/<int:pk>', views.subcategory_search_by_user, name='subcategory_search_by_user'),
    path('account', views.account, name='account'),
    path('login_func', views.login_func, name='login_func'),

    path('email/confirmation/<str:activation_key>/', views.email_confirm, name='email_activation'  ),

    path('func_logout', views.func_logout, name='func_logout'),
    path('cart', views.cart, name='cart'),
    path('check_coupon', views.check_coupon, name='check_coupon'),
    path('details_products/pro-<int:pk>-all', views.details_products, name='details_products'),
    path('details_products/product_search', views.product_search, name='product_search'),
]
