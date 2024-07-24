from lxml import etree

tree = etree.parse("src/web_page.html")
# print(tree)
# print(etree.tostring(tree))

# title_element = tree.find("head/title")
# print(title_element.text)
#
# p_element = tree.find("body/p")
# print(p_element.text)
#
# list_items = tree.findall("body/ul/li")
# # print(list_items)
# for li in list_items:
#     print(li.text)

# for li in list_items:
#     a = li.find("a")
#     if a is not None:
#         print(f"{li.text.strip()} {a.text}")
#     else:
#         print(li.text)

# title_element = tree.xpath("//title")[0]
# print(title_element.text)
#
# title_element = tree.xpath("//title/text()")[0]
# print(title_element)
#
# title_element = tree.xpath("//p/text()")[0]
# print(title_element)

# list_items = tree.xpath("//li")
# for li in list_items:
#     print(etree.tostring(li))

# list_items = tree.xpath("//li")
# for li in list_items:
#     text = ''.join(map(str.strip, li.xpath(".//text()")))
#     print(text)


# list_items = tree.xpath("//ul/descendant::li")  # потомки элемента ul
#
# for li in list_items:
#     text = ''.join(map(str.strip, li.xpath(".//text()")))
#     print(text)


html = tree.getroot()
# title_element = html.cssselect("title")[0]
# print(title_element.text)

p_element = html.cssselect("p")[0]
print(p_element.text)

list_items = html.cssselect("li")
for li in list_items:
    a = li.cssselect("a")
    if len(a) == 0:
        print(li.text)
    else:
        print(f"{li.text.strip()} {a[0].text}")
