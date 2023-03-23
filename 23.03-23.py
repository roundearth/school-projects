import math
import time

# Utregning av volum
print("Regner ut volum...")
VPR = float((2*2*3 + 2*2*2 + 2*3*2)/2)  # Volum av prisme i m2
VK = float(2*3*3 + 2*3*2 + 2*3*2)  # Volum av kube i m2
VS = float(math.pi*0.67**2*3)  # Volum av sylinder i m2

VfigM = float(VPR+VK-(VS/4))  # Volum av figur i m2
VfigL = str(round(VfigM * 1000, 0))  # Volum av figur i L

time.sleep(2)
print("Volumet er", VfigL, "liter.")

# Utregning av overflateareal
time.sleep(1)
print("Regner ut areal...")

AP = float(2*2/2 + 2*2/2 + 3*2.8)  # Areal av prisme
AKV = float((2-0.67)*3)  # Areal av kortvegg
ALH = float((3-0.67)*2 + (3-0.67)*2)  # Areal av langvegg til høyre for sylinder
ARS = float(0.67*0.67-math.pi*0.67**2/4)  # Areal rundt sylinder
AOS = float((2-0.67)*0.67+(2-0.67)*0.67)  # Areal over sylinder
AS = float((2*math.pi*0.67**2)+2*math.pi*0.67*3)  # Areal av sylinder

Afig = str(  # Areal av figur rundet av til to desimaler
    round(AP + AKV + ALH + ARS + AOS + AS, 2)
    )

time.sleep(2)
print("Arealet er", Afig, "kvadratmeter")

# Utregning av flis
time.sleep(1)
print("Regner ut hvor mye flis som må kjøpes...")
FP = 799  # Flispris
FA = int(math.ceil(float(Afig))) # Areal av figur rundet opp til nærmeste m2.

time.sleep(2)
print("Du må kjøpe inn flis til å dekke", FA, "m2\nRegner ut flisenes pris...")

P = (int(FA*FP))
time.sleep(2)
print("Flisene koster", P, "kr. \nLykke til med å betale.")
