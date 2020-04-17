#!/usr/bin/env python3 
import bs4 
import requests
import re
import wordcloud
import argparse

# constants
_href_re = re.compile(r"^#cite_note-.*$")
_text_re = re.compile(r"^\[update\]")
_url = "https://en.wikipedia.org/wiki/The_Beatles"
_stopwords = {"beatle", "beatles", "music", "album", "band", "albums"}


def cmd_line(f):
    """
    Parse command line arguments
    """
    def cmd_line_(*args, **kwargs):
        ap = argparse.ArgumentParser(description="Generate a Beatles wordcloud from Wikipedia.")
        ap.add_argument("-f", "--file", required=True, type=str, help="The output file to save the wordcloud.")
        ap.add_argument("-s", "--stopwords", type=str, nargs="*", help="Any additional stopwords (optional)")
        return f(ap.parse_args(), *args, **kwargs)
    return cmd_line_


def is_good_link(in_href, in_text):
    """
    Validate link text
    """
    return in_href and in_text and not _href_re.match(in_href) and not _text_re.match(in_text)


def get_text():
    """
    Retrieve link text from Beatles wikipedia page
    """
    soup = bs4.BeautifulSoup(requests.get(_url).content, features="lxml")
    links = set()
    for p in soup.findAll("p"):
        for a in p.findAll("a"):
            href = a.get("href")
            link = a.text
            if is_good_link(href, link):
                links.add(link.lower())
    return " ".join(links)


@cmd_line
def main(args):
    """
    Run program
    """
    stopwords = _stopwords|set(wordcloud.STOPWORDS)
    if args.stopwords:
        for sw in args.stopwords:
            stopwords.add(sw)
    cloud = wordcloud.WordCloud(stopwords=stopwords)
    cloud.generate(get_text())
    cloud.to_file(args.file)


if __name__ == "__main__":
    main()
