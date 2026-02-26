"""
Converts all CodingBat-Java problems and testers into Python equivalents
in a CodingBat-Python folder.
"""

import os
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JAVA_DIR = os.path.join(SCRIPT_DIR, "data", "CodingBat-Java")
PY_DIR = os.path.join(SCRIPT_DIR, "data", "CodingBat-Python")


def camel_to_snake(name):
    """Convert camelCase to snake_case."""
    s1 = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    s2 = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s1)
    return s2.lower()


def java_val_to_python(val):
    """Convert a Java literal to Python literal."""
    val = val.strip()
    if val == "true":
        return "True"
    if val == "false":
        return "False"
    if val == "null":
        return "None"
    # Java arrays {1, 2, 3} → Python lists [1, 2, 3]
    if val.startswith('{') and val.endswith('}'):
        inner = val[1:-1]
        return '[' + inner + ']'
    # new int[]{...} → [...]
    m = re.match(r'new\s+\w+\[\]\s*\{(.*)\}', val)
    if m:
        return '[' + m.group(1) + ']'
    return val


def convert_example_line(line):
    """Convert a Java example line to Python style."""
    # e.g. sleepIn(false, false) → true  =>  sleep_in(False, False) → True
    line = line.replace("true", "True").replace("false", "False").replace("null", "None")
    # Convert arrays: {1, 2} → [1, 2]
    line = re.sub(r'\{([^}]*)\}', r'[\1]', line)
    return line


def extract_from_java_problem(filepath):
    """Extract description, examples, function name, and params from a problem .java file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract description (lines starting with " * " between the first /** and */)
    desc_lines = []
    examples = []
    in_examples = False
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('* Examples:'):
            in_examples = True
            continue
        if line.startswith('*/'):
            break
        if in_examples and line.startswith('*'):
            ex = line.lstrip('* ').strip()
            if ex and '→' in ex:
                examples.append(ex)
        elif line.startswith('*') and not line.startswith('/**'):
            txt = line.lstrip('* ').strip()
            if txt and not txt.startswith('CodingBat') and not txt.startswith('http') and not txt.startswith('SOLUTION'):
                desc_lines.append(txt)

    description = ' '.join(desc_lines)

    # Extract function name and params from the method signature
    # Pattern: public TYPE funcName(TYPE param, TYPE param2) {
    match = re.search(
        r'public\s+\w+(?:\[\])?\s+(\w+)\(([^)]*)\)',
        content
    )
    func_name = ""
    params = []
    if match:
        func_name = match.group(1)
        params_str = match.group(2).strip()
        if params_str:
            for p in params_str.split(','):
                p = p.strip()
                parts = p.split()
                if len(parts) >= 2:
                    params.append(parts[-1])  # just the param name

    return {
        "description": description,
        "examples": examples,
        "func_name": func_name,
        "params": params,
    }


def extract_test_cases_from_tester(filepath):
    """Extract test cases from a Tester.java file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    tests = []
    # Find all FAIL messages which contain the test case info
    # Pattern: FAIL: funcName(args) expected result
    for match in re.finditer(r'FAIL:\s*(\w+)\((.+?)\)\s*expected\s*(.+?)\\?"', content):
        func_name = match.group(1)
        args = match.group(2)
        expected = match.group(3)
        tests.append((func_name, args, expected))

    return tests


def java_args_to_python(args_str):
    """Convert Java argument values to Python."""
    # Handle arrays, booleans, etc.
    result = args_str
    result = result.replace("true", "True").replace("false", "False").replace("null", "None")
    # Java arrays {1, 2, 3} → [1, 2, 3]
    result = re.sub(r'\{([^}]*)\}', r'[\1]', result)
    # new int[]{...}
    result = re.sub(r'new\s+\w+\[\]\s*\{([^}]*)\}', r'[\1]', result)
    return result


def java_expected_to_python(val):
    """Convert expected value from Java to Python."""
    val = val.strip()
    if val == "true":
        return "True"
    if val == "false":
        return "False"
    if val == "null":
        return "None"
    if val.startswith('{') and val.endswith('}'):
        return '[' + val[1:-1] + ']'
    m = re.match(r'new\s+\w+\[\]\s*\{(.*)\}', val)
    if m:
        return '[' + m.group(1) + ']'
    return val


def infer_python_default(examples):
    """Infer a Python default return value from examples."""
    if not examples:
        return "None"
    # Check the first example's result
    first = examples[0]
    match = re.search(r'→\s*(.+)', first)
    if match:
        result = match.group(1).strip()
        if result in ("true", "false", "True", "False"):
            return "False"
        if result.startswith('"'):
            return '""'
        if result.startswith('{') or result.startswith('['):
            return '[]'
        try:
            int(result)
            return "0"
        except ValueError:
            try:
                float(result)
                return "0.0"
            except ValueError:
                pass
    return "None"


