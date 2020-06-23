# bounce.py

height = 60
count = 0
while (height >= 0 and count < 10):
    count = count + 1
    print (count, round(height, 4))
    height = height * .6
print ("That's all folks")