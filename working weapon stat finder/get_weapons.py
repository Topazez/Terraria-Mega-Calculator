user_input = input("Weapon Name: ")
with open("weaponslist.txt", "r") as file:
    for i, line in enumerate(file):
        if user_input == line.strip():
            with open("weapons_stats.txt", "r") as stats_file:
                stats_lines = stats_file.readlines()
                start = ((i + 1) * 5 - 5)
                weapon_stat = 0
                for j in range(start, start + 5):
                    weapon_stat += 1
                    if j < len(stats_lines):
                        if weapon_stat == 1:
                            try:
                                weapon_damage = int(stats_lines[j].strip())
                            except:
                                try:
                                    weapon_damage = float(stats_lines[j].strip())
                                except:
                                    weapon_damage = (stats_lines[j].strip())
                        elif weapon_stat == 2:
                            type_class = (stats_lines[j].strip())
                        elif weapon_stat == 3:
                            try:
                                weapon_knockback = int(stats_lines[j].strip())
                            except:
                                try:
                                    weapon_knockback = float(stats_lines[j].strip())
                                except:
                                    weapon_knockback = (stats_lines[j].strip())
                        elif weapon_stat == 4:
                            try:
                                weapon_critchance = int(stats_lines[j].strip())
                            except:
                                try:
                                    weapon_critchance = float(stats_lines[j].strip())
                                except:
                                    weapon_critchance = (stats_lines[j].strip())
                        elif weapon_stat == 5:
                            try:
                                weapon_usetime = int(stats_lines[j].strip())
                            except:
                                try:
                                    weapon_usetime = float(stats_lines[j].strip())
                                except:
                                    weapon_usetime = (stats_lines[j].strip())

print(weapon_damage)
print(type_class)
print(weapon_knockback)
print(weapon_critchance)
print(weapon_usetime)