def generate_python_problem(data, category):
    """Generate a Python problem file."""
    func_name = camel_to_snake(data['func_name']) if data['func_name'] else "solve"
    params = ", ".join(data['params']) if data['params'] else ""
    default = infer_python_default(data['examples'])

    lines = []
    lines.append(f'"""')
    lines.append(f'CodingBat > Python > {category} > {data["func_name"]}')
    lines.append(f'')
    # Word wrap description
    if data['description']:
        words = data['description'].split()
        line = ""
        for w in words:
            if len(line) + len(w) + 1 > 78:
                lines.append(line)
                line = w
            else:
                line = line + " " + w if line else w
        if line:
            lines.append(line)

    if data['examples']:
        lines.append('')
        lines.append('Examples:')
        for ex in data['examples']:
            py_ex = convert_example_line(ex)
            lines.append(f'  {py_ex}')
    lines.append(f'"""')
    lines.append(f'')
    lines.append(f'')
    lines.append(f'def {func_name}({params}):')
    lines.append(f'    # TODO: implement')
    lines.append(f'    return {default}')
    lines.append(f'')

    return '\n'.join(lines), func_name


def generate_python_tester(func_name, java_func_name, test_cases):
    """Generate a Python test file."""
    py_func = func_name

    lines = []
    lines.append(f'"""')
    lines.append(f'Tester for {java_func_name} - CodingBat Python')
    lines.append(f'{len(test_cases)} test cases')
    lines.append(f'"""')
    lines.append(f'')
    # Import from the problem module
    lines.append(f'from {py_func} import {py_func}')
    lines.append(f'')
    lines.append(f'')
    lines.append(f'def run_tests():')
    lines.append(f'    passed = 0')
    lines.append(f'    failed = 0')
    lines.append(f'')

    for i, (jfn, args, expected) in enumerate(test_cases):
        py_args = java_args_to_python(args)
        py_expected = java_expected_to_python(expected)

        lines.append(f'    # Test {i+1}')
        lines.append(f'    result = {py_func}({py_args})')
        lines.append(f'    if result == {py_expected}:')
        lines.append(f'        passed += 1')
        lines.append(f'    else:')

        display_args = py_args.replace("'", "\\'")
        lines.append(f'        print(f"FAIL: {py_func}({display_args}) expected {py_expected}, got {{result}}")')
        lines.append(f'        failed += 1')
        lines.append(f'')

    lines.append(f'    print(f"{py_func}: {{passed}}/{{passed + failed}} tests passed.")')
    lines.append(f'    if failed == 0:')
    lines.append(f'        print("All tests passed!")')
    lines.append(f'')
    lines.append(f'')
    lines.append(f'if __name__ == "__main__":')
    lines.append(f'    run_tests()')
    lines.append(f'')

    return '\n'.join(lines)


def main():
    print(f"Java source: {JAVA_DIR}")
    print(f"Python output: {PY_DIR}")
    os.makedirs(PY_DIR, exist_ok=True)

    total_problems = 0
    total_tests = 0

    categories = sorted(os.listdir(JAVA_DIR))
    for category in categories:
        cat_java = os.path.join(JAVA_DIR, category)
        if not os.path.isdir(cat_java):
            continue

        print(f"\n{'='*60}")
        print(f"  Category: {category}")
        print(f"{'='*60}")

        cat_py = os.path.join(PY_DIR, category)
        os.makedirs(cat_py, exist_ok=True)

        # Find all problem files (not Tester, not Solution)
        problem_files = sorted(glob.glob(os.path.join(cat_java, "*.java")))
        problem_files = [f for f in problem_files
                         if not f.endswith("Tester.java") and not f.endswith("Solution.java")]

        print(f"  Found {len(problem_files)} problems\n")

        for pf in problem_files:
            basename = os.path.splitext(os.path.basename(pf))[0]
            tester_path = os.path.join(cat_java, f"{basename}Tester.java")

            print(f"  {basename}...", end=" ", flush=True)

            try:
                data = extract_from_java_problem(pf)
                if not data['func_name']:
                    data['func_name'] = basename[0].lower() + basename[1:]

                # Generate Python problem file
                py_content, py_func_name = generate_python_problem(data, category)
                py_filename = f"{py_func_name}.py"
                with open(os.path.join(cat_py, py_filename), "w", encoding="utf-8") as f:
                    f.write(py_content)

                # Generate Python test file
                tc_count = 0
                if os.path.exists(tester_path):
                    test_cases = extract_test_cases_from_tester(tester_path)
                    tc_count = len(test_cases)
                    if test_cases:
                        test_content = generate_python_tester(py_func_name, data['func_name'], test_cases)
                        test_filename = f"{py_func_name}_test.py"
                        with open(os.path.join(cat_py, test_filename), "w", encoding="utf-8") as f:
                            f.write(test_content)

                total_problems += 1
                total_tests += tc_count
                print(f"OK ({tc_count} tests)")

            except Exception as e:
                print(f"ERROR: {e}")

    print(f"\n{'='*60}")
    print(f"  DONE! {total_problems} problems, {total_tests} test cases total.")
    print(f"  Output: {PY_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
