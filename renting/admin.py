from django.contrib import admin
from renting.models import *


# Register your models here.
@admin.register(Manager)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'phone_number', 'location',)
    list_filter = ('gender',)
    fieldsets = (
        ('MANAGER', {'fields': ('user', 'gender', 'phone_number', 'location',)}),
    )
    add_fieldsets = (
        ('REGISTER NEW USER', {
            'classes': ('wide',),
            'fields': ('user', 'gender', 'phone_number', 'location',),
        }),
    )
    search_fields = ('user','phone_number',)
    ordering = ('user',)



@admin.register(Landlord)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'phone_number', 'location',)
    list_filter = ('gender',)
    fieldsets = (
        ('MANAGER', {'fields': ('user', 'gender', 'phone_number', 'location',)}),
    )
    add_fieldsets = (
        ('REGISTER NEW USER', {
            'classes': ('wide',),
            'fields': ('user', 'gender', 'phone_number', 'location',),
        }),
    )
    search_fields = ('user','phone_number',)
    ordering = ('user',)



@admin.register(City)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'phone_number', 'location',)
    list_filter = ('gender',)
    fieldsets = (
        ('MANAGER', {'fields': ('user', 'gender', 'phone_number', 'location',)}),
    )
    add_fieldsets = (
        ('REGISTER NEW USER', {
            'classes': ('wide',),
            'fields': ('user', 'gender', 'phone_number', 'location',),
        }),
    )
    search_fields = ('user','phone_number',)
    ordering = ('user',)



@admin.register(PropertyType)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'phone_number', 'location',)
    list_filter = ('gender',)
    fieldsets = (
        ('MANAGER', {'fields': ('user', 'gender', 'phone_number', 'location',)}),
    )
    add_fieldsets = (
        ('REGISTER NEW USER', {
            'classes': ('wide',),
            'fields': ('user', 'gender', 'phone_number', 'location',),
        }),
    )
    search_fields = ('user','phone_number',)
    ordering = ('user',)



@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'renting_price', 'status', 'created_date', 'image',)
    list_filter = ('located_city','property_type','bedrooms','bathrooms','floors','is_furnished',)
    fieldsets = (
        ('PROPERTY DETAILS', {'fields': ('user', 'gender', 'phone_number', 'location',)}),
        ('PROPERTY DETAILS', {'fields': ('user', 'gender', 'phone_number', 'location',)}),
        ('PROPERTY DETAILS', {'fields': ('user', 'gender', 'phone_number', 'location',)}),
    )
    add_fieldsets = (
        ('RECORD NEW PROPERTY', {
            'classes': ('wide',),
            'fields': ('user', 'gender', 'phone_number', 'location',),
        }),
    )
    search_fields = ('user','phone_number',)
    ordering = ('user',)



@admin.register(PublishingPayment)
class PublishingPaymentAdmin(admin.ModelAdmin):
    list_display = ('property', 'landlord', 'payment_amount', 'payment_method','created_date',)
    list_filter = ('property', 'landlord', 'payment_method',)
    fieldsets = (
        ('PUBLISHED PAYMENT', {'fields': ('property', 'landlord', 'payment_amount', 'payment_method',)}),
    )
    add_fieldsets = (
        ('NEW PUBLISHED PAYMENT', {
            'classes': ('wide',),
            'fields': ('property', 'landlord', 'payment_amount', 'payment_method',),
        }),
    )
    search_fields = ('property', 'landlord', 'payment_method',)
    ordering = ('payment_method',)



# sorting models
def get_app_list(self, request, app_label=None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        # Retrieve the original list
        app_dict = self._build_app_dict(request, app_label)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models customably within each app.
        for app in app_list:
            if app['app_label'] == 'RENTING':
                ordering = {
                    'Manager': 1,
                    'Landlord': 2,
                    'City': 3,
                    'PropertyType': 4,
                    'Property': 5,
                    'PublishingPayment': 6,
                }
                app['models'].sort(key=lambda x: ordering[x['name']])
               
        return app_list
    
    
admin.AdminSite.get_app_list = get_app_list