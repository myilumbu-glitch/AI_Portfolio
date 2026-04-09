def scalar_multiply(vectors, scalar):
    if not isinstance(scalar, (int, float)):
        return "Scalar must be a number"
    
    result = []

    for i in range(len(vectors)):
        result.append(scalar * vectors[i])
    
    return result


print("New quantity:", scalar_multiply([2, 3], 4))
print("New velocity:", scalar_multiply([1, 2, 6], -0.5))
print("Error:", scalar_multiply([1, 2], "no number here"))