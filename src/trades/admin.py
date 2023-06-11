from django.contrib import admin
from django.utils.html import format_html
from rangefilter.filters import DateRangeFilterBuilder

from trades.models import Trade, Asset, TradeScreenshot


class TradeScreenshotInline(admin.TabularInline):
    model = TradeScreenshot


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    inlines = [TradeScreenshotInline]
    list_display = ['__str__', 'trading_tool', 'action', 'result_points_colored']
    list_filter = [
        'trading_tool',
        'asset',
        'reason_out',
        ('open_date', DateRangeFilterBuilder()),
        ('close_date', DateRangeFilterBuilder()),
    ]
    autocomplete_fields = ['asset']

    def result_points_colored(self, instance):
        if instance.result_points:
            color = 'red' if instance.result_points < 0 else 'green'
            tag = f'<span style="color:{color}">{instance.result_points}</span>'
            return format_html(tag)
        return instance.result_points
    result_points_colored.short_description = 'result points'


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'market']
    list_filter = ['market']
    search_fields = ['symbol']
