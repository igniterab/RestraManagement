from django.db import models

class StaffUser(models.Model):
  email = models.EmailField(max_length = 50, unique = True)
  first_name = models.CharField(max_length = 20)
  last_name = models.CharField(max_length = 10)
  native_name = models.CharField(max_length = 50, blank = False, unique = True)
  phone_no = models.CharField(max_length = 10)
  address = models.CharField(max_length = 100)
  busy = models.BooleanField()

  REQUIRED_FIELDS = ['username', 'native_name', 'first_name', 'last_name']

  def __str__(self):
      return self.native_name
