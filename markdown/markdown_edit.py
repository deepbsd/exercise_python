import re


def parse_markdown(markdown):

    result = ""
    list_items = []

    def build_ul(list):
        return "".join(list)

    for line in markdown.split("\n"):
        line = re.sub(r'__(.*?)__',r'<strong>\1</strong>',line)
        line = re.sub(r'_(.*?)_',r'<em>\1</em>',line)

        hdr_match = re.match(r'(#+) (.*)', line)
        if hdr_match: line = "<h{0}>{1}</h{0}>".format(len(hdr_match.group(1)), hdr_match.group(2))

        li_match = re.match('^\* (.*)',line)
        if li_match: 
            item = "<li>"+li_match.group(1)+"</li>"
            if list_items and list_items[0] != "<ul>": list_items.insert(0, "<ul>")
            if list_items and list_items[-1] == "</ul>":  list_items.pop()
            list_items.append(item)
            if list_items[-1] != "</ul>": list_items.append("</ul>")

        
        p_unmatch = re.match('<h|<ul|<p|<li',line)
        if not p_unmatch: line = "<p>"+line+"</p>"

        result += line

    if list_items: result = build_ul(list_items)

    return result

