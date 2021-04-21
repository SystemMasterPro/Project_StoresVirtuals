from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

#CLASS STORE
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    direction = models.CharField(max_length=100, null=True)
    phone = models.IntegerField()
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        ordering = ['name']
    
    def __str__(self):
        return self.name

#CLASS CATEGORY
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=False)
    state = models.BooleanField('State', default=True)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name

def url_product(self, filename):
    route = "static/images/Products/%s/%s" % (self.product, str(filename))
    return route

#CLASS PRODUCT
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    state = models.BooleanField('State', default=True)
    image = models.ImageField(upload_to=url_product)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def image_product(self):
        return mark_safe('<a href="/%s" ><img src="/%s" height="50px" width="50px" /></a>' % (self.image, self.image))
    image_product.allow_tags = True
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['product']

    def __str__(self):
        return self.product


#CLASS SUPPLIER    
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    state = models.BooleanField('State', default=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'
        ordering = ['name']

    def __str__(self):
        return self.name

#METHOD IMAGE PROFILE USER
def url_profile(self, filename):
    route = "static/images/Profiles/%s/%s" % (self.user, str(filename))
    return route

#CLASS CASHIER
class Cashier(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    direction = models.CharField(max_length=100, null=True)
    box = models.IntegerField()
    state = models.BooleanField('State', default=True)
    image = models.ImageField(upload_to=url_profile)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def image_profile(self):
        if self.image:
            return mark_safe('<a href="/%s"><img src="/%s" height="50px" width="50px" /></a>' % (self.image, self.image))
        else:
            return mark_safe('No existe una imagen')
    image_profile.allow_tags = True

    class Meta:
        verbose_name = 'cashier'
        verbose_name_plural = 'cashiers'

    def __str__(self):
        return self.user.username

#CLASS CLIENT
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    direction = models.CharField(max_length=100, null=True)
    phone = models.IntegerField()
    state = models.BooleanField('State', default=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        ordering = ['name']

    def __str__(self):
        return self.name

#CLASS SALE
class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    value_final = models.DecimalField(max_digits=20,decimal_places=2)
    date = models.DateField('Date of Creation', auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'sale'
        verbose_name_plural = 'sales'

    def __str__(self):
        return self.client.name