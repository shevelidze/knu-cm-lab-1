import math

eps = 0.005
a = 2
b = 15
I2 = 0.00222196
M2 = 0.24691358024691357
h = 0.25

def function(x: float) -> float:
    return (1/(1 + x**3))

def ddfunction(x: float) -> float:
    return (12*x**4-6*x)/(x**9+3*x**6+3*x**3+1)

def hvalue(a: float, b: float, M2: float, eps: float) -> float:
    return math.sqrt((24*eps)/(M2*(b-a)))


print(f"M2 = {ddfunction(a)}")
print(f"h >= {hvalue(a, b, M2, eps)}")
print(f"h = 0.25")

I1 = 0
counter = 0
a += h/2
while(a <= b - h/2):
    if(counter <= 6 or counter >= 46):
        print(f"x = {a}; f(x) = {function(a)}")
    I1 += h * function(a)
    a += h
    counter += 1

print(f"count = {counter}")
print(f"I1 = {I1}")
print(f"I = {I2+I1}")