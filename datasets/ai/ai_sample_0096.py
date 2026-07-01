def parse_xml(text):
    tag_objects = []

    root = ET.fromstring(text)
    for child in root:
        tag = Tag(child.attrib["id"])
        for subchild in child:
            tag.add_value(subchild.attrib["value"])
        tag_objects.append(tag)

    return tag_objects

class Tag:
    def __init__(self, tag_id):
        self.tag_id = tag_id
        self.values = []
    
    def add_value(self, value):
        self.values.append(value)