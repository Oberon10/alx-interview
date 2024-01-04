def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return triangle

# This shows how the function prints
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)

