from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2)
    month_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.last_name + ' - ' + str(self.monthly_budget)


class List(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=5000, default=None)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name + ' - ' + str(self.total_sum)


class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=5000, default=None)
    is_prioritized = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + str(self.price)
