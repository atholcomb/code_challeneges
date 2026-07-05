#!/usr/bin/python3
# written by: atholcomb
# imgur_parser.py

def imgurUrlParser(link):
    original_link = link    

    formats = [".png", ".jpg", ".gif"]
    for f in formats:
        if f in link:
            pos_in_format = link.index(f)
            link = link[:pos_in_format]

    if '/a/' in link:
        a_slash = link.index('/a/')
        return f'(id: "{link[a_slash+3:]}", type: "album")' + ' -> ' + link
    elif "gallery" in link:
        gal = link.index('gallery')
        return f'(id: "{link[gal+8:]}", type: "gallery")' + ' -> ' + link
    elif 'i.imgur' in link:
        image = link.index('i.imgur')
        return f'(id: "{link[image+12:]}", type: "image")' + ' -> ' + original_link
    else:
        return f'(id: "{link[17:]}", type: "image")' + ' -> ' + link


print(imgurUrlParser("http://imgur.com/a/cjh4E"))
print(imgurUrlParser("http://imgur.com/gallery/59npG"))
print(imgurUrlParser("http://imgur.com/OzZUNMM"))
print(imgurUrlParser("http://i.imgur.com/altd8Ld.png"))
print(imgurUrlParser("http://i.imgur.com/x0kAx1.jpg"))
print(imgurUrlParser("http://i.imgur.com/lOpNjuD.gif"))
