# Чистая сеть с несколькими входами
def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

weights = [0.1, 0.2, -.1]

def neural_network(input, weights):
    pred = w_sum(input, weights)
    return pred

# ПРОГНОЗ + СРАВНЕНИЕ: получение прогноза, вычисление ошибки и разности
toes = [8.5 , 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2 , 1.3, 0.5, 1.0]

win_or_lose_binary = [1, 1, 0, 1] 
true = win_or_lose_binary[0]
input = [toes[0],wlrec[0],nfans[0]] 
pred = neural_network(input, weights) 
error = (pred - true) ** 2
delta = pred - true

print(f"input: {input}, pred: {pred}")
print(f"error: {error}, delta: {delta}")

# ОБУЧЕНИЕ: вычисление всех приращений weight_delta и добавление их в каждый вес
def ele_mul(number,vector):
    output = [0,0,0]
    assert(len(output) == len(vector))
    for i in range(len(vector)): 
        output[i] = number * vector[i]
    return output


input = [toes[0],wlrec[0],nfans[0]] 
pred = neural_network(input, weights) 
error = (pred - true) ** 2
delta = pred - true
weight_deltas = ele_mul(delta,input)

print(f"input: {input}, pred: {pred}")
print(f"error: {error}, delta: {delta}")
print(f"weight_deltas: {weight_deltas}")

# ОБУЧЕНИЕ: корректировка весов
input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(input, weights)
error = (pred - true) ** 2
delta = pred - true
weight_deltas = ele_mul(delta,input)
alpha = 0.01
for i in range(len(weights)):
    weights[i] -= alpha * weight_deltas[i]

print("Weights:" + str(weights))
print("Weight Deltas:" + str(weight_deltas))
