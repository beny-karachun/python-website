/**
 * Tester for FirstTwo - CodingBat Java
 * 8 test cases
 */
public class FirstTwoTester {

    public static void main(String[] args) {
        FirstTwo obj = new FirstTwo();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.firstTwo("Hello").equals("He")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"Hello\") expected \"He\"");
            failed++;
        }

        // Test 2
        if (obj.firstTwo("abcdefg").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"abcdefg\") expected \"ab\"");
            failed++;
        }

        // Test 3
        if (obj.firstTwo("ab").equals("ab")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"ab\") expected \"ab\"");
            failed++;
        }

        // Test 4
        if (obj.firstTwo("a").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"a\") expected \"a\"");
            failed++;
        }

        // Test 5
        if (obj.firstTwo("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.firstTwo("Kitten").equals("Ki")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"Kitten\") expected \"Ki\"");
            failed++;
        }

        // Test 7
        if (obj.firstTwo("hi").equals("hi")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"hi\") expected \"hi\"");
            failed++;
        }

        // Test 8
        if (obj.firstTwo("hiya").equals("hi")) {
            passed++;
        } else {
            System.out.println("FAIL: firstTwo(\"hiya\") expected \"hi\"");
            failed++;
        }

        System.out.println("firstTwo: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}