from datetime import datetime
from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from .constants import RenewalType, SubscriptionStatus

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		"""Create and return a `User` with an email and password."""
		if email is None:
			raise TypeError('Users must have an email address.')
		user = self.model(email=email, **kwargs)
		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, email, password=None, **kwargs):
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.model(email=email, **kwargs)
		user.set_password(password)
		user.is_superuser = True
		user.is_staff = True
		user.is_verified = True
		user.role = 'admin'
		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin):
	first_name = models.CharField(verbose_name='First Name', max_length=60)
	last_name = models.CharField(verbose_name='Last Name', max_length=60, null=True, blank=True)
	email = models.EmailField(db_index=True, unique=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	get_notified = models.BooleanField(default=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		"""
		Returns a user's  full_name
		"""
		return '%s %s' % (self.first_name, self.last_name)


class SaleOrder(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, default=None)
    amount = models.FloatField(default=0, null=True)
    renewal = models.IntegerField(choices=RenewalType.choices(), default=RenewalType.MONTHLY.value)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    start_date = models.DateTimeField(default=datetime.now, null=True)
    due_date = models.DateTimeField(default=None, null=True)
    paid = models.BooleanField(default = False)
    
    def __str__(self):
        return "%s (%s)" % (self.name, self.amount)


class Country(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)
    
    def __str__(self):
        return "%s" % (self.name)


class SuperAgent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)


class Store(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)
    
    def __str__(self):
        return "%s" % (self.name)
    

class Subscribers(models.Model):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.PROTECT, null=True, blank=True)
    status = models.IntegerField(choices=SubscriptionStatus.choices(), default=SubscriptionStatus.PENDING.value)
    meta = models.JSONField(default=None, null=True)
    bounce = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null = True, blank = True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null = True, blank = True)
    super_agent = models.ForeignKey(SuperAgent, on_delete=models.CASCADE, null = True, blank = True)
    

    
class NotificationTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length=255, default=None, null=True)
    sent = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add=True)
