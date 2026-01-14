#Welcome Branch

#Libraries Imported Here
import sys
import time

print("Welcome Branch - Developer: Matthew Smith")
print("\nWelcom to InfoTechCenter V.1.0")


x = 0 
ellipsis = 0

while x != 20: 
    x += 1
    ellipsisMessage = ("InfoTechCenter OS is Booting Up" + "." * ellipsis)
    ellipsis += 1 
    sys.stdout.write("\r"+ ellipsisMessage) 
    sys.stdout.flush()
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating System Booted Up - Access Granted")