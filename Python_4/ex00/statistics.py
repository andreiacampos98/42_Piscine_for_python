def ft_mean(args: tuple):
    return sum(args)/len(args)


def ft_median(args: tuple):
    list_args = sorted(args)
    count = len(list_args)
    mid = count // 2
    if count % 2 == 0:
        return ((list_args[mid] + list_args[mid - 1]) / 2)
    else:
        return (list_args[mid])


def ft_var(args: tuple):
    mean = ft_mean(args)
    new_list = [(x - mean)**2 for x in args]
    return (sum(new_list)/len(new_list))


def ft_std(args: tuple):
    if not args:
        print("ERROR")
        return
    return (ft_var(args) ** 0.5)


def ft_quartile(args: tuple):
    list_args = sorted(args)
    count = len(list_args)
    q_1 = count // 4
    if q_1 % 2 == 0:
        q_1_value = ((list_args[q_1] + list_args[q_1 - 1]) / 2)
    else:
        q_1_value = (list_args[q_1])
    q_3 = (count // 4) * 3
    if q_3 % 2 == 0:
        q_3_value = ((list_args[q_3] + list_args[q_3 - 1]) / 2)
    else:
        q_3_value = (list_args[q_3])
    return (q_1_value, q_3_value)


def ft_statistics(*args, **kwargs) -> None:
    if not args:
        for _ in kwargs:
            print("ERROR")
        return
    for k, val in kwargs.items():
        if val == "mean":
            print(f"mean: {ft_mean(args)}")
        elif val == "median":
            print(f"median: {ft_median(args)}")
        elif val == "std":
            print(f"std: {ft_std(args)}")
        elif val == "var":
            print(f"var: {ft_var(args)}")
        elif val == "quartile":
            print(f"quartile: {ft_quartile(args)}")
