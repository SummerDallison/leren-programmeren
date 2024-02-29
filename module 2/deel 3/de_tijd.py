periods = ["AM","PM"]

periode_index = 0
while periode_index < len(periods):
    hour = 1
    while hour <= 12:
        print(f"{hour}{periods[periode_index]}")
        hour += 1
    periode_index += 1