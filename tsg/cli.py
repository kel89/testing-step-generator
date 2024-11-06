import os
from . import generate_script


def init():
    secret_key = input("Enter your OpenAi API Key: ")
    config_dir = os.path.expanduser("~/.tsg")
    config_file = os.path.join(config_dir, "config")
    os.makedirs(config_dir, exist_ok=True)
    with open(config_file, "w") as f:
        f.write(secret_key)
    print("Config file created at: ", config_file)


def generate():
    config_file = os.path.expanduser("~/.tsg/config")

    # Check if the config file exists
    if not os.path.isfile(config_file):
        print("Config file not found. Please run 'tsg init' first.")
        return

    # Read the secret key
    with open(config_file, "r") as f:
        secret_key = f.read().strip()

    generate_script.main(secret_key)
