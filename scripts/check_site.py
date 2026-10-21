#!/usr/bin/env python3
"""Check a Hugo build without network access or third-party packages."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


POST_PATH = "posts/2022/06/法罗群岛/"
REQUIRED_FILES = (
    "index.html",
    "about/index.html",
    "posts/index.html",
    "tags/index.html",
    POST_PATH + "index.html",
    "cv/Resume.pdf",
    "images/Profile.jpg",
    "CNAME",
    "index.xml",
    "posts/index.xml",
    "sitemap.xml",
)
CSS_URL = re.compile(r"url\(\s*(?:\"([^\"]*)\"|'([^']*)'|([^)]*?))\s*\)", re.I)


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name in ("href", "src"):
            if attrs.get(name):
                self.references.append(attrs[name])
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical = attrs.get("href")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            match = re.search(r";\s*url\s*=\s*(.*)", attrs.get("content", ""), re.I)
            if match:
                self.references.append(match.group(1).strip(" \"'"))


def read_html(path):
    parser = HTMLLinks()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def check_site(root):
    errors = []
    for name in REQUIRED_FILES:
        path = root / name
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty file: {name}")
    if not (root / "index.html").is_file():
        return errors

    base_url = read_html(root / "index.html").canonical
    if (not base_url or urlsplit(base_url).scheme not in ("http", "https")
            or not urlsplit(base_url).netloc):
        errors.append("The homepage needs an absolute HTTP(S) canonical URL.")
        return errors
    base = urlsplit(base_url)
    base_path = unquote(base.path).rstrip("/") + "/"
    base_url = base_url.rstrip("/") + "/"

    def page_url(path):
        relative = path.relative_to(root).as_posix()
        if relative.endswith("index.html"):
            relative = relative[:-len("index.html")]
        return urljoin(base_url, relative)

    def local_path(reference, source):
        if not reference or reference.startswith("#"):
            return None
        target = urlsplit(urljoin(page_url(source), reference))
        if target.scheme not in ("http", "https") or target.netloc != base.netloc:
            return None
        path = unquote(target.path)
        if path == base_path.rstrip("/"):
            path += "/"
        if not path.startswith(base_path):
            errors.append(f"{source.relative_to(root)}: URL is outside the site: {reference}")
            return None
        return root / path[len(base_path):]

    def check_reference(reference, source):
        target = local_path(reference, source)
        if target is None:
            return
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file():
            errors.append(f"{source.relative_to(root)}: Missing local target: {reference}")

    html_files = sorted(root.rglob("*.html"))
    for path in html_files:
        for reference in read_html(path).references:
            check_reference(reference, path)

    css_files = sorted(root.rglob("*.css"))
    if not css_files:
        errors.append("The build contains no CSS files.")
    for path in css_files:
        for match in CSS_URL.finditer(path.read_text(encoding="utf-8")):
            check_reference(next(value for value in match.groups() if value is not None), path)

    xml_files = sorted(root.rglob("*.xml"))
    for path in xml_files:
        try:
            document = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{path.relative_to(root)}: Invalid XML: {exc}")
            continue
        kind = document.tag.rsplit("}", 1)[-1]
        expected_kind = {"index.xml": "rss", "posts/index.xml": "rss",
                         "sitemap.xml": "urlset"}.get(path.relative_to(root).as_posix())
        if expected_kind and kind != expected_kind:
            errors.append(f"{path.relative_to(root)}: Expected {expected_kind}, found {kind}.")
        if kind == "rss":
            for element in document.findall("./channel/item/link"):
                check_reference(element.text or "", path)
            if path == root / "posts/index.xml":
                links = [local_path(item.text or "", path)
                         for item in document.findall("./channel/item/link")]
                if root / POST_PATH not in links:
                    errors.append("posts/index.xml: The existing Chinese post is missing.")
        elif kind in ("urlset", "sitemapindex"):
            for element in document.iter():
                if element.tag.rsplit("}", 1)[-1] == "loc":
                    check_reference(element.text or "", path)

    cname = root / "CNAME"
    if cname.is_file() and cname.read_text(encoding="utf-8").strip() != "psyduck.wang":
        errors.append("CNAME must preserve the domain psyduck.wang.")
    if not errors:
        print(f"Site check passed: {len(html_files)} HTML, {len(css_files)} CSS, "
              f"and {len(xml_files)} XML files.")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Hugo output directory, such as public")
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error(f"Output directory does not exist: {args.directory}")
    errors = check_site(args.directory.resolve())
    for error in sorted(set(errors)):
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
