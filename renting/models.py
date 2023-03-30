from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator


# get user model
User = get_user_model()

# Create your models here.
class Manager(models.Model):
    class Gender(models.TextChoices):
        SELECT = "", "Select Gender"
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="Gender", choices=Gender.choices, default=Gender.SELECT, max_length=10)
    phone_number = PhoneNumberField(verbose_name = "Phone Number",blank=True)
    location = models.CharField(verbose_name="Location Address", max_length=255, blank=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name,self.user.last_name)



class Landlord(models.Model):
    class Gender(models.TextChoices):
        SELECT = "", "Select Gender"
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="Gender", choices=Gender.choices, default=Gender.SELECT, max_length=10)
    phone_number = PhoneNumberField(verbose_name = "Phone Number",blank=True)
    location = models.CharField(verbose_name="Location Address", max_length=255, blank=True)
    profile_image = models.ImageField(
        verbose_name="Profile Picture", 
        upload_to='', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        validators=[FileExtensionValidator(['png','jpg','jpeg'])]
    )
    
    def  image(self):
        return mark_safe('<img src="/../../media/%s" width="70" />' % (self.profile_image))

    image.allow_tags = True 
    
    def __str__(self):
        return '{} {}'.format(self.user.first_name,self.user.last_name)


class City(models.Model):
    name = models.CharField(verbose_name="City/District", max_length=100, unique=True)

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(verbose_name="Property Type", max_length=100, unique=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    landlord = models.ForeignKey(Landlord, verbose_name="Landlord", on_delete=models.CASCADE, blank=False)
    city = models.ForeignKey(City, verbose_name="City/District", on_delete=models.PROTECT)
    type = models.ForeignKey(PropertyType, verbose_name="Property Type", on_delete=models.CASCADE)
    locationAddress = models.CharField(verbose_name="Location Address", max_length=255, blank=False)
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
    property_image = models.ImageField(
        verbose_name="Property Image", 
        upload_to='', 
        height_field=None, 
        width_field=None, 
        max_length=None,
        validators=[FileExtensionValidator(['png','jpg','jpeg'])]
    )
    
    def  image(self):
        return mark_safe('<img src="/../../media/%s" width="70" />' % (self.property_image))

    image.allow_tags = True 
    
    def __str__(self):
        return self.name