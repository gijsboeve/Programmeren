huidige_tijd = int(input("hoelaat is het nu?"))
alarm_tijd = int(input("hoe lang zet je het alarm?"))
alarm_afgaan = (huidige_tijd + alarm_tijd) % 24

print("de wekker gaat af om", alarm_afgaan, "uur")


