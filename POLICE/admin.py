from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from .forms import *

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'phone', 'sex', 'title', 'is_active',
                    'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('personal', {'fields': ('first_name', 'middle_name', 'last_name', 'sex', 'phone', 'title'),
                      }),

        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups',
                                    'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)


class StaffAdmin(ImportExportModelAdmin):
    list_display = ('user', 'title', 'station', 'registered_on',)
    search_fields = ['user__username']
    list_filter = ['title', 'station']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Staff, StaffAdmin)


class ComplainantAdmin(ImportExportModelAdmin):
    list_display = ('user', 'code', 'registered_on',)
    search_fields = ['user__username']
    # list_filter = ['title', 'station']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Complainant, ComplainantAdmin)


class TitleAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    # list_filter = ['title', 'station']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Title, TitleAdmin)


class ZoneAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    # list_filter = ['title', 'station']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Zone, ZoneAdmin)


class RegionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'zone')
    search_fields = ['name']
    list_filter = ['zone']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Region, RegionAdmin)


class DistrictAdmin(ImportExportModelAdmin):
    list_display = ('name', 'region')
    search_fields = ['name']
    list_filter = ['region']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(District, DistrictAdmin)


class StationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'district')
    search_fields = ['name']
    list_filter = ['district']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Station, StationAdmin)


class CrimeAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    # list_filter = ['title', 'station']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Crime, CrimeAdmin)


class StatusAdmin(ImportExportModelAdmin):
    list_display = ('name', 'code')
    search_fields = ['name']
    # list_filter = ['title', 'station']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Status,StatusAdmin)


class CaseAdmin(ImportExportModelAdmin):
    list_display = ('rb', 'complainant', 'registerer', 'crime', 'registered_on',)
    search_fields = ['rb']
    list_filter = ['complainant', 'crime', 'registered_on']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Case, CaseAdmin)


class CaseInvestigatorAdmin(ImportExportModelAdmin):
    list_display = ('case', 'investigator', 'is_active', 'registered_on',)
    search_fields = ['case__rb']
    list_filter = ['investigator', 'case', 'is_active']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(CaseInvestigator, CaseInvestigatorAdmin)


class InvestigationRecordAdmin(ImportExportModelAdmin):
    list_display = ('case_investigator', 'status', 'is_active', 'report_date',)
    search_fields = ['case_investigator__case__rb']
    list_filter = ['case_investigator', 'status', 'is_active']

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(InvestigationRecord, InvestigationRecordAdmin)