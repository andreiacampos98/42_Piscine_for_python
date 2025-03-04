from datetime import datetime


date_now_2 = datetime.today()
date_now_3 = date_now_2.timestamp()
scientific = "{:e}".format(date_now_3)

print(date_now_2)
print(f"Seconds since January 1, 1970: {date_now_3} or \
      {scientific} in scientific notation")
print(date_now_2.strftime("%b %d %Y"))
