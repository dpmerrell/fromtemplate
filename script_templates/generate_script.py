"""
    Functions for generating a script from 
    a template, inferred from a suffix.
"""

from os.path import basename
import datetime
import pkg_resources
import argparse

"""
    Given a file suffix, get the path to the
    appropriate template file.

    E.g., given "py", return the path to "template.py".
    By default we assume  
"""
def get_template_file_path(suffix):

    return pkg_resources.resource_filename("script_templates", 
                                           f"template.{suffix}")


"""
    Given the path to a template file and a dictionary of fields to
    populate, return a string with all of the necessary substitutions.
    
"""
def fill_template(template_path, fields):

    with open(template_path, "r") as f:
        template_str = f.read() 

    for k, v in fields.items():
        template_str = template_str.replace(k, v)

    return template_str


"""
    Parse command line arguments and generate a 
    script from an appropriate template.

    The choice of template is governed by the suffix of the
    provided path.

    TODO 
        * allow templates to be specified in a config file 
        * allow the set of fields to be set in a config file
"""
def generate_script():

    parser = argparse.ArgumentParser()
    parser.add_argument("new_script_path", help="Path to the newly generated script")
    args = parser.parse_args()

    script_path = args.new_script_path
    script_basename = basename(script_path)
    
    # The `suffix` is everything after the first period in the basename.
    suffix = ".".join(script_basename.split(".")[1:])

    # Get the appropriate template
    template_path = get_template_file_path(suffix)

    # Fields for populating the template
    script_year = str(datetime.datetime.now().year)
    fields = {"__SCRIPT_NAME__": script_basename,
              "__SCRIPT_YEAR__": script_year
             }

    # Fill in the template
    template_str = fill_template(template_path, fields)

    # Write the template to the new script
    with open(script_path, "w") as f:
        f.write(template_str)

    # And we're done!
    return


if __name__=="__main__":

    generate_script()


