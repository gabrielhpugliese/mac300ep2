import time
import functools


def time_measure(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        t = time.clock()

        resp = func(*args, **kwargs)

        t = time.clock() - t
        func_name = func.__name__
        print 'Tempo levado para conclusao do metodo %s: %s' % (func_name,
                                                                str(t))
        return resp

    return wrap

