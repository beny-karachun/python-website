/**
 * Tester for StrCopies - CodingBat Java
 * 14 test cases
 */
public class StrCopiesTester {

    public static void main(String[] args) {
        StrCopies obj = new StrCopies();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.strCopies("catcowcat", "cat", 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"catcowcat\", \"cat\", 2) expected true");
            failed++;
        }

        // Test 2
        if (obj.strCopies("catcowcat", "cow", 2) == false) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"catcowcat\", \"cow\", 2) expected false");
            failed++;
        }

        // Test 3
        if (obj.strCopies("catcowcat", "cow", 1) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"catcowcat\", \"cow\", 1) expected true");
            failed++;
        }

        // Test 4
        if (obj.strCopies("iiijjj", "i", 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiijjj\", \"i\", 3) expected true");
            failed++;
        }

        // Test 5
        if (obj.strCopies("iiijjj", "i", 4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiijjj\", \"i\", 4) expected false");
            failed++;
        }

        // Test 6
        if (obj.strCopies("iiijjj", "ii", 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiijjj\", \"ii\", 2) expected true");
            failed++;
        }

        // Test 7
        if (obj.strCopies("iiijjj", "ii", 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiijjj\", \"ii\", 3) expected false");
            failed++;
        }

        // Test 8
        if (obj.strCopies("iiijjj", "x", 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiijjj\", \"x\", 3) expected false");
            failed++;
        }

        // Test 9
        if (obj.strCopies("iiijjj", "x", 0) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiijjj\", \"x\", 0) expected true");
            failed++;
        }

        // Test 10
        if (obj.strCopies("iiiiij", "iii", 3) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiiiij\", \"iii\", 3) expected true");
            failed++;
        }

        // Test 11
        if (obj.strCopies("iiiiij", "iii", 4) == false) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"iiiiij\", \"iii\", 4) expected false");
            failed++;
        }

        // Test 12
        if (obj.strCopies("ijiiiiij", "iiii", 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"ijiiiiij\", \"iiii\", 2) expected true");
            failed++;
        }

        // Test 13
        if (obj.strCopies("ijiiiiij", "iiii", 3) == false) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"ijiiiiij\", \"iiii\", 3) expected false");
            failed++;
        }

        // Test 14
        if (obj.strCopies("dogcatdogcat", "dog", 2) == true) {
            passed++;
        } else {
            System.out.println("FAIL: strCopies(\"dogcatdogcat\", \"dog\", 2) expected true");
            failed++;
        }

        System.out.println("strCopies: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}