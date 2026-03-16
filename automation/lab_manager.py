import subprocess
import os

class LabManager:

    def start_lab(self):
        print("Starting Cybersecurity Lab...")
        subprocess.run(["docker-compose", "-f", "configs/docker-compose.yml", "up", "-d"])

    def stop_lab(self):
        print("Stopping Cybersecurity Lab...")
        subprocess.run(["docker-compose", "-f", "configs/docker-compose.yml", "down"])

    def lab_status(self):
        subprocess.run(["docker", "ps"])


if __name__ == "__main__":
    manager = LabManager()

    print("1. Start Lab")
    print("2. Stop Lab")
    print("3. Status")

    choice = input("Select option: ")

    if choice == "1":
        manager.start_lab()

    elif choice == "2":
        manager.stop_lab()

    elif choice == "3":
        manager.lab_status()
