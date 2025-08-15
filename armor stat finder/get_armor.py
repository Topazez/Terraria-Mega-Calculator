user_input = input("Armor: ")
with open("armor_names.txt", "r") as file:
    for i, line in enumerate(file):
        if user_input == line.strip():
            with open("armor_stats.txt", "r") as stats_file:
                stats_lines = stats_file.readlines()
                start = ((i + 1) * 18 - 18)
                armor_stat = 0
                for j in range(start, start + 18):
                    armor_stat += 1
                    if j < len(stats_lines):
                        if armor_stat == 1:
                            melee_damage = int(stats_lines[j].strip())
                        elif armor_stat == 2:
                            ranged_damage = int(stats_lines[j].strip())
                        elif armor_stat == 3:
                            magic_damage = int(stats_lines[j].strip())
                        elif armor_stat == 4:
                            summon_damage = int(stats_lines[j].strip())
                        elif armor_stat == 5:
                            melee_crit = int(stats_lines[j].strip())
                        elif armor_stat == 6:
                            ranged_crit = int(stats_lines[j].strip())
                        elif armor_stat == 7:
                            magic_crit = int(stats_lines[j].strip())
                        #These three are damage+critical and serve no purpose and thus are skipped
                        elif armor_stat == 8:
                            continue
                        elif armor_stat == 9:
                            continue
                        elif armor_stat == 10:
                            continue
                        elif armor_stat == 11:
                            melee_speed = (stats_lines[j].strip())
                        elif armor_stat == 12:
                            max_mana = (stats_lines[j].strip())
                        elif armor_stat == 13:
                            mana_usage = (stats_lines[j].strip())
                        elif armor_stat == 14:
                            minion_cap = (stats_lines[j].strip())
                        elif armor_stat == 15:
                            sentry_cap = (stats_lines[j].strip())      
                        elif armor_stat == 16:
                            defense = (stats_lines[j].strip())
                        elif armor_stat == 17:
                            movement_bonus = (stats_lines[j].strip())    
                        elif armor_stat == 18:
                            extra_bonus = (stats_lines[j].strip())

print(melee_damage)
print(ranged_damage)
print(magic_damage)
print(summon_damage)
print(melee_crit)
print(ranged_crit)
print(magic_crit)
print(melee_speed)
print(max_mana)
print(mana_usage)
print(minion_cap)
print(sentry_cap)
print(defense)
print(movement_bonus)
print(extra_bonus)