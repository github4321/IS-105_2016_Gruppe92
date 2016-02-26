def test():
    L = [i for i in range(500)]

if __name__=='__main__':
    from timeit import Timer
    t = Timer("test()", "from __main__ import test")
    print(t.timeit())