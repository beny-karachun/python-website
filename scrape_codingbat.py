"""
CodingBat Java Problem Scraper - Full Test Cases Edition
Scrapes all problems from specified categories, submits dummy code to get ALL
test cases (not just the 3 visible examples), and saves everything as .java files.
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import time
import html as html_module
import urllib.parse
from datetime import datetime

BASE_URL = "https://codingbat.com"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CodingBat-Java")

CATEGORIES = [
    "Warmup-1", "Warmup-2",
    "String-1", "String-2", "String-3",
    "Logic-1", "Logic-2",
    "Recursion-1", "Recursion-2",
]

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})


def get_html(url):
    """Fetch raw HTML and soup."""
    resp = SESSION.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text, BeautifulSoup(resp.text, "html.parser")


def get_problem_links(category):
    """Get all problem (name, url, id) tuples from a category page."""
    url = f"{BASE_URL}/java/{category}"
    _, soup = get_html(url)
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/prob/"):
            name = a.get_text(strip=True)
            prob_id = href.replace("/prob/", "")
            if name:
                links.append((name, BASE_URL + href, prob_id))
    return links


def submit_code_and_get_tests(prob_id, code):
    """Submit code to CodingBat's /run endpoint and extract all test cases from results."""
    adate = datetime.utcnow().strftime("%Y%m%d-%H%M%Sz")
    data = {
        "id": prob_id,
        "code": code,
        "cuname": "",
        "owner": "",
        "adate": adate,
    }
    resp = SESSION.post(f"{BASE_URL}/run", data=data, timeout=15)
    resp.raise_for_status()
    return resp.text


def extract_all_tests_from_results(results_html):
    """Parse the results HTML to extract all test cases (Expected column)."""
    soup = BeautifulSoup(results_html, "html.parser")
    tests = []
    
    # Results are in a table with class "out"
    table = soup.find("table")
    if not table:
        return tests
    
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 1:
            # First cell contains: funcName(args) → expected
            expected_text = cells[0].get_text(strip=True)
            if "→" in expected_text or "\u2192" in expected_text:
                tests.append(expected_text)
    
    return tests


def build_dummy_code(func_name, examples, raw_html):
    """Build minimal code that will compile (so CodingBat shows all test cases)."""
    return_type = infer_return_type(examples)
    
    # Try to extract parameter types from page examples
    params = infer_params(examples)
    
    default_return = {
        "boolean": "false",
        "int": "0",
        "double": "0.0",
        "String": '""',
        "int[]": "new int[]{}",
    }.get(return_type, "null")
    
    return f"public {return_type} {func_name}({params}) {{ return {default_return}; }}"


def extract_problem(url, prob_id, name):
    """Extract problem description, submit dummy code, get ALL test cases."""
    raw_html, soup = get_html(url)

    # --- Description ---
    desc = ""
    p_tag = soup.find("p", class_="max2")
    if p_tag:
        desc = p_tag.get_text(strip=True)

    # --- Visible examples (for type inference) ---
    visible_examples = []
    example_regex = re.compile(
        r'(\w+\([^)]*\))\s*'
        r'(?:\u2192|&rarr;|&#8594;)'
        r'\s*'
        r'('
            r'&quot;[^&]*&quot;'
            r'|"[^"]*"'
            r'|\{[^}]*\}'
            r'|[^\s<]+'
        r')',
        re.UNICODE
    )
    for m in example_regex.finditer(raw_html):
        call = html_module.unescape(m.group(1))
        result = html_module.unescape(m.group(2))
        ex = f"{call} → {result}"
        if ex not in visible_examples:
            visible_examples.append(ex)

    # --- Solution from onclick ---
    solution = ""
    for btn in soup.find_all("button"):
        onclick = btn.get("onclick", "")
        btn_text = btn.get_text(strip=True)
        if "unescape" in onclick and "Solution" in btn_text:
            match = re.search(r"unescape\('([^']*)'\)", onclick)
            if match:
                decoded = urllib.parse.unquote(match.group(1))
                decoded = re.sub(r'<[^>]+>', '', decoded)
                decoded = html_module.unescape(decoded)
                solution = decoded.strip()
                break

    # --- Submit code to get ALL test cases ---
    all_tests = []
    
    # Try using the solution first (will give correct output and reveal all tests)
    submit_code = solution if solution else None
    
    if not submit_code:
        # Build a dummy that compiles
        submit_code = build_dummy_code(name, visible_examples, raw_html)
    
    try:
        results_html = submit_code_and_get_tests(prob_id, submit_code)
        all_tests = extract_all_tests_from_results(results_html)
    except Exception as e:
        pass  # Fall back to visible examples
    
    # If submission failed or returned no tests, use visible examples
    if not all_tests:
        all_tests = visible_examples

    return {
        "description": desc,
        "examples": all_tests,
        "solution": solution,
    }


