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