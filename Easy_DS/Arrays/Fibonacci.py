class Fibonacci:
    def __init__(self, num):
        self.num = num

    def generate_fibonacci(self):
        if self.num <=1 :
            return 1

        fibArr = [0] * (self.num+1)
        fibArr[0] = 0
        fibArr[1] = 1
        for i in range(2, self.num+1):
            fibArr[i] = fibArr[i-1] + fibArr[i-2]

        return fibArr[self.num]


number = 5
print(Fibonacci(number).generate_fibonacci())
