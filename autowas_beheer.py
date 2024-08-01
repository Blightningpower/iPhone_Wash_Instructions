import os
import json

# Gebruik forward slashes voor de paddefinities
file_path = os.path.expanduser('https://blightningpower.github.io/iPhone_Wash_Instructions/Autowas_Cyclus/auto_cycle.json')

# De cyclus van autowasacties
cycle = [
    "Washin7 wassen bij halve tank",
    "Zelf wassen bij wasbox",
    "CarPro wassen bij lege tank",
    "Zelf wassen bij wasbox"
]

# Functie om de huidige index op te halen
def get_current_index():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('current_index', 0)
    return 0

# Functie om de volgende index op te slaan
def save_next_index(current_index):
    next_index = (current_index + 1) % len(cycle)
    with open(file_path, 'w') as file:
        json.dump({'current_index': next_index}, file)
    return next_index

# Huidige index ophalen
current_index = get_current_index()

# Huidige actie weergeven
current_action = cycle[current_index]
print(f"De huidige wasbeurt is: {current_action}")

# Update de index zonder invoer te vragen
next_index = save_next_index(current_index)
next_action = cycle[next_index]
print(f"De volgende wasbeurt is: {next_action}")
