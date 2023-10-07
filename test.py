upgrade_options = {
    "Upgrade 1": {"cost": 400, "description": "Increase efficency"},
    "Upgrade 2": {"cost": 2000, "description": "Increase efficency"},
    "Upgrade 3": {"cost": 5000, "description": "Increase efficency"},
}


def singular_upgrade_multiplier():
    pass


# .items is a built in function that works with dictionaries.
# It allows you to access items within the dict.

for option, info in upgrade_options.items():
    print(f"{option}: Cost {info['cost']} - {info['description']}")
