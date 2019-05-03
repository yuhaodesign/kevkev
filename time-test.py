from datetime import datetime

s = '11:30'

e = '12:45'

start = datetime.strptime(s, '%H:%M')
end = datetime.strptime(e, '%H:%M')

print(start.time())
print(end.time())

delta = end - start

print(round(2 * delta.seconds/3600) /2 )

