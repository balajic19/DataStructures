'''
e^x = 1 + x^1 / 1! +  x^2 / 2!  +  x^3 / 3!  +  x^4 / 4!  +  x^5 / 5!  + ...
'''
class taylorSeries:
    def __init__(self):
        self.p = 1
        self.f = 1
        return


    def taylor_series_recursion(self, x, n):
        if n == 0:
            return 1
        result = self.taylor_series_recursion(x, n - 1)  
        self.p *= x
        self.f *= n
        return result + self.p/self.f



x = 2
n = 5
'''
which means we need to find e^2 till x^5 / 5!
'''

print(taylorSeries().taylor_series_recursion(x, n))