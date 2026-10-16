"""Dependency-free checks for broken local references and accidental content mistakes."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1] / 'site'
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.stack, self.errors = set(), [], [], []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if 'id' in a:
            if a['id'] in self.ids:
                self.errors.append(f'Duplicate id: {a["id"]}')
            self.ids.add(a['id'])
        if tag == 'img' and 'alt' not in a:
            self.errors.append('Image missing alt text')
        for key in ('href', 'src'):
            if key in a:
                self.refs.append(a[key])
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f'Unbalanced closing tag: {tag}')
        else:
            self.stack.pop()

pages = {}
errors = []
for path in ROOT.rglob('*.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path.resolve()] = page
    errors.extend(f'{path.name}: {e}' for e in page.errors)
    if page.stack:
        errors.append(f'{path.name}: unclosed tags {page.stack}')
for path, page in pages.items():
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            if url.scheme not in ('https', 'mailto', 'tel'):
                errors.append(f'Unexpected URL scheme: {ref}')
            continue
        if url.path.startswith('/'):
            errors.append(f'Use relative paths for GitHub project Pages: {ref}')
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir():
            target /= 'index.html'
        if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
            errors.append(f'Missing or out-of-site asset: {ref}')
        if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'Missing anchor: {ref}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Checked {len(pages)} HTML page(s): local assets, anchors, HTML nesting, image alt text, and portable URLs passed.')
