import json
import sys
import re


def iterator(chapter):
    for sub in chapter.get('sub_items', []):
        iterator(sub.get('Chapter', None))

    content = chapter.get('content','')

    pattern = "\{\{children\}\}"
    replacement = ""

    for sub in chapter.get('sub_items', []):
        if "Chapter" in sub:
            path = sub['Chapter'].get('path', '')
            path = re.sub(" ", "%20", path)
            replacement += "- [" + sub['Chapter'].get("name", 'Untitled') + "](./" + path + ")" +  "\n"

    new_content = re.sub(pattern, replacement, content)


    chapter['content'] = new_content


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'supports':
            sys.exit(0)

context, book = json.load(sys.stdin)

for section in book['sections']:
    if 'Chapter' in section:
        chapter = section['Chapter']

        iterator(chapter)

# book['sections'][0]['Chapter']['content'] = str(book)

print(json.dumps(book))
