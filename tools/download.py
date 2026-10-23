"""
Polite downloader: python tools/download.py urls.txt

urls.txt: one URL per line (lines starting with # are skipped).
Saves files to data/raw/ and logs every file to data/manifest.csv.
"""

import csv
import hashlib
import os
import sys
import time
from datetime import date
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests


RAW = "data/raw"
MANIFEST = "data/manifest.csv"

HEADERS = {
    "User-Agent": (
        "ExamateStudentProject/1.0 "
        "(learning project; contact: your-email@example.com)"
    )
}

DELAY = 2  # Seconds between requests: be polite to government servers

robots = {}


def allowed(url):
    root = "{0.scheme}://{0.netloc}".format(urlparse(url))

    if root not in robots:
        rp = RobotFileParser(root + "/robots.txt")

        try:
            rp.read()
        except Exception:
            rp = None  # robots.txt unreachable: proceed carefully

        robots[root] = rp

    rp = robots[root]

    return rp is None or rp.can_fetch(HEADERS["User-Agent"], url)


def name_for(url):
    name = os.path.basename(urlparse(url).path) or "index.html"

    return name.replace(" ", "_")