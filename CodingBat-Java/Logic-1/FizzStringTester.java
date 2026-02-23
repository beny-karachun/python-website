/**
 * Tester for FizzString - CodingBat Java
 * 16 test cases
 */
public class FizzStringTester {

    public static void main(String[] args) {
        FizzString obj = new FizzString();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.fizzString("fig").equals("Fizz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"fig\") expected \"Fizz\"");
            failed++;
        }

        // Test 2
        if (obj.fizzString("dib").equals("Buzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"dib\") expected \"Buzz\"");
            failed++;
        }

        // Test 3
        if (obj.fizzString("fib").equals("FizzBuzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"fib\") expected \"FizzBuzz\"");
            failed++;
        }

        // Test 4
        if (obj.fizzString("abc").equals("abc")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"abc\") expected \"abc\"");
            failed++;
        }

        // Test 5
        if (obj.fizzString("fooo").equals("Fizz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"fooo\") expected \"Fizz\"");
            failed++;
        }

        // Test 6
        if (obj.fizzString("booo").equals("booo")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"booo\") expected \"booo\"");
            failed++;
        }

        // Test 7
        if (obj.fizzString("ooob").equals("Buzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"ooob\") expected \"Buzz\"");
            failed++;
        }

        // Test 8
        if (obj.fizzString("fooob").equals("FizzBuzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"fooob\") expected \"FizzBuzz\"");
            failed++;
        }

        // Test 9
        if (obj.fizzString("f").equals("Fizz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"f\") expected \"Fizz\"");
            failed++;
        }

        // Test 10
        if (obj.fizzString("b").equals("Buzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"b\") expected \"Buzz\"");
            failed++;
        }

        // Test 11
        if (obj.fizzString("abcb").equals("Buzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"abcb\") expected \"Buzz\"");
            failed++;
        }

        // Test 12
        if (obj.fizzString("Hello").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"Hello\") expected \"Hello\"");
            failed++;
        }

        // Test 13
        if (obj.fizzString("Hellob").equals("Buzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"Hellob\") expected \"Buzz\"");
            failed++;
        }

        // Test 14
        if (obj.fizzString("af").equals("af")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"af\") expected \"af\"");
            failed++;
        }

        // Test 15
        if (obj.fizzString("bf").equals("bf")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"bf\") expected \"bf\"");
            failed++;
        }

        // Test 16
        if (obj.fizzString("fb").equals("FizzBuzz")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString(\"fb\") expected \"FizzBuzz\"");
            failed++;
        }

        System.out.println("fizzString: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}