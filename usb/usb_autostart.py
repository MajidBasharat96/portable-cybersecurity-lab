
import subprocess
import time

def start():
    print("USB detected. Launching Cybersecurity Lab...")
    subprocess.run(["bash", "../scripts/start_lab.sh"])

if __name__ == "__main__":
    time.sleep(2)
    start()
