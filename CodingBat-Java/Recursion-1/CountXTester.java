/**
 * Tester for CountX - CodingBat Java
 * 8 test cases
 */
public class CountXTester {

    public static void main(String[] args) {
        CountX obj = new CountX();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countX("xxhixx") == 4) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"xxhixx\") expected 4");
            failed++;
        }

        // Test 2
        if (obj.countX("xhixhix") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"xhixhix\") expected 3");
            failed++;
        }

        // Test 3
        if (obj.countX("hi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"hi\") expected 0");
            failed++;
        }

        // Test 4
        if (obj.countX("h") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"h\") expected 0");
            failed++;
        }

        // Test 5
        if (obj.countX("x") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"x\") expected 1");
            failed++;
        }

        // Test 6
        if (obj.countX("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"\") expected 0");
            failed++;
        }

        // Test 7
        if (obj.countX("hihi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"hihi\") expected 0");
            failed++;
        }

        // Test 8
        if (obj.countX("hiAAhi12hi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countX(\"hiAAhi12hi\") expected 0");
            failed++;
        }

        System.out.println("countX: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}