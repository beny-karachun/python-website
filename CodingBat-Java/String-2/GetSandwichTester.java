/**
 * Tester for GetSandwich - CodingBat Java
 * 12 test cases
 */
public class GetSandwichTester {

    public static void main(String[] args) {
        GetSandwich obj = new GetSandwich();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.getSandwich("breadjambread").equals("jam")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"breadjambread\") expected \"jam\"");
            failed++;
        }

        // Test 2
        if (obj.getSandwich("xxbreadjambreadyy").equals("jam")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"xxbreadjambreadyy\") expected \"jam\"");
            failed++;
        }

        // Test 3
        if (obj.getSandwich("xxbreadyy").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"xxbreadyy\") expected \"\"");
            failed++;
        }

        // Test 4
        if (obj.getSandwich("xxbreadbreadjambreadyy").equals("breadjam")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"xxbreadbreadjambreadyy\") expected \"breadjam\"");
            failed++;
        }

        // Test 5
        if (obj.getSandwich("breadAbread").equals("A")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"breadAbread\") expected \"A\"");
            failed++;
        }

        // Test 6
        if (obj.getSandwich("breadbread").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"breadbread\") expected \"\"");
            failed++;
        }

        // Test 7
        if (obj.getSandwich("abcbreaz").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"abcbreaz\") expected \"\"");
            failed++;
        }

        // Test 8
        if (obj.getSandwich("xyz").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"xyz\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.getSandwich("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"\") expected \"\"");
            failed++;
        }

        // Test 10
        if (obj.getSandwich("breadbreaxbread").equals("breax")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"breadbreaxbread\") expected \"breax\"");
            failed++;
        }

        // Test 11
        if (obj.getSandwich("breaxbreadybread").equals("y")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"breaxbreadybread\") expected \"y\"");
            failed++;
        }

        // Test 12
        if (obj.getSandwich("breadbreadbreadbread").equals("breadbread")) {
            passed++;
        } else {
            System.out.println("FAIL: getSandwich(\"breadbreadbreadbread\") expected \"breadbread\"");
            failed++;
        }

        System.out.println("getSandwich: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}