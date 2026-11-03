import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [round(e/ total, 4) for e in exps]