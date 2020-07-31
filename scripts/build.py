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

    item = '<div class="news-item">'
    item += '<div class="news-date">' + " " + '</div>'
    item += '<div class="news-text">' + "<a href=\"./news.html\">See news from " + news[-1]["date"] + " to " + news[0]["date"] + '</a></div>'
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
            item += '<a href=\"' + p["link"] + '\">' + p["title"] + '</a> ' if p["link"] else p["title"]
            item += '<nobr><small>(' if p["code"] or p["slides"] else ""
            item += '<a href ="' + p["code"] + '">code</a>' if p["code"] else ""
            item += '<a href="' + p["slides"] + '">slides</a>' if p["slides"] else ""
            item += ')</small></nobr>' if p["code"] or p["slides"] else ""
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

### Define templates and fill them in

profile_html = """
<div class="profile">
    <div class="profile-left">
        <img class="headshot" align="left" src="%s" />
        </abbr>
        %s
        <p>Here is my
            <a href="%s">CV</a>.
        You can reach me at <a href="%s">fengnick@cs.toronto.edu</a>.
        </p>
    </div>
</div>
""" % (profile["headshot"], profile["blurb"], profile["cv"], profile["email"])

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
    <h3>Conference Research Papers</h3>
    <div class="hbar"> </div>
    <div id="publications">
        %s
    </div>
</div>
""" % (full_pubs_list)

short_pubs_html = """
<div class="section">
    <h3>Workshop and Short Papers</h3>
    <div class="hbar"> </div>
    <div id="publications">
        %s TBA
    </div>
</div>
""" % (short_pubs_list)


### Put it all together into a coherent index.html

head_html = """
<head>
    <title>Nick Feng</title>
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
</body>
""" % (profile_html, news_html, full_pubs_html, short_pubs_html)


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

########### News website
with open('includes/news.json') as f:
    news = json.load(f)
    news_list = ""

    for n in news:
        print(n["date"])
        item = '<div class="news-item">'
        item += '<div class="news-date">' + n["date"] + '</div>'
        item += '<div class="news-text">' + n["text"] + '</div>'
        item += '</div>\n\t\t'
        news_list += item

news_section_html = """
<div class="section">
    <h3>News</h3>
    <div class="hbar"> </div>
    <div id="news">
        %s
    </div>
</div>
""" % (news_list)

body_html = """
<body>
    %s
</body>
""" % (news_section_html)

news_html = """
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
    if name in news_html:
        print(name)
        news_html = news_html.replace(name, "<a href=\"%s\">%s</a>" % (auto_links[name], name))

### Write it to file

with open('news.html', 'w') as index:
    index.write(news_html)