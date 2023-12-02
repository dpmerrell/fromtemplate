"""
    Functions for generating a directory from a template.
"""

from fromtemplate.generate_file import generate_file
from pathlib import Path

"""
    Recursively generate a directory (or a file) by populating a template.
"""
def generate_dir(new_file_path, template_path, fields, verbose=False, print_str=""):

    tp = Path(template_path)
    nfp = Path(new_file_path)

    # Base case: template path is a file
    if tp.is_file():
        generate_file(new_file_path, template_path, fields)

    # Recursive case: template path is a directory
    elif tp.is_dir():
        # Make a new directory at `nfp`
        nfp.mkdir(parents=True, exist_ok=True)

        # Get children of the template path (directory)
        for child_path in tp.iterdir():
            
            # Perform any string substitutions in the temporary file/directory name
            child_basename = child_path.name
            for k,v in fields.items():
                child_basename = child_basename.replace(k,v) 
            # Need to make sure we emulate the template directory structure.
            new_child_str = str(nfp.joinpath(child_basename))
 
            # For each child, call generate_dir. 
            template_child_str = str(child_path)
            generate_dir(new_child_str, template_child_str, fields,
                         verbose=verbose, print_str=f"\t{print_str}")
    else:
        raise ValueError(f"{template_path} is not a file or directory.")

    return


