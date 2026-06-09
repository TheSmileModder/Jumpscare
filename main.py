import pygame
import os
import random
import time
import json
import sys


# stop global hotkey
def stop_program():
    print("Stopping")
    pygame.quit()
    os._exit(0)


# config
with open("config.json", "r") as config_file:
    config = json.load(config_file)


# Auto set screen height and width if not set
pygame.init()

SCREEN_WIDTH = pygame.display.Info().current_w if config["screen_width"] is 0 else config["screen_width"]
SCREEN_HEIGHT = pygame.display.Info().current_h if config["screen_height"] is 0 else config["screen_height"]
print(SCREEN_WIDTH, SCREEN_HEIGHT) 

JUMPSCARE_FOLDER = config["jumpscare_folder"]
MIN_WAIT_SECONDS = config["min_wait_seconds"]
MAX_WAIT_SECONDS = config["max_wait_seconds"]
STOP_HOTKEY = config["stop_global_hotkey"]


clock = pygame.time.Clock()
direname = os.path.dirname(__file__)


if sys.platform == "win32":
    import keyboard
    keyboard.add_hotkey(STOP_HOTKEY, stop_program)

# Auto find folder for jumpscars
def find_all_jumpscares(jumpscare_folder):
    jumpscare_list = []

    # loop through everything in the jumpscare folder
    for folder_name in os.listdir(jumpscare_folder):
        folder_path = os.path.join(jumpscare_folder, folder_name)

        # skip if not a folder
        if not os.path.isdir(folder_path):
            continue

        # get all files in the folder
        files_in_folder = os.listdir(folder_path)

        # find the audio and images
        image_file = next((file for file in files_in_folder if file.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif"))), None)
        audio_file = next((file for file in files_in_folder if file.endswith((".wav", ".mp3", ".ogg"))), None)

        # only add if both files are there
        if image_file and audio_file:
            jumpscare_list.append({
                "image": os.path.join(folder_path, image_file),
                "audio": os.path.join(folder_path, audio_file)
            })

    return jumpscare_list


class Jumpscare:
    def __init__(self):
        pass


    def display_image(self, path_to_image):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)


        jumpscare_image = pygame.image.load(os.path.join(direname, path_to_image)).convert()
        jumpscare_image = pygame.transform.scale(jumpscare_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(jumpscare_image, (0, 0))
        pygame.display.flip()


    def play_audio(self, path_to_audio):
        pygame.mixer.init()
        self.jumpscare_audio = pygame.mixer.Sound(path_to_audio)
        self.jumpscare_audio.play()
        duration = self.jumpscare_audio.get_length()
        print(f"Audio length: {round(duration, 2)} seconds")
        time.sleep(duration + 0.2)


    def trigger_random_jumpscare(self):
        # pick random wait time before jumpscare happens
        wait_time_jumpscare = random.uniform(MIN_WAIT_SECONDS, MAX_WAIT_SECONDS)
        print(f"The next Jumpscare is in {round(wait_time_jumpscare, 2)} seconds")
        time.sleep(wait_time_jumpscare)

        all_jumpscares = find_all_jumpscares(JUMPSCARE_FOLDER)
        chosen_jumpscare = random.choice(all_jumpscares)

        print(f"Triggered Jumpscare: {chosen_jumpscare}")
        self.display_image(chosen_jumpscare["image"])
        self.play_audio(chosen_jumpscare["audio"])

        pygame.quit()

jumpscare = Jumpscare()



while True:
    jumpscare.trigger_random_jumpscare()

    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    print(width, height)
