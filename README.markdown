# fromtemplate

A python package and command line tool that helps you quickly generate 
files and directories from templates.

# Installation and usage

Install via pip:
```
$ pip install git+ssh://git@github.com/dpmerrell/fromtemplate
```

After installation, you will have the `fromtemplate` command line tool:
```
$ fromtemplate my_new_script.py
$ ls
my_new_script.py
```

The command line tool infers the *kind* of file from the file suffix.

Alternatively, you can specify the *kind* of file with the `--kind` flag:
```
$ fromtemplate my_new_package --kind python_package
$ ls
my_new_package
```
In this example, we just created a new python package called `my_new_package`.

# Extending for new file types; customizing templates

As of this writing, `fromtemplate` only comes with: 
* a template python file;
* a template python package.

Find them in the `fromtemplate/default_templates` directory in this repository.

The `fromtemplate` tool is highly extensible, though. You can create a YAML file at the following location:
```
$HOME/.fromtemplate/config.yaml
```
that specifies (i) how to fill in the fields of template files; and (ii) the locations of template files for new file types.

The `example_config.yaml` illustrates what `config.yaml` ought to look like.

For example, for template R scripts you could create a template file `$HOME/.fromtemplate/template.R` and then add a new entry to your `config.yaml`:
```
templates:
    R: "/PATH/TO/YOUR/HOME/.fromtemplate/template.R"
``` 

Then, if you run 
```
$ fromtemplate new_script.R
```
the `fromtemplate` command line tool will know what to do.


