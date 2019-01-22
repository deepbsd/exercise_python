import re


def parse_markdown(markdown):

    result = ""
    hdr_line = ""
    list_items = []
    include_hdr = False

    def build_ul(list):
        return "".join(list)

    for line in markdown.split("\n"):
        line = re.sub(r'__(.*?)__',r'<strong>\1</strong>',line)
        line = re.sub(r'_(.*?)_',r'<em>\1</em>',line)

        hdr_match = re.match(r'(#+) (.*)', line)
        if hdr_match: 
            line = "<h{0}>{1}</h{0}>".format(len(hdr_match.group(1)), hdr_match.group(2))
            hdr_line = line
        if hdr_match: include_hdr = True

        li_match = re.match('^\* (.*)',line)
        if li_match: 
            item = "<li>"+li_match.group(1)+"</li>"
            if list_items and list_items[0] != "<ul>": list_items.insert(0, "<ul>")
            if list_items and list_items[-1] == "</ul>":  list_items.pop()
            list_items.append(item)
            if list_items[-1] != "</ul>": list_items.append("</ul>")

        p_unmatch = re.match('<h|<ul|<p|<li|\*',line)
        if not p_unmatch: line = "<p>"+line+"</p>"

        result += line

    if include_hdr and list_items: 
        list_items.insert(0,hdr_line)
        result = build_ul(list_items)
    if list_items and not include_hdr: result = build_ul(list_items)
    

    return result

