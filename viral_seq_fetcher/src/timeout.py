#! /usr/bin/python
# -*- coding: utf-8 -*-



# from http://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish
# works only under UNIX!

from functools import wraps
import errno
import os
import signal

try:
    err_num = errno.ETIME
except: #works under windows
    err_num = 1460 

class TimeoutError(Exception):
    pass


def timeout(seconds=10, error_message=os.strerror(err_num)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator
