from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

# Inline admin for editing user profiles directly within the User admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend the built-in User admin to include profile info
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)

# Unregister default User admin, then register new one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Optional: Also register UserProfile directly if you want it separately visible
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'bio')
