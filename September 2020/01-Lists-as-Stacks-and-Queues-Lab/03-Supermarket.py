from collections import deque

queue = deque([])

while True:
    name = input()

    if name == "End":
        print(f"{len(queue)} people remaining.")
        break

    if name == "Paid":
        for name in queue:
            print(name)
        queue.clear()
        continue

    queue.append(name)