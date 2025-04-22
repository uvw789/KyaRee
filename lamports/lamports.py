class LamportClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = 0  # Initialize Lamport clock

    def send_request(self):
        """Increment clock and return the timestamp with request"""
        self.clock += 1
        print(f"[Process {self.process_id}] Sent request with timestamp {self.clock}")
        return self.clock

    def receive_request(self, timestamp):
        """Update clock on receiving a request"""
        self.clock = max(self.clock, timestamp) + 1
        print(f"[Process {self.process_id}] Received request (timestamp {timestamp}) → Updated clock to {self.clock}")

    def internal_event(self):
        """Increment clock for an internal event"""
        self.clock += 1
        print(f"[Process {self.process_id}] Internal event → Timestamp updated to {self.clock}")

# Simulating interactions between three processes
def simulate():
    process1 = LamportClock(1)
    process2 = LamportClock(2)
    process3 = LamportClock(3)

    print("\n--- Simulation Start ---\n")

    # Process 1: Internal event, then sends requests
    process1.internal_event()
    timestamp1 = process1.send_request()  # Sent to Process 2
    timestamp2 = process1.send_request()  # Sent to Process 3

    # Process 2: Internal event, receives request from P1, sends request to P3
    process2.internal_event()
    process2.receive_request(timestamp1)
    timestamp3 = process2.send_request()  # Sent to Process 3

    # Process 3: Internal event, receives requests from P1 & P2
    process3.internal_event()
    process3.receive_request(timestamp2)  # From P1
    process3.receive_request(timestamp3)  # From P2

    # Process 1 & 2 receive responses from P3
    process1.receive_request(process3.clock)
    process2.receive_request(process3.clock)

    print("\n--- Simulation End ---\n")

# Run simulation
if __name__ == "__main__":
    simulate()


# output
# PS C:\Users\HP\Desktop\dc\exp4> python lamports.py

# --- Simulation Start ---

# [Process 1] Internal event → Timestamp updated to 1
# [Process 1] Sent request with timestamp 2
# [Process 1] Sent request with timestamp 3
# [Process 2] Internal event → Timestamp updated to 1
# [Process 2] Received request (timestamp 2) → Updated clock to 3
# [Process 2] Sent request with timestamp 4
# [Process 3] Internal event → Timestamp updated to 1
# [Process 3] Received request (timestamp 3) → Updated clock to 4
# [Process 3] Received request (timestamp 4) → Updated clock to 5
# [Process 1] Received request (timestamp 5) → Updated clock to 6
# [Process 2] Received request (timestamp 5) → Updated clock to 6

# --- Simulation End ---