def infer_return_type(examples):
    """Guess Java return type from examples."""
    for ex in examples:
        match = re.search(r'→\s*(.+)', ex)
        if match:
            result = match.group(1).strip()
            if result in ("true", "false"):
                return "boolean"
            if result.startswith('"'):
                return "String"
            if result.startswith('{') or result.startswith('['):
                return "int[]"
            try:
                int(result)
                return "int"
            except ValueError:
                try:
                    float(result)
                    return "double"
                except ValueError:
                    pass
    return "int"


def infer_params(examples):
    """Infer Java method parameter declaration from examples."""
    if not examples:
        return ""
    
    match = re.match(r'\w+\((.+?)\)\s*→', examples[0])
    if not match:
        return ""
    
    args_str = match.group(1)
    raw_args = split_top_level(args_str)
    
    param_types = []
    for arg in raw_args:
        arg = arg.strip()
        if arg in ("true", "false"):
            param_types.append("boolean")
        elif arg.startswith('"'):
            param_types.append("String")
        elif arg.startswith('{') or arg.startswith('['):
            param_types.append("int[]")
        else:
            try:
                int(arg)
                param_types.append("int")
            except ValueError:
                try:
                    float(arg)
                    param_types.append("double")
                except ValueError:
                    param_types.append("int")
    
    # Generate param names
    params = []
    type_counts = {}
    for pt in param_types:
        name_map = {
            "String": "str", "boolean": "b", "int": "n",
            "double": "d", "int[]": "arr"
        }
        base = name_map.get(pt, "x")
        count = type_counts.get(pt, 0)
        type_counts[pt] = count + 1
        suffix = str(count + 1) if count > 0 else ""
        params.append(f"{pt} {base}{suffix}")
    
    return ", ".join(params)


def split_top_level(s):
    """Split string by commas not inside braces/quotes."""
    result = []
    depth = 0
    current = ""
    in_string = False
    for ch in s:
        if ch == '"' and not in_string:
            in_string = True
            current += ch
        elif ch == '"' and in_string:
            in_string = False
            current += ch
        elif ch == '{':
            depth += 1
            current += ch
        elif ch == '}':
            depth -= 1
            current += ch
        elif ch == ',' and depth == 0 and not in_string:
            result.append(current.strip())
            current = ""
        else:
            current += ch
    if current.strip():
        result.append(current.strip())
    return result


def parse_test_cases(examples):
    """Parse examples into (args, expected) tuples."""
    cases = []
    for ex in examples:
        match = re.match(r'(\w+)\((.+?)\)\s*→\s*(.+)', ex)
        if match:
            args_str = match.group(2).strip()
            expected = match.group(3).strip()
            cases.append((args_str, expected))
    return cases


def format_java_value(val):
    """Format a value for Java code."""
    val = val.strip()
    if val in ("true", "false"):
        return val
    if val.startswith('"') and val.endswith('"'):
        return val
    if val.startswith('\u201c') and val.endswith('\u201d'):
        return '"' + val[1:-1] + '"'
    try:
        int(val)
        return val
    except ValueError:
        pass
    try:
        float(val)
        return val
    except ValueError:
        pass
    if val.startswith('{') or val.startswith('['):
        return val.replace('[', '{').replace(']', '}')
    return val


def format_args(args_str):
    """Format args for a Java method call."""
    parts = split_top_level(args_str)
    return ", ".join(format_java_value(p) for p in parts)


