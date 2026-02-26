/**
 * Tester for AtFirst - CodingBat Java
 * 7 test cases
 */
public class AtFirstTester {

    public static void main(String[] args) {
        AtFirst obj = new AtFirst();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.atFirst("hello").equals("he")) {
            passed++;
        } else {
            System.out.println("FAIL: atFirst(\"hello\") expected \"he\"");
            failed++;
        }

        // Test 2
        if (obj.atFirst("hi").equals("hi")) {
            passed++;
        } else {
            System.out.println("FAIL: atFirst(\"hi\") expected \"hi\"");
            failed++;
        }

        // Test 3
        if (obj.atFirst("h").equals("h@")) {
            passed++;
        } else {
            System.out.println("FAIL: atFirst(\"h\") expected \"h@\"");
            failed++;
        }

        // Test 4
        if (obj.atFirst("").equals("@@")) {
            passed++;
        } else {
            System.out.println("FAIL: atFirst(\"\") expected \"@@\"");
            failed++;
        }

        // Test 5
        if (obj.atFirst("kitten").equals("ki")) {
            passed++;
        } else {
            System.out.println("FAIL: atFirst(\"kitten\") expected \"ki\"");
            failed++;
        }

        // Test 6
        if (obj.atFirst("java").equals("ja")) {
            passed++;
        } else {
            System.out.println("FAIL: atFirst(\"java\") expected \"ja\"");
            failed++;
        }

        // Test 7
        if (obj.atFirst("j").equals("j@")) {
            passed++;
        } else {
            System.out.println("FAIL: atFirst(\"j\") expected \"j@\"");
            failed++;
        }

        System.out.println("atFirst: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}