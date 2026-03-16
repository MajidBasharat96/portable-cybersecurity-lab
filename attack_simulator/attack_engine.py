
import random
import time

ATTACKS = [
    "port_scan",
    "sql_injection",
    "xss",
    "bruteforce"
]

class AttackSimulator:

    def simulate(self):
        attack = random.choice(ATTACKS)
        print("Simulating attack:", attack)
        time.sleep(1)

    def run(self, rounds=10):
        for _ in range(rounds):
            self.simulate()

if __name__ == "__main__":
    sim = AttackSimulator()
    sim.run()
