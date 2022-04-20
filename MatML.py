import xml.etree.ElementTree as ET

tree = ET.parse('MatML3e1.xml')
root = tree.getroot()
                
def printName(element):
    line_new = '{:<25}  {:>25}'.format('> Name', element.text)
    print(line_new)
    
def printClass(element):
    for name_data in element.iterfind('Name'):
        line_new = '{:<25}  {:>25}'.format('> Class', name_data.text)
        print(line_new)
        
def printSubClass(element):
    for name_data in element.iterfind('Name'):
        line_new = '{:<25}  {:>25}'.format('> Subclass', name_data.text)
        print(line_new)
        
def printPropertyData(element):
    print(element.attrib)
        
def void(element):
    print(element.tag)

dicti = {'Name': printName,
         'Class': printClass,
         'Subclass': printSubClass,
         'Specification': void,
         'Source': void,
         'Form': void,
         'ProcessingDetails': void,
         'Characterization': void,
         'PropertyData': printPropertyData,
         'Notes': void}

for material in root.iterfind('Material'):
    for bulkDetails in material:
        for bulkData in bulkDetails.iterfind('*'):
            dicti[bulkData.tag](bulkData)

