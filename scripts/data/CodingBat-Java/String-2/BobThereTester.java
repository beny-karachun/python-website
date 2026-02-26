/**
 * Tester for BobThere - CodingBat Java
 * 13 test cases
 */
public class BobThereTester {

    public static void main(String[] args) {
        BobThere obj = new BobThere();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.bobThere("abcbob") == true) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"abcbob\") expected true");
            failed++;
        }

        // Test 2
        if (obj.bobThere("b9b") == true) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"b9b\") expected true");
            failed++;
        }

        // Test 3
        if (obj.bobThere("bac") == false) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"bac\") expected false");
            failed++;
        }

        // Test 4
        if (obj.bobThere("bbb") == true) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"bbb\") expected true");
            failed++;
        }

        // Test 5
        if (obj.bobThere("abcdefb") == false) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"abcdefb\") expected false");
            failed++;
        }

        // Test 6
        if (obj.bobThere("123abcbcdbabxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"123abcbcdbabxyz\") expected true");
            failed++;
        }

        // Test 7
        if (obj.bobThere("b12") == false) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"b12\") expected false");
            failed++;
        }

        // Test 8
        if (obj.bobThere("b1b") == true) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"b1b\") expected true");
            failed++;
        }

        // Test 9
        if (obj.bobThere("b12b1b") == true) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"b12b1b\") expected true");
            failed++;
        }

        // Test 10
        if (obj.bobThere("bbc") == false) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"bbc\") expected false");
            failed++;
        }

        // Test 11
        if (obj.bobThere("bbb") == true) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"bbb\") expected true");
            failed++;
        }

        // Test 12
        if (obj.bobThere("bb") == false) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"bb\") expected false");
            failed++;
        }

        // Test 13
        if (obj.bobThere("b") == false) {
            passed++;
        } else {
            System.out.println("FAIL: bobThere(\"b\") expected false");
            failed++;
        }

        System.out.println("bobThere: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}