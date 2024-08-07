"""
    Functions for managing the configuration of 
    file generation.

    This includes (1) loading default configuration
    and (2) updating it with user-provided specifications.
"""

from pathlib import Path
import pkg_resources
import datetime
import yaml
import copy

"""
    By default, template files are assumed to reside
    in the `default_templates` directory of this package.
"""
def default_template_path(template_name):

    return pkg_resources.resource_filename("fromtemplate",
                                           str(Path("default_templates", 
                                                     template_name
                                                    )
                                              )
                                          )

"""
    Populate file generation parameters with information
    from the default config and the config YAML.
"""
def get_params(name, kind, default_config, config):

    # Populate params from the defaults
    params = {"fields": default_config["fields"],
              "template_path": None
              }
    params["template_path"] = default_config["templates"].get(kind)
    params["fields"]["__FILE_NAME__"] = name 

    # Update the template file path from the config, if applicable
    if "templates" in config.keys():
        templates = config["templates"]
        if isinstance(templates, dict) and kind in templates.keys():
            params["template_path"] = str(Path(templates[kind]).expanduser())

    # Update template fields from the config, if applicable
    if "fields" in config.keys():
        params["fields"].update(config["fields"])

    return params


DEFAULT_CONFIG = {"fields": 
                     {"__FILE_YEAR__": str(datetime.datetime.now().year).zfill(4),
                      "__FILE_MONTH__": str(datetime.datetime.now().month).zfill(2),
                      "__FILE_DAY__": str(datetime.datetime.now().day).zfill(2),
                      "__FILE_NAME__": "__NONAME__"
                     },
                  "templates": 
                      {
                       "py": default_template_path("python_script"),
                       "python_script": default_template_path("python_script"),
                       "python_package": default_template_path("python_package"),
                      }
                 }

"""
    Populate file generation parameters. 
    Make sure they're updated with the contents of 
    the config YAML (if it exists).
"""
def prepare_params(file_name, template_kind, config_yaml, default_config=DEFAULT_CONFIG):
    
    # Read the config YAML, if it exists
    config = {}
    if Path(config_yaml).exists():
        with open(config_yaml, "r") as f: 
            config = yaml.safe_load(f)

    # Get the generation params from from 
    # the default config and config YAML
    params = get_params(file_name, template_kind, default_config, config)

    return params["template_path"], params["fields"]


