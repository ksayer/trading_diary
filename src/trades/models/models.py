from django.db import models
from filer.fields.image import FilerImageField

from admintools.models import CoreModel
from strategies.models import TradingTool


class Asset(CoreModel):
    class MarketChoices(models.TextChoices):
        STOCKS = 'STOCKS'
        FOREX = 'FOREX'
        CRYPTO = 'CRYPTO'

    symbol = models.CharField(max_length=255, unique=True)
    market = models.CharField(max_length=6, choices=MarketChoices.choices)

    def __str__(self):
        return '{symbol}'.format(symbol=self.symbol, market=self.market)

    class Meta:
        ordering = ['symbol']


class Trade(CoreModel):
    class ReasonOutChoices(models.TextChoices):
        SL = 'SL', 'Stop Loss'
        TP = 'TP', 'Take Profit'
        MANUALLY = 'M'

    class TradeActionChoice(models.TextChoices):
        SELL = 'S'
        BUY = 'B'

    class TrendChoices(models.TextChoices):
        SELL = 'S'
        BUY = 'B'
        UNKNOWN = 'U'

    asset = models.ForeignKey(Asset, related_name='trades', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True, blank=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    result_points = models.IntegerField(null=True, blank=True)
    result_amount = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True
    )
    trading_tool = models.ForeignKey(
        TradingTool, related_name='trades', on_delete=models.CASCADE
    )
    reason_out = models.CharField(
        max_length=2, choices=ReasonOutChoices.choices, blank=True
    )
    action = models.CharField(max_length=1, choices=TradeActionChoice.choices)
    trend = models.CharField(max_length=1, choices=TrendChoices.choices)

    def __str__(self):
        return '{asset}. {open_date}'.format(
            asset=self.asset,
            open_date=self.open_date.date()
        )


class TradeScreenshot(CoreModel):
    class TimeframeChoices(models.TextChoices):
        M1 = 'M1'
        M5 = 'M5'
        M15 = 'M15'
        M30 = 'M30'
        H1 = 'H1'
        H4 = 'H4'
        D1 = 'D1'

    timeframe = models.CharField(max_length=3, choices=TimeframeChoices.choices)
    screenshot = FilerImageField(on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return 'Screenshot {timeframe}. {trade}'.format(
            trade=self.trade, timeframe=self.timeframe
        )
