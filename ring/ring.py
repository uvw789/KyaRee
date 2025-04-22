class RingProcess:
    def __init__(self, id):
        self.id = id
        self.coordinator = None
        self.next = None 

    def start_election(self):
        print(f"Process {self.id} starts an election.")
        active_list = [self.id]
        self.send_election_message(active_list)

    def send_election_message(self, active_list):
        if self.next:
            print(f"Process {self.id} forwards election list {active_list}.")
            self.next.receive_election_message(active_list)

    def receive_election_message(self, active_list):
        if self.id not in active_list:
            active_list.append(self.id)
            self.send_election_message(active_list)
        else:

            new_coordinator = max(active_list)
            print(f"Process {self.id} elects {new_coordinator} as the coordinator.")
            self.send_coordinator_message(new_coordinator)

    def send_coordinator_message(self, new_coordinator):
        if self.next:
            print(f"Process {self.id} informs that {new_coordinator} is the new coordinator.")
            self.coordinator = new_coordinator
            self.next.receive_coordinator_message(new_coordinator)

    def receive_coordinator_message(self, new_coordinator):
        if self.coordinator is None:
            self.coordinator = new_coordinator
            self.send_coordinator_message(new_coordinator)


processes = [RingProcess(i) for i in range(1, 6)]


for i in range(len(processes)):
    processes[i].next = processes[(i + 1) % len(processes)]

processes[1].start_election()


# output
# PS C:\Users\HP\Desktop\dc\exp5> python ring.py         
# Process 2 starts an election.
# Process 2 forwards election list [2].
# Process 3 forwards election list [2, 3].
# Process 4 forwards election list [2, 3, 4].
# Process 5 forwards election list [2, 3, 4, 5].
# Process 1 forwards election list [2, 3, 4, 5, 1].
# Process 2 elects 5 as the coordinator.
# Process 2 informs that 5 is the new coordinator.
# Process 3 informs that 5 is the new coordinator.
# Process 4 informs that 5 is the new coordinator.
# Process 5 informs that 5 is the new coordinator.
# Process 1 informs that 5 is the new coordinator.