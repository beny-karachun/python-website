/**
 * Tester for Left2 - CodingBat Java
 * 8 test cases
 */
public class Left2Tester {

    public static void main(String[] args) {
        Left2 obj = new Left2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.left2("Hello").equals("lloHe")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"Hello\") expected \"lloHe\"");
            failed++;
        }

        // Test 2
        if (obj.left2("java").equals("vaja")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"java\") expected \"vaja\"");
            failed++;
        }

        // Test 3
        if (obj.left2("Hi").equals("Hi")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"Hi\") expected \"Hi\"");
            failed++;
        }

        // Test 4
        if (obj.left2("code").equals("deco")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"code\") expected \"deco\"");
            failed++;
        }

        // Test 5
        if (obj.left2("cat").equals("tca")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"cat\") expected \"tca\"");
            failed++;
        }

        // Test 6
        if (obj.left2("12345").equals("34512")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"12345\") expected \"34512\"");
            failed++;
        }

        // Test 7
        if (obj.left2("Chocolate").equals("ocolateCh")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"Chocolate\") expected \"ocolateCh\"");
            failed++;
        }

        // Test 8
        if (obj.left2("bricks").equals("icksbr")) {
            passed++;
        } else {
            System.out.println("FAIL: left2(\"bricks\") expected \"icksbr\"");
            failed++;
        }

        System.out.println("left2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}