from datetime import datetime, timedelta
def date_difference(time_str: str):
    """Вычитает текущию дату из time_str даты. И проверяет на ноль  """
    now_time = datetime.strptime(time_str, "%Y.%m.%d %H:%M")

    current_time = datetime.now()
    current_time_without_ms = datetime.strptime(current_time.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")

    difference = now_time - current_time_without_ms

    years, remainder = divmod(difference.days, 365)
    days = remainder
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if years <= 0 and days <= 0 and hours <= 0 and minutes <= 0:
      return('null')
    elif years < 0 or days < 0 or hours < 0 or minutes < 0:
      return('null')

