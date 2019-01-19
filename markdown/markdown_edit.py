import re


def parse_markdown(markdown):

    result = ""
    list_items = ""

    for line in markdown.split("\n"):
        line = re.sub(r'__(.*?)__',r'<strong>\1</strong>',line)
        line = re.sub(r'_(.*?)_',r'<em>\1</em>',line)

        hdr_match = re.match(r'(#+) (.*)', line)
        if hdr_match: line = "<h{0}>{1}</h{0}>".format(len(hdr_match.group(1)), hdr_match.group(2))

        li_match = re.match('^* (.*)',line)
        if li_match: 
            line = "<li>"+li_match.group(1)+"</li>"
            list_items += line

        #h1_match = re.match('# (.*)',line)
        #h2_match = re.match('## (.*)',line)
        #h6_match = re.match('###### (.*)',line)
        #bold_match = re.match('(.*)__(.*)__(.*)',line)
        #italic_match = re.match('(.*)_(.*)_(.*)',line)
        #li_match = re.match(r'\* (.*)',line)
        #par_match = re.match('<h|<ul|<p|<li',line)

        #if h1_match:
        #    line = return_h1(h1_match.group(1))

        #if h2_match:
        #    line = return_h2(h2_match.group(1))

        #if h6_match:
        #    line = return_h6(h6_match.group(1))

        #if bold_match:
        #    line = "{}{}{}".format(bold_match.group(1),return_bold(bold_match.group(2)),bold_match.group(3))

        #if italic_match:
        #    line = "{}{}{}".format(italic_match.group(1),return_italic(italic_match.group(2)),italic_match.group(3))

        #if  re.match(r'\* (.*)', line):
        #    line = "{}".format(return_li(line))

        #if not par_match:
        #    line = "{}".format(return_paragraph(line))


        #list_items = "<ul>"+list_items+"</ul>"

        p_unmatch = re.match('<h|<ul|<p|<li',line)
        if not p_unmatch: line = "<p>"+line+"</p>"

        result += line

    return result

