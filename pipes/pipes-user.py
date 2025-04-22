import multiprocessing

def child_process(conn):
    message = conn.recv()  # Receive message from parent
    print(f"Child received: {message}")
    conn.close()

def parent_process():
    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(target=child_process, args=(child_conn,))
    process.start()

    child_conn.close()  # Close child end in parent

    # Take user input in parent process
    message = input("Parent: Enter a message to send to the child: ")
    parent_conn.send(message)  # Send message to child

    parent_conn.close()
    process.join()

if __name__ == "__main__":
    parent_process()


# output
# PS C:\Users\HP\Desktop\dc\exp3> python pipes-user.py
# Parent: Enter a message to send to the child: hello child
# Child received: hello child