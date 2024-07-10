import json
import sys
import re


def iterator(chapter):
    for sub in chapter.get('sub_items', []):
        iterator(sub.get('Chapter', None))

    content = chapter.get('content','')

    pattern = "\{\{customization:\s*" + customization + "\}\}([\s\S]*)\{\{\/customization\}\}"
    replacement = r"\1"
    new_content = re.sub(pattern, replacement, content)

    pattern = "\{\{customization:\s*\S*\}\}[\s\S]*\{\{\/customization\}\}"
    replacement = ""
    new_content = re.sub(pattern, replacement, content)

    chapter['content'] = new_content


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports':      
            sys.exit(0)

context, book = json.load(sys.stdin)

customization = context['config']['preprocessor']['customization']['name']

for section in book['sections']:
    if 'Chapter' in section:
        chapter = section['Chapter']

        iterator(chapter)

print(json.dumps(book))
