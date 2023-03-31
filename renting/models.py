from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator


# get user model
User = get_user_model()

# Create your models here.
class Province(models.Model):
    province_name = models.CharField(verbose_name="Province Name", max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.province_name
    
class District(models.Model):
    province = models.ForeignKey(Province,verbose_name="Province", on_delete=models.CASCADE, related_name='districts')
    district_name = models.CharField(verbose_name="District Name", max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.district_name
    

class Sector(models.Model):
    district = models.ForeignKey(District,verbose_name="District", on_delete=models.CASCADE, related_name='sectors')
    sector_name = models.CharField(verbose_name="Sector Name", max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.sector_name

class Cell(models.Model):
    sector = models.ForeignKey(Sector,verbose_name="Sector", on_delete=models.CASCADE, related_name='cells')
    cell_name = models.CharField(verbose_name="Cell Name", max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.cell_name


class Manager(models.Model):
    class Gender(models.TextChoices):
        SELECT = "", "Select Gender"
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="Gender", choices=Gender.choices, default=Gender.SELECT, max_length=10)
    phone_number = PhoneNumberField(verbose_name = "Phone Number",blank=True, unique=True)
    province = models.ForeignKey(Province, verbose_name="Province", on_delete=models.PROTECT)
    district = models.ForeignKey(District, verbose_name="District", on_delete=models.PROTECT)
    sector = models.ForeignKey(Sector, verbose_name="Sector", on_delete=models.PROTECT)
    profile_image = models.ImageField(
        verbose_name="Profile Picture", 
        upload_to='profile', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        validators=[FileExtensionValidator(['png','jpg','jpeg'])]
    )
    
    def image(self):
        return mark_safe('<img src="/../../media/%s" width="70" />' % (self.profile_image))

    image.allow_tags = True 
    
    def __str__(self):
        return '{} {}'.format(self.user.first_name,self.user.last_name)



class Landlord(models.Model):
    class Gender(models.TextChoices):
        SELECT = "", "Select Gender"
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="Gender", choices=Gender.choices, default=Gender.SELECT, max_length=10)
    phone_number = PhoneNumberField(verbose_name = "Phone Number",blank=True, unique=True)
    province = models.ForeignKey(Province, verbose_name="Province", on_delete=models.PROTECT)
    district = models.ForeignKey(District, verbose_name="District", on_delete=models.PROTECT)
    sector = models.ForeignKey(Sector, verbose_name="Sector", on_delete=models.PROTECT)
    cell = models.ForeignKey(Cell, verbose_name="Cell", on_delete=models.PROTECT)
    profile_image = models.ImageField(
        verbose_name="Profile Picture", 
        upload_to='profile', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        validators=[FileExtensionValidator(['png','jpg','jpeg'])]
    )
    
    def image(self):
        return mark_safe('<img src="/../../media/%s" width="70" />' % (self.profile_image))

    image.allow_tags = True 
    
    def __str__(self):
        return '{} {}'.format(self.user.first_name,self.user.last_name)


class PropertyType(models.Model):
    type_name = models.CharField(verbose_name="Property Type", max_length=100, unique=True)

    def __str__(self):
        return self.type_name

class Property(models.Model):
    landlord = models.ForeignKey(Landlord, verbose_name="Landlord", on_delete=models.CASCADE, blank=False)
    property_type = models.ForeignKey(PropertyType, verbose_name="Property Type", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Property Title", max_length=100)
    description = models.TextField(verbose_name="Property Description", blank=False)
    bedrooms = models.IntegerField(verbose_name="Bedrooms")
    bathrooms = models.IntegerField(verbose_name="Bathrooms")
    is_furnished = models.BooleanField(verbose_name="Is funished", default=False)
    floors = models.IntegerField(verbose_name="Floors")
    plot_size = models.CharField(verbose_name="Plot Size", max_length=50)
    renting_price = models.FloatField(verbose_name="Renting Price",)
    status = models.BooleanField(verbose_name="Available")
    pub_date = models.DateTimeField(verbose_name="Published Date",auto_now=True)
    created_date = models.DateTimeField(verbose_name="Created Date",auto_now_add=True)
    province = models.ForeignKey(Province, verbose_name="Province", on_delete=models.PROTECT)
    district = models.ForeignKey(District, verbose_name="District", on_delete=models.PROTECT)
    sector = models.ForeignKey(Sector, verbose_name="Sector", on_delete=models.PROTECT)
    cell = models.ForeignKey(Cell, verbose_name="Cell", on_delete=models.PROTECT)
    street = models.CharField(verbose_name="Street Address", max_length=50,blank=False)
    
    def __str__(self):
        return self.title
    

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, verbose_name="Property", on_delete=models.CASCADE, related_name='images')
    property_image = models.ImageField(
        verbose_name="Property Image", 
        upload_to='properties',
        validators=[FileExtensionValidator(['png','jpg','jpeg'])]
    )
    def __str__(self):
        return '{} {}'.format(self.property, self.property_image)


class PublishingPayment(models.Model):
    property = models.ForeignKey(Property, verbose_name="Property", on_delete=models.PROTECT)
    landlord = models.ForeignKey(Landlord, verbose_name="Landlord", on_delete=models.PROTECT)
    payment_amount = models.FloatField(verbose_name="Payment Amount", null=False, blank=False)
    payment_method = models.CharField(verbose_name="Payment Method", max_length=50, null=False, blank=False)
    created_date = models.DateTimeField(verbose_name="Created Date",auto_now_add=True)
    
    def __str__(self):
        return '{} {}'.format(self.property, self.payment_amount)