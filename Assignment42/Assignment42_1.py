import math

def main():

    data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]
    X_new = float(input("Enter the X coordinate: "))
    Y_new = float(input("Enter the Y coordinate: "))

    distances = []

    for p, x, y, label in data:
        distance = math.sqrt((X_new-x)**2 + (Y_new - y)**2)
        distances.append((distance, p, label))

    distances.sort()

    print("\nDistances from the new point:")

    for distance, point, label in distances:
        print(f"{point}: Distance = {distance}, Label: {label}")

    k = 3
    nearest_neighbours = distances[:k]

    print(f"\n{k} nearest neighbours: ")

    for distance, point, label in nearest_neighbours:
        print(f"{point}: Distance: {distance:.2f}, Label: {label}")

    red_count = 0
    blue_count = 0

    for label in nearest_neighbours:
        if label == 'Red':
            red_count +=1
        elif label == "Blue":
            blue_count +=1 

    if red_count>blue_count:
        prediction = 'Red'
    else:
        prediction = 'Blue'

    print(f"Predicted class: {prediction}")

if __name__ == "__main__":
    main()