import hikari

def error_embed( msg ):
  """Simple error embed. """
  return hikari.Embed(
    title = msg,
    color = "red",
  )

def debug_embed( msg ):
  """Simple debug embed. """
  return hikari.Embed(
    title = msg,
    color = "yellow"
  )