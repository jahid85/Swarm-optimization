import numpy as np
# Number of Particles
number_of_particles = 20

# Objective Function


def objective_function(x, y):
    return (x**2 + y**2)


# Parameters
w = 0.7
c1 = 1.5
c2 = 0

# Search Space
x_max = 10
x_min = 10

# Velocity Range
v_max = 10
v_min = -10

# Random Initialization
X = np.random.uniform(-1, 1, (number_of_particles, 2))
V = np.random.uniform(-1, 1, (number_of_particles, 2))*0.1
print(X)
p_best = X
p_best_fit = objective_function(X[:, 0], X[:, 1])
print(p_best_fit)
g_best = X[np.argmin(p_best_fit)]
g_best_fit = objective_function(g_best[0], g_best[1])
# print(X)
# print(V)
# print(g_best)


def update():
    global X, V, p_best, p_best_fit, g_best, g_best_fit
    r1, r2 = np.random.rand(), np.random.rand()
    V = w*V + c1*r1*(p_best - X) + c2*r2*(g_best-X)
    for i in range(number_of_particles):
        if V[i][0] > v_max:
            V[i][0] = v_max
        if V[i][1] > v_max:
            V[i][1] = v_max
        elif V[i][0] < v_min:
            V[i][0] = v_min
        elif V[i][1] < v_min:
            V[i][1] = v_min
    # print(V)
    # print('\n\n\n')
    X = X + V

    new_fit = np.random.uniform(-1, 1, number_of_particles)*10
    for i in range(number_of_particles):
        new_fit[i] = objective_function(X[i][0], X[i][1])
    for i in range(number_of_particles):
        if new_fit[i] < p_best_fit[i]:
            p_best[i] = X[i]
            p_best_fit[i] = new_fit[i]
        if p_best_fit[i] < g_best_fit:
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
