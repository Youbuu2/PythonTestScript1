import random
import keyboard
import pyautogui


def characterSelect():
   Characters = ["Commando", "Huntress", "Bandit", "MUL-T", "Engineer", "Artificer", "Mercenary", "Rex", "Loader", "Acrid", "Captain", "Railgunner", "Void Fiend", "Seeker", "Chef", "False Son"]
   random_character = random.choice(Characters)
   print(random_character)

keyboard.add_hotkey('a+r',characterSelect)
