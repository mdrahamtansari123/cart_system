from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=105, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['id'] 

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_quantity = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name if self.product else 'No Product'} - Qty: {self.total_quantity} - Total: {self.total_price}"

    def save(self, *args, **kwargs):
        if self.product:
            if not self.pk and self.product.quantity < self.total_quantity:
                raise ValueError("Not enough product in stock.")

            # Calculate total price
            self.total_price = self.product.price * self.total_quantity

            # Update product quantity
            if not self.pk:  # Only reduce stock for new items
                self.product.quantity -= self.total_quantity
                self.product.save()
        super().save(*args, **kwargs)

   