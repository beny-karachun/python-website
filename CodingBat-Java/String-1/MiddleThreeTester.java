/**
 * Tester for MiddleThree - CodingBat Java
 * 7 test cases
 */
public class MiddleThreeTester {

    public static void main(String[] args) {
        MiddleThree obj = new MiddleThree();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.middleThree("Candy").equals("and")) {
            passed++;
        } else {
            System.out.println("FAIL: middleThree(\"Candy\") expected \"and\"");
            failed++;
        }

        // Test 2
        if (obj.middleThree("and").equals("and")) {
            passed++;
        } else {
            System.out.println("FAIL: middleThree(\"and\") expected \"and\"");
            failed++;
        }

        // Test 3
        if (obj.middleThree("solving").equals("lvi")) {
            passed++;
        } else {
            System.out.println("FAIL: middleThree(\"solving\") expected \"lvi\"");
            failed++;
        }

        // Test 4
        if (obj.middleThree("Hi yet Hi").equals("yet")) {
            passed++;
        } else {
            System.out.println("FAIL: middleThree(\"Hi yet Hi\") expected \"yet\"");
            failed++;
        }

        // Test 5
        if (obj.middleThree("java yet java").equals("yet")) {
            passed++;
        } else {
            System.out.println("FAIL: middleThree(\"java yet java\") expected \"yet\"");
            failed++;
        }

        // Test 6
        if (obj.middleThree("Chocolate").equals("col")) {
            passed++;
        } else {
            System.out.println("FAIL: middleThree(\"Chocolate\") expected \"col\"");
            failed++;
        }

        // Test 7
        if (obj.middleThree("XabcxyzabcX").equals("xyz")) {
            passed++;
        } else {
            System.out.println("FAIL: middleThree(\"XabcxyzabcX\") expected \"xyz\"");
            failed++;
        }

        System.out.println("middleThree: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}