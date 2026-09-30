# Features list
CAMERA =1
LOCATION = 2
BLUETOOTH = 4
NFC = 8

features =  int(input("Enter features value : "))  #3

# check if the bluetooth is on or not
if features & BLUETOOTH:  #  3(0011) & 4(0100)
    #   0100
    #   0011
    # & 0000
    print("Bluetooth is already on!!")
else:
    features = features | BLUETOOTH   #   features = 0011(3)  | 0100(4)
    # 0011
    # 0100
    # 0111
    print("Bluetooth is on!")
    if features & CAMERA:
        print("Camera is on!")
    if features & LOCATION:
        print("Location is on!")
    if features & NFC:   #  0011  & 1000= 0000  -> off
        print("NFC is on!")

print("Feature Final Value : ",features)