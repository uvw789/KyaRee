class Process:
    def __init__(self, id):
        self.id = id
        self.active = True
        self.coordinator = None
        self.next = None

    def start_election(self):
        if not self.active:
            print(f"Process {self.id} is down.")
            return
        print(f"Process {self.id} starts an election.")
        self.pass_election([self.id])

    def pass_election(self, ids):
        if self.next.active:
            if self.next.id in ids:
                leader = max(ids)
                print(f"Process {self.id} elects {leader} as the coordinator.")
                self.pass_coordinator(leader)
            else:
                ids.append(self.next.id)
                print(f"Process {self.id} forwards election list {ids}.")
                self.next.pass_election(ids)
        else:
            self.next.pass_election(ids)

    def pass_coordinator(self, leader):
        self.coordinator = leader
        print(f"Process {self.id} informs that {leader} is the new coordinator.")
        if self.next.coordinator != leader:
            self.next.pass_coordinator(leader)

def setup_ring(n):
    plist = [Process(i) for i in range(1, n + 1)]
    for i in range(n):
        plist[i].next = plist[(i + 1) % n]
    return plist

def run():
    n = int(input("Enter number of processes: "))
    ring = setup_ring(n)

    while True:
        cmd = input(">> ").strip().split()
        if not cmd: continue
        if cmd[0] == "start":
            ring[int(cmd[1]) - 1].start_election()
        elif cmd[0] == "down":
            ring[int(cmd[1]) - 1].active = False
            print(f"Process {cmd[1]} is now down.")
        elif cmd[0] == "up":
            p = ring[int(cmd[1]) - 1]
            p.active, p.coordinator = True, None
            print(f"Process {cmd[1]} is back up.")
        elif cmd[0] == "status":
            for p in ring:
                state = "UP" if p.active else "DOWN"
                coord = f" | Coordinator: {p.coordinator}" if p.coordinator else ""
                print(f"Process {p.id} is {state}{coord}")
        elif cmd[0] == "exit":
            print("Exiting simulation.")
            break

if __name__ == "__main__":
    run()

# output
# PS C:\Users\HP\Desktop\dc\exp5> python ring-user.py
# Enter number of processes: 5
# >> status
# Process 1 is UP
# Process 2 is UP
# Process 3 is UP
# Process 4 is UP
# Process 5 is UP
# >> down 5
# Process 5 is now down.
# >> start 3
# Process 3 starts an election.
# Process 3 forwards election list [3, 4].
# Process 5 forwards election list [3, 4, 1].
# Process 1 forwards election list [3, 4, 1, 2].
# Process 2 elects 4 as the coordinator.
# Process 2 informs that 4 is the new coordinator.
# Process 3 informs that 4 is the new coordinator.
# Process 4 informs that 4 is the new coordinator.
# Process 5 informs that 4 is the new coordinator.
# Process 1 informs that 4 is the new coordinator.
# >> status
# Process 1 is UP | Coordinator: 4
# Process 2 is UP | Coordinator: 4
# Process 3 is UP | Coordinator: 4
# Process 4 is UP | Coordinator: 4
# Process 5 is DOWN | Coordinator: 4
# >> exit
# Exiting simulation.
