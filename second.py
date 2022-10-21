weight = 0.5 
goal_pred = 0.8
input = 2
alpha = 0.1

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2 
    derivative = input * (pred - goal_pred) 
    weight = weight - (alpha * derivative)
    
    print(f"Weight: {weight}, Derivative: {derivative}")
    print(f"{iteration}, Error: {str(error)}  Prediction: {str(pred)}")
