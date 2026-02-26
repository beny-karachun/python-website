/**
 * Tester for AllStar - CodingBat Java
 * 8 test cases
 */
public class AllStarTester {

    public static void main(String[] args) {
        AllStar obj = new AllStar();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.allStar("hello").equals("h*e*l*l*o")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"hello\") expected \"h*e*l*l*o\"");
            failed++;
        }

        // Test 2
        if (obj.allStar("abc").equals("a*b*c")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"abc\") expected \"a*b*c\"");
            failed++;
        }

        // Test 3
        if (obj.allStar("ab").equals("a*b")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"ab\") expected \"a*b\"");
            failed++;
        }

        // Test 4
        if (obj.allStar("a").equals("a")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"a\") expected \"a\"");
            failed++;
        }

        // Test 5
        if (obj.allStar("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"\") expected \"\"");
            failed++;
        }

        // Test 6
        if (obj.allStar("3.14").equals("3*.*1*4")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"3.14\") expected \"3*.*1*4\"");
            failed++;
        }

        // Test 7
        if (obj.allStar("Chocolate").equals("C*h*o*c*o*l*a*t*e")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"Chocolate\") expected \"C*h*o*c*o*l*a*t*e\"");
            failed++;
        }

        // Test 8
        if (obj.allStar("1234").equals("1*2*3*4")) {
            passed++;
        } else {
            System.out.println("FAIL: allStar(\"1234\") expected \"1*2*3*4\"");
            failed++;
        }

        System.out.println("allStar: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}