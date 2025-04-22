class Process:
    def __init__(self, pid):
        self.pid = pid
        self.waiting_for = []

    def request_resource(self, holders, initiator):
        if not holders:
            print(f"Process {self.pid} found no holders.")
            return False
        for h in holders:
            probe = [initiator, self.pid, h.pid]
            print(f"{self.pid} → sending probe {probe} to {h.pid}")
            if h.receive_probe(probe):
                print(f"Deadlock detected by process {initiator}!")
                return True
        return False

    def receive_probe(self, probe):
        initiator, sender, receiver = probe
        print(f"{self.pid} ← received probe {probe}")
        if self.pid == initiator:
            print(f"Cycle found at {self.pid} → DEADLOCK!")
            return True
        if not self.waiting_for:
            print(f"{self.pid} waits for no one. Ignoring.")
            return False
        for nxt in self.waiting_for:
            new_probe = [initiator, self.pid, nxt.pid]
            print(f"{self.pid} → forwarding probe {new_probe} to {nxt.pid}")
            if nxt.receive_probe(new_probe):
                return True
        return False

def build_graph():
    n = int(input("Number of processes: "))
    processes = {i: Process(i) for i in range(1, n + 1)}
    
    print("Enter dependencies (waiting_for), e.g., '1 2' means P1 waits for P2.")
    print("Type 'done' when finished.\n")

    while True:
        inp = input(">> ")
        if inp == "done":
            break
        try:
            p1, p2 = map(int, inp.split())
            processes[p1].waiting_for.append(processes[p2])
        except:
            print("Invalid input. Try again.")

    return processes

def run_detection():
    processes = build_graph()
    start = int(input("\nEnter initiator process ID: "))
    if start in processes:
        if processes[start].request_resource(processes[start].waiting_for, start):
            print("Deadlock confirmed.")
        else:
            print("No deadlock detected.")
    else:
        print("Invalid process ID.")

if __name__ == "__main__":
    run_detection()

# output
# PS C:\Users\HP\Desktop\dc\exp7> python deadlock-user.py
# Number of processes: 4
# Enter dependencies (waiting_for), e.g., '1 2' means P1 waits for P2.
# Type 'done' when finished.

# >> 1 2
# >> 2 3
# >> 3 4
# >> 4 1
# >> done

# Enter initiator process ID: 1
# 1 → sending probe [1, 1, 2] to 2
# 2 ← received probe [1, 1, 2]
# 2 → forwarding probe [1, 2, 3] to 3
# 3 ← received probe [1, 2, 3]
# 3 → forwarding probe [1, 3, 4] to 4
# 4 ← received probe [1, 3, 4]
# 4 → forwarding probe [1, 4, 1] to 1
# 1 ← received probe [1, 4, 1]
# Cycle found at 1 → DEADLOCK!
# Deadlock detected by process 1!
# Deadlock confirmed.