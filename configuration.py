test_settings = { 'theme': 'light', 'language': 'English' }

def add_setting(settings, setting):
    key, value = setting
    # Fix: Ensure lookups handle casing consistently with how they are saved
    if key.lower() in settings:
        return f"Setting '{key.lower()}' already exists! Cannot add a new setting with this name."
    else:
        settings[key.lower()] = value.lower()
        return f"Setting '{key.lower()}' added with value '{value.lower()}' successfully!"

print(add_setting({'theme': 'light', 'language': 'English'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))


def update_setting(settings, setting):
    key, value = setting
    if key.lower() in settings:
        settings[key.lower()] = value.lower()
        return f"Setting '{key.lower()}' updated to '{value.lower()}' successfully!"
    else:
        return f"Setting '{key.lower()}' does not exist! Cannot update a non-existing setting."

print(update_setting({'theme': 'light', 'language': 'English'}, ('theme', 'dark')))


def delete_setting(settings, setting_key):
    # Fix: Simplified to accept just the key string instead of an incomplete tuple
    key_lower = setting_key.lower()
    if key_lower in settings:
        settings.pop(key_lower)  # Fix: Pop from the 'settings' dict, not 'setting'
        return f"Setting '{key_lower}' deleted successfully!"
    else:
        return "Setting not found!"

# Fix: Passed just the string 'theme' to match the updated parameters
print(delete_setting({'theme': 'light', 'language': 'English'}, 'theme'))


def view_setting(test_settings):
    if not test_settings:
        return "No settings available."
    else:
        view = "Current user settings:\n" # Fix: Capitalized 'Current' for consistency
        for key, value in test_settings.items():
            view += f"{key.capitalize()}: {value.capitalize()}\n" # Fix: Capitalized value for 'English'/'Light'
        return view

print(view_setting(test_settings))
print("Hello! The configuration script is running successfully.")
# Example fix
username = input("Please enter your configuration name: ")
print(f"Configuration set up for: {username}")
