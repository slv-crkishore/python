from pathlib import Path
import glob
base_path = Path(r"D:\my_prog\RuleCreation.csv")
m = Path(r"D:\my_prog")
print(base_path.stem)
# print(list(base_path.iterdir()))
print(base_path.parent.parent)
# breakpoint()

for i in base_path.parent.iterdir():
    print(i.name)


print(m.rglob(), "*.csv")
