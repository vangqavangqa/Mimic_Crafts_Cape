from django.contrib import admin
from .models import Product_Details, Categories, posted_jobs, job_post_status, Order, EmailConfirmed, bennar, contact_table, Subcategory, Discount_Coupon, blog_post, Blogs_Comments, Brands, Custom_Project, catalog, newsletter_table

# Register your models here.


class EmailConfirmedAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'activation_key', 'email_confirmed']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(EmailConfirmed, EmailConfirmedAdmin)



class show_order(admin.ModelAdmin):
    list_display = ['id', 'user', 'company_name', 'email', 'order_date']


class show_Custom_Project(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Company_Name', 'Email_Adress', 'Project_Name']


class show_newsletter(admin.ModelAdmin):
    list_display = ['id', 'email_address', 'time']



class show_product(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'subcategory', 'Brands', 'product_status']


admin.site.register(Custom_Project, show_Custom_Project)
admin.site.register(newsletter_table, show_newsletter)
admin.site.register(Product_Details, show_product)
admin.site.register(Categories)
# admin.site.register(posted_jobs)
# admin.site.register(job_post_status)
admin.site.register(Order, show_order)
admin.site.register(bennar)
admin.site.register(contact_table)
admin.site.register(Subcategory)
admin.site.register(Discount_Coupon)
admin.site.register(blog_post)
admin.site.register(Blogs_Comments)
admin.site.register(Brands)
admin.site.register(catalog)