import json
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports':
            print(sys.argv[2])
            return 1