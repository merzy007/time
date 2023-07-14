import time

def pomodoro_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"Remaining time: {minutes:02d}:{seconds:02d}", end="\r", flush=True)
        time.sleep(1)

    print("\nTime's up!")

# 设置专注时长为25分钟
pomodoro_timer(25)
