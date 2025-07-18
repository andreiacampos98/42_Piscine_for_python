import sys
from typing import Iterator


def ft_tqdm(lst: range) -> Iterator[int]:
    """My own tqdm function, Creates a load bar."""
    total = len(lst)
    for i, item in enumerate(lst, 1):
        percentage = int((i/total) * 100)
        bar = '=' * (percentage // 2) + '>' + ' ' * ((100 - percentage) // 2)
        sys.stdout.write(f'\r{percentage}% |{bar}| {i}/{total}')
        yield item
    return
