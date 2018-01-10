# HW07
## Quantopian 策略程式

績效：
Return = 81.33%
Alpha = 0.08
Beta = 0.66
Sharpe = 1.20
Max Drawdown = -16.81%

程式碼：
def initialize(context):
    # In our example, we're looking at Apple.  If you re-type
    # this line you'll see the auto-complete popup after `sid(`.
    context.securities = [sid(24),sid(5061)]

    # Specify that we want the 'rebalance' method to run once a day
    schedule_function(rebalance, date_rule=date_rules.every_day())

def vwap(prices, volumes):
    return (prices * volumes).sum() / volumes.sum()


"""
Rebalance function scheduled to run once per day (at market open).
"""
def rebalance(context, data):
    # To make market decisions, we're calculating the stock's
    # moving average for the last 1 days.

    # We get the price and volume history for the last 1 days.
    hist = data.history(
        context.securities,
        fields=['price', 'volume'] ,
        bar_count=1000, #歷史資料
        frequency='1d'
        )

    vwap_15 = vwap(hist["price"][-15:], hist["volume"][-15:])
    vwap_30 = vwap(hist["price"], hist["volume"])

    for s in context.securities:
        if vwap_15[s] > vwap_30[s]:
            order(s, 50)
