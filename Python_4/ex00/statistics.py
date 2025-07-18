

def ft_statistics(*args, **kwargs) -> None:
    print(args)
    for k, val in kwargs.items():
        if val == "mean":
            mean(args)
        elif val =="median":
            median(args)
        elif val=="std":
            std(args)
        elif val=="var":
            var(args)
        elif val=="quartile":
            quartile(args)
        print(k, val)
