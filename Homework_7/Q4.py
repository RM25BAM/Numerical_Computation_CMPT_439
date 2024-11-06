import os, numpy as np, matplotlib.pyplot as plt 
plt.style.use('seaborn-v0_8-pastel')
def fun_input(expression):
    return eval("lambda x: " + expression) 
def Lagrange(z, x, f):
    n = len(x)
    Interpolated_Value = 0 
    for i in range(n):
        Lagrangian = 1  
        for j in range(n):
            if j != i:
                if x[i] == x[j]:
                    print("Error: Duplicate x-coordinates detected, which causes division by zero.")
                    return None
                Lagrangian *= ((z - x[j]) / (x[i] - x[j])) 
        Interpolated_Value += Lagrangian * f[i]  
    return Interpolated_Value
def plot_interpolation(x, f, z, interpolated_value, figure_name):
    x_range = np.linspace(min(x), max(x), 500)
    y_range = [Lagrange(xi, x, f) for xi in x_range]
    output_dir = f'./Homework_7/Screenshot/Problem_d'
    os.makedirs(output_dir, exist_ok=True)
    plt.plot(x_range, y_range, label="Lagrange Interpolating Polynomial", linestyle="--", linewidth=1)  
    plt.scatter(x, f, color="red", label="Given Points", s=30) 
    plt.scatter(z, interpolated_value, color="blue", label=f"Interpolated value at z = {z}", marker='x', s=50) 
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Lagrange Interpolation")
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, figure_name))
    plt.clf()
def main():
    while True:
        print("Lagrange Interpolation")
        x = list(map(float, input("Enter the x-coordinates (comma-separated): ").split(',')))
        f = list(map(float, input("Enter the corresponding y-coordinates (comma-separated): ").split(',')))
        if len(x) != len(f):
            print("Error: The x and y arrays must have the same number of elements.")
            return main()
        z = float(input("Enter the point at which you want to interpolate: "))
        cases = [
            ("First_Run", x[:3], f[:3]),
            ("Second_Run", x[:4], f[:4]),
            ("Third_Run", x[1:], f[1:]),
            ("Forth_Run", x, f)
        ]
        
        for label, x_subset, f_subset in cases:
            val = Lagrange(z, x_subset, f_subset)
            plot_interpolation(x_subset, f_subset, z, val, figure_name=label)
            print(f"Interpolated value at {z} with '{label.replace('_', ' ')}' points: {val}\n")
        cont = input('Would you like to continue:(Y/N) ')
        if cont == 'N' or cont == 'n':
            break
        if cont == 'Y' or cont == 'y':
            continue
main()
