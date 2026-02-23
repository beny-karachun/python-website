/**
 * Tester for FizzString2 - CodingBat Java
 * 17 test cases
 */
public class FizzString2Tester {

    public static void main(String[] args) {
        FizzString2 obj = new FizzString2();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.fizzString2(1).equals("1!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(1) expected \"1!\"");
            failed++;
        }

        // Test 2
        if (obj.fizzString2(2).equals("2!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(2) expected \"2!\"");
            failed++;
        }

        // Test 3
        if (obj.fizzString2(3).equals("Fizz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(3) expected \"Fizz!\"");
            failed++;
        }

        // Test 4
        if (obj.fizzString2(4).equals("4!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(4) expected \"4!\"");
            failed++;
        }

        // Test 5
        if (obj.fizzString2(5).equals("Buzz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(5) expected \"Buzz!\"");
            failed++;
        }

        // Test 6
        if (obj.fizzString2(6).equals("Fizz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(6) expected \"Fizz!\"");
            failed++;
        }

        // Test 7
        if (obj.fizzString2(7).equals("7!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(7) expected \"7!\"");
            failed++;
        }

        // Test 8
        if (obj.fizzString2(8).equals("8!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(8) expected \"8!\"");
            failed++;
        }

        // Test 9
        if (obj.fizzString2(9).equals("Fizz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(9) expected \"Fizz!\"");
            failed++;
        }

        // Test 10
        if (obj.fizzString2(15).equals("FizzBuzz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(15) expected \"FizzBuzz!\"");
            failed++;
        }

        // Test 11
        if (obj.fizzString2(16).equals("16!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(16) expected \"16!\"");
            failed++;
        }

        // Test 12
        if (obj.fizzString2(18).equals("Fizz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(18) expected \"Fizz!\"");
            failed++;
        }

        // Test 13
        if (obj.fizzString2(19).equals("19!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(19) expected \"19!\"");
            failed++;
        }

        // Test 14
        if (obj.fizzString2(21).equals("Fizz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(21) expected \"Fizz!\"");
            failed++;
        }

        // Test 15
        if (obj.fizzString2(44).equals("44!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(44) expected \"44!\"");
            failed++;
        }

        // Test 16
        if (obj.fizzString2(45).equals("FizzBuzz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(45) expected \"FizzBuzz!\"");
            failed++;
        }

        // Test 17
        if (obj.fizzString2(100).equals("Buzz!")) {
            passed++;
        } else {
            System.out.println("FAIL: fizzString2(100) expected \"Buzz!\"");
            failed++;
        }

        System.out.println("fizzString2: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}