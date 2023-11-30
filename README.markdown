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
 
