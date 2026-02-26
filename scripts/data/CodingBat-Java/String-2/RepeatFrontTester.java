/**
 * Tester for RepeatFront - CodingBat Java
 * 9 test cases
 */
public class RepeatFrontTester {

    public static void main(String[] args) {
        RepeatFront obj = new RepeatFront();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.repeatFront("Chocolate", 4).equals("ChocChoChC")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"Chocolate\", 4) expected \"ChocChoChC\"");
            failed++;
        }

        // Test 2
        if (obj.repeatFront("Chocolate", 3).equals("ChoChC")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"Chocolate\", 3) expected \"ChoChC\"");
            failed++;
        }

        // Test 3
        if (obj.repeatFront("Ice Cream", 2).equals("IcI")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"Ice Cream\", 2) expected \"IcI\"");
            failed++;
        }

        // Test 4
        if (obj.repeatFront("Ice Cream", 1).equals("I")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"Ice Cream\", 1) expected \"I\"");
            failed++;
        }

        // Test 5
        if (obj.repeatFront("Ice Cream", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"Ice Cream\", 0) expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.repeatFront("xyz", 3).equals("xyzxyx")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"xyz\", 3) expected \"xyzxyx\"");
            failed++;
        }

        // Test 7
        if (obj.repeatFront("", 0).equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"\", 0) expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.repeatFront("Java", 4).equals("JavaJavJaJ")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"Java\", 4) expected \"JavaJavJaJ\"");
            failed++;
        }

        // Test 9
        if (obj.repeatFront("Java", 1).equals("J")) {
            passed++;
        } else {
            System.out.println("FAIL: repeatFront(\"Java\", 1) expected \"J\"");
            failed++;
        }

        System.out.println("repeatFront: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}