from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from accounts.models import StudentProfile, MentorProfile,Mentor_assign
from accounts.models import User
# Register your models here.

Desc = 'Add College Email-ID'

class CustomUserAdmin(UserAdmin):
    
    model=User
    list_display=('email','staff','active','superuser',)
    list_filter=('email','staff','active','superuser',)

    fieldsets = (
        (None, {
            'classes':('wide',),
            "fields": (
                'email','password1','password2','staff','active'
            ),
        }),
    )
    
    search_fields=('email',)
    ordering=('email',)

  
# class UserAdminConfig(UserAdmin):
#     model = User
#     search_fields = ('email', 'user_name', 'first_name',)
#     list_filter = ('username','email', 'first_name', 'is_active', 'is_staff')
#     ordering = ('email',)
#     list_display = ('username','email', 'first_name',
#                     'is_active', 'is_staff')
#     fieldsets = (
#         ('Section 1', {'fields': ('email', 'first_name', 'last_name',),  
#                        'description': '%s' % Desc,
        
#         }),
#         ('Permissions', {'fields': ('is_staff', 'is_active'),
#                          'classes': ('collapse',),
#         }),
       
#     )
    
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )

class Admin(admin.AdminSite):
    site_header = 'MPT'

# admin.site.unregister(User)

admin_site = Admin(name='MPTAdmin')
# admin_site.register(User,UserAdminConfig)
admin_site.register(User,CustomUserAdmin)
admin_site.register(StudentProfile)
admin_site.register(MentorProfile)
admin_site.register(Mentor_assign)

