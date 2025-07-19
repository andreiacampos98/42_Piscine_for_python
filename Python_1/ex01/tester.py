from array2D import slice_me

family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
try:
    print(slice_me(family, 0, 2))
except Exception as e:
    print(f"{e}")

try:
    print(slice_me(family, 1, -2))
except Exception as e:
    print(f"{e}")

family_1 = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
try:
    print(slice_me(family_1, 1, 3))
except Exception as e:
    print(f"{e}")

family_2 = "Ola"
try:
    print(slice_me(family_2, 0, 2))
except Exception as e:
    print(f"{e}")

family_3 = [[1.80, 78.4],
            [2.15, 102.7, 11.6],
            [2.10, 98.5],
            [1.88, 75.2]]
try:
    print(slice_me(family_3, 0, 2))
except Exception as e:
    print(f"{e}")
