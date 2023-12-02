"""
    Functions for generating a file from a template.
"""

"""
    Given the path to a template file and a dictionary of fields to
    populate, return a string with all of the necessary substitutions.
    
"""
def fill_file_template(template_str, fields):
    for k, v in fields.items():
        template_str = template_str.replace(k, v)

    return template_str

"""
    Generate a new file from a template file,
    performing string substitutions specified
    by `fields`.
"""
def generate_file(newfile_path, template_path, fields, verbose=False, print_prefix=""):

    # Load the template file as a string
    try:
        with open(template_path, "r") as f:
            template_str = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template {template_path} does not exist! Try specifying one in your config YAML.")
 
    # Fill in the template
    template_str = fill_file_template(template_str, 
                                      fields)

    # Write the template to the new file 
    with open(newfile_path, "w") as f:
        f.write(template_str)

    if verbose:
        print(f"{print_prefix}{newfile_path}")

    # And we're done!
    return



