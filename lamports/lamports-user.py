class LamportClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = 0

    def send_request(self):
        self.clock += 1
        print(f"[Process {self.process_id}] Sent request with timestamp {self.clock}")
        return self.clock

    def receive_request(self, timestamp):
        self.clock = max(self.clock, timestamp) + 1
        print(f"[Process {self.process_id}] Received request (timestamp {timestamp}) → Updated clock to {self.clock}")

    def internal_event(self):
        self.clock += 1
        print(f"[Process {self.process_id}] Internal event → Timestamp updated to {self.clock}")

def get_process(processes, pid):
    if pid not in processes:
        processes[pid] = LamportClock(pid)
    return processes[pid]

def simulate_with_input():
    processes = {}
    sent_messages = {}  # Store messages by name

    print("\n--- Lamport Clock Simulation (User Input) ---\n")
    print("Commands:")
    print("  internal <pid>")
    print("  send <sender_pid> <message_name>")
    print("  receive <receiver_pid> <sender_pid> <message_name>")
    print("  show")
    print("  exit\n")

    while True:
        command = input("Enter command: ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        if action == "internal" and len(command) == 2:
            pid = int(command[1])
            proc = get_process(processes, pid)
            proc.internal_event()

        elif action == "send" and len(command) == 3:
            pid = int(command[1])
            msg_name = command[2]
            proc = get_process(processes, pid)
            sent_messages[msg_name] = proc.send_request()

        elif action == "receive" and len(command) == 4:
            receiver_pid = int(command[1])
            sender_pid = int(command[2])
            msg_name = command[3]

            if msg_name not in sent_messages:
                print(f"Error: Message '{msg_name}' not found.")
                continue

            proc = get_process(processes, receiver_pid)
            proc.receive_request(sent_messages[msg_name])

        elif action == "show":
            for pid in sorted(processes):
                print(f"Process {pid}: Clock = {processes[pid].clock}")

        elif action == "exit":
            print("\n--- Simulation Ended ---")
            break

        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    simulate_with_input()


# output
# PS C:\Users\HP\Desktop\dc\exp4> python lamports-user.py

# --- Lamport Clock Simulation (User Input) ---

# Commands:
#   internal <pid>
#   send <sender_pid> <message_name>
#   receive <receiver_pid> <sender_pid> <message_name>
#   show
#   exit

# Enter command: internal 1
# [Process 1] Internal event → Timestamp updated to 1
# Enter command: send 1 msgA
# [Process 1] Sent request with timestamp 2
# Enter command: internal 2
# [Process 2] Internal event → Timestamp updated to 1
# Enter command: receive 2 1 msgA
# [Process 2] Received request (timestamp 2) → Updated clock to 3
# Enter command: send 2 msgB
# [Process 2] Sent request with timestamp 4
# Enter command: receive 3 1 msgA
# [Process 3] Received request (timestamp 2) → Updated clock to 3
# Enter command: receive 3 2 msgB
# [Process 3] Received request (timestamp 4) → Updated clock to 5
# Enter command: show
# Process 1: Clock = 2
# Process 2: Clock = 4
# Process 3: Clock = 5
# Enter command: exit

# --- Simulation Ended ---