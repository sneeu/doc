import os
import sys

import markdown
import typogrify


HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
<title>%s</title>
<style type="text/css" media="screen,projection">
*{font-size:1em;font-style:inherit;font-weight:inherit;margin:0;padding:0}
body{background:#fff;color:#222;font:100%%/1.5 "Helvetica Neue",Arial,Helvetica,sans-serif;margin:0;padding:3em}
a{border-bottom:1px solid;color:#00c;font-weight:inherit;padding-bottom:1px;text-decoration:none}
strong{font-weight:bold}
em{font-style:italic}
code{background:#ddd;font:100%%/0 Monaco,monospace}
h1{font-size:2em;font-weight:bold;line-height:1.5em;padding:0 0 0.75em}
h2{font-size:1.5em;font-weight:bold;line-height:2em}
h3{font-size:1.2em;font-weight:bold;line-height:1.25em;padding:0.625em 0}
p,ul,ol,.address{padding:0 0 1.5em}
ul,ol{padding-left:1.5em}
pre{background:#ddd;border:1px solid #bbb;font:100%%/1.5 Monaco,monospace;margin:-2px -1px 1.5em;padding:1.5em}
.address span{display:block}
p .caps,li .caps{font-variant:small-caps;text-transform:lowercase}
</style>
<style type="text/css" media="print">
*{font-size:1em;font-style:inherit;font-weight:inherit;margin:0;padding:0}
body{background:#fff;color:#222;font:100%%/1.5 "Helvetica Neue",Arial,Helvetica,sans-serif;padding:3em}
a{color:inherit;font-weight:inherit;text-decoration:none}
a:not([href^=mailto]):after{content: " (" attr(href) ")"}
.nolink a:after{content:""}
strong{font-weight:bold}
em{font-style:italic}
code{background:#ddd;font:100%%/0 Monaco,monospace}
h1{font-size:2em;font-weight:bold;line-height:1.5em;padding:0 0 0.75em;page-break-after:avoid}
h2{font-size:1.5em;font-weight:bold;line-height:2em;page-break-after:avoid}
h3{font-size:1.2em;font-weight:bold;line-height:1.25em;padding:0.625em 0;page-break-after:avoid}
p,ul,ol,.address{padding:0 0 1.5em}
ul,ol{padding-left:1.5em}
pre{background:#ddd;border:1px solid #bbb;font:100%%/1.5 Monaco,monospace;margin:-2px -1px 1.5em;padding:1.5em}
.address span{display:block}
p .caps,li .caps{font-variant:small-caps;text-transform:lowercase}
</style>
</head>
<body>"""
FOOTER = """</body></html>"""


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
        in_file = open(filename, 'r')
        md = in_file.read()
        in_file.close()

        title = os.path.basename(filename)
        content = typogrify.typogrify(
            markdown.markdown(md, ['abbr', 'headerid']))

        out_file = open(filename + '.html', 'w')
        out_file.write((HEADER % title) + content + FOOTER)
        out_file.close()
    else:
        print u'Filename not supplied.'
