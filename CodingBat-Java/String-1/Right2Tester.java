/**
 * Tester for Right2 - CodingBat Java
 * 6 test cases
 */
public class Right2Tester {

    public static void main(String[] args) {
        Right2 obj = new Right2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.right2("Hello").equals("loHel")) {
            passed++;
        } else {
            System.out.println("FAIL: right2(\"Hello\") expected \"loHel\"");
            failed++;
        }

        // Test 2
        if (obj.right2("java").equals("vaja")) {
            passed++;
        } else {
            System.out.println("FAIL: right2(\"java\") expected \"vaja\"");
            failed++;
        }

        // Test 3
        if (obj.right2("Hi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: right2(\"Hi\") expected \"Hi\"");
            failed++;
        }

        // Test 4
        if (obj.right2("code").equals("deco")) {
            passed++;
        } else {
            System.out.println("FAIL: right2(\"code\") expected \"deco\"");
            failed++;
        }

        // Test 5
        if (obj.right2("cat").equals("atc")) {
            passed++;
        } else {
            System.out.println("FAIL: right2(\"cat\") expected \"atc\"");
            failed++;
        }

        // Test 6
        if (obj.right2("12345").equals("45123")) {
            passed++;
        } else {
            System.out.println("FAIL: right2(\"12345\") expected \"45123\"");
            failed++;
        }

        System.out.println("right2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}