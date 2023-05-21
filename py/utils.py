# # # # # # # # # # # # # # # # # # # # # # # #
#     Disable Printing
# # # # # # # # # # # # # # # # # # # # # # # #
# Alternative to debug logging; simply prevent default printing functionality if required
LOGGING = False

if not LOGGING:
  def print( *_ ):
    ...


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

# # # # # # # # # # # # # # # # # # # # # # # #
#     Get Object Properties
# # # # # # # # # # # # # # # # # # # # # # # #

def get_all_props( instance: object ) -> list[ str ]:
  """
  Returns a list of all keys / props in given user-defined Class instance. \n
  This will ignore dunder methods (eg, Python's inbuilt methods)
  """
  return [ prop for prop in dir( instance ) if not prop.startswith( "__" ) ]

def get_props( instance: object ) -> list[ str ]:
  """
  Returns a list of all keys / props in given user-defined Class instance. \n
  This will ignore any Class Methods!!
  This will ignore dunder methods (eg, Python's inbuilt methods)
  """
  return [ prop for prop in dir( instance ) if not prop.startswith( "__" ) and not callable( getattr( instance, prop ) ) ]
