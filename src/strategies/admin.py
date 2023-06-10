from django.contrib import admin

from strategies.models import TradingTool


@admin.register(TradingTool)
class TradeAdmin(admin.ModelAdmin):
    list_display = ['title']
