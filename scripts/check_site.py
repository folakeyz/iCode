"""Validate the static site's structure and local navigation without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.stack, self.errors = set(), [], [], []
        self.headings = self.mains = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append('duplicate ID: ' + attrs['id'])
            self.ids.add(attrs['id'])
        self.headings += tag == 'h1'
        self.mains += tag == 'main'
        if tag in ('a', 'link'):
            self.links.append(attrs.get('href', ''))
        if tag not in VOID:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append('unbalanced closing tag: ' + tag)
        else:
            self.stack.pop()

pages = {}
for path in ROOT.glob('*.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path.name] = page
errors = []
for name, page in pages.items():
    errors.extend(f'{name}: {error}' for error in page.errors)
    if page.stack or page.headings != 1 or page.mains != 1:
        errors.append(f'{name}: invalid document structure {page.stack}')
    for href in page.links:
        url = urlsplit(href)
        if url.scheme or url.netloc:
            continue
        target = unquote(url.path) or name
        if not (ROOT / target).is_file():
            errors.append(f'{name}: missing file {target}')
        if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{name}: missing anchor {href}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'{len(pages)} pages passed structure, local link and anchor checks.')
