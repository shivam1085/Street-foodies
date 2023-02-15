from django.db import models 
# class Food(models.Model): 
	
  
#     title = models.CharField(max_length = 50,null=True,default=True,unique=True) 
   
#     desc=models.TextField(max_length = 250,null=True,default=True) 
#     f_img = models.ImageField(upload_to = "mobiles",null=True,default=True) 
#     m_img = models.ImageField(upload_to = "mobiles",null=True,default=True)
#     rating=models.IntegerField(null=True,default=True)
#     location=models.CharField(max_length = 100,null=True,default=True)
#     contact=models.CharField(max_length=15,null=True,default=True)
#     time=models.CharField(max_length=20,null=True,default=True)
#     category=models.CharField(max_length=20,null=True,default=True)
#     def __str__(self): 
# 	    return self.title 


class Blog(models.Model): 
    heading = models.CharField(max_length = 100,null=True,default=True) 
    writer = models.CharField(max_length = 50,null=True,default=True) 
    desc=models.TextField(max_length = 500,null=True,default=True) 
    f_img = models.ImageField(upload_to = "Blogs",null=True,default=True)
     
class Vendor(models.Model): 
    title = models.CharField(max_length = 50,default=True,null=True) 
    # img = models.ImageField(upload_to = "mobiles",null=True,default=True) 
    rating=models.IntegerField(null=True,default=True)
    location=models.CharField(max_length = 100,null=True,default=True)
    mobile=models.CharField(max_length=15,unique=True,default=True,null=True)
    time=models.CharField(max_length=20,null=True,default=True)
    category=models.CharField(max_length=20,null=True,default=True)
    license_no=models.CharField(max_length=20,null=True,default=True)
    # user_name = models.CharField(max_length = 50,null=True,default=True,unique=True) 
    password = models.CharField(max_length = 20,default=True,null=True) 
    img = models.ImageField(upload_to = "vendors",null=True,default=True) 
    shaadi=models.BooleanField(default=False)
    reward=models.IntegerField(null=True,default=True)
    
class Appuser(models.Model): 
    mobile = models.CharField(max_length = 50,null=True,default=True,unique=True) 
    
    password = models.CharField(max_length = 50,null=True,default=True) 
   
    # desc=models.TextField(max_length = 250,null=True,default=True) 
    # img = models.ImageField(upload_to = "vendors",null=True,default=True) 
    # contact=models.CharField(max_length=15,null=True,default=True)
