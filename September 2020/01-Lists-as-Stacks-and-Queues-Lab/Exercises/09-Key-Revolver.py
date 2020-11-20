from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(_) for _ in input().split()])
locks = deque([int(_) for _ in input().split()])
intelligence_value = int(input())

count_shots = 0
barrel_size = gun_barrel_size

while True:

    if barrel_size == 0:
        if len(bullets) > 0:
            print("Reloading!")
            barrel_size += gun_barrel_size

    if len(locks) == 0:
        money_earned = intelligence_value - (count_shots * bullet_price)
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break

    if len(bullets) == 0:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break


    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print(f"Bang!")
        count_shots += 1
        barrel_size -= 1

    else:
        print("Ping!")
        locks.appendleft(current_lock)
        count_shots += 1
        barrel_size -= 1
