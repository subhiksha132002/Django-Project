from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey( 'Product',on_delete = models.SET_NULL,null = True,related_name = '+')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    slug = models.SlugField()
    unit_price = models.DecimalField(max_digits = 6,decimal_places = 2)
    inventory = models.IntegerField()
    # last_updated = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection,on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP = [ 
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 255)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1,choices = MEMBERSHIP,default = MEMBERSHIP_BRONZE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['first_name','last_name']
    


class Order(models.Model):
    
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETED = 'C'
    PAYMENT_STATUS_FAILED = 'F'


    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETED,'Completed'),
        (PAYMENT_STATUS_FAILED,'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1,choices = PAYMENT_STATUS_CHOICES,default = PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer,on_delete = models.PROTECT)



class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    customer = models.OneToOneField(Customer,on_delete = models.CASCADE,primary_key = True)



class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.PROTECT)
    product = models.ForeignKey(Product,on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6,decimal_places = 2)


class Cart(models.Model):
    item = models.DateTimeField(auto_now_add = True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

