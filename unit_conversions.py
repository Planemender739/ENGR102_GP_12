quantity_tbc=(float(input("Please enter the quantity to be converted: ")))   #Asking for what value we want to conver with, Where quantity_TBC is the quantity to be converted

#---------------------------------------------
#This gives us the conversion for pounds --> Newtons
    #We use the f"{quantity_tbc:.2f}" command to make sure that we use 1.00 instead of 1.0 or 1.
    #This is the case for all the functions below

newtons=(quantity_tbc*4.45)
print((f"{quantity_tbc:.2f}"), "pounds force is equivalent to",(f"{newtons:.3}"),"newtons")

#----------------------------------------------
#This gives us the covnersion for meters --> Feet

feet=(quantity_tbc*3.28)
print((f"{quantity_tbc:.2f}"), "meters is equivalent to",(f"{feet:.3}"),"feet")

#-----------------------------------------------
#This gives us the conversion for atmospheres --> Kilopascals

kilopascals=(quantity_tbc*101.33)
print((f"{quantity_tbc:.2f}"),"atmospheres is equal to",(f"{kilopascals}"),"kilopascals")

#----------------------------------------------
#This gives us the conversion for Watts --> BTU

BTU_per_hour=(quantity_tbc*3.41)
print((f"{quantity_tbc:.2f}"),"watts is equivalent to",(f"{BTU_per_hour:.3}"),"BTU per hour")

#----------------------------------------------
#This gives us the conversion for Liters -->US Gallons per Minute

US_GPM=(quantity_tbc*15.85)
print((f"{quantity_tbc:.2f}"),"liters per second is equivalent to",(f"{US_GPM:.4}"),"US gallons per minute")

#-----------------------------------------------
#This gives us the conversion for Degrees C --> Degrees Fahrenheit

Deg_Fahr=(float(quantity_tbc*33.80))
print((f"{quantity_tbc:.2f}"),"degrees Celsius is equivalent to",(f"{Deg_Fahr:.2f}"),"degrees Fahrenheit")