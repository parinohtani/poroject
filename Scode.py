import random

# تعداد وزرا (N)
N = 8

# ایجاد جمعیت اولیه
def create_population(size):
    return [random.sample(range(N), N) for _ in range(size)]

# محاسبه تناسب (fitness)
def fitness(board):
    conflicts = 0
    # بررسی تعارضات بین وزرا
    for i in range(N):
        for j in range(i + 1, N):
            # بررسی تعارضات افقی و قطری
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return 28 - conflicts  # حداکثر تعداد تعارضات 28 است

# انتخاب (انتخاب چرخ رولت)
def selection(population):
    weights = [fitness(board) for board in population]  # محاسبه تناسب هر فرد
    total_fitness = sum(weights)  # مجموع تناسب‌ها
    # محاسبه احتمال انتخاب
    probabilities = [w / total_fitness for w in weights]
    # انتخاب فرد بر اساس احتمال
    return population[random.choices(range(len(population)), probabilities)[0]]

# ترکیب (Crossover)
def crossover(parent1, parent2):
    point = random.randint(1, N - 1)  # انتخاب نقطه ترکیب
    child = parent1[:point] + [x for x in parent2 if x not in parent1[:point]]  # ترکیب والدین
    # تکمیل فرزند با وزرای باقی‌مانده
    for i in range(N):
        if i not in child:
            child.append(i)
    return child

# جهش (Mutation)
def mutate(board, mutation_rate):
    # بررسی احتمال جهش
    if random.random() < mutation_rate:
        i = random.randint(0, N - 1)  # انتخاب یک وزیر تصادفی
        board[i] = random.randint(0, N - 1)  # تغییر موقعیت وزیر
    return board

