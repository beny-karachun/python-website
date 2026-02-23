/**
 * Tester for GHappy - CodingBat Java
 * 12 test cases
 */
public class GHappyTester {

    public static void main(String[] args) {
        GHappy obj = new GHappy();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.gHappy("xxggxx") == true) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"xxggxx\") expected true");
            failed++;
        }

        // Test 2
        if (obj.gHappy("xxgxx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"xxgxx\") expected false");
            failed++;
        }

        // Test 3
        if (obj.gHappy("xxggyygxx") == false) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"xxggyygxx\") expected false");
            failed++;
        }

        // Test 4
        if (obj.gHappy("g") == false) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"g\") expected false");
            failed++;
        }

        // Test 5
        if (obj.gHappy("gg") == true) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"gg\") expected true");
            failed++;
        }

        // Test 6
        if (obj.gHappy("") == true) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"\") expected true");
            failed++;
        }

        // Test 7
        if (obj.gHappy("xxgggxyz") == true) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"xxgggxyz\") expected true");
            failed++;
        }

        // Test 8
        if (obj.gHappy("xxgggxyg") == false) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"xxgggxyg\") expected false");
            failed++;
        }

        // Test 9
        if (obj.gHappy("xxgggxygg") == true) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"xxgggxygg\") expected true");
            failed++;
        }

        // Test 10
        if (obj.gHappy("mgm") == false) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"mgm\") expected false");
            failed++;
        }

        // Test 11
        if (obj.gHappy("mggm") == true) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"mggm\") expected true");
            failed++;
        }

        // Test 12
        if (obj.gHappy("yyygggxyy") == true) {
            passed++;
        } else {
            System.out.println("FAIL: gHappy(\"yyygggxyy\") expected true");
            failed++;
        }

        System.out.println("gHappy: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}