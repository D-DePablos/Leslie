import json
from binance.client import Client 


class LeslieTrader:
    def __init__(self, clientInstance, main_asset='BTC'):
        self.clientInstance = clientInstance
        self.main_asset = main_asset
    
    def __repr__(self):
        return f"{self.clientInstance} - Main Asset : {self.main_asset}"

    def depositAsset(self, assetSymbol):
        print(self.clientInstance.get_deposit_address(asset=assetSymbol))


    def checkBalance(self, assetSymbol="BTC"):
        balance = self.clientInstance.get_asset_balance(asset=assetSymbol)
        print(f"You have {balance} {assetSymbol}")
        return balance

    def createOrder(self, assetSymbol, side, quantity, order_type="market", testOrder=True):
        """
        Create a test / real order for a given coin.
        Parameters:
        
        symbol: 3 / 4 digit string of the coin (e.g ENJ)
        side: "BUY or SELL"
        quantity: Amount to trade with. If empty asks to use full balance?
        order_type: "market" or "limit", if limit needs additional implementation
        testOrder: Whether test order or not
        """

        # Handle limit and market orders
        if order_type == "market":
            order_type = Client.ORDER_TYPE_MARKET

        elif order_type == "limit":
            order_type = Client.ORDER_TYPE_LIMIT
            raise NotImplementedError("Limit orders are not yet implemented")

        else:
            raise NotImplementedError(f"No order type {order_type}, please use market instead")

        print(f"Creating {'test' if testOrder else ''} {order_type} order"  
              f" to {side} {quantity} {assetSymbol} {'for' if side == 'SELL' else 'with'} {self.main_asset}")

        # Allow for test Orders or real orders
        if testOrder:
            order_function = self.clientInstance.create_test_order
        else:
            order_function = self.clientInstance.create_order
        
        order_function(
            symbol=f"{assetSymbol}{self.main_asset}",
            side=side,
            type=order_type,
            quantity=quantity,
        )

# Secrets to get Binance API keys
with open("Utils/Secrets.json", "r") as file:
    secrets = json.load(file)

api_key = secrets["API_KEY"]
api_secret =  secrets["SECRET_KEY"]

# Open connection to Binance Client and instantiate Leslie
client = Client(api_key, api_secret)
trade = LeslieTrader(client, "USDT")

tradeDictionary = {
    "assetSymbol": "ENJ",
    "side": "SELL",
    "quantity": 100,
    "order_type": "market",
    "testOrder": True
}

trade.checkBalance(tradeDictionary["assetSymbol"])
trade.depositAsset(tradeDictionary["assetSymbol"])
trade.createOrder(**tradeDictionary)
