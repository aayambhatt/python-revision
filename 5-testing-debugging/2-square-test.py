def square(x):
    return x*x

def square_testing():
    assert square(3)==9
    assert square(5)==25
    assert square(1.5)==2.25
    print("All tests passed")

square_testing()