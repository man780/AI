"""Обучение методом градиентного спуска с несколькими входами и выходами"""

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

# Обобщение градиентного спуска для обучения сетей произвольной величины

weights = [[0.1, 0.1, -0.3],# травмы?
            [0.1, 0.2, 0.0], # победа? 
            [0.0, 1.3, 0.1] ]# печаль?

def vect_mat_mul(vect,matrix): 
    assert(len(vect) == len(matrix)) 
    output = [0,0,0]
    for i in range(len(vect)): 
        output[i] = w_sum(vect,matrix[i]) 
    return output

def neural_network(input, weights): 
    pred = vect_mat_mul(input,weights) 
    return pred


## 2. ПРОГНОЗ: получение прогноза и вычисление ошибки и разности
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
  
hurt = [0.1, 0.0, 0.0, 0.1] 
win = [ 1, 1, 0, 1] 
sad = [0.1, 0.0, 0.1, 0.2]

alpha = 0.01

input = [toes[0],wlrec[0],nfans[0]] 
true = [hurt[0], win[0], sad[0]]

pred = neural_network(input,weights)

error = [0, 0, 0] 
delta = [0, 0, 0]

for i in range(len(true)):
    error[i] = (pred[i] - true[i]) ** 2 
    delta = pred[i] - true[i]

## 3. СРАВНЕНИЕ: вычисление каждого приращения weight_delta и коррекция каждого веса
def outer_prod(vec_a, vec_b):
    out = zeros_matrix(len(a), len(b))
    for i in range(len(a)): 
        for j in range(len(b)):
            out[i][j] = vec_a[i]*vec_b[j] 
    return out
input = [toes[0],wlrec[0], nfans[0]] 
true = [hurt[0], win[0], sad[0]]
pred = neural_network(input,weights)
error = [0, 0, 0] 
delta = [0, 0, 0]

for i in range(len(true)):
    error[i] = (pred[i] - true[i]) ** 2 
    delta = pred[i] - true[i]
    weight_deltas = outer_prod(input,delta)