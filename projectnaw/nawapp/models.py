from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=80, unique=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    adrtype = models.CharField(max_length=10)
    street = models.CharField(max_length=80)
    postcode = models.CharField(max_length=15)
    city = models.CharField(max_length=25)

    def __str__(self):
        template = "Address Type: "+ str(self.adrtype) + "   Street: " + str(self.street)
        return template

    