def generate_tester(func_name, return_type, test_cases, class_name):
    """Generate a Java tester class with ALL test cases."""
    lines = [
        f"/**",
        f" * Tester for {class_name} - CodingBat Java",
        f" * {len(test_cases)} test cases",
        f" */",
        f"public class {class_name}Tester {{",
        f"",
        f"    public static void main(String[] args) {{",
        f"        {class_name} obj = new {class_name}();",
        f"        int passed = 0;",
        f"        int failed = 0;",
        f"",
    ]

    for i, (args_str, expected) in enumerate(test_cases):
        formatted_args = format_args(args_str)
        formatted_expected = format_java_value(expected)
        
        display = f"{func_name}({args_str}) expected {expected}"
        display = display.replace('\\', '\\\\').replace('"', '\\"')

        if return_type == "String":
            compare = f'obj.{func_name}({formatted_args}).equals({formatted_expected})'
        elif return_type == "int[]":
            compare = f'java.util.Arrays.equals(obj.{func_name}({formatted_args}), new int[]{formatted_expected})'
        else:
            compare = f'obj.{func_name}({formatted_args}) == {formatted_expected}'

        lines.extend([
            f'        // Test {i+1}',
            f'        if ({compare}) {{',
            f'            passed++;',
            f'        }} else {{',
            f'            System.out.println("FAIL: {display}");',
            f'            failed++;',
            f'        }}',
            f'',
        ])

    lines.extend([
        f'        System.out.println("{func_name}: " + passed + "/" + (passed + failed) + " tests passed.");',
        f'        if (failed == 0) System.out.println("All tests passed!");',
        f"    }}",
        f"}}",
    ])
    return "\n".join(lines)


def main():
    print(f"Output directory: {OUTPUT_DIR}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total_problems = 0
    total_tests = 0

    for category in CATEGORIES:
        print(f"\n{'='*60}")
        print(f"  Category: {category}")
        print(f"{'='*60}")

        cat_dir = os.path.join(OUTPUT_DIR, category)
        os.makedirs(cat_dir, exist_ok=True)

        try:
            problems = get_problem_links(category)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        print(f"  Found {len(problems)} problems\n")

        for idx, (name, url, prob_id) in enumerate(problems):
            print(f"  [{idx+1}/{len(problems)}] {name}...", end=" ", flush=True)

            try:
                data = extract_problem(url, prob_id, name)
                class_name = name[0].upper() + name[1:]

                # ---- Problem .java ----
                with open(os.path.join(cat_dir, f"{class_name}.java"), "w", encoding="utf-8") as f:
                    f.write(f"/**\n")
                    f.write(f" * CodingBat > Java > {category} > {name}\n")
                    f.write(f" * {url}\n")
                    f.write(f" *\n")
                    words = data['description'].split()
                    line = " *"
                    for w in words:
                        if len(line) + len(w) + 1 > 80:
                            f.write(line + "\n")
                            line = " * " + w
                        else:
                            line += " " + w
                    f.write(line + "\n")

                    if data['examples']:
                        f.write(f" *\n")
                        f.write(f" * Examples:\n")
                        for ex in data['examples']:
                            f.write(f" *   {ex}\n")
                    f.write(f" */\n")
                    f.write(f"public class {class_name} {{\n\n")
                    # Method stub
                    return_type = infer_return_type(data['examples'])
                    params = infer_params(data['examples'])
                    default_return = {
                        "boolean": "false", "int": "0", "double": "0.0",
                        "String": '""', "int[]": "new int[]{}",
                    }.get(return_type, "null")
                    f.write(f"    public {return_type} {name}({params}) {{\n")
                    f.write(f"        // TODO: implement\n")
                    f.write(f"        return {default_return};\n")
                    f.write(f"    }}\n")
                    f.write(f"\n}}\n")

                # ---- Tester .java ----
                test_cases = parse_test_cases(data['examples'])
                tc_count = len(test_cases)
                if test_cases:
                    return_type = infer_return_type(data['examples'])
                    tester = generate_tester(name, return_type, test_cases, class_name)
                    with open(os.path.join(cat_dir, f"{class_name}Tester.java"), "w", encoding="utf-8") as f:
                        f.write(tester)

                # ---- Solution .java ----
                has_sol = bool(data['solution'])
                if has_sol:
                    with open(os.path.join(cat_dir, f"{class_name}Solution.java"), "w", encoding="utf-8") as f:
                        f.write(f"/**\n")
                        f.write(f" * SOLUTION: CodingBat > Java > {category} > {name}\n")
                        f.write(f" * {url}\n")
                        f.write(f" */\n")
                        f.write(f"public class {class_name}Solution {{\n\n")
                        for sl in data['solution'].split('\n'):
                            f.write(f"    {sl}\n")
                        f.write(f"\n}}\n")

                total_problems += 1
                total_tests += tc_count
                sol_mark = "✓" if has_sol else "✗"
                print(f"OK ({tc_count} tests, solution: {sol_mark})")

            except Exception as e:
                print(f"ERROR: {e}")

            time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"  DONE! {total_problems} problems, {total_tests} test cases total.")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
