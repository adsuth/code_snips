
# # # # # # # # # # # # # # # # # # # # # # # #
#     Debug Logging
# # # # # # # # # # # # # # # # # # # # # # # #

DEBUG_LOGGING_INCLUDED = True

def dlog( *args ):
  """ Debug Logging. Prints only if DEBUG_LOGGING_INCLUDED has been set to True
  """
  if DEBUG_LOGGING_INCLUDED:
    print( *args )


# # # # # # # # # # # # # # # # # # # # # # # #
#     Verbose printing
# # # # # # # # # # # # # # # # # # # # # # # #

VERBOSE_PRINTING_INCLUDED = True

def vprint( *args ):
  """ Verbose Printing. Prints only if VERBOSE_PRINTING_INCLUDED is True.
  """
  if VERBOSE_PRINTING_INCLUDED:
    print( *args )


# # # # # # # # # # # # # # # # # # # # # # # #
#     Stripping File Lines
# # # # # # # # # # # # # # # # # # # # # # # #

lines = [line.strip() for line in file]


# # # # # # # # # # # # # # # # # # # # # # # #
#     Function Timer
# # # # # # # # # # # # # # # # # # # # # # # #

# Requires: time

def func_timer( func ):
  """
  Decorator that returns the time taken for a function to complete \n
  Dependencies: time
  """
  def wrapper():
    from time import time
    start_time = time()
    output = func()
    end_time   = time()
    
    print( f"Total time to run {func.__name__} >> {end_time - start_time}" )
    return output
  return wrapper