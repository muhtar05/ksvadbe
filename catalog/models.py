from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize
from sorl.thumbnail import ImageField



class TitleKeywordsDescriptionModel(models.Model):
    seo_title = models.CharField(max_length=255)
    seo_keywords = models.TextField(blank=True,null=True)
    seo_description = models.TextField(blank=True,null=True)


    class Meta:
        abstract = True



class City(models.Model):
    name = models.CharField(max_length=100)
    alt_name = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

class Category(MPTTModel):
    name = models.CharField(max_length=150,unique=True)
    alt_name = models.SlugField(max_length=200,unique=True)
    parent = TreeForeignKey('self',null=True,blank=True,related_name='children')
    seo_title = models.CharField(max_length=255,blank=True)
    seo_keywords = models.CharField(max_length=255,blank=True)
    seo_description = models.TextField(blank=True)

    def get_absolute_url(self):
        return "/catalog/%s" % self.alt_name

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Firm(models.Model):
    title = models.CharField(max_length=200)
    alt_title = models.SlugField(max_length=250)
    info = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='catalog/firms')
    smart = ImageSpecField(
        source='avatar',processors=[SmartResize(400,400)],format='PNG'
    )
    category = models.ManyToManyField(Category,related_name='category')
    city = models.ForeignKey(City)
    address = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=50,blank=True)
    seo_title = models.CharField(max_length=255,blank=True)
    seo_keywords = models.CharField(max_length=255,blank=True)
    seo_description = models.TextField(blank=True)


    def get_absolute_url(self):
        return "/catalog/firm/%s" % self.alt_title

    def __unicode__(self):
        return self.title




class Product(models.Model):
    title = models.CharField(max_length=255)
    alt_title = models.SlugField(max_length=255,unique=True)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20,decimal_places=4)
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = ImageField(upload_to='catalog/product')
    firm = models.ForeignKey(Firm)
    seo_title = models.CharField(max_length=255,blank=True)
    seo_keywords = models.CharField(max_length=255,blank=True)
    seo_description = models.TextField(blank=True)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/product/%d" % self.id


    def get_price(self):
        return self.price

    def get_title(self):
        return self.title


class ProductPhoto(models.Model):
    image = ImageField(upload_to='catalog/productphoto')
    alt = models.CharField(max_length=255)
    main = models.BooleanField(default=False)
    product = models.ForeignKey(Product)

    def __unicode__(self):
        return self.alt

