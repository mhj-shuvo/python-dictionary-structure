#Script Begins

#Dictionary Structure
myDict = {}                         # Defining an empty dictionary
print (myDict)
                                    # Defining dictionary with elements
myDict = {
    'Programming': 'Lnguages',
    1: 'Python', 
    2: 'Java', 
    3: 'PHP',
    4: 'Pearl',
    5: 'Ruby'
    }
print (myDict)

myDict[3] = 'C++'                   # Changing the value of defined key
print (myDict)

myDict['3rd'] = 'Kotlin'            # Adding new key-value pair
print (myDict)

val = myDict.pop('3rd')             # Removes the provided key and the corresponding value
print ('Removed key-value pair:', val)
print ('Dictionary:', myDict)

val = myDict.popitem()              # Removes the last key-value pair
print ('Removed key-value pair:', val)
print ('Dictionary:',myDict)

print (myDict[2])                   # Provides the value of defined key

print (myDict.keys())               # Returns all the keys 
print (myDict.values())             # Returns all the values
print(myDict.items())               # Returns all the key-value pairs
print (myDict.get('Programming'))   # Returns the value of defined key

myDict.clear()                  # Clears the dictionary
print ('Dictionary:', myDict)

# Script Ends(())