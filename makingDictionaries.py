name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Burt"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "monkeys", "zamboomafoo"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) >= len(arr2):
        for i in range(len(arr1)):
            if i >= len(arr2):
                new_dict[arr1[i]] = ""
            else:
                new_dict[arr1[i]] = arr2[i] 

    else:
        for i in range(len(arr1)):
            if i >= len(arr1):
                new_dict[arr2[i]] = ""
            else:
                new_dict[arr2[i]] = arr1[i]
    return new_dict

print make_dict(name, favorite_animal)