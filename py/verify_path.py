# ------------------------------------------- #
#     Veripath
# ------------------------------------------- #
# 
# Recursively get all files in a given directory of a certain file type.
# You can also opt to exclude given files
# 

def get_files_recursively( directory: str = None, extension: str = "", exclusion_list: list[str] = [] ) -> list[str]:
  """ Retrieve all files from a given directory.
  Also includes all subfiles.
  You can also pass a list of extensions to exclude

  Dependencies:
  - os
  """
  # break: no directory given.
  if directory == None:
    raise Exception( "No directory was given. " )

  output = []
  for path in os.walk( directory ):
    for innerPath in path[2]:
      formatted_path = f"{ path[0] }\\{ innerPath }"
      should_exclude = False

      for excluded_file in exclusion_list:
        if excluded_file in formatted_path:
          should_exclude = True
          break    
      
      should_include = (
        not should_exclude               
        and os.path.isfile( formatted_path ) 
        and formatted_path.endswith( extension )
      ) 

      if should_include:
        # you can add a dlog or vlog here, eg
        # print( f"{CLR.blue}Found file {formatted_path}{CLR.end}" )
        output.append( formatted_path )

  return output
