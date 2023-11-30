"""
    Functions for generating a script from 
    a template, inferred from a suffix.
"""

from os.path import basename
from pathlib import Path
import pkg_resources
import argparse
import datetime
import yaml


"""
    Given a file suffix, get the path to the
    appropriate default template file.

    By default, template files are assumed to reside
    in the `script_templates` directory of this package.
    The user may specify other template files in 
    a config YAML.

    E.g., given "py", return the path to "template.py".
    By default we assume  
"""
def get_default_template_path(suffix):

    return pkg_resources.resource_filename("script_templates", 
                                           f"template.{suffix}")


"""
    Update the file generation parameters with information
    from the config YAML.
"""
def update_params(params, suffix, config):

    # Update the template file path, if applicable
    if "templates" in config.keys():
        d = config["templates"]
        if isinstance(d, dict) and suffix in d.keys():
            params["template_path"] = d[suffix]

    # Update the template fields, if applicable
    if "fields" in config.keys():
        params["fields"].update(config["fields"])

    return params


"""
    Return a config dictionary populated with default values;
    but check if a YAML exists at config_path.
    If it does, then load a config dictionary from there. 
"""
def prep_params(script_path, config_path):
    
    script_basename = basename(script_path)
    
    # The `suffix` is everything after the first period in the basename.
    suffix = ".".join(script_basename.split(".")[1:])

    # Get the appropriate template
    default_template_path = get_default_template_path(suffix)

    # Populate the params with default values
    script_year = str(datetime.datetime.now().year)
    params = {"template_path": default_template_path,
              "fields": { "__SCRIPT_NAME__": script_basename,
                          "__SCRIPT_YEAR__": script_year,
                        }
             }

    # Read the config YAML, if it exists
    if Path(config_path).exists():
        with open(config_path, "r") as f: 
            config = yaml.safe_load(f)
        # Overwrite the params with values from the config YAML
        params = update_params(params, suffix, config)

    return params


"""
    Given the path to a template file and a dictionary of fields to
    populate, return a string with all of the necessary substitutions.
    
"""
def fill_template(template_str, fields):
    for k, v in fields.items():
        template_str = template_str.replace(k, v)

    return template_str


"""
    Parse command line arguments and generate a 
    script from an appropriate template.

    The choice of template is governed by the suffix of the
    provided path.
"""
def generate_script():

    parser = argparse.ArgumentParser()
    parser.add_argument("new_script_path", help="Path to the newly generated script.")
    parser.add_argument("--config-yaml", default=str(Path.home().joinpath(".script_templates","config.yaml")),
                                         help="Path to a YAML configuration file. By default, looks for one at $HOME/.script_templates/config.yaml.")

    args = parser.parse_args()
    script_path = args.new_script_path
    config_path = args.config_yaml

    # Get the configuration for this new script
    params = prep_params(script_path, config_path)

    # Load the template file as a string
    with open(params["template_path"], "r") as f:
        template_str = f.read()
     
    # Fill in the template
    template_str = fill_template(template_str, 
                                 params["fields"])

    # Write the template to the new script
    with open(script_path, "w") as f:
        f.write(template_str)

    # And we're done!
    return


if __name__=="__main__":

    generate_script()


