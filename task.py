import numpy as np
# Number of Particles
number_of_particles = 200

# Objective Function


def objective_function(x):
    return (x**3 - 10*(x**2)+15)


# Parameters
w = 0.7
c1 = 1.5
c2 = 1.3

# Search Space
x_max = 10
x_min = 10

# Velocity Range
v_max = 10
v_min = -10

# Random Initialization
X = np.random.uniform(-1, 1, number_of_particles)*10
V = np.random.uniform(-1, 1, number_of_particles)*0.01

p_best = X
p_best_fit = objective_function(X)

g_best = X[np.argmin(p_best_fit)]
g_best_fit = objective_function(g_best)
# print(X)
# print(V)
# print(g_best)


def update():
    global X, V, p_best, p_best_fit, g_best, g_best_fit
    r1, r2 = np.random.rand(), np.random.rand()
    V = w*V + c1*r1*(p_best - X) + c2*r2*(g_best-X)
    for i in range(number_of_particles):
        if V[i] > v_max:
            V[i] = v_max
        elif V[i] < v_min:
            V[i] = v_min
    # print(V)
    # print('\n\n\n')
    X = X + V

    new_fit = objective_function(X)
    for i in range(number_of_particles):
        if new_fit[i] >p_best_fit[i]:
            p_best[i] = X[i]
            p_best_fit[i] = new_fit[i]
        if p_best_fit[i] > g_best_fit:
            g_best_fit = p_best_fit[i]
            g_best = p_best[i]


# number of iterations
number_of_iter = 100
for i in range(number_of_iter):
    update()
    print(
        f'Iteration {i+1}: Swarm Fitness = {g_best_fit} and Best Particle = {g_best}')

print(
    f'\n\n\n\nFinal Swarm Fitness = {g_best_fit} and Best Particle = {g_best}')
