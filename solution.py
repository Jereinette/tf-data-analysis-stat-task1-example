import pandas as pd
import numpy as np
import math


chat_id = 402739329 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    total_lamps = np.sum(x)
    lambda_ = total_lamps / (len(x) * 4)
    return lambda_
