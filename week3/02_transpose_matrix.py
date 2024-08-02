def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    
    transpose: list[list[int]] = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

def print_matrix(matrix: list[list[int]])->None:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print("") 

def main():
    matrix:list[list[int]] = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
    ]
    
    result = transpose_matrix(matrix)
    print_matrix(result)

if __name__ == "__main__":
    main()
