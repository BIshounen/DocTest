import json
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports':
            sys.stdout.write("test\n")
            sys.stdout.write(sys.argv[2] + "\n")
            sys.stdout.wite(sys.argv[3] + "\n")
            
            sys.exit(0)

context, book = json.load(sys.stdin)

book['sections'][0]['Chapter']['content'] = '# Hello'

print(json.dumps(book))
