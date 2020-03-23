import sys
from os.path import dirname,abspath
project_path =dirname(dirname(abspath(__file__)))
sys.path.append(project_path+"\\project1")
from calculator import add

print(add(4,5))