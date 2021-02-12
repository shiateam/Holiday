from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category=models.CharField(max_length=20)

class Brand(models.Model):
    Brand=models.CharField(max_length=20)

class Color(models.Model):
    color=models.CharField(max_length=25)

class Guarantee(models.Model):
    guarantee=models.CharField(max_length=150)

class Sellers(models.Model):
    name=models.CharField(max_length=50)
    shop_name=models.CharField(max_length=35)
    ssn=models.CharField(max_length=15,null=True,blank=True)
    phone=models.CharField(max_length=15,unique=True)
    
class Headset(models.Model):
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
    weight=models.CharField(max_length=10)
    publish_date=models.CharField(max_length=20)
    contact_type=models.BooleanField(default=False)
    summary_disc=models.TextField(max_length=150)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)


class PowerBank(models.Model):
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
    publish_date=models.CharField(max_length=20)
    dimensions=models.CharField(max_length=25)
    weight_class=models.CharField(max_length=30)
    weight=models.CharField(max_length=10)
    capacity_limit=models.CharField(max_length=35)
    capacity=models.CharField(max_length=35)
    enter_volt=models.CharField(max_length=10)
    out_volt=models.CharField(max_length=10)
    enter_current=models.CharField(max_length=10)
    out_current=models.CharField(max_length=10)
    gate_count=models.CharField(max_length=10)
    summary_disc=models.TextField(max_length=250)
    body_material=models.CharField(max_length=20)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)


class ChargerAdabter(models.Model):
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
    dimensions=models.CharField(max_length=25)
    enter_volt=models.CharField(max_length=25)
    out_gate_count=models.PositiveSmallIntegerField()
    output_type_gate=models.CharField(max_length=20)
    summary_disc=models.TextField(max_length=250)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)


class FlashMemory(models.Model):
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
    dimensions=models.CharField(max_length=25)
    capacity=models.CharField(max_length=5)
    weight=models.CharField(max_length=10)
    gate_type=models.CharField(max_length=10)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)


class mouse(models.Model):
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
    class_type=models.CharField(max_length=20,null=True,blank=True)
    dimetions=models.CharField(max_length=35)
    weight=models.CharField(max_length=10)
    contact_type_choice=(
        ('wire','باسیم'),
        ('bluetooth',' بی سیم bt'),
        ('bluetooth','بی سیم wifi'),
    )
    contact_type=models.CharField(choices=contact_type_choice,max_length=20)
    cable_lenght=models.CharField(max_length=25)
    contact_gate=models.CharField(max_length=25)
    charge_gate=models.CharField(max_length=25)
    battery_monitoring=models.BooleanField(default=False)
    OnOff_key=models.BooleanField(default=False)
    hand_choice=(
        ('left','left'),
        ('right','right'),
    )
    hand=models.CharField(default='right',choices=hand_choice,max_length=15)
    sensor_type_choice=(
        (1,'laser'),
        (2,'oprical')
    )
    resolution=models.CharField(max_length=50)
    mouse_key_count=models.PositiveSmallIntegerField()
    key_lifeTime=models.CharField(max_length=50,null=True,blank=True)
    programmable_gate=models.BooleanField(default=False)
    rgb=models.BooleanField(default=False)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)


class BluetoothDongle(models.Model):
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
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    material_body=models.CharField(max_length=30)
    blutooth_version=models.CharField(max_length=20)
    summary_desc=models.TextField(max_length=150)
    CountSell=models.PositiveSmallIntegerField(default=0)


from ..models.MobileVsTablets import Mobile
class MobileCovers(models.Model):
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
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    material_body=models.CharField(max_length=30)
    summary_desc=models.TextField(max_length=150)
    CountSell=models.PositiveSmallIntegerField(default=0)


class Screen_Glass(models.Model):
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
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    mobile=models.ForeignKey(Mobile, on_delete=models.CASCADE)    
    anti_hurt=models.BooleanField(default=True)
    reflex=models.BooleanField(default=True)
    Scratch=models.BooleanField(default=True)
    Thickness=models.CharField(max_length=25)
    FrontOrBack_choice=(
        (1,'front'),
        (2,'back')
    )
    FrontOrBack=models.CharField(default='1',choices=FrontOrBack_choice,max_length=10)
    summary_desc=models.TextField(max_length=200)
    CountSell=models.PositiveSmallIntegerField(default=0)


class SmartWatch(models.Model):
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
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    gender_choice=(
        (1,'آقایان'),
        (2,'خانم ها'),
        (3,'آقایان و خانم ها')
    )
    gender=models.CharField(default='3',choices=gender_choice,max_length=15)
    dimension=models.CharField(max_length=50)
    weight=models.CharField(max_length=25)
    glass_material=models.CharField(max_length=35)
    body_material=models.CharField(max_length=35)
    body_desc=models.CharField(max_length=35)
    dam_material=models.CharField(max_length=35)
    dam_type=models.CharField(max_length=25)
    colorfull_screen=models.BooleanField(default=True)
    touch_screen=models.BooleanField(default=True)
    screen_dimension=models.CharField(max_length=35)
    simCard=models.BooleanField(default=False)
    gps=models.BooleanField()
    descriptions=models.TextField(max_length=900)
    CountSell=models.PositiveSmallIntegerField(default=0)


class SDcards(models.Model):
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
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    dimenson=models.CharField(max_length=35)
    type_choice=(
        ('SD','SD'),
        ('Micro','Micro')
    )
    type=models.CharField(default='Micro',choices=type_choice,max_length=10)
    capacity_choice=(
        ('8','8'),
        ('16','16'),
        ('32','32'),
        ('64','64'),
        ('128','128'),
        ('256','256'),
    )
    capacity=models.CharField(choices=capacity_choice,default='32',max_length=10)
    classType=models.CharField(default='10',max_length=15)
    read_speed=models.CharField(max_length=35)
    write_speed=models.CharField(max_length=35)
    Water_proof=models.BooleanField(default=True)
    anti_hurt=models.BooleanField(default=True)
    summary_desc=models.TextField(max_length=150,null=True,blank=True)
    CountSell=models.PositiveSmallIntegerField(default=0)

class MonopadVsHolder(models.Model):
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
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    weight=models.CharField(max_length=25)
    max_lenght=models.CharField(max_length=25)
    min_lenght=models.CharField(max_length=25)
    weight_carrier=models.CharField(max_length=35)
    summary_desc=models.TextField(max_length=350)
    CountSell=models.PositiveSmallIntegerField(default=0)



    

    
    
    







    







    


    
    
    

    



    
    


