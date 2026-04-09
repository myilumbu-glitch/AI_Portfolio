position = [12, 8]
velocity = [3, -1]
student_scores = [88, 91, 79]

print("Position:", position)
print("Velocity:", velocity)
print("Student Scores:", student_scores)

#Adding two vectors

position = [4, 8]
movement = [2, -5]

result = [position[0] + movement[0], position[1] + movement[1]]
print("New position:", result)

#Adding three vectors
def add_vectors(v1, v2, v3):
    if len(v1) != len(v2) or len(v1) != len(v3):  #for error handling
        return "Vectors must be of the same length"
    results = []

    for i in range(len(v1)):
        results.append(v1[i] + v2[i] + v3[i])
    return results

print("New position:", add_vectors([2, 3, 6], [4, 5, 7], [1, 2, 3]))
print("New velocity:", add_vectors([1, 2, 3], [4, 5, 6], [7, 8, 9]))