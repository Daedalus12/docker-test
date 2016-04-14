import argparse

def arrow(arg1, arg2):
    return arg1 + " ----> " + arg2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Join two strings.')
    parser.add_argument('string1', type=str, help='The first string')
    parser.add_argument('string2', type=str, help='The second string')

    args = parser.parse_args()

    print arrow(args.string1, args.string2)
