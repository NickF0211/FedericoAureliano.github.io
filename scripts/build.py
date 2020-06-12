import json

### Load and prepare data

with open('includes/auto_links.json') as f:
    auto_links = json.load(f)[0]

with open('includes/profile.json') as f:
    profile = json.load(f)[0]

print("Adding news:")
with open('includes/news.json') as f:
    news = json.load(f)
    news_list = ""

    for n in news[:5]:
        print(n["date"])
        item = '<div class="news-item">'
        item += '<div class="news-date">' + n["date"] + '</div>'
        item += '<div class="news-text">' + n["text"] + '</div>'
        item += '</div>\n\t\t'
        news_list += item

print("\nAdding full publications:")
with open('includes/pubs.json') as f:
    pubs = json.load(f)
    full_pubs_list = ""

    for p in pubs:
        if "full" in p["tags"]:
            print(p["title"])
            item = '<div class="paper">'
            item += '<div class="conference">' + p["conference"] + '</div>'
            item += '<div class="citation">'
            item += '<a href=\"' + p["link"] + '\">' + p["title"] + '</a> '
            item += '<nobr><small>('
            item += '<a href ="' + p["code"] + '">code</a>'
            item += ', <a href="' + p["slides"] + '">slides</a>' if p["slides"] else ""
            item += ')</small></nobr>'
            item += '<br>' + p["authors"]
            item += '</div>'
            item += '</div>\n\t\t'
            full_pubs_list += item

print("\nAdding short publications:")
with open('includes/pubs.json') as f:
    pubs = json.load(f)
    short_pubs_list = ""

    for p in pubs:
        if "short" in p["tags"]:
            print(p["title"])
            item = '<div class="paper">'
            item += '<div class="conference">' + p["conference"] + '</div>'
            item += '<div class="citation">'
            item += '<a href=\"' + p["link"] + '\">' + p["title"] + '</a> '
            item += '<nobr><small>('
            item += '<a href ="' + p["code"] + '">code</a>'
            item += ', <a href="' + p["slides"] + '">slides</a>' if p["slides"] else ""
            item += ')</small></nobr>'
            item += '<br>' + p["authors"]
            item += '</div>'
            item += '</div>\n\t\t'
            short_pubs_list += item


print("\nAdding other")
with open('includes/other.txt') as f:
    other = f.read()

### Define templates and fill them in

profile_html = """
<div class="profile">
    <div class="profile-left">
        <abbr title=\"Cartoon by Elizabeth Polgreen\">
        <img class="headshot" align="left" src="%s" onmouseover="this.src='images/cartoon.png';" onmouseout="this.src='%s';" />
        </abbr>
        %s
        <p>Here is my
            <a href="%s">CV</a>,
            <a href="%s">GitHub</a>, and
            <a href="%s">Google Scholar</a>.
        You can reach me at <a href="%s">fmora@cs.berkeley.edu</a>.
        </p>
    </div>
</div>
""" % (profile["headshot"], profile["headshot"], profile["blurb"], profile["cv"], profile["github"], profile["scholar"], profile["email"])

news_html = """
<div class="section">
    <h3>News</h3>
    <div class="hbar"> </div>
    <div id="news">
        %s
    </div>
</div>
""" % (news_list)

full_pubs_html = """
<div class="section">
    <h3>Full Publications</h3>
    <div class="hbar"> </div>
    <div id="publications">
        %s
    </div>
</div>
""" % (full_pubs_list)

short_pubs_html = """
<div class="section">
    <h3>Short Publications</h3>
    <div class="hbar"> </div>
    <div id="publications">
        %s
    </div>
</div>
""" % (short_pubs_list)

other_html = """
<div class="section">
    <h3>Other</h3>
    <div class="hbar"> </div>
    <p id="other">
        %s
    </p>
</div>
""" % (other)


### Put it all together into a coherent index.html

head_html = """
<head>
    <title>Federico Mora Rocha</title>
    <link href="https://fonts.googleapis.com/css?family=Muli" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="main.css">
    <link rel="shortcut icon" type="image/png" href="./images/favicon.png" />
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-65924431-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag('config', 'UA-65924431-1');
    </script>
</head>
"""

body_html = """
<body>
    <div class="hbar"></div>
    %s
    %s
    %s
    %s
    %s
</body>
""" % (profile_html, news_html, full_pubs_html, short_pubs_html, other_html)


index_html = """
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
%s
%s
</html>
""" % (head_html, body_html)

### Add in the auto links
print("\nAdding links:")
for name in auto_links.keys():
    if name in index_html:
        print(name)
        index_html = index_html.replace(name, "<a href=\"%s\">%s</a>" % (auto_links[name], name))

### Write it to file

with open('index.html', 'w') as index:
    index.write(index_html)
