"""
    __FILE_NAME__.py
    (c) __USER_NAME__ __FILE_YEAR__
    __USER_EMAIL__

    TODO description
"""

import argparse



def __FILE_NAME___script():

    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", help="TODO")
    parser.add_argument("out_file", help="")
    parser.add_argument("--option1", default=None, help="")
    parser.add_argument("--option2", nargs="+", help="") 

    args = parser.parse_args()



if __name__=="__main__":

    __FILE_NAME___script()


