# Ovan beräknad volym motsvarar Xantal mjölkpaket
# antal=total volym/volym för ett mjölkpaket
print ("hello")
def sphere(radie_sphere):
     return 4/3*3.14*radie_sphere**3
#funtion that calculates the volume of the sphere. 

def cone(radie_cone, height_cone):
    return 1/3*3.14*radie_cone**2*height_cone
#Function that calculates the volume of the cone.



form = input("\n\nWelcome! Tell me the form of the figure. \n\nPlease enter 1 if it´s a sphere or 2 if it´s a cone?\n")
#create variabel so i can use it in functions. Need to be input about the form. 

if form =="1":
    radie_sphere=float(input("\nPlease enter the radie of the sphere!\n"))
    print(f"\nIf the radie of your sphere is {radie_sphere} cm then the volume is", sphere(radie_sphere), "cm^3.")
    
elif form =="2":
    radie_cone=float(input("\nPlease enter the radie of the cone!\n"))
    height_cone=float(input("\nPlease enter the height of the cone!\n"))
    print(f"\nIf the radie of the cone is {radie_cone} and the height is {height_cone} cm then the volume is", cone(radie_cone, height_cone), "cm^3.")
else: 
    print("Sorry, can´t understand. Please try again.")
    
#Planering för inköp av Mjölkpaket a´1.5L
print("\nNu gör vi ett antagande att volymen som du har räknat ut ska omvandlas till hur många mjölkpaket(1,5L) det motsvarar.\n")
print(f"Du fick en beräknad volym på: {sphere(radie_sphere)} cm3. Det motsvarar", round (sphere(radie_sphere)/1.5), "st. 1,5L mjölkpaket.\n")
print("\nKan vi nu räkna ut hur många mjölkpaket som får plats i vårt kylskåp, på en specifik hylla.\n")
print("I och med att höjden på 1,5L mjölkpaket är konstant behöver vi enbart bottenarean på hyllan.\n")
print("***********************************************")
def refrig(depth_refrig, widht_refrig):
    return (depth_refrig * widht_refrig) 
widht_refrig=float(input("Please enter the widht of your milk shell in your refrigerator:"))
depth_refrig=float(input("And now: Please enter the depth of your milk shell in your refrigerator:\n"))

depth_amount_milk=depth_refrig/7
widht_amount_milk=widht_refrig/7
total_milk=depth_amount_milk*widht_amount_milk
#print(f"Den beräknade arean på din mjölkhylla är: {refrig(depth_refrig, widht_refrig)}cm3(Liter)\n")
print(f"Varje sida på ett mjölkpaket är 7cm. Det leder till att det får plats {depth_amount_milk} st mjölkpaket.\n")
print(f"Vi behöver också räkna hur många mjölkpaket som får plats på bredden av din hylla. Du angav en bredd på {widht_refrig}. Det motsvarar: {widht_amount_milk} st. mjölkpaket.\n")
print(f"This leeds to a total amount of milk of {total_milk} on your shell.")
