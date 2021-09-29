def sphere(radie_sphere):
     return 4/3*3.14*radie_sphere**3
#funtion that calculates the volume of the sphere. 

def cone(radie_cone, height_cone):
    return 1/3*3.14*radie_cone**2*height_cone
#Function that calculates the volume of the cone.   


form = input("\n\nHello! Tell me the form of the figure. \nPlease enter 1 if it´s a sphere or 2 if it´s a cone")
#create variabel so i can use it in functions. Need to be input about the form. 

if form =="1":
    radie_sphere=float(input("fdfdf please enter the radie of yout sphere"))
    print(f"Great, if the radie of your sphere is {radie_sphere} cm then the volume is", sphere(radie_sphere), "cm^3.")
elif form =="2":
    radie_cone=float(input("fdfdf please enter the radie of yout cone"))
    height_cone=float(input("fdfdf please enter the height of yout cone"))
    print(f"Great, if the radie of your cone is {radie_cone} and the height is {height_cone} cm then the volume is", cone(radie_cone, height_cone), "cm^3.")
else: 
    print("Sorry, can´t understand. Please try again.")
