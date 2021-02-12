from django.db import models
from django.contrib.auth.models import User
from .models import Category
from .models import Brand
from .models import Color
from .models import Guarantee
from .models import Sellers
    
#digikala
class Mobile(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    guarantee=models.TextField(max_length=200,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    pg=models.BooleanField(default=False)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    guarantee_price=models.PositiveSmallIntegerField(default=0)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.PositiveSmallIntegerField()
    dimensions=models.CharField(max_length=30)
    sim_card=models.CharField(max_length=30)
    weight=models.CharField(max_length=10)
    special_prop=models.CharField(max_length=100)
    sim_count=models.CharField(max_length=20)
    publish_date=models.CharField(max_length=20)
    slot=models.BooleanField(default=False)
    model=models.CharField(max_length=35)
    chipest=models.CharField(max_length=20)
    cpu=models.CharField(max_length=20)
    cpu_type=models.CharField(max_length=20)
    frequencies=models.CharField(max_length=20)
    gpu=models.CharField(max_length=20)
    internal_memory=models.CharField(max_length=20)
    ram=models.CharField(max_length=20)
    microSd=models.BooleanField(default=False)
    touchScreen=models.BooleanField(default=False)
    screen_technology=models.CharField(max_length=15)
    screen_limit=models.CharField(max_length=15)
    screen_dimension=models.CharField(max_length=15)
    screen_resolution=models.CharField(max_length=15)
    screen_pixel=models.CharField(max_length=25)
    screen_ratio=models.CharField(max_length=20)
    net=models.CharField(max_length=25)
    bluetooth=models.CharField(max_length=20)
    bluetooth_version=models.CharField(max_length=20)
    location_tech=models.CharField(max_length=20)
    contact_gate=models.CharField(max_length=20)
    camera=models.CharField(max_length=20)
    camera_disc=models.TextField(max_length=400)
    sound_jac=models.BooleanField(default=False)
    os_choice=(
        ('ios','ios'),
        ('android','android'),
        ('windows','windows'),
    )
    os=models.CharField(choices=os_choice,default='android',max_length=10)
    os_version=models.CharField(max_length=15)
    persian_language=models.BooleanField(default=False)
    default_softwares=models.TextField(max_length=150)
    sensors=models.TextField(max_length=150)
    battery_changable=models.BooleanField(default=False)
    battery_prop=models.TextField(max_length=200)
    others_disc=models.TextField(max_length=150)
    summary_disc=models.TextField(max_length=150)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)


#lion
class Tablet(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    guarantee=models.TextField(max_length=200,null=True,blank=True)
    color=models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    pg=models.BooleanField(default=False)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    guarantee_price=models.PositiveSmallIntegerField(default=0)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.PositiveSmallIntegerField()
    internal_capacity=models.CharField(max_length=25)
    slot_capacity=models.CharField(max_length=35)
    sim_card=models.BooleanField(default=False)
    os_choice=(
        ('ios','ios'),
        ('android','android'),
        ('windows','windows'),
    )
    os=models.CharField(choices=os_choice,default='android',max_length=20)
    ram=models.CharField(max_length=15)
    chipset=models.CharField(max_length=35)
    gpu=models.CharField(max_length=35)
    screen_type=models.CharField(max_length=10)
    resolution=models.CharField(max_length=25)
    camera=models.CharField(max_length=15)
    selfie=models.CharField(max_length=15)
    wifi=models.CharField(max_length=25)
    bluetooth=models.CharField(max_length=14)
    usb_type=models.CharField(max_length=15)
    battery=models.CharField(max_length=15)
    weight=models.CharField(max_length=15)
    summary_disc=models.TextField(max_length=250)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)


