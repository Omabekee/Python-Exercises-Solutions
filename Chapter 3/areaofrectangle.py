#2 AREA OF A RECTANGLE

#Area of a rectangle = L * W

#Ask user to enter length and Width of first Rectangle
lengthOne = float(input("Enter length of first rectangle: "))
widthOne = float(input("Enter width of first rectangle: "))

#Ask user to enter length and width of second Rectangle
lengthTwo = float(input("Enter length of second rectangle: "))
widthTwo = float(input("Enter width of second rectangle: "))


#Calculate
areaOne = lengthOne * widthOne
areaTwo = lengthTwo * widthTwo


#Check for greater area or if areas are same
if areaOne > areaTwo:
    print("Rectangle 1 is greater than Rectangle 2")
elif areaTwo > areaOne:
    print("Rectangle 2 is greater than Rectangle 1")
else:
    print("Both areas are the same")

