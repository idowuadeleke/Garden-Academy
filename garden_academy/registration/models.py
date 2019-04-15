from django.db import models

# Create your models here.
class Register(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    number_of_delegates = models.CharField(max_length=200)
    corps_member = models.CharField(max_length=200,null=True)
    transaction_id = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=200)
    transaction_reference = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.fullname, self.email,
         self.transaction_reference, self.amount, self.date)

