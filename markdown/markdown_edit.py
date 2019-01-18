import re


def parse_markdown(markdown):

    def return_paragraph(input):
        return "<p>{}</p>".format(input)

    def return_h1(input):
        return "<h1>{}</h1>".format(input)

    def return_h2(input):
        return "<h2>{}</h2>".format(input)
    
    def return_h6(input):
        return "<h6>{}</h6>".format(input)

    def return_italic(input):
        return "<em>{}</em>".format(input)

    def return_bold(input):
        return "<strong>{}</strong>".format(input)

    def return_open_ul(input):
        return "<ul>{}".format(input)
    
    def return_close(input):
        return "{}</ul>".format(input)

    def return_li(input):
        return "<li>{}</li>".format(input)
    
    lines = markdown.split("\n")

    result = ""

    for line in lines:
        h1_match = re.match('# (.*)',line)
        h2_match = re.match('## (.*)',line)
        h6_match = re.match('###### (.*)',line)
        bold_match = re.match('(.*)__(.*)__(.*)',line)
        italic_match = re.match('(.*)_(.*)_(.*)',line)
        li_match = re.match(r'\* (.*)',line)
        par_match = re.match('<h|<ul|<p|<li',line)

        if h1_match:
            line = return_h1(h1_match.group(1))

        if h2_match:
            line = return_h2(h2_match.group(1))

        if h6_match:
            line = return_h6(h6_match.group(1))

        if bold_match:
            line = "{}{}{}".format(bold_match.group(1),return_bold(bold_match.group(2)),bold_match.group(3))

        if italic_match:
            line = "{}{}{}".format(italic_match.group(1),return_italic(italic_match.group(2)),italic_match.group(3))

        if  re.match(r'\* (.*)', line):
            line = "{}".format(return_li(line))

        if not par_match:
            line = "{}".format(return_paragraph(line))

        result += line

    return result

