class BuyAndSellStocksII:
    def __init__(self):
        return

    def get_max_profit(self, arr):

        arrLen = len(arr)
        low = 0
        high = 0
        maxProfit = 0
        i = 0

        while(i < arrLen - 1):

            # To buy we need the low priced stock
            while(i < arrLen - 1 and arr[i] >= arr[i+1]):
                i += 1
            
            low = arr[i]

            # To sell we need the high prices stock
            while(i < arrLen - 1 and arr[i] <= arr[i+1]):
                i += 1

            high = arr[i]

            maxProfit += high - low
        return maxProfit

    
    def get_max_profit_refined(self, arr):
        maxProfit = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                maxProfit += arr[i] - arr[i-1]

        return maxProfit




arr = [1, 2, 3, 4, 5]

obj = BuyAndSellStocksII()
print(obj.get_max_profit(arr))
print(obj.get_max_profit_refined(arr))
    