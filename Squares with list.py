num=[2,3,4,5]
squares=[]
def Square(num):
    for i in num:
        squares=i*i
        print(squares)
num.append(6)
Square(num)
