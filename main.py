today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

print(tomorrow.strftime('завтра %d.%m'))