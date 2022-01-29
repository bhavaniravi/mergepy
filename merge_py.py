import ast
from collections import namedtuple
import sys, inspect, importlib
import astunparse
import glob


imports = []
classes = []
class_names = []

def get_imports(path):
    with open(path) as fh:        
       root = ast.parse(fh.read(), path)

    for node in ast.iter_child_nodes(root):
        print (node)
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):  
            module = node.module.split('.')
        elif isinstance(node, ast.ClassDef):
            class_names.append(node.name)
            source = astunparse.unparse(node)
            classes.append(source)
            continue
        else:
            continue
        

        for n in node.names:
            if not module:
                statement = f"import {n.name}"
            else:
                statement = f"from {'.'.join(module)} import {n.name}"
                if n.asname:
                    statement = statement + f"as {n.asname}" 
            
            imports.append(statement)
    return classes


input_folder_path = input("Input folder path: ") or "example/input"
output_file_path = input("Output file path with .py extension: ") or "example/output/eg.py"

print (glob.glob(f"{input_folder_path}/*.py"))
for f in glob.glob(f"{input_folder_path}/*.py"):
    print (f"Processing file :: {f}")
    get_imports(f)


with open(output_file_path, "w") as f:
    for i in imports:
        print(i, file=f)    

    for c in classes:
        print(c.replace("\\n", "\n"), file=f)