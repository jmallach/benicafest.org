#!/usr/bin/env python3
"""Simple static site generator for benicafest.org."""

import shutil
import tomllib
from datetime import datetime
from pathlib import Path

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / "content"
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
DIST_DIR = ROOT / "dist"


def load_config():
    with open(ROOT / "site.toml", "rb") as f:
        cfg = tomllib.load(f)
    site = cfg.get("params", {})
    site["baseURL"] = cfg.get("baseURL", "/")
    return site


def load_artists():
    artists = []
    for path in sorted((CONTENT_DIR / "lineup").glob("*.md")):
        post = frontmatter.load(path)
        artist = dict(post.metadata)
        artist["content"] = markdown.markdown(post.content)
        # Normalise: drop empty string social links so {% if %} works cleanly
        for key, val in list(artist.items()):
            if val == "" or val is None:
                artist[key] = None
        artists.append(artist)
    return sorted(artists, key=lambda a: a.get("order", 99))


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()

    site = load_config()
    artists = load_artists()
    base_url = site["baseURL"].rstrip("/") + "/"

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,  # content is trusted; autoescape would mangle Markdown HTML
    )

    ctx = {
        "site": site,
        "artists": artists,
        "base_url": base_url,
        "now_year": datetime.now().year,
        "is_home": True,
        "permalink": base_url,
        "page_title": "",
    }

    # Render index.html
    tmpl = env.get_template("index.html")
    (DIST_DIR / "index.html").write_text(
        tmpl.render(**ctx),
        encoding="utf-8",
    )

    # Copy static/ assets verbatim (CSS, JS, images, favicons, 404.html, CNAME…)
    for item in STATIC_DIR.iterdir():
        dst = DIST_DIR / item.name
        if item.is_dir():
            shutil.copytree(item, dst)
        else:
            shutil.copy2(item, dst)

    # robots.txt
    (DIST_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {base_url}sitemap.xml\n",
        encoding="utf-8",
    )

    # sitemap.xml
    (DIST_DIR / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        "  <url>\n"
        f"    <loc>{base_url}</loc>\n"
        "    <changefreq>weekly</changefreq>\n"
        "    <priority>1.0</priority>\n"
        "  </url>\n"
        "</urlset>\n",
        encoding="utf-8",
    )

    print(f"✓ Built {1 + len(list(STATIC_DIR.rglob('*')))} files → {DIST_DIR}/")


if __name__ == "__main__":
    build()
