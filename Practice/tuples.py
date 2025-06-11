days= ('monday','sunday','tuesday','wednesday','sunday')

print(days.count('sunday'))
weeks = list(days)

weeks.append("Saturday")
weeks.sort()
weeks.reverse()
weeks.remove('Saturday')
days= tuple(weeks)

print(days)

print(type(days),days )
print(len(days))
