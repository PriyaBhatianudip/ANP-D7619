import xml.etree.ElementTree as et

tree = et.parse("Students.xml")
print("tree : ",tree)
root = tree.getroot()
print("root : ",root)
# ob = root.findall("Student")
#
# print(ob)
for st in root.findall("Student"):
    print(f"Roll Number : {st.find("rollno").text}")
    print(f"Name : {st.find("name").text}")
    print(f"Age : {st.find("age").text}")
    print(f"Course : {st.find("course").text}")
    print(f"Marks : {st.find("marks").text}")