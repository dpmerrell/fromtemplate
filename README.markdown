# script_templates

A python package and command line tool that helps you quickly generate 
scripts from templates.

Quickly write a lot of scripts without filling in boilerplate!


# Installation and usage

Install via pip:
```
$ pip install git+ssh://git@github.com/dpmerrell/script_templates
```

After installation, you will have the `template_script` command line tool:
```
$ template_script my_new_script.py
$ ls
my_new_script.py
```

The command line tool infers the *kind* of script from the file suffix.


# Extending for new file types; customizing templates

As of this writing, `script_templates` only comes with a template python file.

However, the tool is highly extensible. You can create a YAML file at the following location:
```
$HOME/.script_templates/config.yaml
```
that specifies (i) how to fill in the fields of template files; and (ii) the locations of template files for new file types.

The `example_config.yaml` illustrates what `config.yaml` ought to look like.

For example, for template R scripts you could create a template file `$HOME/.script_templates/template.R` and then add a new entry to your `config.yaml`:
```
templates:
    R: "/PATH/TO/YOUR/HOME/.script_templates/template.R"
``` 

Then, if you run 
```
$ template_script new_script.R
```
the `template_script` command line tool will know what to do.


