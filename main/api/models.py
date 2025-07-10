from django.db import models
from django.utils import timezone

# Create your models here.
class Expense(models.Model):

    title = models.CharField(max_length=255) # A short title for the expense (e.g., Amazon order, Metro ticket).

    amount = models.DecimalField(max_digit=10,decimal_places=2) # The amount spent.

    CATEGORY_CHOICES = [
        ('shopping', 'Shopping'),
        ('transport', 'Transport'),
        ('entertainment', 'Entertainment'),
        ('food', 'Food'),
        ('health', 'Health'),
        ('bills', 'Bills & Utilities'),
        ('subscriptions', 'Subscriptions'),
        ('education', 'Education'),
        ('others', 'Others'),
    ]
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='others') # Category under which the expense falls.

    date = models.DateField(default=timezone.now) # The date of the expense. Defaults to today's date.

    note = models.TextField(blank=True,null=True) # Optional note or description for the expense

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - ₹{self.amount} ({self.get_category_display()})"

    class Meta:
        ordering = ['-date', '-created_at']

