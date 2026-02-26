/**
 * Tester for WithoutDoubles - CodingBat Java
 * 12 test cases
 */
public class WithoutDoublesTester {

    public static void main(String[] args) {
        WithoutDoubles obj = new WithoutDoubles();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.withoutDoubles(2, 3, true) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(2, 3, true) expected 5");
            failed++;
        }

        // Test 2
        if (obj.withoutDoubles(3, 3, true) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(3, 3, true) expected 7");
            failed++;
        }

        // Test 3
        if (obj.withoutDoubles(3, 3, false) == 6) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(3, 3, false) expected 6");
            failed++;
        }

        // Test 4
        if (obj.withoutDoubles(2, 3, false) == 5) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(2, 3, false) expected 5");
            failed++;
        }

        // Test 5
        if (obj.withoutDoubles(5, 4, true) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(5, 4, true) expected 9");
            failed++;
        }

        // Test 6
        if (obj.withoutDoubles(5, 4, false) == 9) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(5, 4, false) expected 9");
            failed++;
        }

        // Test 7
        if (obj.withoutDoubles(5, 5, true) == 11) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(5, 5, true) expected 11");
            failed++;
        }

        // Test 8
        if (obj.withoutDoubles(5, 5, false) == 10) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(5, 5, false) expected 10");
            failed++;
        }

        // Test 9
        if (obj.withoutDoubles(6, 6, true) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(6, 6, true) expected 7");
            failed++;
        }

        // Test 10
        if (obj.withoutDoubles(6, 6, false) == 12) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(6, 6, false) expected 12");
            failed++;
        }

        // Test 11
        if (obj.withoutDoubles(1, 6, true) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(1, 6, true) expected 7");
            failed++;
        }

        // Test 12
        if (obj.withoutDoubles(6, 1, false) == 7) {
            passed++;
        } else {
            System.out.println("FAIL: withoutDoubles(6, 1, false) expected 7");
            failed++;
        }

        System.out.println("withoutDoubles: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}