from django.contrib import admin
from renting.models import *


# Register your models here.
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'phone_number', 'image',)
    list_filter = ('gender',)
    fieldsets = (
        ('LANDLORD INFO', {'fields': ('user', 'gender', 'phone_number','profile_image',)}),
        ('Location Address', {'fields': ('province', 'district', 'sector',)}),
    )
    add_fieldsets = (
        ('REGISTER LANDLORD', {'fields': ('user', 'gender', 'phone_number','profile_image',)}),
        ('Location Address', {'fields': ('province', 'district', 'sector',)}),
    )
    search_fields = ('user',)
    ordering = ('user',)



@admin.register(Landlord)
class LandlordAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'phone_number', 'image',)
    list_filter = ('gender',)
    fieldsets = (
        ('LANDLORD INFO', {'fields': ('user', 'gender', 'phone_number','profile_image',)}),
        ('Location Address', {'fields': ('province', 'district', 'sector', 'cell',)}),
    )
    add_fieldsets = (
        ('REGISTER LANDLORD', {'fields': ('user', 'gender', 'phone_number','profile_image',)}),
        ('Location Address', {'fields': ('province', 'district', 'sector', 'cell',)}),
    )
    search_fields = ('user',)
    ordering = ('user',)


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    fieldsets = (
        ('PROPERTY TYPE', {'fields': ('type_name',)}),
    )
    add_fieldsets = (
        ('NEW PROPERTY TYPE', {
            'classes': ('wide',),
            'fields': ('type_name',),
        }),
    )
    search_fields = ('type_name',)
    ordering = ('type_name',)



@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','description','renting_price','bedrooms','bathrooms','floors','is_furnished', 'status', 'created_date',)
    list_filter = ('district','property_type','bedrooms','bathrooms','floors','is_furnished',)
    fieldsets = (
        ('PROPERTY DETAILS', {'fields': ('title','description','property_type',('bedrooms','bathrooms','floors','is_furnished'),'plot_size','renting_price','status',)}),
        ('Location Address', {'fields': ('province', 'district', 'sector', 'cell', 'street',)}),
        ('Property Owner', {'fields': ('landlord',)}),
        ('Other Info', {'fields': ('created_date', 'pub_date',)}),
    )
    add_fieldsets = (
        ('Property Owner', {'fields': ('landlord',)}),
        ('NEW PROPERTY', {'fields': ('title','description','property_type',('bedrooms','bathrooms','floors','is_furnished'),'plot_size','renting_price','status',)}),
        ('Location Address', {'fields': ('province', 'district', 'sector', 'cell', 'street',)}),
    )
    search_fields = ('landlord','title',)
    ordering = ('property_type','district',)



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

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('province_name',)
    fieldsets = (
        ('PROVINCE', {'fields': ('province_name',)}),
    )
    add_fieldsets = (
        ('NEW PROVINCE', {'fields': ('province_name',)}),
    )
    search_fields = ('province_name',)
    ordering = ('province_name',)



@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_name','province',)
    list_filter = ('province',)
    fieldsets = (
        ('DISTRICT', {'fields': ('province','district_name',)}),
    )
    add_fieldsets = (
        ('NEW DISTRICT', {'fields': ('province','district_name',)}),
    )
    search_fields = ('province','district_name',)
    ordering = ('province',)



@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('sector_name','district',)
    list_filter = ('district',)
    fieldsets = (
        ('SECTOR', {'fields': ('district','sector_name',)}),
    )
    add_fieldsets = (
        ('NEW SECTOR', {'fields': ('district','sector_name',)}),
    )
    search_fields = ('district','sector_name',)
    ordering = ('district',)



@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = ('cell_name','sector',)
    list_filter = ('sector',)
    fieldsets = (
        ('CELL', {'fields': ('sector','cell_name',)}),
    )
    add_fieldsets = (
        ('NEW CELL', {'fields': ('sector','cell_name',)}),
    )
    search_fields = ('sector','cell_name',)
    ordering = ('sector',)





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
                    'Province': 7,
                    'District': 8,
                    'Sector': 9,
                    'Cell': 10,
                }
                app['models'].sort(key=lambda x: ordering[x['name']])
               
        return app_list
    
    
admin.AdminSite.get_app_list = get_app_list