/**
 * Tester for CigarParty - CodingBat Java
 * 11 test cases
 */
public class CigarPartyTester {

    public static void main(String[] args) {
        CigarParty obj = new CigarParty();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.cigarParty(30, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(30, false) expected false");
            failed++;
        }

        // Test 2
        if (obj.cigarParty(50, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(50, false) expected true");
            failed++;
        }

        // Test 3
        if (obj.cigarParty(70, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(70, true) expected true");
            failed++;
        }

        // Test 4
        if (obj.cigarParty(30, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(30, true) expected false");
            failed++;
        }

        // Test 5
        if (obj.cigarParty(50, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(50, true) expected true");
            failed++;
        }

        // Test 6
        if (obj.cigarParty(60, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(60, false) expected true");
            failed++;
        }

        // Test 7
        if (obj.cigarParty(61, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(61, false) expected false");
            failed++;
        }

        // Test 8
        if (obj.cigarParty(40, false) == true) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(40, false) expected true");
            failed++;
        }

        // Test 9
        if (obj.cigarParty(39, false) == false) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(39, false) expected false");
            failed++;
        }

        // Test 10
        if (obj.cigarParty(40, true) == true) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(40, true) expected true");
            failed++;
        }

        // Test 11
        if (obj.cigarParty(39, true) == false) {
            passed++;
        } else {
            System.out.println("FAIL: cigarParty(39, true) expected false");
            failed++;
        }

        System.out.println("cigarParty: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}