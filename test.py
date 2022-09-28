from Generator import *


results=[]
for i in range(5000):
    p=genPass()
    results.append(passTest(p))
print("\nTests with only password generation and no checking")
print("Passes: " +str(results.count(True)))
print("Fails: " +str(results.count(False)))


results=[]
for i in range(5000):
    p=genCheck()
    results.append(passTest(p))
print("\nTests with password generation and checking")
print("Passes: " +str(results.count(True)))
print("Fails: " +str(results.count(False)))