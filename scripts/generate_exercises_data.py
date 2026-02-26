"""
Generates exercises_data.js from CodingBat-Java problem files.
Extracts test cases from the examples listed in the Java problem Javadocs (→ lines),
converting Java syntax to Python.
"""
import os, re, json, glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JAVA_DIR = os.path.join(SCRIPT_DIR, "data", "CodingBat-Java")
PY_DIR = os.path.join(SCRIPT_DIR, "data", "CodingBat-Python")
OUT = os.path.join(SCRIPT_DIR, "..", "exercises_data.js")

CATEGORIES = [
    "Warmup-1", "Warmup-2",
    "String-1", "String-2", "String-3",
    "Logic-1", "Logic-2",
    "Recursion-1", "Recursion-2",
]

def camel_to_snake(name):
    s1 = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    return re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s1).lower()

def java_to_python_value(val):
    """Convert a single Java value to Python."""
    val = val.strip()
    if val == "true": return "True"
    if val == "false": return "False"
    if val == "null": return "None"
    # Arrays: {1, 2, 3} → [1, 2, 3]
    if val.startswith('{') and val.endswith('}'):
        return '[' + val[1:-1] + ']'
    return val

def java_call_to_python(call_str, func_name):
    """Convert funcName(args) to python_func(args) with Python values."""
    py_func = camel_to_snake(func_name)
    # Extract the args portion
    match = re.match(r'\w+\((.+)\)$', call_str, re.DOTALL)
    if not match:
        return f"{py_func}()"
    args_str = match.group(1)
    
    # Convert Java values in args
    args_str = args_str.replace("true", "True").replace("false", "False").replace("null", "None")
    # Convert arrays
    args_str = re.sub(r'\{([^}]*)\}', r'[\1]', args_str)
    
    return f"{py_func}({args_str})"

def extract_from_java_file(filepath):
    """Extract problem data from a Java problem file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Get description
    desc_lines = []
    examples = []
    in_examples = False
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('*/'):
            break
        if line.startswith('* Examples:'):
            in_examples = True
            continue
        if in_examples and line.startswith('*'):
            ex = line.lstrip('* ').strip()
            if ex and '→' in ex:
                examples.append(ex)
        elif line.startswith('*') and not line.startswith('/**'):
            txt = line.lstrip('* ').strip()
            if txt and not txt.startswith('CodingBat') and not txt.startswith('http') and not txt.startswith('SOLUTION'):
                desc_lines.append(txt)
    
    description = ' '.join(desc_lines)
    
    # Get function name from method signature  
    match = re.search(r'public\s+\w+(?:\[\])?\s+(\w+)\(([^)]*)\)', content)
    java_func = match.group(1) if match else ""
    java_params = match.group(2).strip() if match else ""
    
    # Convert params to Python
    py_params = []
    if java_params:
        for p in java_params.split(','):
            p = p.strip()
            parts = p.split()
            if len(parts) >= 2:
                py_params.append(parts[-1])
    
    py_func = camel_to_snake(java_func) if java_func else ""
    
    # Build stub
    params_str = ", ".join(py_params)
    stub = f"def {py_func}({params_str}):\n    # TODO: implement\n    pass\n"
    
    # Convert examples to test cases
    tests = []
    for ex in examples:
        # Parse: funcName(args) → result
        m = re.match(r'(\w+)\((.+?)\)\s*→\s*(.+)', ex)
        if m:
            func = m.group(1)
            args_raw = m.group(2).strip()
            expected_raw = m.group(3).strip()
            
            # Convert args
            py_args = args_raw.replace("true", "True").replace("false", "False").replace("null", "None")
            py_args = re.sub(r'\{([^}]*)\}', r'[\1]', py_args)
            
            # Convert expected
            py_expected = java_to_python_value(expected_raw)
            
            py_call = f"{py_func}({py_args})"
            tests.append({"call": py_call, "expected": py_expected})
    
    # Convert description: replace Java-isms with Python equivalents
    description = description.replace("str.toUpperCase()", "str.upper()")
    description = description.replace("str.toLowerCase()", "str.lower()")
    description = description.replace("str.length()", "len(str)")
    description = description.replace("Math.abs(n)", "abs(n)")
    description = description.replace("String", "string")
    description = description.replace("boolean", "bool")
    
    return {
        "id": py_func,
        "name": py_func,
        "description": description,
        "stub": stub,
        "tests": tests,
        "java_func": java_func,
    }


def main():
    data = {"categories": []}
    total = 0
    total_tests = 0
    
    for cat in CATEGORIES:
        cat_data = {"name": cat, "problems": []}
        java_dir = os.path.join(JAVA_DIR, cat)
        
        if not os.path.isdir(java_dir):
            print(f"SKIP {cat}: directory not found")
            continue
        
        # Get all Java problem files (not Tester, not Solution)
        java_files = sorted(glob.glob(os.path.join(java_dir, "*.java")))
        java_files = [f for f in java_files 
                      if not f.endswith("Tester.java") and not f.endswith("Solution.java")]
        
        cat_tests = 0
        for jf in java_files:
            try:
                problem = extract_from_java_file(jf)
                if not problem["id"]:
                    continue
                
                # Remove java_func from output
                del problem["java_func"]
                
                cat_data["problems"].append(problem)
                total += 1
                cat_tests += len(problem["tests"])
            except Exception as e:
                print(f"  ERROR {os.path.basename(jf)}: {e}")
        
        data["categories"].append(cat_data)
        total_tests += cat_tests
        print(f"{cat}: {len(cat_data['problems'])} problems, {cat_tests} tests")
    
    # Write as JS
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// Auto-generated CodingBat exercises data\n")
        f.write("const EXERCISES_DATA = ")
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    
    print(f"\nDone! {total} problems, {total_tests} tests → {OUT}")


if __name__ == "__main__":
    main()
