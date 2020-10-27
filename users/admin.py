from django.contrib import admin

from django.contrib import admin
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin
from .models import Profile

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

CustomUser = get_user_model()

class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete=False
    verbose_plural_name="User Profile"
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  search_fields = ('email',)
  ordering = ('email',)
  list_display = ['email', 'username','date_joined', 'user_type']
  inlines = (UserProfileInline,)


admin.site.register(CustomUser, CustomUserAdmin)
