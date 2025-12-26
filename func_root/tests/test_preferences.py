
from func_root.ui.language_options import load_preferences, save_preferences

prefs = load_preferences()
print("Loaded:", prefs)

prefs["language"] = "en-IN"
prefs["gender"] = "male"

save_preferences(prefs)

print("Reloaded:", load_preferences())
