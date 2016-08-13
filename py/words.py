#!/usr/bin/env python3
"""Retrieve and print words from a URL.
Usage:
    
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a url
    Args:
        url:The URL of a UTF-8 text document
    Returns:
        A list of strings containing the words from
        the document. 
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.
    Args:
        An iterable series of printable items
    """
    for word in items:
        print(word)


def main(url):
    """Print items one per line.
    Args:
        An iterable series of printable items
    """
    words = fetch_words(url)
    print_items(words)


""" NOTE:
    module scope code - all top level code are run on import
    any .py file constitutes a python module... convinient import with api. 
    scripts are usually written for convinient import and execution.
    programs are  composed of modules
"""  
if __name__ == '__main__':
    main(sys.argv[1])
    

        