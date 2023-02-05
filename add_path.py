from pyPath import MYPATH

my_path = MYPATH()
print("Adding piglatin - ", my_path.addfile_to_path("piglatin","piglatin",exe=True))
print("Adding main file - ", my_path.addfile_to_path("main.py","pig_latin_main_py.py"))

