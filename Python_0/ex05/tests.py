from building import main
import subprocess


tests = [
    ["Python 3.0, released in 2008, was a major revision that is not completely backward-\
compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."],
    ["What is the text to count?"],
    ["Hello World!"],
    ["Hello World!\r"],
    ["Hello World!", "Ola Andreia"]
]

for args in tests:
    print(f"$ python3 building.py {' '.join(args)}")
    subprocess.run(["python3", "Python_0/ex05/building.py"] + args)
    print()
