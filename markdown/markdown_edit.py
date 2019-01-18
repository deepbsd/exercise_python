import re


def parse_markdown(markdown):

    def return_paragraph(input):
        return "<p>{}</p>".format(input)

    def return_h1(input):
        return "<h1>{}</h1>".format(input)

    def return_h2(input):
        return "<h2>{}</h2>".format(input)

    def return_italics(input):
        return "<em>{}</em>".format(input)

    def return_bold(input):
        return "<strong>{}</strong>".format(input)

    def return_ol(input):
        return "<ol>{}</ol>".format(input)

    def return_ul(input):
        return "<ul>{}</ul>".format(input)

    def return_li(input):
        return "<li>{}</li>".format(input)
