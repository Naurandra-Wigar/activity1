mountains = ["Everest", "K2", "Kilimanjaro", "Fuji"]
print(mountains)

mountains.append("Semeru")              
mountains.insert(0, "Denali")           
print(mountains)

del mountains[1]                       
popped = mountains.pop()                
print(f"Popped: {popped}")
mountains.remove("Fuji")                
print(mountains)

print(sorted(mountains))                
mountains.sort()                       
print(mountains)
mountains.reverse()                     
print(mountains)

print(len(mountains))                  