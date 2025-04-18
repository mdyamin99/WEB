def multiple():
    return 3,4
# print(multiple())

things='pen','water bottle','sunglass','phone','webcam'
print(type(things))
print(things)
print(things[1])
print(things[-2])
print(things[1:4])
if 'phone' in things:
    print("exiest")
for item in things:
    print(item)