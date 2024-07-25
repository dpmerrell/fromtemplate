"""
    Master script for generating files/directories
    from templates.
"""


from fromtemplate.config_util import prepare_params
from fromtemplate.generate_dir import generate_dir
from os.path import basename, dirname
from pathlib import Path


"""
    Generate a file or directory from a template.
"""
def fromtemplate(new_file_name, kind=None, config_yaml=None, verbose=True):

    new_file_name_path = Path(new_file_name)
    # Get the new file's `kind`
    file_basename = str(new_file_name_path.name)
    if kind is None:
        # Try to infer the new file's `kind` from its suffix.
        # The `suffix` is everything after the first period in the basename.
        kind = ".".join(file_basename.split(".")[1:])
        if kind == "":
            raise ValueError(f"{new_file_name} does NOT have a file suffix. You MUST provide the `--kind` argument to fromtemplate!")
    
    template_path, fields = prepare_params(file_basename, kind, config_yaml) 

    # Generate the result; note that `generate_dir` already
    # recursively checks whether its argument is a directory
    # or file, so we can call it on files as well.
    if Path(template_path).exists():
        new_parent = new_file_name_path.parent
        generate_dir(new_parent, template_path, fields, 
                     verbose=verbose,
                    )
    else:
        raise ValueError(f"Error generating {new_file_name}. No template exists for kind `{kind}`")

    return 


"""
    Command line interface for `fromtemplate`.
"""
def fromtemplate_script():
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("new_file_name", help="Name for the newly generate file (or directory).")
    parser.add_argument("--kind", default=None, help="`kind` of file (or directory) to generate.")
    parser.add_argument("--config-yaml", default=str(Path.home().joinpath(".fromtemplate","config.yaml")),
                                         help="Path to a YAML configuration file. By default, looks for one at $HOME/.fromtemplate/config.yaml.")
    parser.add_argument("--silent", default=False, action="store_true", help="Disable stdout. Default False.")

    args = parser.parse_args()
    fromtemplate(args.new_file_name,
                 kind=args.kind,
                 config_yaml=args.config_yaml,
                 verbose=(not args.silent)
                )


if __name__=="__main__":

    fromtemplate_script()


