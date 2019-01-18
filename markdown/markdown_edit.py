import re


def parse_markdown(markdown):

    result = ""

    for line in markdown.split("\n"):
        line = re.sub(r'__(.*?)__',r'<strong>\1</strong>',line)
        line = re.sub(r'_(.*?)_',r'<em>\1</em>',line)

        head_match = re.match('(#+) (.*)',line)
        hdr_level = len(head_match.group(1))

        if head_match:
            line = "<h{0}>{1}</h{0}>".format(hdr_level,head_match.group(2))

        

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

        result += line

    return result

