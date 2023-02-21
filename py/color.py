class Color:
  """
  Contains Console color codes.\n
  To use them, wrap your string like \n
  `f"{Color.blue}This will be blue. {Color.end}"`
  """
  header    = '\033[95m'
  blue      = '\033[94m'
  cyan      = '\033[96m'
  green     = '\033[92m'
  yellow    = '\033[93m'
  red       = '\033[91m'
  end       = '\033[0m'
  bold      = '\033[1m'
  underline = '\033[4m'