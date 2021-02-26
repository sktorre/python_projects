# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# timer.py:   Contains a function to measure the runtime of a specified function or method.     #
#                                                                                               #
#                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import time



def timedFunction(function):
    """
    Description:	Decorator which captures execution time of a function.

    Return:			VOID; Prints execution time to standard output.
    """

    def timedWrapper(*args, **kwargs):
        start = time.time()
        print(function.__name__ + ": Process Started.")
        returnValue = function(*args, **kwargs)
        end = time.time()

        print(function.__name__ + ": Completed in ", round(end - start, 2), " seconds.")
        return returnValue

    return timedWrapper
