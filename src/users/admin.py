from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username", "email", "verified_status",
        "followers_count", "following_count", "is_staff", "created_at",
    )
    list_filter = ("is_verified", "is_staff", "is_active")
    search_fields = ("username", "email")
    readonly_fields = ("followers_count", "following_count", "created_at")
    ordering = ("-created_at",)

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("bio", "avatar", "is_verified",
                       "followers_count", "following_count")
        }),
    )

    @admin.display(description="Verified", boolean=True, ordering="is_verified")
    def verified_status(self, obj):
        return obj.is_verified
