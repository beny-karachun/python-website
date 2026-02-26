/**
 * Tester for MixStart - CodingBat Java
 * 7 test cases
 */
public class MixStartTester {

    public static void main(String[] args) {
        MixStart obj = new MixStart();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.mixStart("mix snacks") == true) {
            passed++;
        } else {
            System.out.println("FAIL: mixStart(\"mix snacks\") expected true");
            failed++;
        }

        // Test 2
        if (obj.mixStart("pix snacks") == true) {
            passed++;
        } else {
            System.out.println("FAIL: mixStart(\"pix snacks\") expected true");
            failed++;
        }

        // Test 3
        if (obj.mixStart("piz snacks") == false) {
            passed++;
        } else {
            System.out.println("FAIL: mixStart(\"piz snacks\") expected false");
            failed++;
        }

        // Test 4
        if (obj.mixStart("nix") == true) {
            passed++;
        } else {
            System.out.println("FAIL: mixStart(\"nix\") expected true");
            failed++;
        }

        // Test 5
        if (obj.mixStart("ni") == false) {
            passed++;
        } else {
            System.out.println("FAIL: mixStart(\"ni\") expected false");
            failed++;
        }

        // Test 6
        if (obj.mixStart("n") == false) {
            passed++;
        } else {
            System.out.println("FAIL: mixStart(\"n\") expected false");
            failed++;
        }

        // Test 7
        if (obj.mixStart("") == false) {
            passed++;
        } else {
            System.out.println("FAIL: mixStart(\"\") expected false");
            failed++;
        }

        System.out.println("mixStart: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}