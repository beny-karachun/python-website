/**
 * Tester for DoubleX - CodingBat Java
 * 11 test cases
 */
public class DoubleXTester {

    public static void main(String[] args) {
        DoubleX obj = new DoubleX();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.doubleX("axxbb") == true) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"axxbb\") expected true");
            failed++;
        }

        // Test 2
        if (obj.doubleX("axaxax") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"axaxax\") expected false");
            failed++;
        }

        // Test 3
        if (obj.doubleX("xxxxx") == true) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"xxxxx\") expected true");
            failed++;
        }

        // Test 4
        if (obj.doubleX("xaxxx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"xaxxx\") expected false");
            failed++;
        }

        // Test 5
        if (obj.doubleX("aaaax") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"aaaax\") expected false");
            failed++;
        }

        // Test 6
        if (obj.doubleX("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"\") expected false");
            failed++;
        }

        // Test 7
        if (obj.doubleX("abc") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"abc\") expected false");
            failed++;
        }

        // Test 8
        if (obj.doubleX("x") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"x\") expected false");
            failed++;
        }

        // Test 9
        if (obj.doubleX("xx") == true) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"xx\") expected true");
            failed++;
        }

        // Test 10
        if (obj.doubleX("xax") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"xax\") expected false");
            failed++;
        }

        // Test 11
        if (obj.doubleX("xaxx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: doubleX(\"xaxx\") expected false");
            failed++;
        }

        System.out.println("doubleX: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}