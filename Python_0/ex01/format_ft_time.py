from datetime import datetime

date_now_2 = datetime.today()
timestamp = date_now_2.timestamp()
date_now_3 = f"{timestamp:.4f}"
scientific = f"{timestamp:.2e}"

print(
    f"Seconds since January 1, 1970: {date_now_3} "
    f"or {scientific} in scientific notation"
)
print(date_now_2.strftime("%b %d %Y"))
