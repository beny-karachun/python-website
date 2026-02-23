/**
 * Tester for WithoutEnd - CodingBat Java
 * 8 test cases
 */
public class WithoutEndTester {

    public static void main(String[] args) {
        WithoutEnd obj = new WithoutEnd();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.withoutEnd("Hello").equals("ell")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"Hello\") expected \"ell\"");
            failed++;
        }

        // Test 2
        if (obj.withoutEnd("java").equals("av")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"java\") expected \"av\"");
            failed++;
        }

        // Test 3
        if (obj.withoutEnd("coding").equals("odin")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"coding\") expected \"odin\"");
            failed++;
        }

        // Test 4
        if (obj.withoutEnd("code").equals("od")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"code\") expected \"od\"");
            failed++;
        }

        // Test 5
        if (obj.withoutEnd("ab").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"ab\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.withoutEnd("Chocolate!").equals("hocolate")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"Chocolate!\") expected \"hocolate\"");
            failed++;
        }

        // Test 7
        if (obj.withoutEnd("kitten").equals("itte")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"kitten\") expected \"itte\"");
            failed++;
        }

        // Test 8
        if (obj.withoutEnd("woohoo").equals("ooho")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutEnd(\"woohoo\") expected \"ooho\"");
            failed++;
        }

        System.out.println("withoutEnd: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}