import re

def is_link_valid(link, perm_link='youtube'):
    links = re.findall(r'\w*[.].+?[ ]*', link)
    for j in links:
        if perm_link not in j:
            return False
    return True