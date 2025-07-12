import sys


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst, 1):
        percentage = int((i/total) * 100)
        bar = '=' * (percentage // 2) + '>' + ' ' * ((100 - percentage) // 2)
        sys.stdout.write(f'\r{percentage}% |{bar}|{i}/{total}')
        yield item
    return
