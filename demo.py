import random

# Khai báo các tham số cho thuật toán
POPULATION_SIZE = 50  # Kích thước quần thể
NUM_GENERATIONS = 100  # Số lượng thế hệ tối đa
MUTATION_RATE = 0.01  # Tỷ lệ đột biến
NUM_CITIES = 50  # số thành phố

# Khởi tạo danh sách các thành phố
# mỗi phần tử là tọa độ của thành phố trong mặt phẳng 2 chiều


def generate_random_cities(num_cities):
    cities = [(random.uniform(0, 10), random.uniform(0, 10))
              for _ in range(num_cities)]
    return cities


cities = generate_random_cities(NUM_CITIES)


def print_cities(cities):
    for city in cities:
        print(city)


print_cities(cities)


# Hàm tính khoảng cách giữa hai thành phố
def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5


# Hàm tính khoảng cách của một cá thể
def fitness(individual):
    distance_sum = 0
    for i in range(len(individual) - 1):
        distance_sum += distance(cities[individual[i]],
                                 cities[individual[i+1]])
    distance_sum += distance(cities[individual[-1]], cities[individual[0]])
    return distance_sum


# Hàm tạo ra một cá thể ngẫu nhiên
def create_individual():
    return random.sample(range(len(cities)), len(cities))


# Khởi tạo quần thể ban đầu
population = [create_individual() for i in range(POPULATION_SIZE)]

# Bắt đầu vòng lặp qua các thế hệ
for generation in range(NUM_GENERATIONS):

    # Đánh giá độ phù hợp của các cá thể
    fitnesses = [fitness(individual) for individual in population]

    # Lựa chọn các cá thể để lai tạo
    selected_parents = random.choices(
        population, weights=[1/fitness for fitness in fitnesses], k=POPULATION_SIZE)

    # Lai tạo để tạo ra các cá thể con
    offspring = []
    for i in range(POPULATION_SIZE):
        parent1, parent2 = random.sample(selected_parents, 2)
        crossover_point = random.randint(1, len(cities)-1)
        child = parent1[:crossover_point] + \
            [x for x in parent2 if x not in parent1[:crossover_point]]
        offspring.append(child)

    # Đột biến để tạo ra sự đa dạng trong quần thể
    for individual in offspring:
        if random.random() < MUTATION_RATE:
            mutation_point1, mutation_point2 = random.sample(
                range(len(cities)), 2)
            individual[mutation_point1:mutation_point2] = reversed(
                individual[mutation_point1:mutation_point2])

    # Thay thế các cá thể cũ bằng các cá thể mới
    new_population = offspring + population
    fitnesses = [fitness(individual) for individual in new_population]
    sorted_population = [x for _, x in sorted(zip(fitnesses, new_population))]
    population = sorted_population[:POPULATION_SIZE]

    # Tìm cá thể có giá trị mục tiêu tối ưu nhất trong quần thể
    best_individual = min(population, key=fitness)

#  In ra lời giải tốt nhất
print("Best route found:")
for city in best_individual:
    print(cities[city])
print("Total distance: ", fitness(best_individual))
