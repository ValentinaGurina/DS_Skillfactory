import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число,если оно больше загаданного,
    то в следующем дропе устанавливаем его в качестве максимального значения, 
    если меньше - то устанавливаем его как минимальное значение следующего дропа.
    
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    min_num = 1
    max_num = 101
    predict = np.random.randint(min_num, max_num)
    
    while number != predict:
        count += 1
        if number > predict:
            min_num = predict
            predict = np.random.randint(min_num, max_num)
        elif number < predict:
            max_num = predict
            predict = np.random.randint(min_num, max_num)
    # Ваш код заканчивается здесь

    return count