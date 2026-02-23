/**
 * Tester for ChangePi - CodingBat Java
 * 10 test cases
 */
public class ChangePiTester {

    public static void main(String[] args) {
        ChangePi obj = new ChangePi();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.changePi("xpix").equals("x3.14x")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"xpix\") expected \"x3.14x\"");
            failed++;
        }

        // Test 2
        if (obj.changePi("pipi").equals("3.143.14")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"pipi\") expected \"3.143.14\"");
            failed++;
        }

        // Test 3
        if (obj.changePi("pip").equals("3.14p")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"pip\") expected \"3.14p\"");
            failed++;
        }

        // Test 4
        if (obj.changePi("pi").equals("3.14")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"pi\") expected \"3.14\"");
            failed++;
        }

        // Test 5
        if (obj.changePi("hip").equals("hip")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"hip\") expected \"hip\"");
            failed++;
        }

        // Test 6
        if (obj.changePi("p").equals("p")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"p\") expected \"p\"");
            failed++;
        }

        // Test 7
        if (obj.changePi("x").equals("x")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"x\") expected \"x\"");
            failed++;
        }

        // Test 8
        if (obj.changePi("").equals("")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"\") expected \"\"");
            failed++;
        }

        // Test 9
        if (obj.changePi("pixx").equals("3.14xx")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"pixx\") expected \"3.14xx\"");
            failed++;
        }

        // Test 10
        if (obj.changePi("xyzzy").equals("xyzzy")) {
            passed++;
        } else {
            System.out.println("FAIL: changePi(\"xyzzy\") expected \"xyzzy\"");
            failed++;
        }

        System.out.println("changePi: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}