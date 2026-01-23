import xml.etree.ElementTree as ET
from sys import argv


html1999 = "{http://www.w3.org/1999/xhtml}"

section = f"{html1999}section"
div = f"{html1999}div"


def divrow() -> ET.Element:
    return ET.Element(div, {'class': 'row'})


svgfile = ET.parse(argv[1])
root = svgfile.getroot()

root.set('width', "1000px")
root.set('height', "1500px")


items_wrapper = root.find(f".//{div}[@class='items-wrapper']")


introduction = divrow()
introduction.append(items_wrapper[1].__copy__())

base_header = items_wrapper[0].__copy__()
base_header.append(introduction)

repositories = items_wrapper[2].__copy__()

header = divrow()
header.append(base_header)
header.append(repositories)


calendar = items_wrapper[3].__copy__()


languages = ET.Element(section)
languages.append(items_wrapper[7].__copy__())
languages.append(items_wrapper[8].__copy__())

habits = items_wrapper[4].__copy__()
for child in items_wrapper[5].__copy__():
    habits.append(child)
habits.append(languages)

recent_activity = items_wrapper[6].__copy__()

activity = divrow()
activity.append(habits)
activity.append(recent_activity)


for e in items_wrapper:
    e.clear()
for e in items_wrapper:
    items_wrapper.remove(e)


items_wrapper.append(header)
items_wrapper.append(calendar)
items_wrapper.append(activity)


svgfile.write('profile.svg')
