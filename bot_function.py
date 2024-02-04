from datetime import datetime, timedelta

time_str = '2024.2.4 15:37'
now_time = datetime.strptime(time_str, "%Y.%m.%d %H:%M")

current_time = datetime.now()
current_time_without_ms = datetime.strptime(current_time.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")

difference = current_time_without_ms - now_time

years, remainder = divmod(difference.days, 365)
days = remainder
hours, remainder = divmod(difference.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print("Годы:", years)
print("Дни:", days)
print("Часы:", hours)
print("Минуты:", minutes)

if years 	<= 0 and days <= 0 and hours	<= 0 and minutes	<= 0:
  print("ура null")