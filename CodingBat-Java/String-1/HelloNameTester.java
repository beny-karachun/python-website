/**
 * Tester for HelloName - CodingBat Java
 * 10 test cases
 */
public class HelloNameTester {

    public static void main(String[] args) {
        HelloName obj = new HelloName();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.helloName("Bob").equals("Hello Bob!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"Bob\") expected \"Hello Bob!\"");
            failed++;
        }

        // Test 2
        if (obj.helloName("Alice").equals("Hello Alice!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"Alice\") expected \"Hello Alice!\"");
            failed++;
        }

        // Test 3
        if (obj.helloName("X").equals("Hello X!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"X\") expected \"Hello X!\"");
            failed++;
        }

        // Test 4
        if (obj.helloName("Dolly").equals("Hello Dolly!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"Dolly\") expected \"Hello Dolly!\"");
            failed++;
        }

        // Test 5
        if (obj.helloName("Alpha").equals("Hello Alpha!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"Alpha\") expected \"Hello Alpha!\"");
            failed++;
        }

        // Test 6
        if (obj.helloName("Omega").equals("Hello Omega!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"Omega\") expected \"Hello Omega!\"");
            failed++;
        }

        // Test 7
        if (obj.helloName("Goodbye").equals("Hello Goodbye!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"Goodbye\") expected \"Hello Goodbye!\"");
            failed++;
        }

        // Test 8
        if (obj.helloName("ho ho ho").equals("Hello ho ho ho!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"ho ho ho\") expected \"Hello ho ho ho!\"");
            failed++;
        }

        // Test 9
        if (obj.helloName("xyz!").equals("Hello xyz!!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"xyz!\") expected \"Hello xyz!!\"");
            failed++;
        }

        // Test 10
        if (obj.helloName("Hello").equals("Hello Hello!")) {
            passed++;
        } else {
            System.out.println("FAIL: helloName(\"Hello\") expected \"Hello Hello!\"");
            failed++;
        }

        System.out.println("helloName: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}