class TowerOfHanoi:
    def __init__(self):
        return 

    def tower_of_hanoi(self, n, A, B, C):
        if n>0:
            self.tower_of_hanoi(n-1, A, C, B)
            print((A, C))
            self.tower_of_hanoi(n-1, B, A, C)
        return 


n = 3
TowerOfHanoi().tower_of_hanoi(n, 1, 2, 3)