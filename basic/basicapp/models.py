from django.db import models

# Create your models here.


class signup_info(models.Model):
    user_name=models.CharField(max_length=200)
    user_email=models.CharField(max_length=200)
    user_pass=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    vanue=models.CharField(max_length=200)

    @staticmethod
    def match_log(email):
        try:
            return signup_info.objects.get(user_email=email)
        except:
            return False



class product_info(models.Model):
    name=models.CharField(max_length=200)
    prize=models.CharField(max_length=200)
    discribe=models.CharField(max_length=500)


