week_day = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

leave_day = int(input("op welke dag weg? (0-6) "))
duration_stay = int(input("hoe lang blijf je? "))

print("je komt terug op een", week_day(leave_day + duration_stay) % len(week_day))
