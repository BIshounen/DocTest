import json
import sys
import re


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports':      
            sys.exit(0)

context, book = json.load(sys.stdin)

customization = context['config']['preprocessor']['customization']['name']

for section in book['sections']:
    content = section['Chapter']['content']

    pattern = "\{\{customization:\s*" + customization + "\}\}([\s\S]*)\{\{\/customization\}\}"
    replacement = r"\1"
    new_content = re.sub(pattern, replacement, content)

    section['Chapter']['content'] = new_content
    

# book['sections'][0]['Chapter']['content'] = str(book['sections'][0])

print(json.dumps(book))
