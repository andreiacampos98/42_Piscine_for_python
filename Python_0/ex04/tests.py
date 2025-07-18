import subprocess


tests = [
    ["14"],
    ["-5"],
    [],
    ["0"],
    ["Hi!"],
    ["13", "5"]
]

for args in tests:
    print(f"$ python3 whatis.py {' '.join(args)}")
    subprocess.run(["python3", "Python_0/ex04/whatis.py"] + args)
    print()
