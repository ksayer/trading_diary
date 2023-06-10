from django.contrib import admin
from trades.models import Trade, Asset, TradeScreenshot


class TradeScreenshotInline(admin.TabularInline):
    model = TradeScreenshot


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    inlines = [TradeScreenshotInline]
    list_display = ['__str__', 'trading_tool', 'action', 'result_points']
    list_filter = ['trading_tool', 'asset']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'market']
    list_filter = ['market']
    search_fields = ['symbol']
