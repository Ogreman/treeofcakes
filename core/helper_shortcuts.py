import re

from .constants import REMOVE_LIST

def short_slugify(inStr):
    aslug = inStr.lower()
    for a in REMOVE_LIST:
        aslug = re.sub(r'\b'+a+r'\b',' ',aslug)
    aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
    aslug = re.sub('\s+', '-', aslug)
    return aslug