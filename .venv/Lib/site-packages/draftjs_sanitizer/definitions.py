import re

ESCAPE_CHARS = re.compile(r"[\x00-\x1f\\\"\b\f\n\r\t<>']")

BLACKLISTED_URL_SCHEMES = ("javascript",)

ENTITIES_HAVING_URLS = {"LINK": ("value", "url", "href"), "IMAGE": ("src",)}
