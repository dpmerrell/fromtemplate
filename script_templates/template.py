"""
    __SCRIPT_NAME__
    __USER_NAME__ (c) __SCRIPT_YEAR__
    __USER_EMAIL__

    TODO description
"""



if __name__=="__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="TODO")
    parser.add_argument("out_file", help="")
    parser.add_argument("--option1", default=None, help="")
    parser.add_argument("--option2", nargs="+", help="") 

    args = parser.parse_args()

