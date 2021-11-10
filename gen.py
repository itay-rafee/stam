import random


# foo(x,y,z) = 6⋅x^3 + 9⋅y^2 + 90⋅z - 25
def foo(x, y, z):
    return 6 * x ** 3 + 9 * y ** 2 + 90 * z - 25


t = foo(0.9594219559145795, 0.9610165051203599, 0.9598798164287896)
print(t)
def genetic_algorithm():
    def fitness(x, y, z):
        ans = foo(x, y, z)

        if ans == 0:
            return 99999
        else:
            return abs(1 / ans)

    solution = []

    for s in range(1000):
        solution.append((random.uniform(0, 10000),
                         random.uniform(0, 10000),
                         random.uniform(0, 10000)))

    for i in range(10000):
        ranked_solution = []
        for s in solution:
            ranked_solution.append((fitness(s[0], s[1], s[2]), s))
        ranked_solution.sort()
        ranked_solution.reverse()

        print(f"=== Gen {i} best solution === ")
        print(ranked_solution[0])

        if ranked_solution[0][0] > 99999:
            break

        best_solution = ranked_solution[:100]

        element = []
        for s in best_solution:
            element.append(s[1][0])
            element.append(s[1][1])
            element.append(s[1][2])

        new_gen = []
        for _ in range(1000):
            e1 = random.choice(element) * random.uniform(0.99, 1.01)
            e2 = random.choice(element) * random.uniform(0.99, 1.01)
            e3 = random.choice(element) * random.uniform(0.99, 1.01)

            new_gen.append((e1, e2, e3))

        solution = new_gen


# genetic_algorithm()
