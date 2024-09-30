from django.contrib import admin
from django.contrib.auth.hashers import make_password # Untuk hashing password
from .models.admin import Admin
from .models.customer import Customer
from .models.order import Order
from .models.product import Product
from .models.users import Users

class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')

    def save_model(self, request, obj, form, change):
    # Simpan admin terlebih dahulu
        super().save_model(request, obj, form, change)

        # Cek apakah user dengan email guru sudah ada
        user, created = Users.objects.get_or_create(username=obj.name, defaults={ # Pastikan ini model Users kustom
        'password': make_password('default_password'), # Menggunakan hashing password
        'role': Users.ADMIN # Pastikan Anda memiliki field role di model Users
        })

        if not created:
            # Jika user sudah ada, perbarui role (untuk berjaga-jaga)
            user.role = Users.ADMIN
            user.save()

# Daftarkan admin dengan custom AdminAdmin
admin.site.register(Admin, AdminAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Users)