/**
 * Tester for WithoutX - CodingBat Java
 * 12 test cases
 */
public class WithoutXTester {

    public static void main(String[] args) {
        WithoutX obj = new WithoutX();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.withoutX("xHix").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"xHix\") expected \"Hi\"");
            failed++;
        }

        // Test 2
        if (obj.withoutX("xHi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"xHi\") expected \"Hi\"");
            failed++;
        }

        // Test 3
        if (obj.withoutX("Hxix").equals("Hxi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"Hxix\") expected \"Hxi\"");
            failed++;
        }

        // Test 4
        if (obj.withoutX("Hi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"Hi\") expected \"Hi\"");
            failed++;
        }

        // Test 5
        if (obj.withoutX("xxHi").equals("xHi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"xxHi\") expected \"xHi\"");
            failed++;
        }

        // Test 6
        if (obj.withoutX("Hix").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"Hix\") expected \"Hi\"");
            failed++;
        }

        // Test 7
        if (obj.withoutX("xaxbx").equals("axb")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"xaxbx\") expected \"axb\"");
            failed++;
        }

        // Test 8
        if (obj.withoutX("xx").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"xx\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.withoutX("x").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"x\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.withoutX("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"\") expected \"\"");
            failed++;
        }

        // Test 11
        if (obj.withoutX("Hello").equals("Hello")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"Hello\") expected \"Hello\"");
            failed++;
        }

        // Test 12
        if (obj.withoutX("Hexllo").equals("Hexllo")) {
            passed++;
        } else {
            System.out.println("FAIL: withoutX(\"Hexllo\") expected \"Hexllo\"");
            failed++;
        }

        System.out.println("withoutX: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}