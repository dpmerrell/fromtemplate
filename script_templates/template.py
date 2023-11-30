"""
    __SCRIPT_NAME__
    David Merrell (c) __SCRIPT_YEAR__

    TODO description
"""



if __name__=="__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="TODO")
    parser.add_argument("--option", default=None, help="")
    parser.add_argument("--ls_option", nargs="+", help="") 
    parser.add_argument("out_file", help="")

    args = parser.parse_args()

