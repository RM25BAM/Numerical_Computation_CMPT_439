import numpy as np
def hadamard(N):
    if not (N & (N - 1) == 0) and N > 0:
        raise ValueError("N must be a power of 2")
    if N == 1:
        return np.array([[1]])
    else:
        smaller_H = hadamard(N // 2)
        top = np.hstack((smaller_H, smaller_H))
        bottom = np.hstack((smaller_H, -smaller_H))
        return np.vstack((top, bottom))
def hadamard_walsh(f):
    N = len(f)
    assert (N & (N - 1)) == 0, "Input length must be a power of 2."
    H = hadamard(N)
    return np.dot(H, f)
def inverse_hadamard_walsh(s):
    N = len(s)
    return hadamard_walsh(s) / N
def main():
    solution = {}
    predefined_vectors = {
    4: np.array([5, -3, 7, -1]),
    8: np.array([2, 4, -6, 8, -2, -4, 6, -8]),
    16: np.array([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]),
    }
    for n, vector in predefined_vectors.items():
        N = len(vector)
        f = vector
        s = hadamard_walsh(f)
        f_inverse = inverse_hadamard_walsh(s)
        solution[N] = {
            "original_vector": f,
            "transformed": s,
            "inverse_transformed": f_inverse,
            "recovered_correctly": np.allclose(f, f_inverse),
        }
    for N, result in solution.items():
        print(f"Results for N = {N}:")
        print("Original vector: ", result['original_vector'].tolist())
        print("Transformed vector:", result['transformed'].tolist())
        inverse_transformed_display = (
            result["inverse_transformed"].astype(int).tolist()
            if result["recovered_correctly"]
            else result["inverse_transformed"].tolist()
        )
        print(f"Inverse transformed (1/N): {inverse_transformed_display}")
        print(f"Recovered correctly: {'Yes' if result['recovered_correctly'] else 'No'}")
        print("{:-^20}".format("")) 
main()