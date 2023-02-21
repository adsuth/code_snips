
def retrieve_args():
  import argparse as ap
  """Gets Command-line Arguments. \n
  See below for extra examples. \n
  Will return the args. Access specific argument values with dot notation \n
  Dependencies: argparse """
  parser = ap.ArgumentParser(
    prog        = "Program Title",
    description = "This is what the program does. ",
  )

  # nargs     = Number of Arguments, + == unnumbered
  # dest      = the key the value is stored at
  # action    = eg: "store_true" will set the dest to True if present
  # help      = what will show for the given arg when --help is used
  # required  = do you need it to run the script or not?
  # type      = the data type (str, int, etc)

  parser.add_argument(
    dest = "sources",
    nargs = "+",
    type = str,
    default = [],
    help = f"Directory of source file(s) to be converted to docs. ",
  )

  parser.add_argument(
    "-t", "--tsv",
    dest = "parseTSV",
    action="store_true",
    default = False,
    help = f"Choose to parse TSV file(s). (default) ",
    required = False
  )

  parser.add_argument(
    "-c", "--csv",
    dest = "parseCSV",
    action="store_true",
    default = False,
    help = f"Choose to parse CSV file(s). ",
    required = False
  )

  parser.add_argument(
    "-v", "--verbose",
    dest = "verboseMessaging",
    action="store_true",
    help = f"If present, verbose messaging will be enabled. ",
    required = False
  )

  parser.add_argument(
    "-d", "--debug",
    dest = "verboseMessaging",
    action="store_true",
    help = f"If present, verbose messaging will be enabled. ",
    required = False
  )

  return parser.parse_args()