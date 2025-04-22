import multiprocessing

def child_process(conn):
    message = "Hello from child process!"
    conn.send(message)
    conn.close()

def parent_process():
    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(target=child_process, args=(child_conn,))
    process.start()

    child_conn.close()  # Close child end in parent

    # Read message from child process
    message = parent_conn.recv()
    print(f"Parent received: {message}")

    parent_conn.close()
    process.join()

if __name__ == "__main__":
    parent_process()


# output:
# PS C:\Users\HP\Desktop\dc\exp3> python pipes.py
# Parent received: Hello from child process!