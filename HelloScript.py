f = open(".\HelloScript.txt", 'w')
for i in range(100):
    print("Hello", file=f)
f.close()