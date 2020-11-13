'''
sinx = x - x^3/3! + x^5/5! - x^7/7!......
'''

class SineSeries():
    def __init__(self):
        return
    

    def factorial(self, num):
        if num == 1 or num == 0:
            return 1
        return num * self.factorial(num-1)

    def power(self, num, p):
        if num == 1:
            return num
        if p == 1:
            return num
        if p == 0:
            return 1
        return num * self.power(num, p-1)
    
    def compute_sine_series(self, x, n):

        # coverting to radians from degrees
        # 2 pi radians = 360 degrees
        x = x * (3.142 / 180.0)
        sinx = x
        numerator = x
        i = 3
        while(i<=n):
            denominator = self.factorial(i)
            numerator = -numerator * self.power(x, 2)
            x1 = numerator / denominator
            sinx += x1
            i += 2
        return sinx



x = 90
n = 17

print(SineSeries().compute_sine_series(x, n))