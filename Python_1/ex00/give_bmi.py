def give_bmi(height: list[int | float], weight: list[int | float]) \
                -> list[int | float]:
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    bmi_list = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight elements must be int or float.")
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        if w <= 0:
            raise ValueError("Weight must be greater than zero.")
        bmi = w / (h * h)
        bmi_list.append(bmi)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    limit_list = []
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI list must contain only int or float values.")
        if b <= limit:
            limit_list.append(False)
        else:
            limit_list.append(True)
    return limit_list
