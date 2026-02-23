/**
 * Tester for CatDog - CodingBat Java
 * 13 test cases
 */
public class CatDogTester {

    public static void main(String[] args) {
        CatDog obj = new CatDog();
        int passed = 0;
        int failed = 0;

        // Test 1
        if (obj.catDog("catdog") == true) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"catdog\") expected true");
            failed++;
        }

        // Test 2
        if (obj.catDog("catcat") == false) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"catcat\") expected false");
            failed++;
        }

        // Test 3
        if (obj.catDog("1cat1cadodog") == true) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"1cat1cadodog\") expected true");
            failed++;
        }

        // Test 4
        if (obj.catDog("catxxdogxxxdog") == false) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"catxxdogxxxdog\") expected false");
            failed++;
        }

        // Test 5
        if (obj.catDog("catxdogxdogxcat") == true) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"catxdogxdogxcat\") expected true");
            failed++;
        }

        // Test 6
        if (obj.catDog("catxdogxdogxca") == false) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"catxdogxdogxca\") expected false");
            failed++;
        }

        // Test 7
        if (obj.catDog("dogdogcat") == false) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"dogdogcat\") expected false");
            failed++;
        }

        // Test 8
        if (obj.catDog("dogogcat") == true) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"dogogcat\") expected true");
            failed++;
        }

        // Test 9
        if (obj.catDog("dog") == false) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"dog\") expected false");
            failed++;
        }

        // Test 10
        if (obj.catDog("cat") == false) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"cat\") expected false");
            failed++;
        }

        // Test 11
        if (obj.catDog("ca") == true) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"ca\") expected true");
            failed++;
        }

        // Test 12
        if (obj.catDog("c") == true) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"c\") expected true");
            failed++;
        }

        // Test 13
        if (obj.catDog("") == true) {
            passed++;
        } else {
            System.out.println("FAIL: catDog(\"\") expected true");
            failed++;
        }

        System.out.println("catDog: " + passed + "/" + (passed + failed) + " tests passed.");
        if (failed == 0) System.out.println("All tests passed!");
    }
}