/**
 * Tester for CountHi2 - CodingBat Java
 * 16 test cases
 */
public class CountHi2Tester {

    public static void main(String[] args) {
        CountHi2 obj = new CountHi2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.countHi2("ahixhi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"ahixhi\") expected 1");
            failed++;
        }

        // Test 2
        if (obj.countHi2("ahibhi") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"ahibhi\") expected 2");
            failed++;
        }

        // Test 3
        if (obj.countHi2("xhixhi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"xhixhi\") expected 0");
            failed++;
        }

        // Test 4
        if (obj.countHi2("hixhi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"hixhi\") expected 1");
            failed++;
        }

        // Test 5
        if (obj.countHi2("hixhhi") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"hixhhi\") expected 2");
            failed++;
        }

        // Test 6
        if (obj.countHi2("hihihi") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"hihihi\") expected 3");
            failed++;
        }

        // Test 7
        if (obj.countHi2("hihihix") == 3) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"hihihix\") expected 3");
            failed++;
        }

        // Test 8
        if (obj.countHi2("xhihihix") == 2) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"xhihihix\") expected 2");
            failed++;
        }

        // Test 9
        if (obj.countHi2("xxhi") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"xxhi\") expected 0");
            failed++;
        }

        // Test 10
        if (obj.countHi2("hixxhi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"hixxhi\") expected 1");
            failed++;
        }

        // Test 11
        if (obj.countHi2("hi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"hi\") expected 1");
            failed++;
        }

        // Test 12
        if (obj.countHi2("xxxx") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"xxxx\") expected 0");
            failed++;
        }

        // Test 13
        if (obj.countHi2("h") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"h\") expected 0");
            failed++;
        }

        // Test 14
        if (obj.countHi2("x") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"x\") expected 0");
            failed++;
        }

        // Test 15
        if (obj.countHi2("") == 0) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"\") expected 0");
            failed++;
        }

        // Test 16
        if (obj.countHi2("Hellohi") == 1) {
            passed++;
        } else {
            System.out.println("FAIL: countHi2(\"Hellohi\") expected 1");
            failed++;
        }

        System.out.println("countHi2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}