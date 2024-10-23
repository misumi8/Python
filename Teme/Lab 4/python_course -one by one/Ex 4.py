# 4 ------------------------------------------------

def buildXmlElement(tag, content, **keyValueElements):
    xmlElement = "<" + tag
    for name, value in keyValueElements.items():
        xmlElement += " " + name + "=\"" + value + "\""
    xmlElement += ">" + content + "</" + tag + ">"
    return xmlElement

# print(buildXmlElement("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
