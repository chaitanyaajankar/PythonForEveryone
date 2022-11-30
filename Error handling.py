x=-5
y=-6
if x < 0:
    raise Exception('x should be positive')

assert (y>=0), 'x is not positive'
try:
    a=5/0
except:
    print("an error happened")