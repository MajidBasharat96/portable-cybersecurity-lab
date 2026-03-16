import os
import subprocess

def start_lab():
    print("Launching Portable Cybersecurity Lab...")
    subprocess.run(["bash", "../start-lab.sh"])

if __name__ == "__main__":
    start_lab()
