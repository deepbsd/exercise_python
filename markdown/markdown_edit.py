import re


def parse_markdown(markdown):

    result = ""
    list_items = []

    for line in markdown.split("\n"):
        line = re.sub(r'__(.*?)__',r'<strong>\1</strong>',line)
        line = re.sub(r'_(.*?)_',r'<em>\1</em>',line)

        hdr_match = re.match(r'(#+) (.*)', line)
        if hdr_match: line = "<h{0}>{1}</h{0}>".format(len(hdr_match.group(1)), hdr_match.group(2))

        li_match = re.match('^\* (.*)',line)
        if li_match: 
            line = "<li>"+li_match.group(1)+"</li>"
            if list_items and list_items[-1] == "</ul>":  list_items.pop()
            list_items.append(line)
            list_items.append("</ul>")
            print("just after 1st append: ",list_items)

        if list_items:
            if list_items[0] != "<ul>":  list_items.insert(0, "<ul>")
            else: continue
            if list_items[-1] != "</ul>":  list_items.append("</ul>")
            print("just after 2nd append: ",list_items)

        
        if list_items: line += "".join(list_items)
        print("after join--list_items: ",list_items)
        print("after join--line: ",line)
        

        p_unmatch = re.match('<h|<ul|<p|<li',line)
        if not p_unmatch: line = "<p>"+line+"</p>"

        result += line

    return result

