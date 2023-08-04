# -*- coding: cp1251 -*-
from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at', 'updated_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('�����', {'fields': ('title', 'description')
        }),
        ('�������', {'fields': ('price', 'auction'),
                    'classes': ['collapse']
        })
    )

    @admin.action(description='������ ����������� �����')
    def make_auction_as_false(self, requests, queryset):
        queryset.update(auction=False)

    @admin.action(description='�������� ����������� �����')
    def make_auction_as_true(self, requests, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)