/**
 * Tester for NearHundred - CodingBat Java
 * 19 test cases
 */
public class NearHundredTester {

    public static void main(String[] args) {
        NearHundred obj = new NearHundred();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.nearHundred(93) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(93) expected true");
            failed++;
        }

        // Test 2
        if (obj.nearHundred(90) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(90) expected true");
            failed++;
        }

        // Test 3
        if (obj.nearHundred(89) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(89) expected false");
            failed++;
        }

        // Test 4
        if (obj.nearHundred(110) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(110) expected true");
            failed++;
        }

        // Test 5
        if (obj.nearHundred(111) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(111) expected false");
            failed++;
        }

        // Test 6
        if (obj.nearHundred(121) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(121) expected false");
            failed++;
        }

        // Test 7
        if (obj.nearHundred(-101) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(-101) expected false");
            failed++;
        }

        // Test 8
        if (obj.nearHundred(-209) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(-209) expected false");
            failed++;
        }

        // Test 9
        if (obj.nearHundred(190) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(190) expected true");
            failed++;
        }

        // Test 10
        if (obj.nearHundred(209) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(209) expected true");
            failed++;
        }

        // Test 11
        if (obj.nearHundred(0) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(0) expected false");
            failed++;
        }

        // Test 12
        if (obj.nearHundred(5) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(5) expected false");
            failed++;
        }

        // Test 13
        if (obj.nearHundred(-50) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(-50) expected false");
            failed++;
        }

        // Test 14
        if (obj.nearHundred(191) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(191) expected true");
            failed++;
        }

        // Test 15
        if (obj.nearHundred(189) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(189) expected false");
            failed++;
        }

        // Test 16
        if (obj.nearHundred(200) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(200) expected true");
            failed++;
        }

        // Test 17
        if (obj.nearHundred(210) == true) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(210) expected true");
            failed++;
        }

        // Test 18
        if (obj.nearHundred(211) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(211) expected false");
            failed++;
        }

        // Test 19
        if (obj.nearHundred(290) == false) {
            passed++;
        } else {
            System.out.println("FAIL: nearHundred(290) expected false");
            failed++;
        }

        System.out.println("nearHundred: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}