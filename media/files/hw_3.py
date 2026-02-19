def distance_function(target):
    def distance(x):
        return abs(x - target)
    return distance

def nearest_number(numbers, target=0):
    distance = distance_function(target)
    return min(numbers, key=distance)

numbers = [1, 2, 5, 6, 4]
target = 8

result = nearest_number(numbers, target)

print("Список:", numbers)
print("Целевое число:", target)
print("Эң жакын сан:", result)