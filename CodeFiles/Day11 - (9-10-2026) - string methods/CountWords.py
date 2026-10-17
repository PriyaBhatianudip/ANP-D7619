ob = {"id":101, "name":"kk", "age":22, "salary":73000}

print(ob)
print(ob.get("name"))
ob["city"]="Delhi"
ob["name"]="varun"

print(ob)

str = "This is a repeated string again and again "
var = {}
for i in str.split():  # i=This
  var[i]=var.get(i,0)+1  # var[This] = var.get("This", 0)
print(var)

sentence = "Python programming is fun!"
newstr = sentence.split(maxsplit=1)

print(newstr)

s1 = input("Enter a string to search: ")
print(f"String found : {sentence.find(s1)}")
if sentence.find(s1) >= 0:
  print(f"{s1} found in {sentence}")
else:
  print(f"{s1} not in {sentence}")

# find function returns the index of the
# substring if it is found, otherwise it returns -1
