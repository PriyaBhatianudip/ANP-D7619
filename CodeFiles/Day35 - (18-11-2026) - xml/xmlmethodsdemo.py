import xml.etree.ElementTree as et


# to create the root in xml
root = et.Element("Employees")

# to get the sub element:-
#  it will create another child element in the xml file
employee = et.SubElement(root, "Employee")
# <Employees>
# <Employee></Employee>
# </Employees>

# to add tags with data
et.SubElement(employee, "Employee_Code").text = "101"
et.SubElement(employee, "Employee_Name").text = "AA"
et.SubElement(employee, "Age").text = "27"
et.SubElement(employee, "Salary").text = "77000"

# create the tree for xml
tree = et.ElementTree(root)

# to format the xml
et.indent(tree, space='    ')

# save xml file
tree.write("Employees.xml", encoding="utf-8",
           xml_declaration=True)

print("xml file created successfully!!")