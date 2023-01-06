from django.db import models

# Create your models here.
class Product (models.Model):
  product_id=models.AutoField
  product_name=models.CharField(max_length=50)
  desc=models.CharField(max_length=50)
  pub_date=models.DateField(auto_now=False, auto_now_add=False)
  category=models.CharField(max_length=50,default="")
  subcategory=models.CharField(max_length=50,default="")
  price=models.IntegerField(default=0)
  image=models.ImageField(upload_to='shop/images', height_field=None, width_field=None, max_length=None,default="")

  def __str__(self):
      return self.product_name
  
class Contact(models.Model):
  product_id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=50,default="")
  email=models.CharField(max_length=70,default="")
  phone=models.CharField(max_length=70,default="")
  desc=models.CharField(max_length=500,default="")

  def __str__(self):
      return self.name

class Orders(models.Model):
  order_id=models.AutoField(primary_key=True)
  items_json=models.CharField(max_length=5000)
  name=models.CharField(max_length=90)
  phone = models.CharField(max_length=111, default="")
  email=models.CharField(max_length=50)
  address=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  state=models.CharField(max_length=50)
  zip_code=models.CharField(max_length=20)

  def __str__(self):
      return self.name

class OrderUpdate(models.Model):
  update_id=models.AutoField(primary_key=True)
  order_id=models.IntegerField(default="")
  update_desc=models.CharField(max_length=500)
  timestamp=models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.update_desc[0:7]+"..."
  
  