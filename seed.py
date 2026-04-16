import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product
from decimal import Decimal

def seed():
    print("Clearing old data...")
    Category.objects.all().delete()
    Product.objects.all().delete()

    print("Creating categories...")
    tech = Category.objects.create(name='Technology', slug='technology')
    apparel = Category.objects.create(name='Apparel', slug='apparel')
    home = Category.objects.create(name='Home', slug='home')

    print("Creating products...")
    Product.objects.create(
        category=tech,
        name='AeroBlade Smart Watch',
        slug='aeroblade-smart-watch',
        description='A beautifully crafted smartwatch with heart rate monitoring, GPS, and a stunning OLED display. Designed for the professionals.',
        price=Decimal('299.99'),
        available=True
    )

    Product.objects.create(
        category=tech,
        name='Noise Cancelling Headphones Pro',
        slug='noise-cancelling-headphones-pro',
        description='Immerse yourself in pure audio bliss with active noise cancellation and 40-hour battery life.',
        price=Decimal('349.00'),
        available=True
    )

    Product.objects.create(
        category=apparel,
        name='Premium Minimalist Backpack',
        slug='premium-minimalist-backpack',
        description='Crafted from water-resistant materials, featuring hidden pockets and ergonomic back support. Perfect for the urban commuter.',
        price=Decimal('120.00'),
        available=True
    )

    Product.objects.create(
        category=home,
        name='Smart Ceramic Coffee Mug',
        slug='smart-ceramic-coffee-mug',
        description='Keep your coffee at the perfect temperature all day long with app-controlled heating.',
        price=Decimal('89.50'),
        available=True
    )

    print("Seed complete!")

if __name__ == '__main__':
    seed()
