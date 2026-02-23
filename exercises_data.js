// Auto-generated CodingBat exercises data
const EXERCISES_DATA = {
  "categories": [
    {
      "name": "Warmup-1",
      "problems": [
        {
          "id": "back_around",
          "name": "back_around",
          "description": "Given a string, take the last char and return a new string with the last char added at the front and back, so \"cat\" yields \"tcatt\". The original string will be length 1 or more.",
          "stub": "def back_around(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "back_around(\"cat\")",
              "expected": "\"tcatt\""
            },
            {
              "call": "back_around(\"Hello\")",
              "expected": "\"oHelloo\""
            },
            {
              "call": "back_around(\"a\")",
              "expected": "\"aaa\""
            },
            {
              "call": "back_around(\"abc\")",
              "expected": "\"cabcc\""
            },
            {
              "call": "back_around(\"read\")",
              "expected": "\"dreadd\""
            },
            {
              "call": "back_around(\"boo\")",
              "expected": "\"obooo\""
            }
          ]
        },
        {
          "id": "close10",
          "name": "close10",
          "description": "Given 2 int values, return whichever value is nearest to the value 10, or return 0 in the event of a tie. Note that abs(n) returns the absolute value of a number.",
          "stub": "def close10(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "close10(8, 13)",
              "expected": "8"
            },
            {
              "call": "close10(13, 8)",
              "expected": "8"
            },
            {
              "call": "close10(13, 7)",
              "expected": "0"
            },
            {
              "call": "close10(7, 13)",
              "expected": "0"
            },
            {
              "call": "close10(9, 13)",
              "expected": "9"
            },
            {
              "call": "close10(13, 8)",
              "expected": "8"
            },
            {
              "call": "close10(10, 12)",
              "expected": "10"
            },
            {
              "call": "close10(11, 10)",
              "expected": "10"
            },
            {
              "call": "close10(5, 21)",
              "expected": "5"
            },
            {
              "call": "close10(0, 20)",
              "expected": "0"
            },
            {
              "call": "close10(10, 10)",
              "expected": "0"
            }
          ]
        },
        {
          "id": "del_del",
          "name": "del_del",
          "description": "Given a string, if the string \"del\" appears starting at index 1, return a string where that \"del\" has been deleted. Otherwise, return the string unchanged.",
          "stub": "def del_del(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "del_del(\"adelbc\")",
              "expected": "\"abc\""
            },
            {
              "call": "del_del(\"adelHello\")",
              "expected": "\"aHello\""
            },
            {
              "call": "del_del(\"adedbc\")",
              "expected": "\"adedbc\""
            },
            {
              "call": "del_del(\"abcdel\")",
              "expected": "\"abcdel\""
            },
            {
              "call": "del_del(\"add\")",
              "expected": "\"add\""
            },
            {
              "call": "del_del(\"ad\")",
              "expected": "\"ad\""
            },
            {
              "call": "del_del(\"a\")",
              "expected": "\"a\""
            },
            {
              "call": "del_del(\"\")",
              "expected": "\"\""
            },
            {
              "call": "del_del(\"del\")",
              "expected": "\"del\""
            },
            {
              "call": "del_del(\"adel\")",
              "expected": "\"a\""
            },
            {
              "call": "del_del(\"aadelbb\")",
              "expected": "\"aadelbb\""
            }
          ]
        },
        {
          "id": "diff21",
          "name": "diff21",
          "description": "Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.",
          "stub": "def diff21(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "diff21(19)",
              "expected": "2"
            },
            {
              "call": "diff21(10)",
              "expected": "11"
            },
            {
              "call": "diff21(21)",
              "expected": "0"
            },
            {
              "call": "diff21(22)",
              "expected": "2"
            },
            {
              "call": "diff21(25)",
              "expected": "8"
            },
            {
              "call": "diff21(30)",
              "expected": "18"
            },
            {
              "call": "diff21(0)",
              "expected": "21"
            },
            {
              "call": "diff21(1)",
              "expected": "20"
            },
            {
              "call": "diff21(2)",
              "expected": "19"
            },
            {
              "call": "diff21(-1)",
              "expected": "22"
            },
            {
              "call": "diff21(-2)",
              "expected": "23"
            },
            {
              "call": "diff21(50)",
              "expected": "58"
            }
          ]
        },
        {
          "id": "end_up",
          "name": "end_up",
          "description": "Given a string, return a new string where the last 3 chars are now in upper case. If the string has less than 3 chars, uppercase whatever is there. Note that str.upper() returns the uppercase version of a string.",
          "stub": "def end_up(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "end_up(\"Hello\")",
              "expected": "\"HeLLO\""
            },
            {
              "call": "end_up(\"hi there\")",
              "expected": "\"hi thERE\""
            },
            {
              "call": "end_up(\"hi\")",
              "expected": "\"HI\""
            },
            {
              "call": "end_up(\"woo hoo\")",
              "expected": "\"woo HOO\""
            },
            {
              "call": "end_up(\"xyz12\")",
              "expected": "\"xyZ12\""
            },
            {
              "call": "end_up(\"x\")",
              "expected": "\"X\""
            },
            {
              "call": "end_up(\"\")",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "every_nth",
          "name": "every_nth",
          "description": "Given a non-empty string and an int N, return the string made starting with char 0, and then every Nth char of the string. So if N is 3, use char 0, 3, 6, ... and so on. N is 1 or more.",
          "stub": "def every_nth(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "every_nth(\"Miracle\", 2)",
              "expected": "\"Mrce\""
            },
            {
              "call": "every_nth(\"abcdefg\", 2)",
              "expected": "\"aceg\""
            },
            {
              "call": "every_nth(\"abcdefg\", 3)",
              "expected": "\"adg\""
            },
            {
              "call": "every_nth(\"Chocolate\", 3)",
              "expected": "\"Cca\""
            },
            {
              "call": "every_nth(\"Chocolates\", 3)",
              "expected": "\"Ccas\""
            },
            {
              "call": "every_nth(\"Chocolates\", 4)",
              "expected": "\"Coe\""
            },
            {
              "call": "every_nth(\"Chocolates\", 100)",
              "expected": "\"C\""
            }
          ]
        },
        {
          "id": "front22",
          "name": "front22",
          "description": "Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, so \"kitten\" yields\"kikittenki\". If the string length is less than 2, use whatever chars are there.",
          "stub": "def front22(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "front22(\"kitten\")",
              "expected": "\"kikittenki\""
            },
            {
              "call": "front22(\"Ha\")",
              "expected": "\"HaHaHa\""
            },
            {
              "call": "front22(\"abc\")",
              "expected": "\"ababcab\""
            },
            {
              "call": "front22(\"ab\")",
              "expected": "\"ababab\""
            },
            {
              "call": "front22(\"a\")",
              "expected": "\"aaa\""
            },
            {
              "call": "front22(\"\")",
              "expected": "\"\""
            },
            {
              "call": "front22(\"Logic\")",
              "expected": "\"LoLogicLo\""
            }
          ]
        },
        {
          "id": "front3",
          "name": "front3",
          "description": "Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.",
          "stub": "def front3(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "front3(\"Java\")",
              "expected": "\"JavJavJav\""
            },
            {
              "call": "front3(\"Chocolate\")",
              "expected": "\"ChoChoCho\""
            },
            {
              "call": "front3(\"abc\")",
              "expected": "\"abcabcabc\""
            },
            {
              "call": "front3(\"abcXYZ\")",
              "expected": "\"abcabcabc\""
            },
            {
              "call": "front3(\"ab\")",
              "expected": "\"ababab\""
            },
            {
              "call": "front3(\"a\")",
              "expected": "\"aaa\""
            },
            {
              "call": "front3(\"\")",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "front_back",
          "name": "front_back",
          "description": "Given a string, return a new string where the first and last chars have been exchanged.",
          "stub": "def front_back(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "front_back(\"code\")",
              "expected": "\"eodc\""
            },
            {
              "call": "front_back(\"a\")",
              "expected": "\"a\""
            },
            {
              "call": "front_back(\"ab\")",
              "expected": "\"ba\""
            },
            {
              "call": "front_back(\"abc\")",
              "expected": "\"cba\""
            },
            {
              "call": "front_back(\"\")",
              "expected": "\"\""
            },
            {
              "call": "front_back(\"Chocolate\")",
              "expected": "\"ehocolatC\""
            },
            {
              "call": "front_back(\"aavJ\")",
              "expected": "\"Java\""
            },
            {
              "call": "front_back(\"hello\")",
              "expected": "\"oellh\""
            }
          ]
        },
        {
          "id": "has_teen",
          "name": "has_teen",
          "description": "We'll say that a number is \"teen\" if it is in the range 13..19 inclusive. Given 3 int values, return true if 1 or more of them are teen.",
          "stub": "def has_teen(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "has_teen(13, 20, 10)",
              "expected": "True"
            },
            {
              "call": "has_teen(20, 19, 10)",
              "expected": "True"
            },
            {
              "call": "has_teen(20, 10, 13)",
              "expected": "True"
            },
            {
              "call": "has_teen(1, 20, 12)",
              "expected": "False"
            },
            {
              "call": "has_teen(19, 20, 12)",
              "expected": "True"
            },
            {
              "call": "has_teen(12, 20, 19)",
              "expected": "True"
            },
            {
              "call": "has_teen(12, 9, 20)",
              "expected": "False"
            },
            {
              "call": "has_teen(12, 18, 20)",
              "expected": "True"
            },
            {
              "call": "has_teen(14, 2, 20)",
              "expected": "True"
            },
            {
              "call": "has_teen(4, 2, 20)",
              "expected": "False"
            },
            {
              "call": "has_teen(11, 22, 22)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "icy_hot",
          "name": "icy_hot",
          "description": "Given two temperatures, return true if one is less than 0 and the other is greater than 100.",
          "stub": "def icy_hot(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "icy_hot(120, -1)",
              "expected": "True"
            },
            {
              "call": "icy_hot(-1, 120)",
              "expected": "True"
            },
            {
              "call": "icy_hot(2, 120)",
              "expected": "False"
            },
            {
              "call": "icy_hot(-1, 100)",
              "expected": "False"
            },
            {
              "call": "icy_hot(-2, -2)",
              "expected": "False"
            },
            {
              "call": "icy_hot(120, 120)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "in1020",
          "name": "in1020",
          "description": "Given 2 int values, return true if either of them is in the range 10..20 inclusive.",
          "stub": "def in1020(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "in1020(12, 99)",
              "expected": "True"
            },
            {
              "call": "in1020(21, 12)",
              "expected": "True"
            },
            {
              "call": "in1020(8, 99)",
              "expected": "False"
            },
            {
              "call": "in1020(99, 10)",
              "expected": "True"
            },
            {
              "call": "in1020(20, 20)",
              "expected": "True"
            },
            {
              "call": "in1020(21, 21)",
              "expected": "False"
            },
            {
              "call": "in1020(9, 9)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "in3050",
          "name": "in3050",
          "description": "Given 2 int values, return true if they are both in the range 30..40 inclusive, or they are both in the range 40..50 inclusive.",
          "stub": "def in3050(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "in3050(30, 31)",
              "expected": "True"
            },
            {
              "call": "in3050(30, 41)",
              "expected": "False"
            },
            {
              "call": "in3050(40, 50)",
              "expected": "True"
            },
            {
              "call": "in3050(40, 51)",
              "expected": "False"
            },
            {
              "call": "in3050(39, 50)",
              "expected": "False"
            },
            {
              "call": "in3050(50, 39)",
              "expected": "False"
            },
            {
              "call": "in3050(40, 39)",
              "expected": "True"
            },
            {
              "call": "in3050(49, 48)",
              "expected": "True"
            },
            {
              "call": "in3050(50, 40)",
              "expected": "True"
            },
            {
              "call": "in3050(50, 51)",
              "expected": "False"
            },
            {
              "call": "in3050(35, 36)",
              "expected": "True"
            },
            {
              "call": "in3050(35, 45)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "int_max",
          "name": "int_max",
          "description": "Given three int values, a b c, return the largest.",
          "stub": "def int_max(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "int_max(1, 2, 3)",
              "expected": "3"
            },
            {
              "call": "int_max(1, 3, 2)",
              "expected": "3"
            },
            {
              "call": "int_max(3, 2, 1)",
              "expected": "3"
            },
            {
              "call": "int_max(9, 3, 3)",
              "expected": "9"
            },
            {
              "call": "int_max(3, 9, 3)",
              "expected": "9"
            },
            {
              "call": "int_max(3, 3, 9)",
              "expected": "9"
            },
            {
              "call": "int_max(8, 2, 3)",
              "expected": "8"
            },
            {
              "call": "int_max(-3, -1, -2)",
              "expected": "-1"
            },
            {
              "call": "int_max(6, 2, 5)",
              "expected": "6"
            },
            {
              "call": "int_max(5, 6, 2)",
              "expected": "6"
            },
            {
              "call": "int_max(5, 2, 6)",
              "expected": "6"
            }
          ]
        },
        {
          "id": "last_digit",
          "name": "last_digit",
          "description": "Given two non-negative int values, return true if they have the same last digit, such as with 27 and 57. Note that the % \"mod\" operator computes remainders, so 17 % 10 is 7.",
          "stub": "def last_digit(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "last_digit(7, 17)",
              "expected": "True"
            },
            {
              "call": "last_digit(6, 17)",
              "expected": "False"
            },
            {
              "call": "last_digit(3, 113)",
              "expected": "True"
            },
            {
              "call": "last_digit(114, 113)",
              "expected": "False"
            },
            {
              "call": "last_digit(114, 4)",
              "expected": "True"
            },
            {
              "call": "last_digit(10, 0)",
              "expected": "True"
            },
            {
              "call": "last_digit(11, 0)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "lone_teen",
          "name": "lone_teen",
          "description": "We'll say that a number is \"teen\" if it is in the range 13..19 inclusive. Given 2 int values, return true if one or the other is teen, but not both.",
          "stub": "def lone_teen(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "lone_teen(13, 99)",
              "expected": "True"
            },
            {
              "call": "lone_teen(21, 19)",
              "expected": "True"
            },
            {
              "call": "lone_teen(13, 13)",
              "expected": "False"
            },
            {
              "call": "lone_teen(14, 20)",
              "expected": "True"
            },
            {
              "call": "lone_teen(20, 15)",
              "expected": "True"
            },
            {
              "call": "lone_teen(16, 17)",
              "expected": "False"
            },
            {
              "call": "lone_teen(16, 9)",
              "expected": "True"
            },
            {
              "call": "lone_teen(16, 18)",
              "expected": "False"
            },
            {
              "call": "lone_teen(13, 19)",
              "expected": "False"
            },
            {
              "call": "lone_teen(13, 20)",
              "expected": "True"
            },
            {
              "call": "lone_teen(6, 18)",
              "expected": "True"
            },
            {
              "call": "lone_teen(99, 13)",
              "expected": "True"
            },
            {
              "call": "lone_teen(99, 99)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "makes10",
          "name": "makes10",
          "description": "Given 2 ints, a and b, return true if one if them is 10 or if their sum is 10.",
          "stub": "def makes10(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "makes10(9, 10)",
              "expected": "True"
            },
            {
              "call": "makes10(9, 9)",
              "expected": "False"
            },
            {
              "call": "makes10(1, 9)",
              "expected": "True"
            },
            {
              "call": "makes10(10, 1)",
              "expected": "True"
            },
            {
              "call": "makes10(10, 10)",
              "expected": "True"
            },
            {
              "call": "makes10(8, 2)",
              "expected": "True"
            },
            {
              "call": "makes10(8, 3)",
              "expected": "False"
            },
            {
              "call": "makes10(10, 42)",
              "expected": "True"
            },
            {
              "call": "makes10(12, -2)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "max1020",
          "name": "max1020",
          "description": "Given 2 positive int values, return the larger value that is in the range 10..20 inclusive, or return 0 if neither is in that range.",
          "stub": "def max1020(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "max1020(11, 19)",
              "expected": "19"
            },
            {
              "call": "max1020(19, 11)",
              "expected": "19"
            },
            {
              "call": "max1020(11, 9)",
              "expected": "11"
            },
            {
              "call": "max1020(9, 21)",
              "expected": "0"
            },
            {
              "call": "max1020(10, 21)",
              "expected": "10"
            },
            {
              "call": "max1020(21, 10)",
              "expected": "10"
            },
            {
              "call": "max1020(9, 11)",
              "expected": "11"
            },
            {
              "call": "max1020(23, 10)",
              "expected": "10"
            },
            {
              "call": "max1020(20, 10)",
              "expected": "20"
            },
            {
              "call": "max1020(7, 20)",
              "expected": "20"
            },
            {
              "call": "max1020(17, 16)",
              "expected": "17"
            }
          ]
        },
        {
          "id": "missing_char",
          "name": "missing_char",
          "description": "Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).",
          "stub": "def missing_char(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "missing_char(\"kitten\", 1)",
              "expected": "\"ktten\""
            },
            {
              "call": "missing_char(\"kitten\", 0)",
              "expected": "\"itten\""
            },
            {
              "call": "missing_char(\"kitten\", 4)",
              "expected": "\"kittn\""
            },
            {
              "call": "missing_char(\"Hi\", 0)",
              "expected": "\"i\""
            },
            {
              "call": "missing_char(\"Hi\", 1)",
              "expected": "\"H\""
            },
            {
              "call": "missing_char(\"code\", 0)",
              "expected": "\"ode\""
            },
            {
              "call": "missing_char(\"code\", 1)",
              "expected": "\"cde\""
            },
            {
              "call": "missing_char(\"code\", 2)",
              "expected": "\"coe\""
            },
            {
              "call": "missing_char(\"code\", 3)",
              "expected": "\"cod\""
            },
            {
              "call": "missing_char(\"chocolate\", 8)",
              "expected": "\"chocolat\""
            }
          ]
        },
        {
          "id": "mix_start",
          "name": "mix_start",
          "description": "Return true if the given string begins with \"mix\", except the 'm' can be anything, so \"pix\", \"9ix\" .. all count.",
          "stub": "def mix_start(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "mix_start(\"mix snacks\")",
              "expected": "True"
            },
            {
              "call": "mix_start(\"pix snacks\")",
              "expected": "True"
            },
            {
              "call": "mix_start(\"piz snacks\")",
              "expected": "False"
            },
            {
              "call": "mix_start(\"nix\")",
              "expected": "True"
            },
            {
              "call": "mix_start(\"ni\")",
              "expected": "False"
            },
            {
              "call": "mix_start(\"n\")",
              "expected": "False"
            },
            {
              "call": "mix_start(\"\")",
              "expected": "False"
            }
          ]
        },
        {
          "id": "monkey_trouble",
          "name": "monkey_trouble",
          "description": "We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return true if we are in trouble.",
          "stub": "def monkey_trouble(b, b2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "monkey_trouble(True, True)",
              "expected": "True"
            },
            {
              "call": "monkey_trouble(False, False)",
              "expected": "True"
            },
            {
              "call": "monkey_trouble(True, False)",
              "expected": "False"
            },
            {
              "call": "monkey_trouble(False, True)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "near_hundred",
          "name": "near_hundred",
          "description": "Given an int n, return true if it is within 10 of 100 or 200. Note: Math.abs(num) computes the absolute value of a number.",
          "stub": "def near_hundred(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "near_hundred(93)",
              "expected": "True"
            },
            {
              "call": "near_hundred(90)",
              "expected": "True"
            },
            {
              "call": "near_hundred(89)",
              "expected": "False"
            },
            {
              "call": "near_hundred(110)",
              "expected": "True"
            },
            {
              "call": "near_hundred(111)",
              "expected": "False"
            },
            {
              "call": "near_hundred(121)",
              "expected": "False"
            },
            {
              "call": "near_hundred(-101)",
              "expected": "False"
            },
            {
              "call": "near_hundred(-209)",
              "expected": "False"
            },
            {
              "call": "near_hundred(190)",
              "expected": "True"
            },
            {
              "call": "near_hundred(209)",
              "expected": "True"
            },
            {
              "call": "near_hundred(0)",
              "expected": "False"
            },
            {
              "call": "near_hundred(5)",
              "expected": "False"
            },
            {
              "call": "near_hundred(-50)",
              "expected": "False"
            },
            {
              "call": "near_hundred(191)",
              "expected": "True"
            },
            {
              "call": "near_hundred(189)",
              "expected": "False"
            },
            {
              "call": "near_hundred(200)",
              "expected": "True"
            },
            {
              "call": "near_hundred(210)",
              "expected": "True"
            },
            {
              "call": "near_hundred(211)",
              "expected": "False"
            },
            {
              "call": "near_hundred(290)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "not_string",
          "name": "not_string",
          "description": "Given a string, return a new string where \"not \" has been added to the front. However, if the string already begins with \"not\", return the string unchanged. Note: use .equals() to compare 2 strings.",
          "stub": "def not_string(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "not_string(\"candy\")",
              "expected": "\"not candy\""
            },
            {
              "call": "not_string(\"x\")",
              "expected": "\"not x\""
            },
            {
              "call": "not_string(\"not bad\")",
              "expected": "\"not bad\""
            },
            {
              "call": "not_string(\"bad\")",
              "expected": "\"not bad\""
            },
            {
              "call": "not_string(\"not\")",
              "expected": "\"not\""
            },
            {
              "call": "not_string(\"is not\")",
              "expected": "\"not is not\""
            },
            {
              "call": "not_string(\"no\")",
              "expected": "\"not no\""
            }
          ]
        },
        {
          "id": "or35",
          "name": "or35",
          "description": "Return true if the given non-negative number is a multiple of 3 or a multiple of 5. Use the % \"mod\" operator -- seeIntroduction to Mod",
          "stub": "def or35(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "or35(3)",
              "expected": "True"
            },
            {
              "call": "or35(10)",
              "expected": "True"
            },
            {
              "call": "or35(8)",
              "expected": "False"
            },
            {
              "call": "or35(15)",
              "expected": "True"
            },
            {
              "call": "or35(5)",
              "expected": "True"
            },
            {
              "call": "or35(9)",
              "expected": "True"
            },
            {
              "call": "or35(4)",
              "expected": "False"
            },
            {
              "call": "or35(7)",
              "expected": "False"
            },
            {
              "call": "or35(6)",
              "expected": "True"
            },
            {
              "call": "or35(17)",
              "expected": "False"
            },
            {
              "call": "or35(18)",
              "expected": "True"
            },
            {
              "call": "or35(29)",
              "expected": "False"
            },
            {
              "call": "or35(20)",
              "expected": "True"
            },
            {
              "call": "or35(21)",
              "expected": "True"
            },
            {
              "call": "or35(22)",
              "expected": "False"
            },
            {
              "call": "or35(45)",
              "expected": "True"
            },
            {
              "call": "or35(99)",
              "expected": "True"
            },
            {
              "call": "or35(100)",
              "expected": "True"
            },
            {
              "call": "or35(101)",
              "expected": "False"
            },
            {
              "call": "or35(121)",
              "expected": "False"
            },
            {
              "call": "or35(122)",
              "expected": "False"
            },
            {
              "call": "or35(123)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "parrot_trouble",
          "name": "parrot_trouble",
          "description": "We have a loud talking parrot. The \"hour\" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return true if we are in trouble.",
          "stub": "def parrot_trouble(b, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "parrot_trouble(True, 6)",
              "expected": "True"
            },
            {
              "call": "parrot_trouble(True, 7)",
              "expected": "False"
            },
            {
              "call": "parrot_trouble(False, 6)",
              "expected": "False"
            },
            {
              "call": "parrot_trouble(True, 21)",
              "expected": "True"
            },
            {
              "call": "parrot_trouble(False, 21)",
              "expected": "False"
            },
            {
              "call": "parrot_trouble(False, 20)",
              "expected": "False"
            },
            {
              "call": "parrot_trouble(True, 23)",
              "expected": "True"
            },
            {
              "call": "parrot_trouble(False, 23)",
              "expected": "False"
            },
            {
              "call": "parrot_trouble(True, 20)",
              "expected": "False"
            },
            {
              "call": "parrot_trouble(False, 12)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "pos_neg",
          "name": "pos_neg",
          "description": "Given 2 int values, return true if one is negative and one is positive. Except if the parameter \"negative\" is true, then return true only if both are negative.",
          "stub": "def pos_neg(n, n2, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "pos_neg(1, -1, False)",
              "expected": "True"
            },
            {
              "call": "pos_neg(-1, 1, False)",
              "expected": "True"
            },
            {
              "call": "pos_neg(-4, -5, True)",
              "expected": "True"
            },
            {
              "call": "pos_neg(-4, -5, False)",
              "expected": "False"
            },
            {
              "call": "pos_neg(-4, 5, False)",
              "expected": "True"
            },
            {
              "call": "pos_neg(-4, 5, True)",
              "expected": "False"
            },
            {
              "call": "pos_neg(1, 1, False)",
              "expected": "False"
            },
            {
              "call": "pos_neg(-1, -1, False)",
              "expected": "False"
            },
            {
              "call": "pos_neg(1, -1, True)",
              "expected": "False"
            },
            {
              "call": "pos_neg(-1, 1, True)",
              "expected": "False"
            },
            {
              "call": "pos_neg(1, 1, True)",
              "expected": "False"
            },
            {
              "call": "pos_neg(-1, -1, True)",
              "expected": "True"
            },
            {
              "call": "pos_neg(5, -5, False)",
              "expected": "True"
            },
            {
              "call": "pos_neg(-6, 6, False)",
              "expected": "True"
            },
            {
              "call": "pos_neg(-5, -6, False)",
              "expected": "False"
            },
            {
              "call": "pos_neg(-2, -1, False)",
              "expected": "False"
            },
            {
              "call": "pos_neg(1, 2, False)",
              "expected": "False"
            },
            {
              "call": "pos_neg(-5, 6, True)",
              "expected": "False"
            },
            {
              "call": "pos_neg(-5, -5, True)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "sleep_in",
          "name": "sleep_in",
          "description": "The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.",
          "stub": "def sleep_in(b, b2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "sleep_in(False, False)",
              "expected": "True"
            },
            {
              "call": "sleep_in(True, False)",
              "expected": "False"
            },
            {
              "call": "sleep_in(False, True)",
              "expected": "True"
            },
            {
              "call": "sleep_in(True, True)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "start_hi",
          "name": "start_hi",
          "description": "Given a string, return true if the string starts with \"hi\" and false otherwise.",
          "stub": "def start_hi(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "start_hi(\"hi there\")",
              "expected": "True"
            },
            {
              "call": "start_hi(\"hi\")",
              "expected": "True"
            },
            {
              "call": "start_hi(\"hello hi\")",
              "expected": "False"
            },
            {
              "call": "start_hi(\"he\")",
              "expected": "False"
            },
            {
              "call": "start_hi(\"h\")",
              "expected": "False"
            },
            {
              "call": "start_hi(\"\")",
              "expected": "False"
            },
            {
              "call": "start_hi(\"ho hi\")",
              "expected": "False"
            },
            {
              "call": "start_hi(\"hi ho\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "start_oz",
          "name": "start_oz",
          "description": "Given a string, return a string made of the first 2 chars (if present), however include first char only if it is 'o' and include the second only if it is 'z', so \"ozymandias\" yields \"oz\".",
          "stub": "def start_oz(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "start_oz(\"ozymandias\")",
              "expected": "\"oz\""
            },
            {
              "call": "start_oz(\"bzoo\")",
              "expected": "\"z\""
            },
            {
              "call": "start_oz(\"oxx\")",
              "expected": "\"o\""
            },
            {
              "call": "start_oz(\"oz\")",
              "expected": "\"oz\""
            },
            {
              "call": "start_oz(\"ounce\")",
              "expected": "\"o\""
            },
            {
              "call": "start_oz(\"o\")",
              "expected": "\"o\""
            },
            {
              "call": "start_oz(\"abc\")",
              "expected": "\"\""
            },
            {
              "call": "start_oz(\"\")",
              "expected": "\"\""
            },
            {
              "call": "start_oz(\"zoo\")",
              "expected": "\"\""
            },
            {
              "call": "start_oz(\"aztec\")",
              "expected": "\"z\""
            },
            {
              "call": "start_oz(\"zzzz\")",
              "expected": "\"z\""
            },
            {
              "call": "start_oz(\"oznic\")",
              "expected": "\"oz\""
            }
          ]
        },
        {
          "id": "string_e",
          "name": "string_e",
          "description": "Return true if the given string contains between 1 and 3 'e' chars.",
          "stub": "def string_e(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_e(\"Hello\")",
              "expected": "True"
            },
            {
              "call": "string_e(\"Heelle\")",
              "expected": "True"
            },
            {
              "call": "string_e(\"Heelele\")",
              "expected": "False"
            },
            {
              "call": "string_e(\"Hll\")",
              "expected": "False"
            },
            {
              "call": "string_e(\"e\")",
              "expected": "True"
            },
            {
              "call": "string_e(\"\")",
              "expected": "False"
            }
          ]
        },
        {
          "id": "sum_double",
          "name": "sum_double",
          "description": "Given two int values, return their sum. Unless the two values are the same, then return double their sum.",
          "stub": "def sum_double(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "sum_double(1, 2)",
              "expected": "3"
            },
            {
              "call": "sum_double(3, 2)",
              "expected": "5"
            },
            {
              "call": "sum_double(2, 2)",
              "expected": "8"
            },
            {
              "call": "sum_double(-1, 0)",
              "expected": "-1"
            },
            {
              "call": "sum_double(3, 3)",
              "expected": "12"
            },
            {
              "call": "sum_double(0, 0)",
              "expected": "0"
            },
            {
              "call": "sum_double(0, 1)",
              "expected": "1"
            },
            {
              "call": "sum_double(3, 4)",
              "expected": "7"
            }
          ]
        }
      ]
    },
    {
      "name": "Warmup-2",
      "problems": [
        {
          "id": "alt_pairs",
          "name": "alt_pairs",
          "description": "Given a string, return a string made of the chars at indexes 0,1, 4,5, 8,9 ... so \"kittens\" yields \"kien\".",
          "stub": "def alt_pairs(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "alt_pairs(\"kitten\")",
              "expected": "\"kien\""
            },
            {
              "call": "alt_pairs(\"Chocolate\")",
              "expected": "\"Chole\""
            },
            {
              "call": "alt_pairs(\"CodingHorror\")",
              "expected": "\"Congrr\""
            },
            {
              "call": "alt_pairs(\"yak\")",
              "expected": "\"ya\""
            },
            {
              "call": "alt_pairs(\"ya\")",
              "expected": "\"ya\""
            },
            {
              "call": "alt_pairs(\"y\")",
              "expected": "\"y\""
            },
            {
              "call": "alt_pairs(\"\")",
              "expected": "\"\""
            },
            {
              "call": "alt_pairs(\"ThisThatTheOther\")",
              "expected": "\"ThThThth\""
            }
          ]
        },
        {
          "id": "array123",
          "name": "array123",
          "description": "Given an array of ints, return true if the sequence of numbers 1, 2, 3 appears in the array somewhere.",
          "stub": "def array123(arr, n, n2, n3, n4):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "array123([1, 1, 2, 3, 1])",
              "expected": "True"
            },
            {
              "call": "array123([1, 1, 2, 4, 1])",
              "expected": "False"
            },
            {
              "call": "array123([1, 1, 2, 1, 2, 3])",
              "expected": "True"
            }
          ]
        },
        {
          "id": "array667",
          "name": "array667",
          "description": "Given an array of ints, return the number of times that two 6's are next to each other in the array. Also count instances where the second \"6\" is actually a 7.",
          "stub": "def array667(arr, n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "array667([6, 6, 2])",
              "expected": "1"
            },
            {
              "call": "array667([6, 6, 2, 6])",
              "expected": "1"
            },
            {
              "call": "array667([6, 7, 2, 6])",
              "expected": "1"
            }
          ]
        },
        {
          "id": "array_count9",
          "name": "array_count9",
          "description": "Given an array of ints, return the number of 9's in the array.",
          "stub": "def array_count9(arr, n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "array_count9([1, 2, 9])",
              "expected": "1"
            },
            {
              "call": "array_count9([1, 9, 9])",
              "expected": "2"
            },
            {
              "call": "array_count9([1, 9, 9, 3, 9])",
              "expected": "3"
            }
          ]
        },
        {
          "id": "array_front9",
          "name": "array_front9",
          "description": "Given an array of ints, return true if one of the first 4 elements in the array is a 9. The array length may be less than 4.",
          "stub": "def array_front9(arr, n, n2, n3, n4):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "array_front9([1, 2, 9, 3, 4])",
              "expected": "True"
            },
            {
              "call": "array_front9([1, 2, 3, 4, 9])",
              "expected": "False"
            },
            {
              "call": "array_front9([1, 2, 3, 4, 5])",
              "expected": "False"
            }
          ]
        },
        {
          "id": "count_xx",
          "name": "count_xx",
          "description": "Count the number of \"xx\" in the given string. We'll say that overlapping is allowed, so \"xxx\" contains 2 \"xx\".",
          "stub": "def count_xx(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_xx(\"abcxx\")",
              "expected": "1"
            },
            {
              "call": "count_xx(\"xxx\")",
              "expected": "2"
            },
            {
              "call": "count_xx(\"xxxx\")",
              "expected": "3"
            },
            {
              "call": "count_xx(\"abc\")",
              "expected": "0"
            },
            {
              "call": "count_xx(\"Hello there\")",
              "expected": "0"
            },
            {
              "call": "count_xx(\"Hexxo thxxe\")",
              "expected": "2"
            },
            {
              "call": "count_xx(\"\")",
              "expected": "0"
            },
            {
              "call": "count_xx(\"Kittens\")",
              "expected": "0"
            },
            {
              "call": "count_xx(\"Kittensxxx\")",
              "expected": "2"
            }
          ]
        },
        {
          "id": "double_x",
          "name": "double_x",
          "description": "Given a string, return true if the first instance of \"x\" in the string is immediately followed by another \"x\".",
          "stub": "def double_x(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "double_x(\"axxbb\")",
              "expected": "True"
            },
            {
              "call": "double_x(\"axaxax\")",
              "expected": "False"
            },
            {
              "call": "double_x(\"xxxxx\")",
              "expected": "True"
            },
            {
              "call": "double_x(\"xaxxx\")",
              "expected": "False"
            },
            {
              "call": "double_x(\"aaaax\")",
              "expected": "False"
            },
            {
              "call": "double_x(\"\")",
              "expected": "False"
            },
            {
              "call": "double_x(\"abc\")",
              "expected": "False"
            },
            {
              "call": "double_x(\"x\")",
              "expected": "False"
            },
            {
              "call": "double_x(\"xx\")",
              "expected": "True"
            },
            {
              "call": "double_x(\"xax\")",
              "expected": "False"
            },
            {
              "call": "double_x(\"xaxx\")",
              "expected": "False"
            }
          ]
        },
        {
          "id": "front_times",
          "name": "front_times",
          "description": "Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;",
          "stub": "def front_times(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "front_times(\"Chocolate\", 2)",
              "expected": "\"ChoCho\""
            },
            {
              "call": "front_times(\"Chocolate\", 3)",
              "expected": "\"ChoChoCho\""
            },
            {
              "call": "front_times(\"Abc\", 3)",
              "expected": "\"AbcAbcAbc\""
            },
            {
              "call": "front_times(\"Ab\", 4)",
              "expected": "\"AbAbAbAb\""
            },
            {
              "call": "front_times(\"A\", 4)",
              "expected": "\"AAAA\""
            },
            {
              "call": "front_times(\"\", 4)",
              "expected": "\"\""
            },
            {
              "call": "front_times(\"Abc\", 0)",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "has271",
          "name": "has271",
          "description": "Given an array of ints, return true if it contains a 2, 7, 1 pattern: a value, followed by the value plus 5, followed by the value minus 1. Additionally the 271 counts even if the \"1\" differs by 2 or less from the correct value.",
          "stub": "def has271(arr, n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "has271([1, 2, 7, 1])",
              "expected": "True"
            },
            {
              "call": "has271([1, 2, 8, 1])",
              "expected": "False"
            },
            {
              "call": "has271([2, 7, 1])",
              "expected": "True"
            }
          ]
        },
        {
          "id": "last2",
          "name": "last2",
          "description": "Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so \"hixxxhi\" yields 1 (we won't count the end substring).",
          "stub": "def last2(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "last2(\"hixxhi\")",
              "expected": "1"
            },
            {
              "call": "last2(\"xaxxaxaxx\")",
              "expected": "1"
            },
            {
              "call": "last2(\"axxxaaxx\")",
              "expected": "2"
            },
            {
              "call": "last2(\"xxaxxaxxaxx\")",
              "expected": "3"
            },
            {
              "call": "last2(\"xaxaxaxx\")",
              "expected": "0"
            },
            {
              "call": "last2(\"xxxx\")",
              "expected": "2"
            },
            {
              "call": "last2(\"13121312\")",
              "expected": "1"
            },
            {
              "call": "last2(\"11212\")",
              "expected": "1"
            },
            {
              "call": "last2(\"13121311\")",
              "expected": "0"
            },
            {
              "call": "last2(\"1717171\")",
              "expected": "2"
            },
            {
              "call": "last2(\"hi\")",
              "expected": "0"
            },
            {
              "call": "last2(\"h\")",
              "expected": "0"
            },
            {
              "call": "last2(\"\")",
              "expected": "0"
            }
          ]
        },
        {
          "id": "no_triples",
          "name": "no_triples",
          "description": "Given an array of ints, we'll say that a triple is a value appearing 3 times in a row in the array. Return true if the array does not contain any triples.",
          "stub": "def no_triples(arr, n, n2, n3, n4):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "no_triples([1, 1, 2, 2, 1])",
              "expected": "True"
            },
            {
              "call": "no_triples([1, 1, 2, 2, 2, 1])",
              "expected": "False"
            },
            {
              "call": "no_triples([1, 1, 1, 2, 2, 2, 1])",
              "expected": "False"
            }
          ]
        },
        {
          "id": "string_bits",
          "name": "string_bits",
          "description": "Given a string, return a new string made of every other char starting with the first, so \"Hello\" yields \"Hlo\".",
          "stub": "def string_bits(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_bits(\"Hello\")",
              "expected": "\"Hlo\""
            },
            {
              "call": "string_bits(\"Hi\")",
              "expected": "\"H\""
            },
            {
              "call": "string_bits(\"Heeololeo\")",
              "expected": "\"Hello\""
            },
            {
              "call": "string_bits(\"HiHiHi\")",
              "expected": "\"HHH\""
            },
            {
              "call": "string_bits(\"\")",
              "expected": "\"\""
            },
            {
              "call": "string_bits(\"Greetings\")",
              "expected": "\"Getns\""
            },
            {
              "call": "string_bits(\"Chocoate\")",
              "expected": "\"Coot\""
            },
            {
              "call": "string_bits(\"pi\")",
              "expected": "\"p\""
            },
            {
              "call": "string_bits(\"Hello Kitten\")",
              "expected": "\"HloKte\""
            },
            {
              "call": "string_bits(\"hxaxpxpxy\")",
              "expected": "\"happy\""
            }
          ]
        },
        {
          "id": "string_match",
          "name": "string_match",
          "description": "Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So \"xxcaazz\" and \"xxbaaz\" yields 3, since the \"xx\", \"aa\", and \"az\" substrings appear in the same place in both strings.",
          "stub": "def string_match(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_match(\"xxcaazz\", \"xxbaaz\")",
              "expected": "3"
            },
            {
              "call": "string_match(\"abc\", \"abc\")",
              "expected": "2"
            },
            {
              "call": "string_match(\"abc\", \"axc\")",
              "expected": "0"
            },
            {
              "call": "string_match(\"hello\", \"he\")",
              "expected": "1"
            },
            {
              "call": "string_match(\"he\", \"hello\")",
              "expected": "1"
            },
            {
              "call": "string_match(\"h\", \"hello\")",
              "expected": "0"
            },
            {
              "call": "string_match(\"\", \"hello\")",
              "expected": "0"
            },
            {
              "call": "string_match(\"aabbccdd\", \"abbbxxd\")",
              "expected": "1"
            },
            {
              "call": "string_match(\"aaxxaaxx\", \"iaxxai\")",
              "expected": "3"
            },
            {
              "call": "string_match(\"iaxxai\", \"aaxxaaxx\")",
              "expected": "3"
            }
          ]
        },
        {
          "id": "string_splosion",
          "name": "string_splosion",
          "description": "Given a non-empty string like \"Code\" return a string like \"CCoCodCode\".",
          "stub": "def string_splosion(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_splosion(\"Code\")",
              "expected": "\"CCoCodCode\""
            },
            {
              "call": "string_splosion(\"abc\")",
              "expected": "\"aababc\""
            },
            {
              "call": "string_splosion(\"ab\")",
              "expected": "\"aab\""
            },
            {
              "call": "string_splosion(\"x\")",
              "expected": "\"x\""
            },
            {
              "call": "string_splosion(\"fade\")",
              "expected": "\"ffafadfade\""
            },
            {
              "call": "string_splosion(\"There\")",
              "expected": "\"TThTheTherThere\""
            },
            {
              "call": "string_splosion(\"Kitten\")",
              "expected": "\"KKiKitKittKitteKitten\""
            },
            {
              "call": "string_splosion(\"Bye\")",
              "expected": "\"BByBye\""
            },
            {
              "call": "string_splosion(\"Good\")",
              "expected": "\"GGoGooGood\""
            },
            {
              "call": "string_splosion(\"Bad\")",
              "expected": "\"BBaBad\""
            }
          ]
        },
        {
          "id": "string_times",
          "name": "string_times",
          "description": "Given a string and a non-negative int n, return a larger string that is n copies of the original string.",
          "stub": "def string_times(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_times(\"Hi\", 2)",
              "expected": "\"HiHi\""
            },
            {
              "call": "string_times(\"Hi\", 3)",
              "expected": "\"HiHiHi\""
            },
            {
              "call": "string_times(\"Hi\", 1)",
              "expected": "\"Hi\""
            },
            {
              "call": "string_times(\"Hi\", 0)",
              "expected": "\"\""
            },
            {
              "call": "string_times(\"Hi\", 5)",
              "expected": "\"HiHiHiHiHi\""
            },
            {
              "call": "string_times(\"Oh Boy!\", 2)",
              "expected": "\"Oh Boy!Oh Boy!\""
            },
            {
              "call": "string_times(\"x\", 4)",
              "expected": "\"xxxx\""
            },
            {
              "call": "string_times(\"\", 4)",
              "expected": "\"\""
            },
            {
              "call": "string_times(\"code\", 2)",
              "expected": "\"codecode\""
            },
            {
              "call": "string_times(\"code\", 3)",
              "expected": "\"codecodecode\""
            }
          ]
        },
        {
          "id": "string_x",
          "name": "string_x",
          "description": "Given a string, return a version where all the \"x\" have been removed. Except an \"x\" at the very start or end should not be removed.",
          "stub": "def string_x(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_x(\"xxHxix\")",
              "expected": "\"xHix\""
            },
            {
              "call": "string_x(\"abxxxcd\")",
              "expected": "\"abcd\""
            },
            {
              "call": "string_x(\"xabxxxcdx\")",
              "expected": "\"xabcdx\""
            },
            {
              "call": "string_x(\"xKittenx\")",
              "expected": "\"xKittenx\""
            },
            {
              "call": "string_x(\"Hello\")",
              "expected": "\"Hello\""
            },
            {
              "call": "string_x(\"xx\")",
              "expected": "\"xx\""
            },
            {
              "call": "string_x(\"x\")",
              "expected": "\"x\""
            },
            {
              "call": "string_x(\"\")",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "string_yak",
          "name": "string_yak",
          "description": "Suppose the string \"yak\" is unlucky. Given a string, return a version where all the \"yak\" are removed, but the \"a\" can be any char. The \"yak\" strings will not overlap.",
          "stub": "def string_yak(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_yak(\"yakpak\")",
              "expected": "\"pak\""
            },
            {
              "call": "string_yak(\"pakyak\")",
              "expected": "\"pak\""
            },
            {
              "call": "string_yak(\"yak123ya\")",
              "expected": "\"123ya\""
            },
            {
              "call": "string_yak(\"yak\")",
              "expected": "\"\""
            },
            {
              "call": "string_yak(\"yakxxxyak\")",
              "expected": "\"xxx\""
            },
            {
              "call": "string_yak(\"HiyakHi\")",
              "expected": "\"HiHi\""
            },
            {
              "call": "string_yak(\"xxxyakyyyakzzz\")",
              "expected": "\"xxxyyzzz\""
            }
          ]
        }
      ]
    },
    {
      "name": "String-1",
      "problems": [
        {
          "id": "at_first",
          "name": "at_first",
          "description": "Given a string, return a string length 2 made of its first 2 chars. If the string length is less than 2, use '@' for the missing chars.",
          "stub": "def at_first(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "at_first(\"hello\")",
              "expected": "\"he\""
            },
            {
              "call": "at_first(\"hi\")",
              "expected": "\"hi\""
            },
            {
              "call": "at_first(\"h\")",
              "expected": "\"h@\""
            },
            {
              "call": "at_first(\"\")",
              "expected": "\"@@\""
            },
            {
              "call": "at_first(\"kitten\")",
              "expected": "\"ki\""
            },
            {
              "call": "at_first(\"java\")",
              "expected": "\"ja\""
            },
            {
              "call": "at_first(\"j\")",
              "expected": "\"j@\""
            }
          ]
        },
        {
          "id": "combo_string",
          "name": "combo_string",
          "description": "Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).",
          "stub": "def combo_string(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "combo_string(\"Hello\", \"hi\")",
              "expected": "\"hiHellohi\""
            },
            {
              "call": "combo_string(\"hi\", \"Hello\")",
              "expected": "\"hiHellohi\""
            },
            {
              "call": "combo_string(\"aaa\", \"b\")",
              "expected": "\"baaab\""
            },
            {
              "call": "combo_string(\"b\", \"aaa\")",
              "expected": "\"baaab\""
            },
            {
              "call": "combo_string(\"aaa\", \"\")",
              "expected": "\"aaa\""
            },
            {
              "call": "combo_string(\"\", \"bb\")",
              "expected": "\"bb\""
            },
            {
              "call": "combo_string(\"aaa\", \"1234\")",
              "expected": "\"aaa1234aaa\""
            },
            {
              "call": "combo_string(\"aaa\", \"bb\")",
              "expected": "\"bbaaabb\""
            },
            {
              "call": "combo_string(\"a\", \"bb\")",
              "expected": "\"abba\""
            },
            {
              "call": "combo_string(\"bb\", \"a\")",
              "expected": "\"abba\""
            },
            {
              "call": "combo_string(\"xyz\", \"ab\")",
              "expected": "\"abxyzab\""
            }
          ]
        },
        {
          "id": "con_cat",
          "name": "con_cat",
          "description": "Given two strings, append them together (known as \"concatenation\") and return the result. However, if the concatenation creates a double-char, then omit one of the chars, so \"abc\" and \"cat\" yields \"abcat\".",
          "stub": "def con_cat(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "con_cat(\"abc\", \"cat\")",
              "expected": "\"abcat\""
            },
            {
              "call": "con_cat(\"dog\", \"cat\")",
              "expected": "\"dogcat\""
            },
            {
              "call": "con_cat(\"abc\", \"\")",
              "expected": "\"abc\""
            },
            {
              "call": "con_cat(\"\", \"cat\")",
              "expected": "\"cat\""
            },
            {
              "call": "con_cat(\"pig\", \"g\")",
              "expected": "\"pig\""
            },
            {
              "call": "con_cat(\"pig\", \"doggy\")",
              "expected": "\"pigdoggy\""
            }
          ]
        },
        {
          "id": "de_front",
          "name": "de_front",
          "description": "Given a string, return a version without the first 2 chars. Except keep the first char if it is 'a' and keep the second char if it is 'b'. The string may be any length. Harder than it looks.",
          "stub": "def de_front(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "de_front(\"Hello\")",
              "expected": "\"llo\""
            },
            {
              "call": "de_front(\"java\")",
              "expected": "\"va\""
            },
            {
              "call": "de_front(\"away\")",
              "expected": "\"aay\""
            },
            {
              "call": "de_front(\"axy\")",
              "expected": "\"ay\""
            },
            {
              "call": "de_front(\"abc\")",
              "expected": "\"abc\""
            },
            {
              "call": "de_front(\"xby\")",
              "expected": "\"by\""
            },
            {
              "call": "de_front(\"ab\")",
              "expected": "\"ab\""
            },
            {
              "call": "de_front(\"ax\")",
              "expected": "\"a\""
            },
            {
              "call": "de_front(\"axb\")",
              "expected": "\"ab\""
            },
            {
              "call": "de_front(\"aaa\")",
              "expected": "\"aa\""
            },
            {
              "call": "de_front(\"xbc\")",
              "expected": "\"bc\""
            },
            {
              "call": "de_front(\"bbb\")",
              "expected": "\"bb\""
            },
            {
              "call": "de_front(\"bazz\")",
              "expected": "\"zz\""
            },
            {
              "call": "de_front(\"ba\")",
              "expected": "\"\""
            },
            {
              "call": "de_front(\"abxyz\")",
              "expected": "\"abxyz\""
            },
            {
              "call": "de_front(\"hi\")",
              "expected": "\"\""
            },
            {
              "call": "de_front(\"his\")",
              "expected": "\"s\""
            },
            {
              "call": "de_front(\"xz\")",
              "expected": "\"\""
            },
            {
              "call": "de_front(\"zzz\")",
              "expected": "\"z\""
            }
          ]
        },
        {
          "id": "ends_ly",
          "name": "ends_ly",
          "description": "Given a string, return true if it ends in \"ly\".",
          "stub": "def ends_ly(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "ends_ly(\"oddly\")",
              "expected": "True"
            },
            {
              "call": "ends_ly(\"y\")",
              "expected": "False"
            },
            {
              "call": "ends_ly(\"oddy\")",
              "expected": "False"
            },
            {
              "call": "ends_ly(\"oddl\")",
              "expected": "False"
            },
            {
              "call": "ends_ly(\"olydd\")",
              "expected": "False"
            },
            {
              "call": "ends_ly(\"ly\")",
              "expected": "True"
            },
            {
              "call": "ends_ly(\"\")",
              "expected": "False"
            },
            {
              "call": "ends_ly(\"Falsey\")",
              "expected": "False"
            },
            {
              "call": "ends_ly(\"evenly\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "extra_end",
          "name": "extra_end",
          "description": "Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.",
          "stub": "def extra_end(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "extra_end(\"Hello\")",
              "expected": "\"lololo\""
            },
            {
              "call": "extra_end(\"ab\")",
              "expected": "\"ababab\""
            },
            {
              "call": "extra_end(\"Hi\")",
              "expected": "\"HiHiHi\""
            },
            {
              "call": "extra_end(\"Candy\")",
              "expected": "\"dydydy\""
            },
            {
              "call": "extra_end(\"Code\")",
              "expected": "\"dedede\""
            }
          ]
        },
        {
          "id": "extra_front",
          "name": "extra_front",
          "description": "Given a string, return a new string made of 3 copies of the first 2 chars of the original string. The string may be any length. If there are fewer than 2 chars, use whatever is there.",
          "stub": "def extra_front(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "extra_front(\"Hello\")",
              "expected": "\"HeHeHe\""
            },
            {
              "call": "extra_front(\"ab\")",
              "expected": "\"ababab\""
            },
            {
              "call": "extra_front(\"H\")",
              "expected": "\"HHH\""
            },
            {
              "call": "extra_front(\"\")",
              "expected": "\"\""
            },
            {
              "call": "extra_front(\"Candy\")",
              "expected": "\"CaCaCa\""
            },
            {
              "call": "extra_front(\"Code\")",
              "expected": "\"CoCoCo\""
            }
          ]
        },
        {
          "id": "first_half",
          "name": "first_half",
          "description": "Given a string of even length, return the first half. So the string \"WooHoo\" yields \"Woo\".",
          "stub": "def first_half(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "first_half(\"WooHoo\")",
              "expected": "\"Woo\""
            },
            {
              "call": "first_half(\"HelloThere\")",
              "expected": "\"Hello\""
            },
            {
              "call": "first_half(\"abcdef\")",
              "expected": "\"abc\""
            },
            {
              "call": "first_half(\"ab\")",
              "expected": "\"a\""
            },
            {
              "call": "first_half(\"\")",
              "expected": "\"\""
            },
            {
              "call": "first_half(\"0123456789\")",
              "expected": "\"01234\""
            },
            {
              "call": "first_half(\"kitten\")",
              "expected": "\"kit\""
            }
          ]
        },
        {
          "id": "first_two",
          "name": "first_two",
          "description": "Given a string, return the string made of its first two chars, so the string \"Hello\" yields \"He\". If the string is shorter than length 2, return whatever there is, so \"X\" yields \"X\", and the empty string \"\" yields the empty string \"\". Note that len(str) returns the length of a string.",
          "stub": "def first_two(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "first_two(\"Hello\")",
              "expected": "\"He\""
            },
            {
              "call": "first_two(\"abcdefg\")",
              "expected": "\"ab\""
            },
            {
              "call": "first_two(\"ab\")",
              "expected": "\"ab\""
            },
            {
              "call": "first_two(\"a\")",
              "expected": "\"a\""
            },
            {
              "call": "first_two(\"\")",
              "expected": "\"\""
            },
            {
              "call": "first_two(\"Kitten\")",
              "expected": "\"Ki\""
            },
            {
              "call": "first_two(\"hi\")",
              "expected": "\"hi\""
            },
            {
              "call": "first_two(\"hiya\")",
              "expected": "\"hi\""
            }
          ]
        },
        {
          "id": "front_again",
          "name": "front_again",
          "description": "Given a string, return true if the first 2 chars in the string also appear at the end of the string, such as with \"edited\".",
          "stub": "def front_again(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "front_again(\"edited\")",
              "expected": "True"
            },
            {
              "call": "front_again(\"edit\")",
              "expected": "False"
            },
            {
              "call": "front_again(\"ed\")",
              "expected": "True"
            },
            {
              "call": "front_again(\"jj\")",
              "expected": "True"
            },
            {
              "call": "front_again(\"jjj\")",
              "expected": "True"
            },
            {
              "call": "front_again(\"jjjj\")",
              "expected": "True"
            },
            {
              "call": "front_again(\"jjjk\")",
              "expected": "False"
            },
            {
              "call": "front_again(\"x\")",
              "expected": "False"
            },
            {
              "call": "front_again(\"\")",
              "expected": "False"
            },
            {
              "call": "front_again(\"java\")",
              "expected": "False"
            },
            {
              "call": "front_again(\"javaja\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "has_bad",
          "name": "has_bad",
          "description": "Given a string, return true if \"bad\" appears starting at index 0 or 1 in the string, such as with \"badxxx\" or \"xbadxx\" but not \"xxbadxx\". The string may be any length, including 0. Note: use .equals() to compare 2 strings.",
          "stub": "def has_bad(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "has_bad(\"badxx\")",
              "expected": "True"
            },
            {
              "call": "has_bad(\"xbadxx\")",
              "expected": "True"
            },
            {
              "call": "has_bad(\"xxbadxx\")",
              "expected": "False"
            },
            {
              "call": "has_bad(\"code\")",
              "expected": "False"
            },
            {
              "call": "has_bad(\"bad\")",
              "expected": "True"
            },
            {
              "call": "has_bad(\"ba\")",
              "expected": "False"
            },
            {
              "call": "has_bad(\"xba\")",
              "expected": "False"
            },
            {
              "call": "has_bad(\"xbad\")",
              "expected": "True"
            },
            {
              "call": "has_bad(\"\")",
              "expected": "False"
            },
            {
              "call": "has_bad(\"badyy\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "hello_name",
          "name": "hello_name",
          "description": "Given a string name, e.g. \"Bob\", return a greeting of the form \"Hello Bob!\".",
          "stub": "def hello_name(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "hello_name(\"Bob\")",
              "expected": "\"Hello Bob!\""
            },
            {
              "call": "hello_name(\"Alice\")",
              "expected": "\"Hello Alice!\""
            },
            {
              "call": "hello_name(\"X\")",
              "expected": "\"Hello X!\""
            },
            {
              "call": "hello_name(\"Dolly\")",
              "expected": "\"Hello Dolly!\""
            },
            {
              "call": "hello_name(\"Alpha\")",
              "expected": "\"Hello Alpha!\""
            },
            {
              "call": "hello_name(\"Omega\")",
              "expected": "\"Hello Omega!\""
            },
            {
              "call": "hello_name(\"Goodbye\")",
              "expected": "\"Hello Goodbye!\""
            },
            {
              "call": "hello_name(\"ho ho ho\")",
              "expected": "\"Hello ho ho ho!\""
            },
            {
              "call": "hello_name(\"xyz!\")",
              "expected": "\"Hello xyz!!\""
            },
            {
              "call": "hello_name(\"Hello\")",
              "expected": "\"Hello Hello!\""
            }
          ]
        },
        {
          "id": "last_chars",
          "name": "last_chars",
          "description": "Given 2 strings, a and b, return a new string made of the first char of a and the last char of b, so \"yo\" and \"java\" yields \"ya\". If either string is length 0, use '@' for its missing char.",
          "stub": "def last_chars(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "last_chars(\"last\", \"chars\")",
              "expected": "\"ls\""
            },
            {
              "call": "last_chars(\"yo\", \"java\")",
              "expected": "\"ya\""
            },
            {
              "call": "last_chars(\"hi\", \"\")",
              "expected": "\"h@\""
            },
            {
              "call": "last_chars(\"\", \"hello\")",
              "expected": "\"@o\""
            },
            {
              "call": "last_chars(\"\", \"\")",
              "expected": "\"@@\""
            },
            {
              "call": "last_chars(\"kitten\", \"hi\")",
              "expected": "\"ki\""
            },
            {
              "call": "last_chars(\"k\", \"zip\")",
              "expected": "\"kp\""
            },
            {
              "call": "last_chars(\"kitten\", \"\")",
              "expected": "\"k@\""
            },
            {
              "call": "last_chars(\"kitten\", \"zip\")",
              "expected": "\"kp\""
            }
          ]
        },
        {
          "id": "last_two",
          "name": "last_two",
          "description": "Given a string of any length, return a new string where the last 2 chars, if present, are swapped, so \"coding\" yields \"codign\".",
          "stub": "def last_two(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "last_two(\"coding\")",
              "expected": "\"codign\""
            },
            {
              "call": "last_two(\"cat\")",
              "expected": "\"cta\""
            },
            {
              "call": "last_two(\"ab\")",
              "expected": "\"ba\""
            },
            {
              "call": "last_two(\"a\")",
              "expected": "\"a\""
            },
            {
              "call": "last_two(\"\")",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "left2",
          "name": "left2",
          "description": "Given a string, return a \"rotated left 2\" version where the first 2 chars are moved to the end. The string length will be at least 2.",
          "stub": "def left2(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "left2(\"Hello\")",
              "expected": "\"lloHe\""
            },
            {
              "call": "left2(\"java\")",
              "expected": "\"vaja\""
            },
            {
              "call": "left2(\"Hi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "left2(\"code\")",
              "expected": "\"deco\""
            },
            {
              "call": "left2(\"cat\")",
              "expected": "\"tca\""
            },
            {
              "call": "left2(\"12345\")",
              "expected": "\"34512\""
            },
            {
              "call": "left2(\"Chocolate\")",
              "expected": "\"ocolateCh\""
            },
            {
              "call": "left2(\"bricks\")",
              "expected": "\"icksbr\""
            }
          ]
        },
        {
          "id": "make_abba",
          "name": "make_abba",
          "description": "Given two strings, a and b, return the result of putting them together in the order abba, e.g. \"Hi\" and \"Bye\" returns \"HiByeByeHi\".",
          "stub": "def make_abba(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "make_abba(\"Hi\", \"Bye\")",
              "expected": "\"HiByeByeHi\""
            },
            {
              "call": "make_abba(\"Yo\", \"Alice\")",
              "expected": "\"YoAliceAliceYo\""
            },
            {
              "call": "make_abba(\"What\", \"Up\")",
              "expected": "\"WhatUpUpWhat\""
            },
            {
              "call": "make_abba(\"aaa\", \"bbb\")",
              "expected": "\"aaabbbbbbaaa\""
            },
            {
              "call": "make_abba(\"x\", \"y\")",
              "expected": "\"xyyx\""
            },
            {
              "call": "make_abba(\"x\", \"\")",
              "expected": "\"xx\""
            },
            {
              "call": "make_abba(\"\", \"y\")",
              "expected": "\"yy\""
            },
            {
              "call": "make_abba(\"Bo\", \"Ya\")",
              "expected": "\"BoYaYaBo\""
            },
            {
              "call": "make_abba(\"Ya\", \"Ya\")",
              "expected": "\"YaYaYaYa\""
            }
          ]
        },
        {
          "id": "make_out_word",
          "name": "make_out_word",
          "description": "Given an \"out\" string length 4, such as \"<<>>\", and a word, return a new string where the word is in the middle of the out string, e.g. \"<<word>>\". Note: use str.substring(i, j) to extract the string starting at index i and going up to but not including index j.",
          "stub": "def make_out_word(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "make_out_word(\"<<>>\", \"Yay\")",
              "expected": "\"<<Yay>>\""
            },
            {
              "call": "make_out_word(\"<<>>\", \"WooHoo\")",
              "expected": "\"<<WooHoo>>\""
            },
            {
              "call": "make_out_word(\"[[]]\", \"word\")",
              "expected": "\"[[word]]\""
            },
            {
              "call": "make_out_word(\"HHoo\", \"Hello\")",
              "expected": "\"HHHellooo\""
            },
            {
              "call": "make_out_word(\"abyz\", \"YAY\")",
              "expected": "\"abYAYyz\""
            }
          ]
        },
        {
          "id": "make_tags",
          "name": "make_tags",
          "description": "The web is built with HTML strings like \"<i>Yay</i>\" which draws Yay as italic text. In this example, the \"i\" tag makes <i> and </i> which surround the word \"Yay\". Given tag and word strings, create the HTML string with tags around the word, e.g. \"<i>Yay</i>\".",
          "stub": "def make_tags(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "make_tags(\"i\", \"Yay\")",
              "expected": "\"<i>Yay</i>\""
            },
            {
              "call": "make_tags(\"i\", \"Hello\")",
              "expected": "\"<i>Hello</i>\""
            },
            {
              "call": "make_tags(\"cite\", \"Yay\")",
              "expected": "\"<cite>Yay</cite>\""
            },
            {
              "call": "make_tags(\"address\", \"here\")",
              "expected": "\"<address>here</address>\""
            },
            {
              "call": "make_tags(\"body\", \"Heart\")",
              "expected": "\"<body>Heart</body>\""
            },
            {
              "call": "make_tags(\"i\", \"i\")",
              "expected": "\"<i>i</i>\""
            },
            {
              "call": "make_tags(\"i\", \"\")",
              "expected": "\"<i></i>\""
            }
          ]
        },
        {
          "id": "middle_three",
          "name": "middle_three",
          "description": "Given a string of odd length, return the string length 3 from its middle, so \"Candy\" yields \"and\". The string length will be at least 3.",
          "stub": "def middle_three(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "middle_three(\"Candy\")",
              "expected": "\"and\""
            },
            {
              "call": "middle_three(\"and\")",
              "expected": "\"and\""
            },
            {
              "call": "middle_three(\"solving\")",
              "expected": "\"lvi\""
            },
            {
              "call": "middle_three(\"Hi yet Hi\")",
              "expected": "\"yet\""
            },
            {
              "call": "middle_three(\"java yet java\")",
              "expected": "\"yet\""
            },
            {
              "call": "middle_three(\"Chocolate\")",
              "expected": "\"col\""
            },
            {
              "call": "middle_three(\"XabcxyzabcX\")",
              "expected": "\"xyz\""
            }
          ]
        },
        {
          "id": "middle_two",
          "name": "middle_two",
          "description": "Given a string of even length, return a string made of the middle two chars, so the string \"string\" yields \"ri\". The string length will be at least 2.",
          "stub": "def middle_two(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "middle_two(\"string\")",
              "expected": "\"ri\""
            },
            {
              "call": "middle_two(\"code\")",
              "expected": "\"od\""
            },
            {
              "call": "middle_two(\"Practice\")",
              "expected": "\"ct\""
            },
            {
              "call": "middle_two(\"ab\")",
              "expected": "\"ab\""
            },
            {
              "call": "middle_two(\"0123456789\")",
              "expected": "\"45\""
            }
          ]
        },
        {
          "id": "min_cat",
          "name": "min_cat",
          "description": "Given two strings, append them together (known as \"concatenation\") and return the result. However, if the strings are different lengths, omit chars from the longer string so it is the same length as the shorter string. So \"Hello\" and \"Hi\" yield \"loHi\". The strings may be any length.",
          "stub": "def min_cat(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "min_cat(\"Hello\", \"Hi\")",
              "expected": "\"loHi\""
            },
            {
              "call": "min_cat(\"Hello\", \"java\")",
              "expected": "\"ellojava\""
            },
            {
              "call": "min_cat(\"java\", \"Hello\")",
              "expected": "\"javaello\""
            },
            {
              "call": "min_cat(\"abc\", \"x\")",
              "expected": "\"cx\""
            },
            {
              "call": "min_cat(\"x\", \"abc\")",
              "expected": "\"xc\""
            },
            {
              "call": "min_cat(\"abc\", \"\")",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "n_twice",
          "name": "n_twice",
          "description": "Given a string and an int n, return a string made of the first and last n chars from the string. The string length will be at least n.",
          "stub": "def n_twice(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "n_twice(\"Hello\", 2)",
              "expected": "\"Helo\""
            },
            {
              "call": "n_twice(\"Chocolate\", 3)",
              "expected": "\"Choate\""
            },
            {
              "call": "n_twice(\"Chocolate\", 1)",
              "expected": "\"Ce\""
            },
            {
              "call": "n_twice(\"Chocolate\", 0)",
              "expected": "\"\""
            },
            {
              "call": "n_twice(\"Hello\", 4)",
              "expected": "\"Hellello\""
            },
            {
              "call": "n_twice(\"Code\", 4)",
              "expected": "\"CodeCode\""
            },
            {
              "call": "n_twice(\"Code\", 2)",
              "expected": "\"Code\""
            }
          ]
        },
        {
          "id": "non_start",
          "name": "non_start",
          "description": "Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.",
          "stub": "def non_start(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "non_start(\"Hello\", \"There\")",
              "expected": "\"ellohere\""
            },
            {
              "call": "non_start(\"java\", \"code\")",
              "expected": "\"avaode\""
            },
            {
              "call": "non_start(\"shotl\", \"java\")",
              "expected": "\"hotlava\""
            },
            {
              "call": "non_start(\"ab\", \"xy\")",
              "expected": "\"by\""
            },
            {
              "call": "non_start(\"ab\", \"x\")",
              "expected": "\"b\""
            },
            {
              "call": "non_start(\"x\", \"ac\")",
              "expected": "\"c\""
            },
            {
              "call": "non_start(\"a\", \"x\")",
              "expected": "\"\""
            },
            {
              "call": "non_start(\"kit\", \"kat\")",
              "expected": "\"itat\""
            },
            {
              "call": "non_start(\"mart\", \"dart\")",
              "expected": "\"artart\""
            }
          ]
        },
        {
          "id": "right2",
          "name": "right2",
          "description": "Given a string, return a \"rotated right 2\" version where the last 2 chars are moved to the start. The string length will be at least 2.",
          "stub": "def right2(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "right2(\"Hello\")",
              "expected": "\"loHel\""
            },
            {
              "call": "right2(\"java\")",
              "expected": "\"vaja\""
            },
            {
              "call": "right2(\"Hi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "right2(\"code\")",
              "expected": "\"deco\""
            },
            {
              "call": "right2(\"cat\")",
              "expected": "\"atc\""
            },
            {
              "call": "right2(\"12345\")",
              "expected": "\"45123\""
            }
          ]
        },
        {
          "id": "see_color",
          "name": "see_color",
          "description": "Given a string, if the string begins with \"red\" or \"blue\" return that color string, otherwise return the empty string.",
          "stub": "def see_color(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "see_color(\"redxx\")",
              "expected": "\"red\""
            },
            {
              "call": "see_color(\"xxred\")",
              "expected": "\"\""
            },
            {
              "call": "see_color(\"blueTimes\")",
              "expected": "\"blue\""
            },
            {
              "call": "see_color(\"NoColor\")",
              "expected": "\"\""
            },
            {
              "call": "see_color(\"red\")",
              "expected": "\"red\""
            },
            {
              "call": "see_color(\"re\")",
              "expected": "\"\""
            },
            {
              "call": "see_color(\"blu\")",
              "expected": "\"\""
            },
            {
              "call": "see_color(\"blue\")",
              "expected": "\"blue\""
            },
            {
              "call": "see_color(\"a\")",
              "expected": "\"\""
            },
            {
              "call": "see_color(\"\")",
              "expected": "\"\""
            },
            {
              "call": "see_color(\"xyzred\")",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "start_word",
          "name": "start_word",
          "description": "Given a string and a second \"word\" string, we'll say that the word matches the string if it appears at the front of the string, except its first char does not need to match exactly. On a match, return the front of the string, or otherwise return the empty string. So, so with the string \"hippo\" the word \"hi\" returns \"hi\" and \"xip\" returns \"hip\". The word will be at least length 1.",
          "stub": "def start_word(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "start_word(\"hippo\", \"hi\")",
              "expected": "\"hi\""
            },
            {
              "call": "start_word(\"hippo\", \"xip\")",
              "expected": "\"hip\""
            },
            {
              "call": "start_word(\"hippo\", \"i\")",
              "expected": "\"h\""
            },
            {
              "call": "start_word(\"hippo\", \"ix\")",
              "expected": "\"\""
            },
            {
              "call": "start_word(\"h\", \"ix\")",
              "expected": "\"\""
            },
            {
              "call": "start_word(\"\", \"i\")",
              "expected": "\"\""
            },
            {
              "call": "start_word(\"hip\", \"zi\")",
              "expected": "\"hi\""
            },
            {
              "call": "start_word(\"hip\", \"zip\")",
              "expected": "\"hip\""
            },
            {
              "call": "start_word(\"hip\", \"zig\")",
              "expected": "\"\""
            },
            {
              "call": "start_word(\"h\", \"z\")",
              "expected": "\"h\""
            },
            {
              "call": "start_word(\"hippo\", \"xippo\")",
              "expected": "\"hippo\""
            },
            {
              "call": "start_word(\"hippo\", \"xyz\")",
              "expected": "\"\""
            },
            {
              "call": "start_word(\"hippo\", \"hip\")",
              "expected": "\"hip\""
            },
            {
              "call": "start_word(\"kitten\", \"cit\")",
              "expected": "\"kit\""
            },
            {
              "call": "start_word(\"kit\", \"cit\")",
              "expected": "\"kit\""
            }
          ]
        },
        {
          "id": "the_end",
          "name": "the_end",
          "description": "Given a string, return a string length 1 from its front, unlessfrontis false, in which case return a string length 1 from its back. The string will be non-empty.",
          "stub": "def the_end(str, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "the_end(\"Hello\", True)",
              "expected": "\"H\""
            },
            {
              "call": "the_end(\"Hello\", False)",
              "expected": "\"o\""
            },
            {
              "call": "the_end(\"oh\", True)",
              "expected": "\"o\""
            },
            {
              "call": "the_end(\"oh\", False)",
              "expected": "\"h\""
            },
            {
              "call": "the_end(\"x\", True)",
              "expected": "\"x\""
            },
            {
              "call": "the_end(\"x\", False)",
              "expected": "\"x\""
            },
            {
              "call": "the_end(\"java\", True)",
              "expected": "\"j\""
            },
            {
              "call": "the_end(\"chocolate\", False)",
              "expected": "\"e\""
            },
            {
              "call": "the_end(\"1234\", True)",
              "expected": "\"1\""
            },
            {
              "call": "the_end(\"code\", False)",
              "expected": "\"e\""
            }
          ]
        },
        {
          "id": "two_char",
          "name": "two_char",
          "description": "Given a string and an index, return a string length 2 starting at the given index. If the index is too big or too small to define a string length 2, use the first 2 chars. The string length will be at least 2.",
          "stub": "def two_char(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "two_char(\"java\", 0)",
              "expected": "\"ja\""
            },
            {
              "call": "two_char(\"java\", 2)",
              "expected": "\"va\""
            },
            {
              "call": "two_char(\"java\", 3)",
              "expected": "\"ja\""
            },
            {
              "call": "two_char(\"java\", 4)",
              "expected": "\"ja\""
            },
            {
              "call": "two_char(\"java\", -1)",
              "expected": "\"ja\""
            },
            {
              "call": "two_char(\"Hello\", 0)",
              "expected": "\"He\""
            },
            {
              "call": "two_char(\"Hello\", 1)",
              "expected": "\"el\""
            },
            {
              "call": "two_char(\"Hello\", 99)",
              "expected": "\"He\""
            },
            {
              "call": "two_char(\"Hello\", 3)",
              "expected": "\"lo\""
            },
            {
              "call": "two_char(\"Hello\", 4)",
              "expected": "\"He\""
            },
            {
              "call": "two_char(\"Hello\", 5)",
              "expected": "\"He\""
            },
            {
              "call": "two_char(\"Hello\", -7)",
              "expected": "\"He\""
            },
            {
              "call": "two_char(\"Hello\", 6)",
              "expected": "\"He\""
            },
            {
              "call": "two_char(\"Hello\", -1)",
              "expected": "\"He\""
            },
            {
              "call": "two_char(\"yay\", 0)",
              "expected": "\"ya\""
            }
          ]
        },
        {
          "id": "withou_end2",
          "name": "withou_end2",
          "description": "Given a string, return a version without both the first and last char of the string. The string may be any length, including 0.",
          "stub": "def withou_end2(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "withou_end2(\"Hello\")",
              "expected": "\"ell\""
            },
            {
              "call": "withou_end2(\"abc\")",
              "expected": "\"b\""
            },
            {
              "call": "withou_end2(\"ab\")",
              "expected": "\"\""
            },
            {
              "call": "withou_end2(\"a\")",
              "expected": "\"\""
            },
            {
              "call": "withou_end2(\"\")",
              "expected": "\"\""
            },
            {
              "call": "withou_end2(\"coldy\")",
              "expected": "\"old\""
            },
            {
              "call": "withou_end2(\"java code\")",
              "expected": "\"ava cod\""
            }
          ]
        },
        {
          "id": "without2",
          "name": "without2",
          "description": "Given a string, if a length 2 substring appears at both its beginning and end, return a string without the substring at the beginning, so \"HelloHe\" yields \"lloHe\". The substring may overlap with itself, so \"Hi\" yields \"\". Otherwise, return the original string unchanged.",
          "stub": "def without2(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "without2(\"HelloHe\")",
              "expected": "\"lloHe\""
            },
            {
              "call": "without2(\"HelloHi\")",
              "expected": "\"HelloHi\""
            },
            {
              "call": "without2(\"Hi\")",
              "expected": "\"\""
            },
            {
              "call": "without2(\"Chocolate\")",
              "expected": "\"Chocolate\""
            },
            {
              "call": "without2(\"xxx\")",
              "expected": "\"x\""
            },
            {
              "call": "without2(\"xx\")",
              "expected": "\"\""
            },
            {
              "call": "without2(\"x\")",
              "expected": "\"x\""
            },
            {
              "call": "without2(\"\")",
              "expected": "\"\""
            },
            {
              "call": "without2(\"Fruits\")",
              "expected": "\"Fruits\""
            }
          ]
        },
        {
          "id": "without_end",
          "name": "without_end",
          "description": "Given a string, return a version without the first and last char, so \"Hello\" yields \"ell\". The string length will be at least 2.",
          "stub": "def without_end(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "without_end(\"Hello\")",
              "expected": "\"ell\""
            },
            {
              "call": "without_end(\"java\")",
              "expected": "\"av\""
            },
            {
              "call": "without_end(\"coding\")",
              "expected": "\"odin\""
            },
            {
              "call": "without_end(\"code\")",
              "expected": "\"od\""
            },
            {
              "call": "without_end(\"ab\")",
              "expected": "\"\""
            },
            {
              "call": "without_end(\"Chocolate!\")",
              "expected": "\"hocolate\""
            },
            {
              "call": "without_end(\"kitten\")",
              "expected": "\"itte\""
            },
            {
              "call": "without_end(\"woohoo\")",
              "expected": "\"ooho\""
            }
          ]
        },
        {
          "id": "without_x",
          "name": "without_x",
          "description": "Given a string, if the first or last chars are 'x', return the string without those 'x' chars, and otherwise return the string unchanged.",
          "stub": "def without_x(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "without_x(\"xHix\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x(\"xHi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x(\"Hxix\")",
              "expected": "\"Hxi\""
            },
            {
              "call": "without_x(\"Hi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x(\"xxHi\")",
              "expected": "\"xHi\""
            },
            {
              "call": "without_x(\"Hix\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x(\"xaxbx\")",
              "expected": "\"axb\""
            },
            {
              "call": "without_x(\"xx\")",
              "expected": "\"\""
            },
            {
              "call": "without_x(\"x\")",
              "expected": "\"\""
            },
            {
              "call": "without_x(\"\")",
              "expected": "\"\""
            },
            {
              "call": "without_x(\"Hello\")",
              "expected": "\"Hello\""
            },
            {
              "call": "without_x(\"Hexllo\")",
              "expected": "\"Hexllo\""
            }
          ]
        },
        {
          "id": "without_x2",
          "name": "without_x2",
          "description": "Given a string, if one or both of the first 2 chars is 'x', return the string without those 'x' chars, and otherwise return the string unchanged. This is a little harder than it looks.",
          "stub": "def without_x2(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "without_x2(\"xHi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x2(\"Hxi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x2(\"Hi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x2(\"xxHi\")",
              "expected": "\"Hi\""
            },
            {
              "call": "without_x2(\"Hix\")",
              "expected": "\"Hix\""
            },
            {
              "call": "without_x2(\"xaxb\")",
              "expected": "\"axb\""
            },
            {
              "call": "without_x2(\"xx\")",
              "expected": "\"\""
            },
            {
              "call": "without_x2(\"x\")",
              "expected": "\"\""
            },
            {
              "call": "without_x2(\"\")",
              "expected": "\"\""
            },
            {
              "call": "without_x2(\"Hello\")",
              "expected": "\"Hello\""
            },
            {
              "call": "without_x2(\"Hexllo\")",
              "expected": "\"Hexllo\""
            },
            {
              "call": "without_x2(\"xHxllo\")",
              "expected": "\"Hxllo\""
            }
          ]
        }
      ]
    },
    {
      "name": "String-2",
      "problems": [
        {
          "id": "bob_there",
          "name": "bob_there",
          "description": "Return true if the given string contains a \"bob\" string, but where the middle 'o' char can be any char.",
          "stub": "def bob_there(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "bob_there(\"abcbob\")",
              "expected": "True"
            },
            {
              "call": "bob_there(\"b9b\")",
              "expected": "True"
            },
            {
              "call": "bob_there(\"bac\")",
              "expected": "False"
            },
            {
              "call": "bob_there(\"bbb\")",
              "expected": "True"
            },
            {
              "call": "bob_there(\"abcdefb\")",
              "expected": "False"
            },
            {
              "call": "bob_there(\"123abcbcdbabxyz\")",
              "expected": "True"
            },
            {
              "call": "bob_there(\"b12\")",
              "expected": "False"
            },
            {
              "call": "bob_there(\"b1b\")",
              "expected": "True"
            },
            {
              "call": "bob_there(\"b12b1b\")",
              "expected": "True"
            },
            {
              "call": "bob_there(\"bbc\")",
              "expected": "False"
            },
            {
              "call": "bob_there(\"bbb\")",
              "expected": "True"
            },
            {
              "call": "bob_there(\"bb\")",
              "expected": "False"
            },
            {
              "call": "bob_there(\"b\")",
              "expected": "False"
            }
          ]
        },
        {
          "id": "cat_dog",
          "name": "cat_dog",
          "description": "Return true if the string \"cat\" and \"dog\" appear the same number of times in the given string.",
          "stub": "def cat_dog(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "cat_dog(\"catdog\")",
              "expected": "True"
            },
            {
              "call": "cat_dog(\"catcat\")",
              "expected": "False"
            },
            {
              "call": "cat_dog(\"1cat1cadodog\")",
              "expected": "True"
            },
            {
              "call": "cat_dog(\"catxxdogxxxdog\")",
              "expected": "False"
            },
            {
              "call": "cat_dog(\"catxdogxdogxcat\")",
              "expected": "True"
            },
            {
              "call": "cat_dog(\"catxdogxdogxca\")",
              "expected": "False"
            },
            {
              "call": "cat_dog(\"dogdogcat\")",
              "expected": "False"
            },
            {
              "call": "cat_dog(\"dogogcat\")",
              "expected": "True"
            },
            {
              "call": "cat_dog(\"dog\")",
              "expected": "False"
            },
            {
              "call": "cat_dog(\"cat\")",
              "expected": "False"
            },
            {
              "call": "cat_dog(\"ca\")",
              "expected": "True"
            },
            {
              "call": "cat_dog(\"c\")",
              "expected": "True"
            },
            {
              "call": "cat_dog(\"\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "count_code",
          "name": "count_code",
          "description": "Return the number of times that the string \"code\" appears anywhere in the given string, except we'll accept any letter for the 'd', so \"cope\" and \"cooe\" count.",
          "stub": "def count_code(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_code(\"aaacodebbb\")",
              "expected": "1"
            },
            {
              "call": "count_code(\"codexxcode\")",
              "expected": "2"
            },
            {
              "call": "count_code(\"cozexxcope\")",
              "expected": "2"
            },
            {
              "call": "count_code(\"cozfxxcope\")",
              "expected": "1"
            },
            {
              "call": "count_code(\"xxcozeyycop\")",
              "expected": "1"
            },
            {
              "call": "count_code(\"cozcop\")",
              "expected": "0"
            },
            {
              "call": "count_code(\"abcxyz\")",
              "expected": "0"
            },
            {
              "call": "count_code(\"code\")",
              "expected": "1"
            },
            {
              "call": "count_code(\"ode\")",
              "expected": "0"
            },
            {
              "call": "count_code(\"c\")",
              "expected": "0"
            },
            {
              "call": "count_code(\"\")",
              "expected": "0"
            },
            {
              "call": "count_code(\"AAcodeBBcoleCCccoreDD\")",
              "expected": "3"
            },
            {
              "call": "count_code(\"AAcodeBBcoleCCccorfDD\")",
              "expected": "2"
            },
            {
              "call": "count_code(\"coAcodeBcoleccoreDD\")",
              "expected": "3"
            }
          ]
        },
        {
          "id": "count_hi",
          "name": "count_hi",
          "description": "Return the number of times that the string \"hi\" appears anywhere in the given string.",
          "stub": "def count_hi(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_hi(\"abc hi ho\")",
              "expected": "1"
            },
            {
              "call": "count_hi(\"ABChi hi\")",
              "expected": "2"
            },
            {
              "call": "count_hi(\"hihi\")",
              "expected": "2"
            },
            {
              "call": "count_hi(\"hiHIhi\")",
              "expected": "2"
            },
            {
              "call": "count_hi(\"\")",
              "expected": "0"
            },
            {
              "call": "count_hi(\"h\")",
              "expected": "0"
            },
            {
              "call": "count_hi(\"hi\")",
              "expected": "1"
            },
            {
              "call": "count_hi(\"Hi is no HI on ahI\")",
              "expected": "0"
            },
            {
              "call": "count_hi(\"hiho not HOHIhi\")",
              "expected": "2"
            }
          ]
        },
        {
          "id": "double_char",
          "name": "double_char",
          "description": "Given a string, return a string where for every char in the original, there are two chars.",
          "stub": "def double_char(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "double_char(\"The\")",
              "expected": "\"TThhee\""
            },
            {
              "call": "double_char(\"AAbb\")",
              "expected": "\"AAAAbbbb\""
            },
            {
              "call": "double_char(\"Hi-There\")",
              "expected": "\"HHii--TThheerree\""
            },
            {
              "call": "double_char(\"Word!\")",
              "expected": "\"WWoorrdd!!\""
            },
            {
              "call": "double_char(\"!!\")",
              "expected": "\"!!!!\""
            },
            {
              "call": "double_char(\"\")",
              "expected": "\"\""
            },
            {
              "call": "double_char(\"a\")",
              "expected": "\"aa\""
            },
            {
              "call": "double_char(\".\")",
              "expected": "\"..\""
            },
            {
              "call": "double_char(\"aa\")",
              "expected": "\"aaaa\""
            }
          ]
        },
        {
          "id": "end_other",
          "name": "end_other",
          "description": "Given two strings, return true if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be \"case sensitive\"). Note: str.lower() returns the lowercase version of a string.",
          "stub": "def end_other(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "end_other(\"Hiabc\", \"abc\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"AbC\", \"HiaBc\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"abc\", \"abXabc\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"Hiabc\", \"abcd\")",
              "expected": "False"
            },
            {
              "call": "end_other(\"Hiabc\", \"bc\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"Hiabcx\", \"bc\")",
              "expected": "False"
            },
            {
              "call": "end_other(\"abc\", \"abc\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"xyz\", \"12xyz\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"yz\", \"12xz\")",
              "expected": "False"
            },
            {
              "call": "end_other(\"Z\", \"12xz\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"12\", \"12\")",
              "expected": "True"
            },
            {
              "call": "end_other(\"abcXYZ\", \"abcDEF\")",
              "expected": "False"
            },
            {
              "call": "end_other(\"ab\", \"ab12\")",
              "expected": "False"
            },
            {
              "call": "end_other(\"ab\", \"12ab\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "get_sandwich",
          "name": "get_sandwich",
          "description": "A sandwich is two pieces of bread with something in between. Return the string that is between the first and last appearance of \"bread\" in the given string, or return the empty string \"\" if there are not two pieces of bread.",
          "stub": "def get_sandwich(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "get_sandwich(\"breadjambread\")",
              "expected": "\"jam\""
            },
            {
              "call": "get_sandwich(\"xxbreadjambreadyy\")",
              "expected": "\"jam\""
            },
            {
              "call": "get_sandwich(\"xxbreadyy\")",
              "expected": "\"\""
            },
            {
              "call": "get_sandwich(\"xxbreadbreadjambreadyy\")",
              "expected": "\"breadjam\""
            },
            {
              "call": "get_sandwich(\"breadAbread\")",
              "expected": "\"A\""
            },
            {
              "call": "get_sandwich(\"breadbread\")",
              "expected": "\"\""
            },
            {
              "call": "get_sandwich(\"abcbreaz\")",
              "expected": "\"\""
            },
            {
              "call": "get_sandwich(\"xyz\")",
              "expected": "\"\""
            },
            {
              "call": "get_sandwich(\"\")",
              "expected": "\"\""
            },
            {
              "call": "get_sandwich(\"breadbreaxbread\")",
              "expected": "\"breax\""
            },
            {
              "call": "get_sandwich(\"breaxbreadybread\")",
              "expected": "\"y\""
            },
            {
              "call": "get_sandwich(\"breadbreadbreadbread\")",
              "expected": "\"breadbread\""
            }
          ]
        },
        {
          "id": "mix_string",
          "name": "mix_string",
          "description": "Given two strings,aandb, create a bigger string made of the first char of a, the first char of b, the second char of a, the second char of b, and so on. Any leftover chars go at the end of the result.",
          "stub": "def mix_string(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "mix_string(\"abc\", \"xyz\")",
              "expected": "\"axbycz\""
            },
            {
              "call": "mix_string(\"Hi\", \"There\")",
              "expected": "\"HTihere\""
            },
            {
              "call": "mix_string(\"xxxx\", \"There\")",
              "expected": "\"xTxhxexre\""
            },
            {
              "call": "mix_string(\"xxx\", \"X\")",
              "expected": "\"xXxx\""
            },
            {
              "call": "mix_string(\"2/\", \"27 around\")",
              "expected": "\"22/7 around\""
            },
            {
              "call": "mix_string(\"\", \"Hello\")",
              "expected": "\"Hello\""
            },
            {
              "call": "mix_string(\"Abc\", \"\")",
              "expected": "\"Abc\""
            },
            {
              "call": "mix_string(\"\", \"\")",
              "expected": "\"\""
            },
            {
              "call": "mix_string(\"a\", \"b\")",
              "expected": "\"ab\""
            },
            {
              "call": "mix_string(\"ax\", \"b\")",
              "expected": "\"abx\""
            },
            {
              "call": "mix_string(\"a\", \"bx\")",
              "expected": "\"abx\""
            },
            {
              "call": "mix_string(\"So\", \"Long\")",
              "expected": "\"SLoong\""
            },
            {
              "call": "mix_string(\"Long\", \"So\")",
              "expected": "\"LSoong\""
            }
          ]
        },
        {
          "id": "one_two",
          "name": "one_two",
          "description": "Given a string, compute a new string by moving the first char to come after the next two chars, so \"abc\" yields \"bca\". Repeat this process for each subsequent group of 3 chars, so \"abcdef\" yields \"bcaefd\". Ignore any group of fewer than 3 chars at the end.",
          "stub": "def one_two(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "one_two(\"abc\")",
              "expected": "\"bca\""
            },
            {
              "call": "one_two(\"tca\")",
              "expected": "\"cat\""
            },
            {
              "call": "one_two(\"tcagdo\")",
              "expected": "\"catdog\""
            },
            {
              "call": "one_two(\"chocolate\")",
              "expected": "\"hocolctea\""
            },
            {
              "call": "one_two(\"1234567890\")",
              "expected": "\"231564897\""
            },
            {
              "call": "one_two(\"xabxabxabxabxabxabxab\")",
              "expected": "\"abxabxabxabxabxabxabx\""
            },
            {
              "call": "one_two(\"abcdefx\")",
              "expected": "\"bcaefd\""
            },
            {
              "call": "one_two(\"abcdefxy\")",
              "expected": "\"bcaefd\""
            },
            {
              "call": "one_two(\"abcdefxyz\")",
              "expected": "\"bcaefdyzx\""
            },
            {
              "call": "one_two(\"\")",
              "expected": "\"\""
            },
            {
              "call": "one_two(\"x\")",
              "expected": "\"\""
            },
            {
              "call": "one_two(\"xy\")",
              "expected": "\"\""
            },
            {
              "call": "one_two(\"xyz\")",
              "expected": "\"yzx\""
            },
            {
              "call": "one_two(\"abcdefghijklkmnopqrstuvwxyz1234567890\")",
              "expected": "\"bcaefdhigkljmnkpqostrvwuyzx231564897\""
            },
            {
              "call": "one_two(\"abcdefghijklkmnopqrstuvwxyz123456789\")",
              "expected": "\"bcaefdhigkljmnkpqostrvwuyzx231564897\""
            },
            {
              "call": "one_two(\"abcdefghijklkmnopqrstuvwxyz12345678\")",
              "expected": "\"bcaefdhigkljmnkpqostrvwuyzx231564\""
            }
          ]
        },
        {
          "id": "plus_out",
          "name": "plus_out",
          "description": "Given a string and a non-emptywordstring, return a version of the original string where all chars have been replaced by pluses (\"+\"), except for appearances of the word string which are preserved unchanged.",
          "stub": "def plus_out(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "plus_out(\"12xy34\", \"xy\")",
              "expected": "\"++xy++\""
            },
            {
              "call": "plus_out(\"12xy34\", \"1\")",
              "expected": "\"1+++++\""
            },
            {
              "call": "plus_out(\"12xy34xyabcxy\", \"xy\")",
              "expected": "\"++xy++xy+++xy\""
            },
            {
              "call": "plus_out(\"abXYabcXYZ\", \"ab\")",
              "expected": "\"ab++ab++++\""
            },
            {
              "call": "plus_out(\"abXYabcXYZ\", \"abc\")",
              "expected": "\"++++abc+++\""
            },
            {
              "call": "plus_out(\"abXYabcXYZ\", \"XY\")",
              "expected": "\"++XY+++XY+\""
            },
            {
              "call": "plus_out(\"abXYxyzXYZ\", \"XYZ\")",
              "expected": "\"+++++++XYZ\""
            },
            {
              "call": "plus_out(\"--++ab\", \"++\")",
              "expected": "\"++++++\""
            },
            {
              "call": "plus_out(\"aaxxxxbb\", \"xx\")",
              "expected": "\"++xxxx++\""
            },
            {
              "call": "plus_out(\"123123\", \"3\")",
              "expected": "\"++3++3\""
            }
          ]
        },
        {
          "id": "prefix_again",
          "name": "prefix_again",
          "description": "Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string appear somewhere else in the string? Assume that the string is not empty and that N is in the range 1..len(str).",
          "stub": "def prefix_again(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "prefix_again(\"abXYabc\", 1)",
              "expected": "True"
            },
            {
              "call": "prefix_again(\"abXYabc\", 2)",
              "expected": "True"
            },
            {
              "call": "prefix_again(\"abXYabc\", 3)",
              "expected": "False"
            },
            {
              "call": "prefix_again(\"xyzxyxyxy\", 2)",
              "expected": "True"
            },
            {
              "call": "prefix_again(\"xyzxyxyxy\", 3)",
              "expected": "False"
            },
            {
              "call": "prefix_again(\"Hi12345Hi6789Hi10\", 1)",
              "expected": "True"
            },
            {
              "call": "prefix_again(\"Hi12345Hi6789Hi10\", 2)",
              "expected": "True"
            },
            {
              "call": "prefix_again(\"Hi12345Hi6789Hi10\", 3)",
              "expected": "True"
            },
            {
              "call": "prefix_again(\"Hi12345Hi6789Hi10\", 4)",
              "expected": "False"
            },
            {
              "call": "prefix_again(\"a\", 1)",
              "expected": "False"
            },
            {
              "call": "prefix_again(\"aa\", 1)",
              "expected": "True"
            },
            {
              "call": "prefix_again(\"ab\", 1)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "repeat_end",
          "name": "repeat_end",
          "description": "Given a string and an int n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string, inclusive.",
          "stub": "def repeat_end(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "repeat_end(\"Hello\", 3)",
              "expected": "\"llollollo\""
            },
            {
              "call": "repeat_end(\"Hello\", 2)",
              "expected": "\"lolo\""
            },
            {
              "call": "repeat_end(\"Hello\", 1)",
              "expected": "\"o\""
            },
            {
              "call": "repeat_end(\"Hello\", 0)",
              "expected": "\"\""
            },
            {
              "call": "repeat_end(\"abc\", 3)",
              "expected": "\"abcabcabc\""
            },
            {
              "call": "repeat_end(\"1234\", 2)",
              "expected": "\"3434\""
            },
            {
              "call": "repeat_end(\"1234\", 3)",
              "expected": "\"234234234\""
            },
            {
              "call": "repeat_end(\"\", 0)",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "repeat_front",
          "name": "repeat_front",
          "description": "Given a string and an int n, return a string made of the first n characters of the string, followed by the first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, inclusive (i.e. n >= 0 and n <= len(str)).",
          "stub": "def repeat_front(str, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "repeat_front(\"Chocolate\", 4)",
              "expected": "\"ChocChoChC\""
            },
            {
              "call": "repeat_front(\"Chocolate\", 3)",
              "expected": "\"ChoChC\""
            },
            {
              "call": "repeat_front(\"Ice Cream\", 2)",
              "expected": "\"IcI\""
            },
            {
              "call": "repeat_front(\"Ice Cream\", 1)",
              "expected": "\"I\""
            },
            {
              "call": "repeat_front(\"Ice Cream\", 0)",
              "expected": "\"\""
            },
            {
              "call": "repeat_front(\"xyz\", 3)",
              "expected": "\"xyzxyx\""
            },
            {
              "call": "repeat_front(\"\", 0)",
              "expected": "\"\""
            },
            {
              "call": "repeat_front(\"Java\", 4)",
              "expected": "\"JavaJavJaJ\""
            },
            {
              "call": "repeat_front(\"Java\", 1)",
              "expected": "\"J\""
            }
          ]
        },
        {
          "id": "repeat_separator",
          "name": "repeat_separator",
          "description": "Given two strings,wordand a separatorsep, return a big string made ofcountoccurrences of the word, separated by the separator string.",
          "stub": "def repeat_separator(str, str2, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "repeat_separator(\"Word\", \"X\", 3)",
              "expected": "\"WordXWordXWord\""
            },
            {
              "call": "repeat_separator(\"This\", \"And\", 2)",
              "expected": "\"ThisAndThis\""
            },
            {
              "call": "repeat_separator(\"This\", \"And\", 1)",
              "expected": "\"This\""
            },
            {
              "call": "repeat_separator(\"Hi\", \"-n-\", 2)",
              "expected": "\"Hi-n-Hi\""
            },
            {
              "call": "repeat_separator(\"AAA\", \"\", 1)",
              "expected": "\"AAA\""
            },
            {
              "call": "repeat_separator(\"AAA\", \"\", 0)",
              "expected": "\"\""
            },
            {
              "call": "repeat_separator(\"A\", \"B\", 5)",
              "expected": "\"ABABABABA\""
            },
            {
              "call": "repeat_separator(\"abc\", \"XX\", 3)",
              "expected": "\"abcXXabcXXabc\""
            },
            {
              "call": "repeat_separator(\"abc\", \"XX\", 2)",
              "expected": "\"abcXXabc\""
            },
            {
              "call": "repeat_separator(\"abc\", \"XX\", 1)",
              "expected": "\"abc\""
            },
            {
              "call": "repeat_separator(\"XYZ\", \"a\", 2)",
              "expected": "\"XYZaXYZ\""
            }
          ]
        },
        {
          "id": "same_star_char",
          "name": "same_star_char",
          "description": "Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the star, they are the same.",
          "stub": "def same_star_char(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "same_star_char(\"xy*yzz\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"xy*zzz\")",
              "expected": "False"
            },
            {
              "call": "same_star_char(\"*xa*az\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"*xa*bz\")",
              "expected": "False"
            },
            {
              "call": "same_star_char(\"*xa*a*\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"*xa*a*a\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"*xa*a*b\")",
              "expected": "False"
            },
            {
              "call": "same_star_char(\"*12*2*2\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"12*2*3*\")",
              "expected": "False"
            },
            {
              "call": "same_star_char(\"abcDEF\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"XY*YYYY*Z*\")",
              "expected": "False"
            },
            {
              "call": "same_star_char(\"XY*YYYY*Y*\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"12*2*3*\")",
              "expected": "False"
            },
            {
              "call": "same_star_char(\"*\")",
              "expected": "True"
            },
            {
              "call": "same_star_char(\"**\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "star_out",
          "name": "star_out",
          "description": "Return a version of the given string, where for every star (*) in the string the star and the chars immediately to its left and right are gone. So \"ab*cd\" yields \"ad\" and \"ab**cd\" also yields \"ad\".",
          "stub": "def star_out(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "star_out(\"ab*cd\")",
              "expected": "\"ad\""
            },
            {
              "call": "star_out(\"ab**cd\")",
              "expected": "\"ad\""
            },
            {
              "call": "star_out(\"sm*eilly\")",
              "expected": "\"silly\""
            },
            {
              "call": "star_out(\"sm*eil*ly\")",
              "expected": "\"siy\""
            },
            {
              "call": "star_out(\"sm**eil*ly\")",
              "expected": "\"siy\""
            },
            {
              "call": "star_out(\"sm***eil*ly\")",
              "expected": "\"siy\""
            },
            {
              "call": "star_out(\"stringy*\")",
              "expected": "\"string\""
            },
            {
              "call": "star_out(\"*stringy\")",
              "expected": "\"tringy\""
            },
            {
              "call": "star_out(\"*str*in*gy\")",
              "expected": "\"ty\""
            },
            {
              "call": "star_out(\"abc\")",
              "expected": "\"abc\""
            },
            {
              "call": "star_out(\"a*bc\")",
              "expected": "\"c\""
            },
            {
              "call": "star_out(\"ab\")",
              "expected": "\"ab\""
            },
            {
              "call": "star_out(\"a*b\")",
              "expected": "\"\""
            },
            {
              "call": "star_out(\"a\")",
              "expected": "\"a\""
            },
            {
              "call": "star_out(\"a*\")",
              "expected": "\"\""
            },
            {
              "call": "star_out(\"*a\")",
              "expected": "\"\""
            },
            {
              "call": "star_out(\"*\")",
              "expected": "\"\""
            },
            {
              "call": "star_out(\"\")",
              "expected": "\"\""
            }
          ]
        },
        {
          "id": "word_ends",
          "name": "word_ends",
          "description": "Given a string and a non-emptywordstring, return a string made of each char just before and just after every appearance of the word in the string. Ignore cases where there is no char before or after the word, and a char may be included twice if it is between two words.",
          "stub": "def word_ends(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "word_ends(\"abcXY123XYijk\", \"XY\")",
              "expected": "\"c13i\""
            },
            {
              "call": "word_ends(\"XY123XY\", \"XY\")",
              "expected": "\"13\""
            },
            {
              "call": "word_ends(\"XY1XY\", \"XY\")",
              "expected": "\"11\""
            },
            {
              "call": "word_ends(\"XYXY\", \"XY\")",
              "expected": "\"XY\""
            },
            {
              "call": "word_ends(\"XY\", \"XY\")",
              "expected": "\"\""
            },
            {
              "call": "word_ends(\"Hi\", \"XY\")",
              "expected": "\"\""
            },
            {
              "call": "word_ends(\"\", \"XY\")",
              "expected": "\"\""
            },
            {
              "call": "word_ends(\"abc1xyz1i1j\", \"1\")",
              "expected": "\"cxziij\""
            },
            {
              "call": "word_ends(\"abc1xyz1\", \"1\")",
              "expected": "\"cxz\""
            },
            {
              "call": "word_ends(\"abc1xyz11\", \"1\")",
              "expected": "\"cxz11\""
            },
            {
              "call": "word_ends(\"abc1xyz1abc\", \"abc\")",
              "expected": "\"11\""
            },
            {
              "call": "word_ends(\"abc1xyz1abc\", \"b\")",
              "expected": "\"acac\""
            },
            {
              "call": "word_ends(\"abc1abc1abc\", \"abc\")",
              "expected": "\"1111\""
            }
          ]
        },
        {
          "id": "xy_balance",
          "name": "xy_balance",
          "description": "We'll say that a string is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char somewhere later in the string. So \"xxy\" is balanced, but \"xyx\" is not. One 'y' can balance multiple 'x's. Return true if the given string is xy-balanced.",
          "stub": "def xy_balance(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "xy_balance(\"aaxbby\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"aaxbb\")",
              "expected": "False"
            },
            {
              "call": "xy_balance(\"yaaxbb\")",
              "expected": "False"
            },
            {
              "call": "xy_balance(\"yaaxbby\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"xaxxbby\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"xaxxbbyx\")",
              "expected": "False"
            },
            {
              "call": "xy_balance(\"xxbxy\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"xxbx\")",
              "expected": "False"
            },
            {
              "call": "xy_balance(\"bbb\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"bxbb\")",
              "expected": "False"
            },
            {
              "call": "xy_balance(\"bxyb\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"xy\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"y\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"x\")",
              "expected": "False"
            },
            {
              "call": "xy_balance(\"\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"yxyxyxyx\")",
              "expected": "False"
            },
            {
              "call": "xy_balance(\"yxyxyxyxy\")",
              "expected": "True"
            },
            {
              "call": "xy_balance(\"12xabxxydxyxyzz\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "xyz_middle",
          "name": "xyz_middle",
          "description": "Given a string, does \"xyz\" appear in the middle of the string? To define middle, we'll say that the number of chars to the left and right of the \"xyz\" must differ by at most one. This problem is harder than it looks.",
          "stub": "def xyz_middle(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "xyz_middle(\"AAxyzBB\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"AxyzBB\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"AxyzBBB\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"AxyzBBBB\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"AAAxyzB\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"AAAxyzBB\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"AAAAxyzBB\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"AAAAAxyzBBB\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"1x345xyz12x4\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"xyzAxyzBBB\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"xyzAxyzBxyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"xyzxyzAxyzBxyzxyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"xyzxyzxyzBxyzxyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"xyzxyzAxyzxyzxyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"xyzxyzAxyzxyzxy\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"AxyzxyzBB\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"x\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"xy\")",
              "expected": "False"
            },
            {
              "call": "xyz_middle(\"xyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_middle(\"xyzz\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "xyz_there",
          "name": "xyz_there",
          "description": "Return true if the given string contains an appearance of \"xyz\" where the xyz is not directly preceeded by a period (.). So \"xxyz\" counts but \"x.xyz\" does not.",
          "stub": "def xyz_there(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "xyz_there(\"abcxyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_there(\"abc.xyz\")",
              "expected": "False"
            },
            {
              "call": "xyz_there(\"xyz.abc\")",
              "expected": "True"
            },
            {
              "call": "xyz_there(\"abcxy\")",
              "expected": "False"
            },
            {
              "call": "xyz_there(\"xyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_there(\"xy\")",
              "expected": "False"
            },
            {
              "call": "xyz_there(\"x\")",
              "expected": "False"
            },
            {
              "call": "xyz_there(\"\")",
              "expected": "False"
            },
            {
              "call": "xyz_there(\"abc.xyzxyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_there(\"abc.xxyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_there(\".xyz\")",
              "expected": "False"
            },
            {
              "call": "xyz_there(\"12.xyz\")",
              "expected": "False"
            },
            {
              "call": "xyz_there(\"12xyz\")",
              "expected": "True"
            },
            {
              "call": "xyz_there(\"1.xyz.xyz2.xyz\")",
              "expected": "False"
            }
          ]
        },
        {
          "id": "zip_zap",
          "name": "zip_zap",
          "description": "Look for patterns like \"zip\" and \"zap\" in the string -- length-3, starting with 'z' and ending with 'p'. Return a string where for all such words, the middle letter is gone, so \"zipXzap\" yields \"zpXzp\".",
          "stub": "def zip_zap(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "zip_zap(\"zipXzap\")",
              "expected": "\"zpXzp\""
            },
            {
              "call": "zip_zap(\"zopzop\")",
              "expected": "\"zpzp\""
            },
            {
              "call": "zip_zap(\"zzzopzop\")",
              "expected": "\"zzzpzp\""
            },
            {
              "call": "zip_zap(\"zibzap\")",
              "expected": "\"zibzp\""
            },
            {
              "call": "zip_zap(\"zip\")",
              "expected": "\"zp\""
            },
            {
              "call": "zip_zap(\"zi\")",
              "expected": "\"zi\""
            },
            {
              "call": "zip_zap(\"z\")",
              "expected": "\"z\""
            },
            {
              "call": "zip_zap(\"\")",
              "expected": "\"\""
            },
            {
              "call": "zip_zap(\"zzp\")",
              "expected": "\"zp\""
            },
            {
              "call": "zip_zap(\"abcppp\")",
              "expected": "\"abcppp\""
            },
            {
              "call": "zip_zap(\"azbcppp\")",
              "expected": "\"azbcppp\""
            },
            {
              "call": "zip_zap(\"azbcpzpp\")",
              "expected": "\"azbcpzp\""
            }
          ]
        }
      ]
    },
    {
      "name": "String-3",
      "problems": [
        {
          "id": "count_triple",
          "name": "count_triple",
          "description": "We'll say that a \"triple\" in a string is a char appearing three times in a row. Return the number of triples in the given string. The triples may overlap.",
          "stub": "def count_triple(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_triple(\"abcXXXabc\")",
              "expected": "1"
            },
            {
              "call": "count_triple(\"xxxabyyyycd\")",
              "expected": "3"
            },
            {
              "call": "count_triple(\"a\")",
              "expected": "0"
            },
            {
              "call": "count_triple(\"\")",
              "expected": "0"
            },
            {
              "call": "count_triple(\"XXXabc\")",
              "expected": "1"
            },
            {
              "call": "count_triple(\"XXXXabc\")",
              "expected": "2"
            },
            {
              "call": "count_triple(\"XXXXXabc\")",
              "expected": "3"
            },
            {
              "call": "count_triple(\"222abyyycdXXX\")",
              "expected": "3"
            },
            {
              "call": "count_triple(\"abYYYabXXXXXab\")",
              "expected": "4"
            },
            {
              "call": "count_triple(\"abYYXabXXYXXab\")",
              "expected": "0"
            },
            {
              "call": "count_triple(\"abYYXabXXYXXab\")",
              "expected": "0"
            },
            {
              "call": "count_triple(\"122abhhh2\")",
              "expected": "1"
            }
          ]
        },
        {
          "id": "count_yz",
          "name": "count_yz",
          "description": "Given a string, count the number of words ending in 'y' or 'z' -- so the 'y' in \"heavy\" and the 'z' in \"fez\" count, but not the 'y' in \"yellow\" (not case sensitive). We'll say that a y or z is at the end of a word if there is not an alphabetic letter immediately following it. (Note: Character.isLetter(char) tests if a char is an alphabetic letter.)",
          "stub": "def count_yz(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_yz(\"fez day\")",
              "expected": "2"
            },
            {
              "call": "count_yz(\"day fez\")",
              "expected": "2"
            },
            {
              "call": "count_yz(\"day fyyyz\")",
              "expected": "2"
            },
            {
              "call": "count_yz(\"day yak\")",
              "expected": "1"
            },
            {
              "call": "count_yz(\"day:yak\")",
              "expected": "1"
            },
            {
              "call": "count_yz(\"!!day--yaz!!\")",
              "expected": "2"
            },
            {
              "call": "count_yz(\"yak zak\")",
              "expected": "0"
            },
            {
              "call": "count_yz(\"DAY abc XYZ\")",
              "expected": "2"
            },
            {
              "call": "count_yz(\"aaz yyz my\")",
              "expected": "3"
            },
            {
              "call": "count_yz(\"y2bz\")",
              "expected": "2"
            },
            {
              "call": "count_yz(\"zxyx\")",
              "expected": "0"
            }
          ]
        },
        {
          "id": "equal_is_not",
          "name": "equal_is_not",
          "description": "Given a string, return true if the number of appearances of \"is\" anywhere in the string is equal to the number of appearances of \"not\" anywhere in the string (case sensitive).",
          "stub": "def equal_is_not(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "equal_is_not(\"This is not\")",
              "expected": "False"
            },
            {
              "call": "equal_is_not(\"This is notnot\")",
              "expected": "True"
            },
            {
              "call": "equal_is_not(\"noisxxnotyynotxisi\")",
              "expected": "True"
            },
            {
              "call": "equal_is_not(\"noisxxnotyynotxsi\")",
              "expected": "False"
            },
            {
              "call": "equal_is_not(\"xxxyyyzzzintint\")",
              "expected": "True"
            },
            {
              "call": "equal_is_not(\"\")",
              "expected": "True"
            },
            {
              "call": "equal_is_not(\"isisnotnot\")",
              "expected": "True"
            },
            {
              "call": "equal_is_not(\"isisnotno7Not\")",
              "expected": "False"
            },
            {
              "call": "equal_is_not(\"isnotis\")",
              "expected": "False"
            },
            {
              "call": "equal_is_not(\"mis3notpotbotis\")",
              "expected": "False"
            }
          ]
        },
        {
          "id": "g_happy",
          "name": "g_happy",
          "description": "We'll say that a lowercase 'g' in a string is \"happy\" if there is another 'g' immediately to its left or right. Return true if all the g's in the given string are happy.",
          "stub": "def g_happy(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "g_happy(\"xxggxx\")",
              "expected": "True"
            },
            {
              "call": "g_happy(\"xxgxx\")",
              "expected": "False"
            },
            {
              "call": "g_happy(\"xxggyygxx\")",
              "expected": "False"
            },
            {
              "call": "g_happy(\"g\")",
              "expected": "False"
            },
            {
              "call": "g_happy(\"gg\")",
              "expected": "True"
            },
            {
              "call": "g_happy(\"\")",
              "expected": "True"
            },
            {
              "call": "g_happy(\"xxgggxyz\")",
              "expected": "True"
            },
            {
              "call": "g_happy(\"xxgggxyg\")",
              "expected": "False"
            },
            {
              "call": "g_happy(\"xxgggxygg\")",
              "expected": "True"
            },
            {
              "call": "g_happy(\"mgm\")",
              "expected": "False"
            },
            {
              "call": "g_happy(\"mggm\")",
              "expected": "True"
            },
            {
              "call": "g_happy(\"yyygggxyy\")",
              "expected": "True"
            }
          ]
        },
        {
          "id": "max_block",
          "name": "max_block",
          "description": "Given a string, return the length of the largest \"block\" in the string. A block is a run of adjacent chars that are the same.",
          "stub": "def max_block(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "max_block(\"hoopla\")",
              "expected": "2"
            },
            {
              "call": "max_block(\"abbCCCddBBBxx\")",
              "expected": "3"
            },
            {
              "call": "max_block(\"\")",
              "expected": "0"
            },
            {
              "call": "max_block(\"xyz\")",
              "expected": "1"
            },
            {
              "call": "max_block(\"xxyz\")",
              "expected": "2"
            },
            {
              "call": "max_block(\"xyzz\")",
              "expected": "2"
            },
            {
              "call": "max_block(\"abbbcbbbxbbbx\")",
              "expected": "3"
            },
            {
              "call": "max_block(\"XXBBBbbxx\")",
              "expected": "3"
            },
            {
              "call": "max_block(\"XXBBBBbbxx\")",
              "expected": "4"
            },
            {
              "call": "max_block(\"XXBBBbbxxXXXX\")",
              "expected": "4"
            },
            {
              "call": "max_block(\"XX2222BBBbbXX2222\")",
              "expected": "4"
            }
          ]
        },
        {
          "id": "mirror_ends",
          "name": "mirror_ends",
          "description": "Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string. In other words, zero or more characters at the very begining of the given string, and at the very end of the string in reverse order (possibly overlapping). For example, the string \"abXYZba\" has the mirror end \"ab\".",
          "stub": "def mirror_ends(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "mirror_ends(\"abXYZba\")",
              "expected": "\"ab\""
            },
            {
              "call": "mirror_ends(\"abca\")",
              "expected": "\"a\""
            },
            {
              "call": "mirror_ends(\"aba\")",
              "expected": "\"aba\""
            },
            {
              "call": "mirror_ends(\"abab\")",
              "expected": "\"\""
            },
            {
              "call": "mirror_ends(\"xxx\")",
              "expected": "\"xxx\""
            },
            {
              "call": "mirror_ends(\"xxYxx\")",
              "expected": "\"xxYxx\""
            },
            {
              "call": "mirror_ends(\"Hi and iH\")",
              "expected": "\"Hi \""
            },
            {
              "call": "mirror_ends(\"x\")",
              "expected": "\"x\""
            },
            {
              "call": "mirror_ends(\"\")",
              "expected": "\"\""
            },
            {
              "call": "mirror_ends(\"123and then 321\")",
              "expected": "\"123\""
            },
            {
              "call": "mirror_ends(\"band andab\")",
              "expected": "\"ba\""
            }
          ]
        },
        {
          "id": "not_replace",
          "name": "not_replace",
          "description": "Given a string, return a string where every appearance of the lowercase word \"is\" has been replaced with \"is not\". The word \"is\" should not be immediately preceeded or followed by a letter -- so for example the \"is\" in \"this\" does not count. (Note: Character.isLetter(char) tests if a char is a letter.)",
          "stub": "def not_replace(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "not_replace(\"is test\")",
              "expected": "\"is not test\""
            },
            {
              "call": "not_replace(\"is-is\")",
              "expected": "\"is not-is not\""
            },
            {
              "call": "not_replace(\"This is right\")",
              "expected": "\"This is not right\""
            },
            {
              "call": "not_replace(\"This is isabell\")",
              "expected": "\"This is not isabell\""
            },
            {
              "call": "not_replace(\"\")",
              "expected": "\"\""
            },
            {
              "call": "not_replace(\"is\")",
              "expected": "\"is not\""
            },
            {
              "call": "not_replace(\"isis\")",
              "expected": "\"isis\""
            },
            {
              "call": "not_replace(\"Dis is bliss is\")",
              "expected": "\"Dis is not bliss is not\""
            },
            {
              "call": "not_replace(\"is his\")",
              "expected": "\"is not his\""
            },
            {
              "call": "not_replace(\"xis yis\")",
              "expected": "\"xis yis\""
            },
            {
              "call": "not_replace(\"AAAis is\")",
              "expected": "\"AAAis is not\""
            }
          ]
        },
        {
          "id": "same_ends",
          "name": "same_ends",
          "description": "Given a string, return the longest substring that appears at both the beginning and end of the string without overlapping. For example, sameEnds(\"abXab\") is \"ab\".",
          "stub": "def same_ends(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "same_ends(\"abXYab\")",
              "expected": "\"ab\""
            },
            {
              "call": "same_ends(\"xx\")",
              "expected": "\"x\""
            },
            {
              "call": "same_ends(\"xxx\")",
              "expected": "\"x\""
            },
            {
              "call": "same_ends(\"xxxx\")",
              "expected": "\"xx\""
            },
            {
              "call": "same_ends(\"javaXYZjava\")",
              "expected": "\"java\""
            },
            {
              "call": "same_ends(\"javajava\")",
              "expected": "\"java\""
            },
            {
              "call": "same_ends(\"xavaXYZjava\")",
              "expected": "\"\""
            },
            {
              "call": "same_ends(\"Hello! and Hello!\")",
              "expected": "\"Hello!\""
            },
            {
              "call": "same_ends(\"x\")",
              "expected": "\"\""
            },
            {
              "call": "same_ends(\"\")",
              "expected": "\"\""
            },
            {
              "call": "same_ends(\"abcb\")",
              "expected": "\"\""
            },
            {
              "call": "same_ends(\"mymmy\")",
              "expected": "\"my\""
            }
          ]
        },
        {
          "id": "sum_digits",
          "name": "sum_digits",
          "description": "Given a string, return the sum of the digits 0-9 that appear in the string, ignoring all other characters. Return 0 if there are no digits in the string. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)",
          "stub": "def sum_digits(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "sum_digits(\"aa1bc2d3\")",
              "expected": "6"
            },
            {
              "call": "sum_digits(\"aa11b33\")",
              "expected": "8"
            },
            {
              "call": "sum_digits(\"Chocolate\")",
              "expected": "0"
            },
            {
              "call": "sum_digits(\"5hoco1a1e\")",
              "expected": "7"
            },
            {
              "call": "sum_digits(\"123abc123\")",
              "expected": "12"
            },
            {
              "call": "sum_digits(\"\")",
              "expected": "0"
            },
            {
              "call": "sum_digits(\"Hello\")",
              "expected": "0"
            },
            {
              "call": "sum_digits(\"X1z9b2\")",
              "expected": "12"
            },
            {
              "call": "sum_digits(\"5432a\")",
              "expected": "14"
            }
          ]
        },
        {
          "id": "sum_numbers",
          "name": "sum_numbers",
          "description": "Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)",
          "stub": "def sum_numbers(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "sum_numbers(\"abc123xyz\")",
              "expected": "123"
            },
            {
              "call": "sum_numbers(\"aa11b33\")",
              "expected": "44"
            },
            {
              "call": "sum_numbers(\"7 11\")",
              "expected": "18"
            },
            {
              "call": "sum_numbers(\"Chocolate\")",
              "expected": "0"
            },
            {
              "call": "sum_numbers(\"5hoco1a1e\")",
              "expected": "7"
            },
            {
              "call": "sum_numbers(\"5$$1;;1!!\")",
              "expected": "7"
            },
            {
              "call": "sum_numbers(\"a1234bb11\")",
              "expected": "1245"
            },
            {
              "call": "sum_numbers(\"\")",
              "expected": "0"
            },
            {
              "call": "sum_numbers(\"a22bbb3\")",
              "expected": "25"
            }
          ]
        },
        {
          "id": "without_string",
          "name": "without_string",
          "description": "Given two strings,baseandremove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with \"xxx\" removing \"xx\" leaves \"x\".",
          "stub": "def without_string(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "without_string(\"Hello there\", \"llo\")",
              "expected": "\"He there\""
            },
            {
              "call": "without_string(\"Hello there\", \"e\")",
              "expected": "\"Hllo thr\""
            },
            {
              "call": "without_string(\"Hello there\", \"x\")",
              "expected": "\"Hello there\""
            },
            {
              "call": "without_string(\"This is a FISH\", \"IS\")",
              "expected": "\"Th  a FH\""
            },
            {
              "call": "without_string(\"THIS is a FISH\", \"is\")",
              "expected": "\"TH  a FH\""
            },
            {
              "call": "without_string(\"THIS is a FISH\", \"iS\")",
              "expected": "\"TH  a FH\""
            },
            {
              "call": "without_string(\"abxxxxab\", \"xx\")",
              "expected": "\"abab\""
            },
            {
              "call": "without_string(\"abxxxab\", \"xx\")",
              "expected": "\"abxab\""
            },
            {
              "call": "without_string(\"abxxxab\", \"x\")",
              "expected": "\"abab\""
            },
            {
              "call": "without_string(\"xxx\", \"x\")",
              "expected": "\"\""
            },
            {
              "call": "without_string(\"xxx\", \"xx\")",
              "expected": "\"x\""
            },
            {
              "call": "without_string(\"xyzzy\", \"Y\")",
              "expected": "\"xzz\""
            },
            {
              "call": "without_string(\"\", \"x\")",
              "expected": "\"\""
            },
            {
              "call": "without_string(\"abcabc\", \"b\")",
              "expected": "\"acac\""
            },
            {
              "call": "without_string(\"AA22bb\", \"2\")",
              "expected": "\"AAbb\""
            },
            {
              "call": "without_string(\"1111\", \"1\")",
              "expected": "\"\""
            },
            {
              "call": "without_string(\"1111\", \"11\")",
              "expected": "\"\""
            },
            {
              "call": "without_string(\"MkjtMkx\", \"Mk\")",
              "expected": "\"jtx\""
            },
            {
              "call": "without_string(\"Hi HoHo\", \"Ho\")",
              "expected": "\"Hi \""
            }
          ]
        }
      ]
    },
    {
      "name": "Logic-1",
      "problems": [
        {
          "id": "alarm_clock",
          "name": "alarm_clock",
          "description": "Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a bool indicating if we are on vacation, return a string of the form \"7:00\" indicating when the alarm clock should ring. Weekdays, the alarm should be \"7:00\" and on the weekend it should be \"10:00\". Unless we are on vacation -- then on weekdays it should be \"10:00\" and weekends it should be \"off\".",
          "stub": "def alarm_clock(n, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "alarm_clock(1, False)",
              "expected": "\"7:00\""
            },
            {
              "call": "alarm_clock(5, False)",
              "expected": "\"7:00\""
            },
            {
              "call": "alarm_clock(0, False)",
              "expected": "\"10:00\""
            },
            {
              "call": "alarm_clock(6, False)",
              "expected": "\"10:00\""
            },
            {
              "call": "alarm_clock(0, True)",
              "expected": "\"off\""
            },
            {
              "call": "alarm_clock(6, True)",
              "expected": "\"off\""
            },
            {
              "call": "alarm_clock(1, True)",
              "expected": "\"10:00\""
            },
            {
              "call": "alarm_clock(3, True)",
              "expected": "\"10:00\""
            },
            {
              "call": "alarm_clock(5, True)",
              "expected": "\"10:00\""
            }
          ]
        },
        {
          "id": "answer_cell",
          "name": "answer_cell",
          "description": "Your cell phone rings. Return true if you should answer it. Normally you answer, except in the morning you only answer if it is your mom calling. In all cases, if you are asleep, you do not answer.",
          "stub": "def answer_cell(b, b2, b3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "answer_cell(False, False, False)",
              "expected": "True"
            },
            {
              "call": "answer_cell(False, False, True)",
              "expected": "False"
            },
            {
              "call": "answer_cell(True, False, False)",
              "expected": "False"
            },
            {
              "call": "answer_cell(True, True, False)",
              "expected": "True"
            },
            {
              "call": "answer_cell(False, True, False)",
              "expected": "True"
            },
            {
              "call": "answer_cell(True, True, True)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "blue_ticket",
          "name": "blue_ticket",
          "description": "You have a blue lottery ticket, with ints a, b, and c on it. This makes three pairs, which we'll call ab, bc, and ac. Consider the sum of the numbers in each pair. If any pair sums to exactly 10, the result is 10. Otherwise if the ab sum is exactly 10 more than either bc or ac sums, the result is 5. Otherwise the result is 0.",
          "stub": "def blue_ticket(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "blue_ticket(9, 1, 0)",
              "expected": "10"
            },
            {
              "call": "blue_ticket(9, 2, 0)",
              "expected": "0"
            },
            {
              "call": "blue_ticket(6, 1, 4)",
              "expected": "10"
            },
            {
              "call": "blue_ticket(6, 1, 5)",
              "expected": "0"
            },
            {
              "call": "blue_ticket(10, 0, 0)",
              "expected": "10"
            },
            {
              "call": "blue_ticket(15, 0, 5)",
              "expected": "5"
            },
            {
              "call": "blue_ticket(5, 15, 5)",
              "expected": "10"
            },
            {
              "call": "blue_ticket(4, 11, 1)",
              "expected": "5"
            },
            {
              "call": "blue_ticket(13, 2, 3)",
              "expected": "5"
            },
            {
              "call": "blue_ticket(8, 4, 3)",
              "expected": "0"
            },
            {
              "call": "blue_ticket(8, 4, 2)",
              "expected": "10"
            },
            {
              "call": "blue_ticket(8, 4, 1)",
              "expected": "0"
            }
          ]
        },
        {
          "id": "caught_speeding",
          "name": "caught_speeding",
          "description": "You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.",
          "stub": "def caught_speeding(n, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "caught_speeding(60, False)",
              "expected": "0"
            },
            {
              "call": "caught_speeding(65, False)",
              "expected": "1"
            },
            {
              "call": "caught_speeding(65, True)",
              "expected": "0"
            },
            {
              "call": "caught_speeding(80, False)",
              "expected": "1"
            },
            {
              "call": "caught_speeding(85, False)",
              "expected": "2"
            },
            {
              "call": "caught_speeding(85, True)",
              "expected": "1"
            },
            {
              "call": "caught_speeding(70, False)",
              "expected": "1"
            },
            {
              "call": "caught_speeding(75, False)",
              "expected": "1"
            },
            {
              "call": "caught_speeding(75, True)",
              "expected": "1"
            },
            {
              "call": "caught_speeding(40, False)",
              "expected": "0"
            },
            {
              "call": "caught_speeding(40, True)",
              "expected": "0"
            },
            {
              "call": "caught_speeding(90, False)",
              "expected": "2"
            }
          ]
        },
        {
          "id": "cigar_party",
          "name": "cigar_party",
          "description": "When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return true if the party with the given values is successful, or false otherwise.",
          "stub": "def cigar_party(n, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "cigar_party(30, False)",
              "expected": "False"
            },
            {
              "call": "cigar_party(50, False)",
              "expected": "True"
            },
            {
              "call": "cigar_party(70, True)",
              "expected": "True"
            },
            {
              "call": "cigar_party(30, True)",
              "expected": "False"
            },
            {
              "call": "cigar_party(50, True)",
              "expected": "True"
            },
            {
              "call": "cigar_party(60, False)",
              "expected": "True"
            },
            {
              "call": "cigar_party(61, False)",
              "expected": "False"
            },
            {
              "call": "cigar_party(40, False)",
              "expected": "True"
            },
            {
              "call": "cigar_party(39, False)",
              "expected": "False"
            },
            {
              "call": "cigar_party(40, True)",
              "expected": "True"
            },
            {
              "call": "cigar_party(39, True)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "date_fashion",
          "name": "date_fashion",
          "description": "You and your date are trying to get a table at a restaurant. The parameter \"you\" is the stylishness of your clothes, in the range 0..10, and \"date\" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).",
          "stub": "def date_fashion(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "date_fashion(5, 10)",
              "expected": "2"
            },
            {
              "call": "date_fashion(5, 2)",
              "expected": "0"
            },
            {
              "call": "date_fashion(5, 5)",
              "expected": "1"
            },
            {
              "call": "date_fashion(3, 3)",
              "expected": "1"
            },
            {
              "call": "date_fashion(10, 2)",
              "expected": "0"
            },
            {
              "call": "date_fashion(2, 9)",
              "expected": "0"
            },
            {
              "call": "date_fashion(9, 9)",
              "expected": "2"
            },
            {
              "call": "date_fashion(10, 5)",
              "expected": "2"
            },
            {
              "call": "date_fashion(2, 2)",
              "expected": "0"
            },
            {
              "call": "date_fashion(3, 7)",
              "expected": "1"
            },
            {
              "call": "date_fashion(2, 7)",
              "expected": "0"
            },
            {
              "call": "date_fashion(6, 2)",
              "expected": "0"
            }
          ]
        },
        {
          "id": "fizz_string",
          "name": "fizz_string",
          "description": "Given a string str, if the string starts with \"f\" return \"Fizz\". If the string ends with \"b\" return \"Buzz\". If both the \"f\" and \"b\" conditions are true, return \"FizzBuzz\". In all other cases, return the string unchanged. (See also:FizzBuzz Code)",
          "stub": "def fizz_string(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "fizz_string(\"fig\")",
              "expected": "\"Fizz\""
            },
            {
              "call": "fizz_string(\"dib\")",
              "expected": "\"Buzz\""
            },
            {
              "call": "fizz_string(\"fib\")",
              "expected": "\"FizzBuzz\""
            },
            {
              "call": "fizz_string(\"abc\")",
              "expected": "\"abc\""
            },
            {
              "call": "fizz_string(\"fooo\")",
              "expected": "\"Fizz\""
            },
            {
              "call": "fizz_string(\"booo\")",
              "expected": "\"booo\""
            },
            {
              "call": "fizz_string(\"ooob\")",
              "expected": "\"Buzz\""
            },
            {
              "call": "fizz_string(\"fooob\")",
              "expected": "\"FizzBuzz\""
            },
            {
              "call": "fizz_string(\"f\")",
              "expected": "\"Fizz\""
            },
            {
              "call": "fizz_string(\"b\")",
              "expected": "\"Buzz\""
            },
            {
              "call": "fizz_string(\"abcb\")",
              "expected": "\"Buzz\""
            },
            {
              "call": "fizz_string(\"Hello\")",
              "expected": "\"Hello\""
            },
            {
              "call": "fizz_string(\"Hellob\")",
              "expected": "\"Buzz\""
            },
            {
              "call": "fizz_string(\"af\")",
              "expected": "\"af\""
            },
            {
              "call": "fizz_string(\"bf\")",
              "expected": "\"bf\""
            },
            {
              "call": "fizz_string(\"fb\")",
              "expected": "\"FizzBuzz\""
            }
          ]
        },
        {
          "id": "fizz_string2",
          "name": "fizz_string2",
          "description": "Given an int n, return the string form of the number followed by \"!\". So the int 6 yields \"6!\". Except if the number is divisible by 3 use \"Fizz\" instead of the number, and if the number is divisible by 5 use \"Buzz\", and if divisible by both 3 and 5, use \"FizzBuzz\". Note: the % \"mod\" operator computes the remainder after division, so 23 % 10 yields 3. What will the remainder be when one number divides evenly into another? (See also:FizzBuzz CodeandIntroduction to Mod)",
          "stub": "def fizz_string2(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "fizz_string2(1)",
              "expected": "\"1!\""
            },
            {
              "call": "fizz_string2(2)",
              "expected": "\"2!\""
            },
            {
              "call": "fizz_string2(3)",
              "expected": "\"Fizz!\""
            },
            {
              "call": "fizz_string2(4)",
              "expected": "\"4!\""
            },
            {
              "call": "fizz_string2(5)",
              "expected": "\"Buzz!\""
            },
            {
              "call": "fizz_string2(6)",
              "expected": "\"Fizz!\""
            },
            {
              "call": "fizz_string2(7)",
              "expected": "\"7!\""
            },
            {
              "call": "fizz_string2(8)",
              "expected": "\"8!\""
            },
            {
              "call": "fizz_string2(9)",
              "expected": "\"Fizz!\""
            },
            {
              "call": "fizz_string2(15)",
              "expected": "\"FizzBuzz!\""
            },
            {
              "call": "fizz_string2(16)",
              "expected": "\"16!\""
            },
            {
              "call": "fizz_string2(18)",
              "expected": "\"Fizz!\""
            },
            {
              "call": "fizz_string2(19)",
              "expected": "\"19!\""
            },
            {
              "call": "fizz_string2(21)",
              "expected": "\"Fizz!\""
            },
            {
              "call": "fizz_string2(44)",
              "expected": "\"44!\""
            },
            {
              "call": "fizz_string2(45)",
              "expected": "\"FizzBuzz!\""
            },
            {
              "call": "fizz_string2(100)",
              "expected": "\"Buzz!\""
            }
          ]
        },
        {
          "id": "green_ticket",
          "name": "green_ticket",
          "description": "You have a green lottery ticket, with ints a, b, and c on it. If the numbers are all different from each other, the result is 0. If all of the numbers are the same, the result is 20. If two of the numbers are the same, the result is 10.",
          "stub": "def green_ticket(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "green_ticket(1, 2, 3)",
              "expected": "0"
            },
            {
              "call": "green_ticket(2, 2, 2)",
              "expected": "20"
            },
            {
              "call": "green_ticket(1, 1, 2)",
              "expected": "10"
            },
            {
              "call": "green_ticket(2, 1, 1)",
              "expected": "10"
            },
            {
              "call": "green_ticket(1, 2, 1)",
              "expected": "10"
            },
            {
              "call": "green_ticket(3, 2, 1)",
              "expected": "0"
            },
            {
              "call": "green_ticket(0, 0, 0)",
              "expected": "20"
            },
            {
              "call": "green_ticket(2, 0, 0)",
              "expected": "10"
            },
            {
              "call": "green_ticket(0, 9, 10)",
              "expected": "0"
            },
            {
              "call": "green_ticket(0, 10, 0)",
              "expected": "10"
            },
            {
              "call": "green_ticket(9, 9, 9)",
              "expected": "20"
            },
            {
              "call": "green_ticket(9, 0, 9)",
              "expected": "10"
            }
          ]
        },
        {
          "id": "in1_to10",
          "name": "in1_to10",
          "description": "Given a number n, return true if n is in the range 1..10, inclusive. Unless outsideMode is true, in which case return true if the number is less or equal to 1, or greater or equal to 10.",
          "stub": "def in1_to10(n, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "in1_to10(5, False)",
              "expected": "True"
            },
            {
              "call": "in1_to10(11, False)",
              "expected": "False"
            },
            {
              "call": "in1_to10(11, True)",
              "expected": "True"
            },
            {
              "call": "in1_to10(10, False)",
              "expected": "True"
            },
            {
              "call": "in1_to10(10, True)",
              "expected": "True"
            },
            {
              "call": "in1_to10(9, False)",
              "expected": "True"
            },
            {
              "call": "in1_to10(9, True)",
              "expected": "False"
            },
            {
              "call": "in1_to10(1, False)",
              "expected": "True"
            },
            {
              "call": "in1_to10(1, True)",
              "expected": "True"
            },
            {
              "call": "in1_to10(0, False)",
              "expected": "False"
            },
            {
              "call": "in1_to10(0, True)",
              "expected": "True"
            },
            {
              "call": "in1_to10(-1, False)",
              "expected": "False"
            },
            {
              "call": "in1_to10(-1, True)",
              "expected": "True"
            },
            {
              "call": "in1_to10(99, False)",
              "expected": "False"
            },
            {
              "call": "in1_to10(-99, True)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "in_order",
          "name": "in_order",
          "description": "Given three ints, a b c, return true if b is greater than a, and c is greater than b. However, with the exception that if \"bOk\" is true, b does not need to be greater than a.",
          "stub": "def in_order(n, n2, n3, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "in_order(1, 2, 4, False)",
              "expected": "True"
            },
            {
              "call": "in_order(1, 2, 1, False)",
              "expected": "False"
            },
            {
              "call": "in_order(1, 1, 2, True)",
              "expected": "True"
            },
            {
              "call": "in_order(3, 2, 4, False)",
              "expected": "False"
            },
            {
              "call": "in_order(2, 3, 4, False)",
              "expected": "True"
            },
            {
              "call": "in_order(3, 2, 4, True)",
              "expected": "True"
            },
            {
              "call": "in_order(4, 2, 2, True)",
              "expected": "False"
            },
            {
              "call": "in_order(4, 5, 2, True)",
              "expected": "False"
            },
            {
              "call": "in_order(2, 4, 6, True)",
              "expected": "True"
            },
            {
              "call": "in_order(7, 9, 10, False)",
              "expected": "True"
            },
            {
              "call": "in_order(7, 5, 6, True)",
              "expected": "True"
            },
            {
              "call": "in_order(7, 5, 4, True)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "in_order_equal",
          "name": "in_order_equal",
          "description": "Given three ints, a b c, return true if they are in strict increasing order, such as 2 5 11, or 5 6 7, but not 6 5 7 or 5 5 7. However, with the exception that if \"equalOk\" is true, equality is allowed, such as 5 5 7 or 5 5 5.",
          "stub": "def in_order_equal(n, n2, n3, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "in_order_equal(2, 5, 11, False)",
              "expected": "True"
            },
            {
              "call": "in_order_equal(5, 7, 6, False)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(5, 5, 7, True)",
              "expected": "True"
            },
            {
              "call": "in_order_equal(5, 5, 7, False)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(2, 5, 4, False)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(3, 4, 3, False)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(3, 4, 4, False)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(3, 4, 3, True)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(3, 4, 4, True)",
              "expected": "True"
            },
            {
              "call": "in_order_equal(1, 5, 5, True)",
              "expected": "True"
            },
            {
              "call": "in_order_equal(5, 5, 5, True)",
              "expected": "True"
            },
            {
              "call": "in_order_equal(2, 2, 1, True)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(9, 2, 2, True)",
              "expected": "False"
            },
            {
              "call": "in_order_equal(0, 1, 0, True)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "last_digit",
          "name": "last_digit",
          "description": "Given three ints, a b c, return true if two or more of them have the same rightmost digit. The ints are non-negative. Note: the % \"mod\" operator computes the remainder, e.g. 17 % 10 is 7.",
          "stub": "def last_digit(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "last_digit(23, 19, 13)",
              "expected": "True"
            },
            {
              "call": "last_digit(23, 19, 12)",
              "expected": "False"
            },
            {
              "call": "last_digit(23, 19, 3)",
              "expected": "True"
            },
            {
              "call": "last_digit(23, 19, 39)",
              "expected": "True"
            },
            {
              "call": "last_digit(1, 2, 3)",
              "expected": "False"
            },
            {
              "call": "last_digit(1, 1, 2)",
              "expected": "True"
            },
            {
              "call": "last_digit(1, 2, 2)",
              "expected": "True"
            },
            {
              "call": "last_digit(14, 25, 43)",
              "expected": "False"
            },
            {
              "call": "last_digit(14, 25, 45)",
              "expected": "True"
            },
            {
              "call": "last_digit(248, 106, 1002)",
              "expected": "False"
            },
            {
              "call": "last_digit(248, 106, 1008)",
              "expected": "True"
            },
            {
              "call": "last_digit(10, 11, 20)",
              "expected": "True"
            },
            {
              "call": "last_digit(0, 11, 0)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "less20",
          "name": "less20",
          "description": "Return true if the given non-negative number is 1 or 2lessthan a multiple of 20. So for example 38 and 39 return true, but 40 returns false. See also:Introduction to Mod",
          "stub": "def less20(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "less20(18)",
              "expected": "True"
            },
            {
              "call": "less20(19)",
              "expected": "True"
            },
            {
              "call": "less20(20)",
              "expected": "False"
            },
            {
              "call": "less20(8)",
              "expected": "False"
            },
            {
              "call": "less20(17)",
              "expected": "False"
            },
            {
              "call": "less20(23)",
              "expected": "False"
            },
            {
              "call": "less20(25)",
              "expected": "False"
            },
            {
              "call": "less20(30)",
              "expected": "False"
            },
            {
              "call": "less20(31)",
              "expected": "False"
            },
            {
              "call": "less20(58)",
              "expected": "True"
            },
            {
              "call": "less20(59)",
              "expected": "True"
            },
            {
              "call": "less20(60)",
              "expected": "False"
            },
            {
              "call": "less20(61)",
              "expected": "False"
            },
            {
              "call": "less20(62)",
              "expected": "False"
            },
            {
              "call": "less20(1017)",
              "expected": "False"
            },
            {
              "call": "less20(1018)",
              "expected": "True"
            },
            {
              "call": "less20(1019)",
              "expected": "True"
            },
            {
              "call": "less20(1020)",
              "expected": "False"
            },
            {
              "call": "less20(1021)",
              "expected": "False"
            },
            {
              "call": "less20(1022)",
              "expected": "False"
            },
            {
              "call": "less20(1023)",
              "expected": "False"
            },
            {
              "call": "less20(37)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "less_by10",
          "name": "less_by10",
          "description": "Given three ints, a b c, return true if one of them is 10 or more less than one of the others.",
          "stub": "def less_by10(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "less_by10(1, 7, 11)",
              "expected": "True"
            },
            {
              "call": "less_by10(1, 7, 10)",
              "expected": "False"
            },
            {
              "call": "less_by10(11, 1, 7)",
              "expected": "True"
            },
            {
              "call": "less_by10(10, 7, 1)",
              "expected": "False"
            },
            {
              "call": "less_by10(-10, 2, 2)",
              "expected": "True"
            },
            {
              "call": "less_by10(2, 11, 11)",
              "expected": "False"
            },
            {
              "call": "less_by10(3, 3, 30)",
              "expected": "True"
            },
            {
              "call": "less_by10(3, 3, 3)",
              "expected": "False"
            },
            {
              "call": "less_by10(10, 1, 11)",
              "expected": "True"
            },
            {
              "call": "less_by10(10, 11, 1)",
              "expected": "True"
            },
            {
              "call": "less_by10(10, 11, 2)",
              "expected": "False"
            },
            {
              "call": "less_by10(3, 30, 3)",
              "expected": "True"
            },
            {
              "call": "less_by10(2, 2, -8)",
              "expected": "True"
            },
            {
              "call": "less_by10(2, 8, 12)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "love6",
          "name": "love6",
          "description": "The number 6 is a truly great number. Given two int values, a and b, return true if either one is 6. Or if their sum or difference is 6. Note: the function Math.abs(num) computes the absolute value of a number.",
          "stub": "def love6(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "love6(6, 4)",
              "expected": "True"
            },
            {
              "call": "love6(4, 5)",
              "expected": "False"
            },
            {
              "call": "love6(1, 5)",
              "expected": "True"
            },
            {
              "call": "love6(1, 6)",
              "expected": "True"
            },
            {
              "call": "love6(1, 8)",
              "expected": "False"
            },
            {
              "call": "love6(1, 7)",
              "expected": "True"
            },
            {
              "call": "love6(7, 5)",
              "expected": "False"
            },
            {
              "call": "love6(8, 2)",
              "expected": "True"
            },
            {
              "call": "love6(6, 6)",
              "expected": "True"
            },
            {
              "call": "love6(-6, 2)",
              "expected": "False"
            },
            {
              "call": "love6(-4, -10)",
              "expected": "True"
            },
            {
              "call": "love6(-7, 1)",
              "expected": "False"
            },
            {
              "call": "love6(7, -1)",
              "expected": "True"
            },
            {
              "call": "love6(-6, 12)",
              "expected": "True"
            },
            {
              "call": "love6(-2, -4)",
              "expected": "False"
            },
            {
              "call": "love6(7, 1)",
              "expected": "True"
            },
            {
              "call": "love6(0, 9)",
              "expected": "False"
            },
            {
              "call": "love6(8, 3)",
              "expected": "False"
            },
            {
              "call": "love6(3, 3)",
              "expected": "True"
            },
            {
              "call": "love6(3, 4)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "max_mod5",
          "name": "max_mod5",
          "description": "Given two int values, return whichever value is larger. However if the two values have the same remainder when divided by 5, then the return the smaller value. However, in all cases, if the two values are the same, return 0. Note: the % \"mod\" operator computes the remainder, e.g. 7 % 5 is 2.",
          "stub": "def max_mod5(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "max_mod5(2, 3)",
              "expected": "3"
            },
            {
              "call": "max_mod5(6, 2)",
              "expected": "6"
            },
            {
              "call": "max_mod5(3, 2)",
              "expected": "3"
            },
            {
              "call": "max_mod5(8, 12)",
              "expected": "12"
            },
            {
              "call": "max_mod5(7, 12)",
              "expected": "7"
            },
            {
              "call": "max_mod5(11, 6)",
              "expected": "6"
            },
            {
              "call": "max_mod5(2, 7)",
              "expected": "2"
            },
            {
              "call": "max_mod5(7, 7)",
              "expected": "0"
            },
            {
              "call": "max_mod5(9, 1)",
              "expected": "9"
            },
            {
              "call": "max_mod5(9, 14)",
              "expected": "9"
            },
            {
              "call": "max_mod5(1, 2)",
              "expected": "2"
            }
          ]
        },
        {
          "id": "more20",
          "name": "more20",
          "description": "Return true if the given non-negative number is 1 or 2 more than a multiple of 20. See also:Introduction to Mod",
          "stub": "def more20(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "more20(20)",
              "expected": "False"
            },
            {
              "call": "more20(21)",
              "expected": "True"
            },
            {
              "call": "more20(22)",
              "expected": "True"
            },
            {
              "call": "more20(23)",
              "expected": "False"
            },
            {
              "call": "more20(25)",
              "expected": "False"
            },
            {
              "call": "more20(30)",
              "expected": "False"
            },
            {
              "call": "more20(31)",
              "expected": "False"
            },
            {
              "call": "more20(59)",
              "expected": "False"
            },
            {
              "call": "more20(60)",
              "expected": "False"
            },
            {
              "call": "more20(61)",
              "expected": "True"
            },
            {
              "call": "more20(62)",
              "expected": "True"
            },
            {
              "call": "more20(1020)",
              "expected": "False"
            },
            {
              "call": "more20(1021)",
              "expected": "True"
            },
            {
              "call": "more20(1000)",
              "expected": "False"
            },
            {
              "call": "more20(1001)",
              "expected": "True"
            },
            {
              "call": "more20(50)",
              "expected": "False"
            },
            {
              "call": "more20(55)",
              "expected": "False"
            },
            {
              "call": "more20(40)",
              "expected": "False"
            },
            {
              "call": "more20(41)",
              "expected": "True"
            },
            {
              "call": "more20(39)",
              "expected": "False"
            },
            {
              "call": "more20(42)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "near_ten",
          "name": "near_ten",
          "description": "Given a non-negative number \"num\", return true if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also:Introduction to Mod",
          "stub": "def near_ten(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "near_ten(12)",
              "expected": "True"
            },
            {
              "call": "near_ten(17)",
              "expected": "False"
            },
            {
              "call": "near_ten(19)",
              "expected": "True"
            },
            {
              "call": "near_ten(31)",
              "expected": "True"
            },
            {
              "call": "near_ten(6)",
              "expected": "False"
            },
            {
              "call": "near_ten(10)",
              "expected": "True"
            },
            {
              "call": "near_ten(11)",
              "expected": "True"
            },
            {
              "call": "near_ten(21)",
              "expected": "True"
            },
            {
              "call": "near_ten(22)",
              "expected": "True"
            },
            {
              "call": "near_ten(23)",
              "expected": "False"
            },
            {
              "call": "near_ten(54)",
              "expected": "False"
            },
            {
              "call": "near_ten(155)",
              "expected": "False"
            },
            {
              "call": "near_ten(158)",
              "expected": "True"
            },
            {
              "call": "near_ten(3)",
              "expected": "False"
            },
            {
              "call": "near_ten(1)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "old35",
          "name": "old35",
          "description": "Return true if the given non-negative number is a multiple of 3 or 5, but not both. Use the % \"mod\" operator -- seeIntroduction to Mod",
          "stub": "def old35(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "old35(3)",
              "expected": "True"
            },
            {
              "call": "old35(10)",
              "expected": "True"
            },
            {
              "call": "old35(15)",
              "expected": "False"
            },
            {
              "call": "old35(5)",
              "expected": "True"
            },
            {
              "call": "old35(9)",
              "expected": "True"
            },
            {
              "call": "old35(8)",
              "expected": "False"
            },
            {
              "call": "old35(7)",
              "expected": "False"
            },
            {
              "call": "old35(6)",
              "expected": "True"
            },
            {
              "call": "old35(17)",
              "expected": "False"
            },
            {
              "call": "old35(18)",
              "expected": "True"
            },
            {
              "call": "old35(29)",
              "expected": "False"
            },
            {
              "call": "old35(20)",
              "expected": "True"
            },
            {
              "call": "old35(21)",
              "expected": "True"
            },
            {
              "call": "old35(22)",
              "expected": "False"
            },
            {
              "call": "old35(45)",
              "expected": "False"
            },
            {
              "call": "old35(99)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "red_ticket",
          "name": "red_ticket",
          "description": "You have a red lottery ticket showing ints a, b, and c, each of which is 0, 1, or 2. If they are all the value 2, the result is 10. Otherwise if they are all the same, the result is 5. Otherwise so long as both b and c are different from a, the result is 1. Otherwise the result is 0.",
          "stub": "def red_ticket(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "red_ticket(2, 2, 2)",
              "expected": "10"
            },
            {
              "call": "red_ticket(2, 2, 1)",
              "expected": "0"
            },
            {
              "call": "red_ticket(0, 0, 0)",
              "expected": "5"
            },
            {
              "call": "red_ticket(2, 0, 0)",
              "expected": "1"
            },
            {
              "call": "red_ticket(1, 1, 1)",
              "expected": "5"
            },
            {
              "call": "red_ticket(1, 2, 1)",
              "expected": "0"
            },
            {
              "call": "red_ticket(1, 2, 0)",
              "expected": "1"
            },
            {
              "call": "red_ticket(0, 2, 2)",
              "expected": "1"
            },
            {
              "call": "red_ticket(1, 2, 2)",
              "expected": "1"
            },
            {
              "call": "red_ticket(0, 2, 0)",
              "expected": "0"
            },
            {
              "call": "red_ticket(1, 1, 2)",
              "expected": "0"
            }
          ]
        },
        {
          "id": "share_digit",
          "name": "share_digit",
          "description": "Given two ints, each in the range 10..99, return true if there is a digit that appears in both numbers, such as the 2 in 12 and 23. (Note: division, e.g. n/10, gives the left digit while the % \"mod\" n%10 gives the right digit.)",
          "stub": "def share_digit(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "share_digit(12, 23)",
              "expected": "True"
            },
            {
              "call": "share_digit(12, 43)",
              "expected": "False"
            },
            {
              "call": "share_digit(12, 44)",
              "expected": "False"
            },
            {
              "call": "share_digit(23, 12)",
              "expected": "True"
            },
            {
              "call": "share_digit(23, 39)",
              "expected": "True"
            },
            {
              "call": "share_digit(23, 19)",
              "expected": "False"
            },
            {
              "call": "share_digit(30, 90)",
              "expected": "True"
            },
            {
              "call": "share_digit(30, 91)",
              "expected": "False"
            },
            {
              "call": "share_digit(55, 55)",
              "expected": "True"
            },
            {
              "call": "share_digit(55, 44)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "sorta_sum",
          "name": "sorta_sum",
          "description": "Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.",
          "stub": "def sorta_sum(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "sorta_sum(3, 4)",
              "expected": "7"
            },
            {
              "call": "sorta_sum(9, 4)",
              "expected": "20"
            },
            {
              "call": "sorta_sum(10, 11)",
              "expected": "21"
            },
            {
              "call": "sorta_sum(12, -3)",
              "expected": "9"
            },
            {
              "call": "sorta_sum(-3, 12)",
              "expected": "9"
            },
            {
              "call": "sorta_sum(4, 5)",
              "expected": "9"
            },
            {
              "call": "sorta_sum(4, 6)",
              "expected": "20"
            },
            {
              "call": "sorta_sum(14, 7)",
              "expected": "21"
            },
            {
              "call": "sorta_sum(14, 6)",
              "expected": "20"
            }
          ]
        },
        {
          "id": "special_eleven",
          "name": "special_eleven",
          "description": "We'll say a number is special if it is a multiple of 11 or if it is one more than a multiple of 11. Return true if the given non-negative number is special. Use the % \"mod\" operator -- seeIntroduction to Mod",
          "stub": "def special_eleven(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "special_eleven(22)",
              "expected": "True"
            },
            {
              "call": "special_eleven(23)",
              "expected": "True"
            },
            {
              "call": "special_eleven(24)",
              "expected": "False"
            },
            {
              "call": "special_eleven(21)",
              "expected": "False"
            },
            {
              "call": "special_eleven(11)",
              "expected": "True"
            },
            {
              "call": "special_eleven(12)",
              "expected": "True"
            },
            {
              "call": "special_eleven(10)",
              "expected": "False"
            },
            {
              "call": "special_eleven(9)",
              "expected": "False"
            },
            {
              "call": "special_eleven(8)",
              "expected": "False"
            },
            {
              "call": "special_eleven(0)",
              "expected": "True"
            },
            {
              "call": "special_eleven(1)",
              "expected": "True"
            },
            {
              "call": "special_eleven(2)",
              "expected": "False"
            },
            {
              "call": "special_eleven(121)",
              "expected": "True"
            },
            {
              "call": "special_eleven(122)",
              "expected": "True"
            },
            {
              "call": "special_eleven(123)",
              "expected": "False"
            },
            {
              "call": "special_eleven(46)",
              "expected": "False"
            },
            {
              "call": "special_eleven(49)",
              "expected": "False"
            },
            {
              "call": "special_eleven(52)",
              "expected": "False"
            },
            {
              "call": "special_eleven(54)",
              "expected": "False"
            },
            {
              "call": "special_eleven(55)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "squirrel_play",
          "name": "squirrel_play",
          "description": "The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a bool isSummer, return true if the squirrels play and false otherwise.",
          "stub": "def squirrel_play(n, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "squirrel_play(70, False)",
              "expected": "True"
            },
            {
              "call": "squirrel_play(95, False)",
              "expected": "False"
            },
            {
              "call": "squirrel_play(95, True)",
              "expected": "True"
            },
            {
              "call": "squirrel_play(90, False)",
              "expected": "True"
            },
            {
              "call": "squirrel_play(90, True)",
              "expected": "True"
            },
            {
              "call": "squirrel_play(50, False)",
              "expected": "False"
            },
            {
              "call": "squirrel_play(50, True)",
              "expected": "False"
            },
            {
              "call": "squirrel_play(100, False)",
              "expected": "False"
            },
            {
              "call": "squirrel_play(100, True)",
              "expected": "True"
            },
            {
              "call": "squirrel_play(105, True)",
              "expected": "False"
            },
            {
              "call": "squirrel_play(59, False)",
              "expected": "False"
            },
            {
              "call": "squirrel_play(59, True)",
              "expected": "False"
            },
            {
              "call": "squirrel_play(60, False)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "sum_limit",
          "name": "sum_limit",
          "description": "Given 2 non-negative ints, a and b, return their sum, so long as the sum has the same number of digits as a. If the sum has more digits than a, just return a without b. (Note: one way to compute the number of digits of a non-negative int n is to convert it to a string with string.valueOf(n) and then check the length of the string.)",
          "stub": "def sum_limit(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "sum_limit(2, 3)",
              "expected": "5"
            },
            {
              "call": "sum_limit(8, 3)",
              "expected": "8"
            },
            {
              "call": "sum_limit(8, 1)",
              "expected": "9"
            },
            {
              "call": "sum_limit(11, 39)",
              "expected": "50"
            },
            {
              "call": "sum_limit(11, 99)",
              "expected": "11"
            },
            {
              "call": "sum_limit(0, 0)",
              "expected": "0"
            },
            {
              "call": "sum_limit(99, 0)",
              "expected": "99"
            },
            {
              "call": "sum_limit(99, 1)",
              "expected": "99"
            },
            {
              "call": "sum_limit(123, 1)",
              "expected": "124"
            },
            {
              "call": "sum_limit(1, 123)",
              "expected": "1"
            },
            {
              "call": "sum_limit(23, 60)",
              "expected": "83"
            },
            {
              "call": "sum_limit(23, 80)",
              "expected": "23"
            },
            {
              "call": "sum_limit(9000, 1)",
              "expected": "9001"
            },
            {
              "call": "sum_limit(90000000, 1)",
              "expected": "90000001"
            },
            {
              "call": "sum_limit(9000, 1000)",
              "expected": "9000"
            }
          ]
        },
        {
          "id": "tea_party",
          "name": "tea_party",
          "description": "We are having a party with amounts of tea and candy. Return the int outcome of the party encoded as 0=bad, 1=good, or 2=great. A party is good (1) if both tea and candy are at least 5. However, if either tea or candy is at least double the amount of the other one, the party is great (2). However, in all cases, if either tea or candy is less than 5, the party is always bad (0).",
          "stub": "def tea_party(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "tea_party(6, 8)",
              "expected": "1"
            },
            {
              "call": "tea_party(3, 8)",
              "expected": "0"
            },
            {
              "call": "tea_party(20, 6)",
              "expected": "2"
            },
            {
              "call": "tea_party(12, 6)",
              "expected": "2"
            },
            {
              "call": "tea_party(11, 6)",
              "expected": "1"
            },
            {
              "call": "tea_party(11, 4)",
              "expected": "0"
            },
            {
              "call": "tea_party(4, 5)",
              "expected": "0"
            },
            {
              "call": "tea_party(5, 5)",
              "expected": "1"
            },
            {
              "call": "tea_party(6, 6)",
              "expected": "1"
            },
            {
              "call": "tea_party(5, 10)",
              "expected": "2"
            },
            {
              "call": "tea_party(5, 9)",
              "expected": "1"
            },
            {
              "call": "tea_party(10, 4)",
              "expected": "0"
            },
            {
              "call": "tea_party(10, 20)",
              "expected": "2"
            }
          ]
        },
        {
          "id": "teen_sum",
          "name": "teen_sum",
          "description": "Given 2 ints, a and b, return their sum. However, \"teen\" values in the range 13..19 inclusive, are extra lucky. So if either value is a teen, just return 19.",
          "stub": "def teen_sum(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "teen_sum(3, 4)",
              "expected": "7"
            },
            {
              "call": "teen_sum(10, 13)",
              "expected": "19"
            },
            {
              "call": "teen_sum(13, 2)",
              "expected": "19"
            },
            {
              "call": "teen_sum(3, 19)",
              "expected": "19"
            },
            {
              "call": "teen_sum(13, 13)",
              "expected": "19"
            },
            {
              "call": "teen_sum(10, 10)",
              "expected": "20"
            },
            {
              "call": "teen_sum(6, 14)",
              "expected": "19"
            },
            {
              "call": "teen_sum(15, 2)",
              "expected": "19"
            },
            {
              "call": "teen_sum(19, 19)",
              "expected": "19"
            },
            {
              "call": "teen_sum(19, 20)",
              "expected": "19"
            },
            {
              "call": "teen_sum(2, 18)",
              "expected": "19"
            },
            {
              "call": "teen_sum(12, 4)",
              "expected": "16"
            },
            {
              "call": "teen_sum(2, 20)",
              "expected": "22"
            },
            {
              "call": "teen_sum(2, 17)",
              "expected": "19"
            },
            {
              "call": "teen_sum(2, 16)",
              "expected": "19"
            },
            {
              "call": "teen_sum(6, 7)",
              "expected": "13"
            }
          ]
        },
        {
          "id": "two_as_one",
          "name": "two_as_one",
          "description": "Given three ints, a b c, return true if it is possible to add two of the ints to get the third.",
          "stub": "def two_as_one(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "two_as_one(1, 2, 3)",
              "expected": "True"
            },
            {
              "call": "two_as_one(3, 1, 2)",
              "expected": "True"
            },
            {
              "call": "two_as_one(3, 2, 2)",
              "expected": "False"
            },
            {
              "call": "two_as_one(2, 3, 1)",
              "expected": "True"
            },
            {
              "call": "two_as_one(5, 3, -2)",
              "expected": "True"
            },
            {
              "call": "two_as_one(5, 3, -3)",
              "expected": "False"
            },
            {
              "call": "two_as_one(2, 5, 3)",
              "expected": "True"
            },
            {
              "call": "two_as_one(9, 5, 5)",
              "expected": "False"
            },
            {
              "call": "two_as_one(9, 4, 5)",
              "expected": "True"
            },
            {
              "call": "two_as_one(5, 4, 9)",
              "expected": "True"
            },
            {
              "call": "two_as_one(3, 3, 0)",
              "expected": "True"
            },
            {
              "call": "two_as_one(3, 3, 2)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "without_doubles",
          "name": "without_doubles",
          "description": "Return the sum of two 6-sided dice rolls, each in the range 1..6. However, if noDoubles is true, if the two dice show the same value, increment one die to the next value, wrapping around to 1 if its value was 6.",
          "stub": "def without_doubles(n, n2, b):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "without_doubles(2, 3, True)",
              "expected": "5"
            },
            {
              "call": "without_doubles(3, 3, True)",
              "expected": "7"
            },
            {
              "call": "without_doubles(3, 3, False)",
              "expected": "6"
            },
            {
              "call": "without_doubles(2, 3, False)",
              "expected": "5"
            },
            {
              "call": "without_doubles(5, 4, True)",
              "expected": "9"
            },
            {
              "call": "without_doubles(5, 4, False)",
              "expected": "9"
            },
            {
              "call": "without_doubles(5, 5, True)",
              "expected": "11"
            },
            {
              "call": "without_doubles(5, 5, False)",
              "expected": "10"
            },
            {
              "call": "without_doubles(6, 6, True)",
              "expected": "7"
            },
            {
              "call": "without_doubles(6, 6, False)",
              "expected": "12"
            },
            {
              "call": "without_doubles(1, 6, True)",
              "expected": "7"
            },
            {
              "call": "without_doubles(6, 1, False)",
              "expected": "7"
            }
          ]
        }
      ]
    },
    {
      "name": "Logic-2",
      "problems": [
        {
          "id": "blackjack",
          "name": "blackjack",
          "description": "Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. Return 0 if they both go over.",
          "stub": "def blackjack(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "blackjack(19, 21)",
              "expected": "21"
            },
            {
              "call": "blackjack(21, 19)",
              "expected": "21"
            },
            {
              "call": "blackjack(19, 22)",
              "expected": "19"
            },
            {
              "call": "blackjack(22, 19)",
              "expected": "19"
            },
            {
              "call": "blackjack(22, 50)",
              "expected": "0"
            },
            {
              "call": "blackjack(22, 22)",
              "expected": "0"
            },
            {
              "call": "blackjack(33, 1)",
              "expected": "1"
            },
            {
              "call": "blackjack(1, 2)",
              "expected": "2"
            },
            {
              "call": "blackjack(34, 33)",
              "expected": "0"
            },
            {
              "call": "blackjack(17, 19)",
              "expected": "19"
            },
            {
              "call": "blackjack(18, 17)",
              "expected": "18"
            },
            {
              "call": "blackjack(16, 23)",
              "expected": "16"
            },
            {
              "call": "blackjack(3, 4)",
              "expected": "4"
            },
            {
              "call": "blackjack(3, 2)",
              "expected": "3"
            },
            {
              "call": "blackjack(21, 20)",
              "expected": "21"
            }
          ]
        },
        {
          "id": "close_far",
          "name": "close_far",
          "description": "Given three ints, a b c, return true if one of b or c is \"close\" (differing from a by at most 1), while the other is \"far\", differing from both other values by 2 or more. Note: Math.abs(num) computes the absolute value of a number.",
          "stub": "def close_far(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "close_far(1, 2, 10)",
              "expected": "True"
            },
            {
              "call": "close_far(1, 2, 3)",
              "expected": "False"
            },
            {
              "call": "close_far(4, 1, 3)",
              "expected": "True"
            },
            {
              "call": "close_far(4, 5, 3)",
              "expected": "False"
            },
            {
              "call": "close_far(4, 3, 5)",
              "expected": "False"
            },
            {
              "call": "close_far(-1, 10, 0)",
              "expected": "True"
            },
            {
              "call": "close_far(0, -1, 10)",
              "expected": "True"
            },
            {
              "call": "close_far(10, 10, 8)",
              "expected": "True"
            },
            {
              "call": "close_far(10, 8, 9)",
              "expected": "False"
            },
            {
              "call": "close_far(8, 9, 10)",
              "expected": "False"
            },
            {
              "call": "close_far(8, 9, 7)",
              "expected": "False"
            },
            {
              "call": "close_far(8, 6, 9)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "evenly_spaced",
          "name": "evenly_spaced",
          "description": "Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the three values are evenly spaced, so the difference between small and medium is the same as the difference between medium and large.",
          "stub": "def evenly_spaced(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "evenly_spaced(2, 4, 6)",
              "expected": "True"
            },
            {
              "call": "evenly_spaced(4, 6, 2)",
              "expected": "True"
            },
            {
              "call": "evenly_spaced(4, 6, 3)",
              "expected": "False"
            },
            {
              "call": "evenly_spaced(6, 2, 4)",
              "expected": "True"
            },
            {
              "call": "evenly_spaced(6, 2, 8)",
              "expected": "False"
            },
            {
              "call": "evenly_spaced(2, 2, 2)",
              "expected": "True"
            },
            {
              "call": "evenly_spaced(2, 2, 3)",
              "expected": "False"
            },
            {
              "call": "evenly_spaced(9, 10, 11)",
              "expected": "True"
            },
            {
              "call": "evenly_spaced(10, 9, 11)",
              "expected": "True"
            },
            {
              "call": "evenly_spaced(10, 9, 9)",
              "expected": "False"
            },
            {
              "call": "evenly_spaced(2, 4, 4)",
              "expected": "False"
            },
            {
              "call": "evenly_spaced(2, 2, 4)",
              "expected": "False"
            },
            {
              "call": "evenly_spaced(3, 6, 12)",
              "expected": "False"
            },
            {
              "call": "evenly_spaced(12, 3, 6)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "lone_sum",
          "name": "lone_sum",
          "description": "Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.",
          "stub": "def lone_sum(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "lone_sum(1, 2, 3)",
              "expected": "6"
            },
            {
              "call": "lone_sum(3, 2, 3)",
              "expected": "2"
            },
            {
              "call": "lone_sum(3, 3, 3)",
              "expected": "0"
            },
            {
              "call": "lone_sum(9, 2, 2)",
              "expected": "9"
            },
            {
              "call": "lone_sum(2, 2, 9)",
              "expected": "9"
            },
            {
              "call": "lone_sum(2, 9, 2)",
              "expected": "9"
            },
            {
              "call": "lone_sum(2, 9, 3)",
              "expected": "14"
            },
            {
              "call": "lone_sum(4, 2, 3)",
              "expected": "9"
            },
            {
              "call": "lone_sum(1, 3, 1)",
              "expected": "3"
            }
          ]
        },
        {
          "id": "lucky_sum",
          "name": "lucky_sum",
          "description": "Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.",
          "stub": "def lucky_sum(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "lucky_sum(1, 2, 3)",
              "expected": "6"
            },
            {
              "call": "lucky_sum(1, 2, 13)",
              "expected": "3"
            },
            {
              "call": "lucky_sum(1, 13, 3)",
              "expected": "1"
            },
            {
              "call": "lucky_sum(1, 13, 13)",
              "expected": "1"
            },
            {
              "call": "lucky_sum(6, 5, 2)",
              "expected": "13"
            },
            {
              "call": "lucky_sum(13, 2, 3)",
              "expected": "0"
            },
            {
              "call": "lucky_sum(13, 2, 13)",
              "expected": "0"
            },
            {
              "call": "lucky_sum(13, 13, 2)",
              "expected": "0"
            },
            {
              "call": "lucky_sum(9, 4, 13)",
              "expected": "13"
            },
            {
              "call": "lucky_sum(8, 13, 2)",
              "expected": "8"
            },
            {
              "call": "lucky_sum(7, 2, 1)",
              "expected": "10"
            },
            {
              "call": "lucky_sum(3, 3, 13)",
              "expected": "6"
            }
          ]
        },
        {
          "id": "make_bricks",
          "name": "make_bricks",
          "description": "We want to make a row of bricks that isgoalinches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return true if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also:Introduction to MakeBricks",
          "stub": "def make_bricks(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "make_bricks(3, 1, 8)",
              "expected": "True"
            },
            {
              "call": "make_bricks(3, 1, 9)",
              "expected": "False"
            },
            {
              "call": "make_bricks(3, 2, 10)",
              "expected": "True"
            },
            {
              "call": "make_bricks(3, 2, 8)",
              "expected": "True"
            },
            {
              "call": "make_bricks(3, 2, 9)",
              "expected": "False"
            },
            {
              "call": "make_bricks(6, 1, 11)",
              "expected": "True"
            },
            {
              "call": "make_bricks(6, 0, 11)",
              "expected": "False"
            },
            {
              "call": "make_bricks(1, 4, 11)",
              "expected": "True"
            },
            {
              "call": "make_bricks(0, 3, 10)",
              "expected": "True"
            },
            {
              "call": "make_bricks(1, 4, 12)",
              "expected": "False"
            },
            {
              "call": "make_bricks(3, 1, 7)",
              "expected": "True"
            },
            {
              "call": "make_bricks(1, 1, 7)",
              "expected": "False"
            },
            {
              "call": "make_bricks(2, 1, 7)",
              "expected": "True"
            },
            {
              "call": "make_bricks(7, 1, 11)",
              "expected": "True"
            },
            {
              "call": "make_bricks(7, 1, 8)",
              "expected": "True"
            },
            {
              "call": "make_bricks(7, 1, 13)",
              "expected": "False"
            },
            {
              "call": "make_bricks(43, 1, 46)",
              "expected": "True"
            },
            {
              "call": "make_bricks(40, 1, 46)",
              "expected": "False"
            },
            {
              "call": "make_bricks(40, 2, 47)",
              "expected": "True"
            },
            {
              "call": "make_bricks(40, 2, 50)",
              "expected": "True"
            },
            {
              "call": "make_bricks(40, 2, 52)",
              "expected": "False"
            },
            {
              "call": "make_bricks(22, 2, 33)",
              "expected": "False"
            },
            {
              "call": "make_bricks(0, 2, 10)",
              "expected": "True"
            },
            {
              "call": "make_bricks(1000000, 1000, 1000100)",
              "expected": "True"
            },
            {
              "call": "make_bricks(2, 1000000, 100003)",
              "expected": "False"
            },
            {
              "call": "make_bricks(20, 0, 19)",
              "expected": "True"
            },
            {
              "call": "make_bricks(20, 0, 21)",
              "expected": "False"
            },
            {
              "call": "make_bricks(20, 4, 51)",
              "expected": "False"
            },
            {
              "call": "make_bricks(20, 4, 39)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "make_chocolate",
          "name": "make_chocolate",
          "description": "We want make a package ofgoalkilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.",
          "stub": "def make_chocolate(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "make_chocolate(4, 1, 9)",
              "expected": "4"
            },
            {
              "call": "make_chocolate(4, 1, 10)",
              "expected": "-1"
            },
            {
              "call": "make_chocolate(4, 1, 7)",
              "expected": "2"
            },
            {
              "call": "make_chocolate(6, 2, 7)",
              "expected": "2"
            },
            {
              "call": "make_chocolate(4, 1, 5)",
              "expected": "0"
            },
            {
              "call": "make_chocolate(4, 1, 4)",
              "expected": "4"
            },
            {
              "call": "make_chocolate(5, 4, 9)",
              "expected": "4"
            },
            {
              "call": "make_chocolate(9, 3, 18)",
              "expected": "3"
            },
            {
              "call": "make_chocolate(3, 1, 9)",
              "expected": "-1"
            },
            {
              "call": "make_chocolate(1, 2, 7)",
              "expected": "-1"
            },
            {
              "call": "make_chocolate(1, 2, 6)",
              "expected": "1"
            },
            {
              "call": "make_chocolate(1, 2, 5)",
              "expected": "0"
            },
            {
              "call": "make_chocolate(6, 1, 10)",
              "expected": "5"
            },
            {
              "call": "make_chocolate(6, 1, 11)",
              "expected": "6"
            },
            {
              "call": "make_chocolate(6, 1, 12)",
              "expected": "-1"
            },
            {
              "call": "make_chocolate(6, 1, 13)",
              "expected": "-1"
            },
            {
              "call": "make_chocolate(6, 2, 10)",
              "expected": "0"
            },
            {
              "call": "make_chocolate(6, 2, 11)",
              "expected": "1"
            },
            {
              "call": "make_chocolate(6, 2, 12)",
              "expected": "2"
            },
            {
              "call": "make_chocolate(60, 100, 550)",
              "expected": "50"
            },
            {
              "call": "make_chocolate(1000, 1000000, 5000006)",
              "expected": "6"
            },
            {
              "call": "make_chocolate(7, 1, 12)",
              "expected": "7"
            },
            {
              "call": "make_chocolate(7, 1, 13)",
              "expected": "-1"
            },
            {
              "call": "make_chocolate(7, 2, 13)",
              "expected": "3"
            }
          ]
        },
        {
          "id": "no_teen_sum",
          "name": "no_teen_sum",
          "description": "Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper \"public int fixTeen(int n) {\"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. \"decomposition\"). Define the helper below and at the same indent level as the main noTeenSum().",
          "stub": "def no_teen_sum(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "no_teen_sum(1, 2, 3)",
              "expected": "6"
            },
            {
              "call": "no_teen_sum(2, 13, 1)",
              "expected": "3"
            },
            {
              "call": "no_teen_sum(2, 1, 14)",
              "expected": "3"
            },
            {
              "call": "no_teen_sum(2, 1, 15)",
              "expected": "18"
            },
            {
              "call": "no_teen_sum(2, 1, 16)",
              "expected": "19"
            },
            {
              "call": "no_teen_sum(2, 1, 17)",
              "expected": "3"
            },
            {
              "call": "no_teen_sum(17, 1, 2)",
              "expected": "3"
            },
            {
              "call": "no_teen_sum(2, 15, 2)",
              "expected": "19"
            },
            {
              "call": "no_teen_sum(16, 17, 18)",
              "expected": "16"
            },
            {
              "call": "no_teen_sum(17, 18, 19)",
              "expected": "0"
            },
            {
              "call": "no_teen_sum(15, 16, 1)",
              "expected": "32"
            },
            {
              "call": "no_teen_sum(15, 15, 19)",
              "expected": "30"
            },
            {
              "call": "no_teen_sum(15, 19, 16)",
              "expected": "31"
            },
            {
              "call": "no_teen_sum(5, 17, 18)",
              "expected": "5"
            },
            {
              "call": "no_teen_sum(17, 18, 16)",
              "expected": "16"
            },
            {
              "call": "no_teen_sum(17, 19, 18)",
              "expected": "0"
            }
          ]
        },
        {
          "id": "round_sum",
          "name": "round_sum",
          "description": "For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper \"public int round10(int num) {\" and call it 3 times. Write the helper entirely below and at the same indent level as roundSum().",
          "stub": "def round_sum(n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "round_sum(16, 17, 18)",
              "expected": "60"
            },
            {
              "call": "round_sum(12, 13, 14)",
              "expected": "30"
            },
            {
              "call": "round_sum(6, 4, 4)",
              "expected": "10"
            },
            {
              "call": "round_sum(4, 6, 5)",
              "expected": "20"
            },
            {
              "call": "round_sum(4, 4, 6)",
              "expected": "10"
            },
            {
              "call": "round_sum(9, 4, 4)",
              "expected": "10"
            },
            {
              "call": "round_sum(0, 0, 1)",
              "expected": "0"
            },
            {
              "call": "round_sum(0, 9, 0)",
              "expected": "10"
            },
            {
              "call": "round_sum(10, 10, 19)",
              "expected": "40"
            },
            {
              "call": "round_sum(20, 30, 40)",
              "expected": "90"
            },
            {
              "call": "round_sum(45, 21, 30)",
              "expected": "100"
            },
            {
              "call": "round_sum(23, 11, 26)",
              "expected": "60"
            },
            {
              "call": "round_sum(23, 24, 25)",
              "expected": "70"
            },
            {
              "call": "round_sum(25, 24, 25)",
              "expected": "80"
            },
            {
              "call": "round_sum(23, 24, 29)",
              "expected": "70"
            },
            {
              "call": "round_sum(11, 24, 36)",
              "expected": "70"
            },
            {
              "call": "round_sum(24, 36, 32)",
              "expected": "90"
            },
            {
              "call": "round_sum(14, 12, 26)",
              "expected": "50"
            },
            {
              "call": "round_sum(12, 10, 24)",
              "expected": "40"
            }
          ]
        }
      ]
    },
    {
      "name": "Recursion-1",
      "problems": [
        {
          "id": "all_star",
          "name": "all_star",
          "description": "Given a string, compute recursively a new string where all the adjacent chars are now separated by a \"*\".",
          "stub": "def all_star(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "all_star(\"hello\")",
              "expected": "\"h*e*l*l*o\""
            },
            {
              "call": "all_star(\"abc\")",
              "expected": "\"a*b*c\""
            },
            {
              "call": "all_star(\"ab\")",
              "expected": "\"a*b\""
            },
            {
              "call": "all_star(\"a\")",
              "expected": "\"a\""
            },
            {
              "call": "all_star(\"\")",
              "expected": "\"\""
            },
            {
              "call": "all_star(\"3.14\")",
              "expected": "\"3*.*1*4\""
            },
            {
              "call": "all_star(\"Chocolate\")",
              "expected": "\"C*h*o*c*o*l*a*t*e\""
            },
            {
              "call": "all_star(\"1234\")",
              "expected": "\"1*2*3*4\""
            }
          ]
        },
        {
          "id": "array11",
          "name": "array11",
          "description": "Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.",
          "stub": "def array11(arr, n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "array11([1, 2, 11], 0)",
              "expected": "1"
            },
            {
              "call": "array11([11, 11], 0)",
              "expected": "2"
            },
            {
              "call": "array11([1, 2, 3, 4], 0)",
              "expected": "0"
            }
          ]
        },
        {
          "id": "array220",
          "name": "array220",
          "description": "Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.",
          "stub": "def array220(arr, n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "array220([1, 2, 20], 0)",
              "expected": "True"
            },
            {
              "call": "array220([3, 30], 0)",
              "expected": "True"
            },
            {
              "call": "array220([3], 0)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "array6",
          "name": "array6",
          "description": "Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.",
          "stub": "def array6(arr, n, n2, n3):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "array6([1, 6, 4], 0)",
              "expected": "True"
            },
            {
              "call": "array6([1, 4], 0)",
              "expected": "False"
            },
            {
              "call": "array6([6], 0)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "bunny_ears",
          "name": "bunny_ears",
          "description": "We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).",
          "stub": "def bunny_ears(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "bunny_ears(0)",
              "expected": "0"
            },
            {
              "call": "bunny_ears(1)",
              "expected": "2"
            },
            {
              "call": "bunny_ears(2)",
              "expected": "4"
            },
            {
              "call": "bunny_ears(3)",
              "expected": "6"
            },
            {
              "call": "bunny_ears(4)",
              "expected": "8"
            },
            {
              "call": "bunny_ears(5)",
              "expected": "10"
            },
            {
              "call": "bunny_ears(12)",
              "expected": "24"
            },
            {
              "call": "bunny_ears(50)",
              "expected": "100"
            },
            {
              "call": "bunny_ears(234)",
              "expected": "468"
            }
          ]
        },
        {
          "id": "bunny_ears2",
          "name": "bunny_ears2",
          "description": "We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the number of \"ears\" in the bunny line 1, 2, ... n (without loops or multiplication).",
          "stub": "def bunny_ears2(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "bunny_ears2(0)",
              "expected": "0"
            },
            {
              "call": "bunny_ears2(1)",
              "expected": "2"
            },
            {
              "call": "bunny_ears2(2)",
              "expected": "5"
            },
            {
              "call": "bunny_ears2(3)",
              "expected": "7"
            },
            {
              "call": "bunny_ears2(4)",
              "expected": "10"
            },
            {
              "call": "bunny_ears2(5)",
              "expected": "12"
            },
            {
              "call": "bunny_ears2(6)",
              "expected": "15"
            },
            {
              "call": "bunny_ears2(10)",
              "expected": "25"
            }
          ]
        },
        {
          "id": "change_pi",
          "name": "change_pi",
          "description": "Given a string, compute recursively (no loops) a new string where all appearances of \"pi\" have been replaced by \"3.14\".",
          "stub": "def change_pi(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "change_pi(\"xpix\")",
              "expected": "\"x3.14x\""
            },
            {
              "call": "change_pi(\"pipi\")",
              "expected": "\"3.143.14\""
            },
            {
              "call": "change_pi(\"pip\")",
              "expected": "\"3.14p\""
            },
            {
              "call": "change_pi(\"pi\")",
              "expected": "\"3.14\""
            },
            {
              "call": "change_pi(\"hip\")",
              "expected": "\"hip\""
            },
            {
              "call": "change_pi(\"p\")",
              "expected": "\"p\""
            },
            {
              "call": "change_pi(\"x\")",
              "expected": "\"x\""
            },
            {
              "call": "change_pi(\"\")",
              "expected": "\"\""
            },
            {
              "call": "change_pi(\"pixx\")",
              "expected": "\"3.14xx\""
            },
            {
              "call": "change_pi(\"xyzzy\")",
              "expected": "\"xyzzy\""
            }
          ]
        },
        {
          "id": "change_xy",
          "name": "change_xy",
          "description": "Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.",
          "stub": "def change_xy(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "change_xy(\"codex\")",
              "expected": "\"codey\""
            },
            {
              "call": "change_xy(\"xxhixx\")",
              "expected": "\"yyhiyy\""
            },
            {
              "call": "change_xy(\"xhixhix\")",
              "expected": "\"yhiyhiy\""
            },
            {
              "call": "change_xy(\"hiy\")",
              "expected": "\"hiy\""
            },
            {
              "call": "change_xy(\"h\")",
              "expected": "\"h\""
            },
            {
              "call": "change_xy(\"x\")",
              "expected": "\"y\""
            },
            {
              "call": "change_xy(\"\")",
              "expected": "\"\""
            },
            {
              "call": "change_xy(\"xxx\")",
              "expected": "\"yyy\""
            },
            {
              "call": "change_xy(\"yyhxyi\")",
              "expected": "\"yyhyyi\""
            },
            {
              "call": "change_xy(\"hihi\")",
              "expected": "\"hihi\""
            }
          ]
        },
        {
          "id": "count11",
          "name": "count11",
          "description": "Given a string, compute recursively (no loops) the number of \"11\" substrings in the string. The \"11\" substrings should not overlap.",
          "stub": "def count11(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count11(\"11abc11\")",
              "expected": "2"
            },
            {
              "call": "count11(\"abc11x11x11\")",
              "expected": "3"
            },
            {
              "call": "count11(\"111\")",
              "expected": "1"
            },
            {
              "call": "count11(\"1111\")",
              "expected": "2"
            },
            {
              "call": "count11(\"1\")",
              "expected": "0"
            },
            {
              "call": "count11(\"\")",
              "expected": "0"
            },
            {
              "call": "count11(\"hi\")",
              "expected": "0"
            },
            {
              "call": "count11(\"11x111x1111\")",
              "expected": "4"
            },
            {
              "call": "count11(\"1x111\")",
              "expected": "1"
            },
            {
              "call": "count11(\"1Hello1\")",
              "expected": "0"
            },
            {
              "call": "count11(\"Hello\")",
              "expected": "0"
            }
          ]
        },
        {
          "id": "count7",
          "name": "count7",
          "description": "Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).",
          "stub": "def count7(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count7(717)",
              "expected": "2"
            },
            {
              "call": "count7(7)",
              "expected": "1"
            },
            {
              "call": "count7(123)",
              "expected": "0"
            },
            {
              "call": "count7(77)",
              "expected": "2"
            },
            {
              "call": "count7(7123)",
              "expected": "1"
            },
            {
              "call": "count7(771237)",
              "expected": "3"
            },
            {
              "call": "count7(771737)",
              "expected": "4"
            },
            {
              "call": "count7(47571)",
              "expected": "2"
            },
            {
              "call": "count7(777777)",
              "expected": "6"
            },
            {
              "call": "count7(70701277)",
              "expected": "4"
            },
            {
              "call": "count7(777576197)",
              "expected": "5"
            },
            {
              "call": "count7(99999)",
              "expected": "0"
            },
            {
              "call": "count7(99799)",
              "expected": "1"
            }
          ]
        },
        {
          "id": "count8",
          "name": "count8",
          "description": "Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).",
          "stub": "def count8(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count8(8)",
              "expected": "1"
            },
            {
              "call": "count8(818)",
              "expected": "2"
            },
            {
              "call": "count8(8818)",
              "expected": "4"
            },
            {
              "call": "count8(8088)",
              "expected": "4"
            },
            {
              "call": "count8(123)",
              "expected": "0"
            },
            {
              "call": "count8(81238)",
              "expected": "2"
            },
            {
              "call": "count8(88788)",
              "expected": "6"
            },
            {
              "call": "count8(8234)",
              "expected": "1"
            },
            {
              "call": "count8(2348)",
              "expected": "1"
            },
            {
              "call": "count8(23884)",
              "expected": "3"
            },
            {
              "call": "count8(0)",
              "expected": "0"
            },
            {
              "call": "count8(1818188)",
              "expected": "5"
            },
            {
              "call": "count8(8818181)",
              "expected": "5"
            },
            {
              "call": "count8(1080)",
              "expected": "1"
            },
            {
              "call": "count8(188)",
              "expected": "3"
            },
            {
              "call": "count8(88888)",
              "expected": "9"
            },
            {
              "call": "count8(9898)",
              "expected": "2"
            },
            {
              "call": "count8(78)",
              "expected": "1"
            }
          ]
        },
        {
          "id": "count_abc",
          "name": "count_abc",
          "description": "Count recursively the total number of \"abc\" and \"aba\" substrings that appear in the given string.",
          "stub": "def count_abc(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_abc(\"abc\")",
              "expected": "1"
            },
            {
              "call": "count_abc(\"abcxxabc\")",
              "expected": "2"
            },
            {
              "call": "count_abc(\"abaxxaba\")",
              "expected": "2"
            },
            {
              "call": "count_abc(\"ababc\")",
              "expected": "2"
            },
            {
              "call": "count_abc(\"abxbc\")",
              "expected": "0"
            },
            {
              "call": "count_abc(\"aaabc\")",
              "expected": "1"
            },
            {
              "call": "count_abc(\"hello\")",
              "expected": "0"
            },
            {
              "call": "count_abc(\"\")",
              "expected": "0"
            },
            {
              "call": "count_abc(\"ab\")",
              "expected": "0"
            },
            {
              "call": "count_abc(\"aba\")",
              "expected": "1"
            },
            {
              "call": "count_abc(\"aca\")",
              "expected": "0"
            },
            {
              "call": "count_abc(\"aaa\")",
              "expected": "0"
            }
          ]
        },
        {
          "id": "count_hi",
          "name": "count_hi",
          "description": "Given a string, compute recursively (no loops) the number of times lowercase \"hi\" appears in the string.",
          "stub": "def count_hi(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_hi(\"xxhixx\")",
              "expected": "1"
            },
            {
              "call": "count_hi(\"xhixhix\")",
              "expected": "2"
            },
            {
              "call": "count_hi(\"hi\")",
              "expected": "1"
            },
            {
              "call": "count_hi(\"hihih\")",
              "expected": "2"
            },
            {
              "call": "count_hi(\"h\")",
              "expected": "0"
            },
            {
              "call": "count_hi(\"\")",
              "expected": "0"
            },
            {
              "call": "count_hi(\"ihihihihih\")",
              "expected": "4"
            },
            {
              "call": "count_hi(\"ihihihihihi\")",
              "expected": "5"
            },
            {
              "call": "count_hi(\"hiAAhi12hi\")",
              "expected": "3"
            },
            {
              "call": "count_hi(\"xhixhxihihhhih\")",
              "expected": "3"
            },
            {
              "call": "count_hi(\"ship\")",
              "expected": "1"
            }
          ]
        },
        {
          "id": "count_hi2",
          "name": "count_hi2",
          "description": "Given a string, compute recursively the number of times lowercase \"hi\" appears in the string, however do not count \"hi\" that have an 'x' immedately before them.",
          "stub": "def count_hi2(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_hi2(\"ahixhi\")",
              "expected": "1"
            },
            {
              "call": "count_hi2(\"ahibhi\")",
              "expected": "2"
            },
            {
              "call": "count_hi2(\"xhixhi\")",
              "expected": "0"
            },
            {
              "call": "count_hi2(\"hixhi\")",
              "expected": "1"
            },
            {
              "call": "count_hi2(\"hixhhi\")",
              "expected": "2"
            },
            {
              "call": "count_hi2(\"hihihi\")",
              "expected": "3"
            },
            {
              "call": "count_hi2(\"hihihix\")",
              "expected": "3"
            },
            {
              "call": "count_hi2(\"xhihihix\")",
              "expected": "2"
            },
            {
              "call": "count_hi2(\"xxhi\")",
              "expected": "0"
            },
            {
              "call": "count_hi2(\"hixxhi\")",
              "expected": "1"
            },
            {
              "call": "count_hi2(\"hi\")",
              "expected": "1"
            },
            {
              "call": "count_hi2(\"xxxx\")",
              "expected": "0"
            },
            {
              "call": "count_hi2(\"h\")",
              "expected": "0"
            },
            {
              "call": "count_hi2(\"x\")",
              "expected": "0"
            },
            {
              "call": "count_hi2(\"\")",
              "expected": "0"
            },
            {
              "call": "count_hi2(\"Hellohi\")",
              "expected": "1"
            }
          ]
        },
        {
          "id": "count_pairs",
          "name": "count_pairs",
          "description": "We'll say that a \"pair\" in a string is two instances of a char separated by a char. So \"AxA\" the A's make a pair. Pair's can overlap, so \"AxAxA\" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.",
          "stub": "def count_pairs(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_pairs(\"axa\")",
              "expected": "1"
            },
            {
              "call": "count_pairs(\"axax\")",
              "expected": "2"
            },
            {
              "call": "count_pairs(\"axbx\")",
              "expected": "1"
            },
            {
              "call": "count_pairs(\"hi\")",
              "expected": "0"
            },
            {
              "call": "count_pairs(\"hihih\")",
              "expected": "3"
            },
            {
              "call": "count_pairs(\"ihihhh\")",
              "expected": "3"
            },
            {
              "call": "count_pairs(\"ihjxhh\")",
              "expected": "0"
            },
            {
              "call": "count_pairs(\"\")",
              "expected": "0"
            },
            {
              "call": "count_pairs(\"a\")",
              "expected": "0"
            },
            {
              "call": "count_pairs(\"aa\")",
              "expected": "0"
            },
            {
              "call": "count_pairs(\"aaa\")",
              "expected": "1"
            }
          ]
        },
        {
          "id": "count_x",
          "name": "count_x",
          "description": "Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.",
          "stub": "def count_x(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "count_x(\"xxhixx\")",
              "expected": "4"
            },
            {
              "call": "count_x(\"xhixhix\")",
              "expected": "3"
            },
            {
              "call": "count_x(\"hi\")",
              "expected": "0"
            },
            {
              "call": "count_x(\"h\")",
              "expected": "0"
            },
            {
              "call": "count_x(\"x\")",
              "expected": "1"
            },
            {
              "call": "count_x(\"\")",
              "expected": "0"
            },
            {
              "call": "count_x(\"hihi\")",
              "expected": "0"
            },
            {
              "call": "count_x(\"hiAAhi12hi\")",
              "expected": "0"
            }
          ]
        },
        {
          "id": "end_x",
          "name": "end_x",
          "description": "Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.",
          "stub": "def end_x(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "end_x(\"xxre\")",
              "expected": "\"rexx\""
            },
            {
              "call": "end_x(\"xxhixx\")",
              "expected": "\"hixxxx\""
            },
            {
              "call": "end_x(\"xhixhix\")",
              "expected": "\"hihixxx\""
            },
            {
              "call": "end_x(\"hiy\")",
              "expected": "\"hiy\""
            },
            {
              "call": "end_x(\"h\")",
              "expected": "\"h\""
            },
            {
              "call": "end_x(\"x\")",
              "expected": "\"x\""
            },
            {
              "call": "end_x(\"xx\")",
              "expected": "\"xx\""
            },
            {
              "call": "end_x(\"\")",
              "expected": "\"\""
            },
            {
              "call": "end_x(\"bxx\")",
              "expected": "\"bxx\""
            },
            {
              "call": "end_x(\"bxax\")",
              "expected": "\"baxx\""
            },
            {
              "call": "end_x(\"axaxax\")",
              "expected": "\"aaaxxx\""
            },
            {
              "call": "end_x(\"xxhxi\")",
              "expected": "\"hixxx\""
            }
          ]
        },
        {
          "id": "factorial",
          "name": "factorial",
          "description": "Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).",
          "stub": "def factorial(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "factorial(1)",
              "expected": "1"
            },
            {
              "call": "factorial(2)",
              "expected": "2"
            },
            {
              "call": "factorial(3)",
              "expected": "6"
            },
            {
              "call": "factorial(4)",
              "expected": "24"
            },
            {
              "call": "factorial(5)",
              "expected": "120"
            },
            {
              "call": "factorial(6)",
              "expected": "720"
            },
            {
              "call": "factorial(7)",
              "expected": "5040"
            },
            {
              "call": "factorial(8)",
              "expected": "40320"
            },
            {
              "call": "factorial(12)",
              "expected": "479001600"
            }
          ]
        },
        {
          "id": "fibonacci",
          "name": "fibonacci",
          "description": "The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.",
          "stub": "def fibonacci(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "fibonacci(0)",
              "expected": "0"
            },
            {
              "call": "fibonacci(1)",
              "expected": "1"
            },
            {
              "call": "fibonacci(2)",
              "expected": "1"
            },
            {
              "call": "fibonacci(3)",
              "expected": "2"
            },
            {
              "call": "fibonacci(4)",
              "expected": "3"
            },
            {
              "call": "fibonacci(5)",
              "expected": "5"
            },
            {
              "call": "fibonacci(6)",
              "expected": "8"
            },
            {
              "call": "fibonacci(7)",
              "expected": "13"
            }
          ]
        },
        {
          "id": "nest_paren",
          "name": "nest_paren",
          "description": "Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like \"(())\" or \"((()))\". Suggestion: check the first and last chars, and then recur on what's inside them.",
          "stub": "def nest_paren():\n    # TODO: implement\n    pass\n",
          "tests": []
        },
        {
          "id": "no_x",
          "name": "no_x",
          "description": "Given a string, compute recursively a new string where all the 'x' chars have been removed.",
          "stub": "def no_x(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "no_x(\"xaxb\")",
              "expected": "\"ab\""
            },
            {
              "call": "no_x(\"abc\")",
              "expected": "\"abc\""
            },
            {
              "call": "no_x(\"xx\")",
              "expected": "\"\""
            },
            {
              "call": "no_x(\"\")",
              "expected": "\"\""
            },
            {
              "call": "no_x(\"axxbxx\")",
              "expected": "\"ab\""
            },
            {
              "call": "no_x(\"Hellox\")",
              "expected": "\"Hello\""
            }
          ]
        },
        {
          "id": "pair_star",
          "name": "pair_star",
          "description": "Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a \"*\".",
          "stub": "def pair_star(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "pair_star(\"hello\")",
              "expected": "\"hel*lo\""
            },
            {
              "call": "pair_star(\"xxyy\")",
              "expected": "\"x*xy*y\""
            },
            {
              "call": "pair_star(\"aaaa\")",
              "expected": "\"a*a*a*a\""
            },
            {
              "call": "pair_star(\"aaab\")",
              "expected": "\"a*a*ab\""
            },
            {
              "call": "pair_star(\"aa\")",
              "expected": "\"a*a\""
            },
            {
              "call": "pair_star(\"a\")",
              "expected": "\"a\""
            },
            {
              "call": "pair_star(\"\")",
              "expected": "\"\""
            },
            {
              "call": "pair_star(\"noadjacent\")",
              "expected": "\"noadjacent\""
            },
            {
              "call": "pair_star(\"abba\")",
              "expected": "\"ab*ba\""
            },
            {
              "call": "pair_star(\"abbba\")",
              "expected": "\"ab*b*ba\""
            }
          ]
        },
        {
          "id": "paren_bit",
          "name": "paren_bit",
          "description": "Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so \"xyz(abc)123\" yields \"(abc)\".",
          "stub": "def paren_bit():\n    # TODO: implement\n    pass\n",
          "tests": []
        },
        {
          "id": "power_n",
          "name": "power_n",
          "description": "Givenbaseandnthat are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).",
          "stub": "def power_n(n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "power_n(3, 1)",
              "expected": "3"
            },
            {
              "call": "power_n(3, 2)",
              "expected": "9"
            },
            {
              "call": "power_n(3, 3)",
              "expected": "27"
            },
            {
              "call": "power_n(2, 1)",
              "expected": "2"
            },
            {
              "call": "power_n(2, 2)",
              "expected": "4"
            },
            {
              "call": "power_n(2, 3)",
              "expected": "8"
            },
            {
              "call": "power_n(2, 4)",
              "expected": "16"
            },
            {
              "call": "power_n(2, 5)",
              "expected": "32"
            },
            {
              "call": "power_n(10, 1)",
              "expected": "10"
            },
            {
              "call": "power_n(10, 2)",
              "expected": "100"
            },
            {
              "call": "power_n(10, 3)",
              "expected": "1000"
            }
          ]
        },
        {
          "id": "str_copies",
          "name": "str_copies",
          "description": "Given a string and a non-empty substringsub, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.",
          "stub": "def str_copies(str, str2, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "str_copies(\"catcowcat\", \"cat\", 2)",
              "expected": "True"
            },
            {
              "call": "str_copies(\"catcowcat\", \"cow\", 2)",
              "expected": "False"
            },
            {
              "call": "str_copies(\"catcowcat\", \"cow\", 1)",
              "expected": "True"
            },
            {
              "call": "str_copies(\"iiijjj\", \"i\", 3)",
              "expected": "True"
            },
            {
              "call": "str_copies(\"iiijjj\", \"i\", 4)",
              "expected": "False"
            },
            {
              "call": "str_copies(\"iiijjj\", \"ii\", 2)",
              "expected": "True"
            },
            {
              "call": "str_copies(\"iiijjj\", \"ii\", 3)",
              "expected": "False"
            },
            {
              "call": "str_copies(\"iiijjj\", \"x\", 3)",
              "expected": "False"
            },
            {
              "call": "str_copies(\"iiijjj\", \"x\", 0)",
              "expected": "True"
            },
            {
              "call": "str_copies(\"iiiiij\", \"iii\", 3)",
              "expected": "True"
            },
            {
              "call": "str_copies(\"iiiiij\", \"iii\", 4)",
              "expected": "False"
            },
            {
              "call": "str_copies(\"ijiiiiij\", \"iiii\", 2)",
              "expected": "True"
            },
            {
              "call": "str_copies(\"ijiiiiij\", \"iiii\", 3)",
              "expected": "False"
            },
            {
              "call": "str_copies(\"dogcatdogcat\", \"dog\", 2)",
              "expected": "True"
            }
          ]
        },
        {
          "id": "str_count",
          "name": "str_count",
          "description": "Given a string and a non-empty substringsub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.",
          "stub": "def str_count(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "str_count(\"catcowcat\", \"cat\")",
              "expected": "2"
            },
            {
              "call": "str_count(\"catcowcat\", \"cow\")",
              "expected": "1"
            },
            {
              "call": "str_count(\"catcowcat\", \"dog\")",
              "expected": "0"
            },
            {
              "call": "str_count(\"cacatcowcat\", \"cat\")",
              "expected": "2"
            },
            {
              "call": "str_count(\"xyx\", \"x\")",
              "expected": "2"
            },
            {
              "call": "str_count(\"iiiijj\", \"i\")",
              "expected": "4"
            },
            {
              "call": "str_count(\"iiiijj\", \"ii\")",
              "expected": "2"
            },
            {
              "call": "str_count(\"iiiijj\", \"iii\")",
              "expected": "1"
            },
            {
              "call": "str_count(\"iiiijj\", \"j\")",
              "expected": "2"
            },
            {
              "call": "str_count(\"iiiijj\", \"jj\")",
              "expected": "1"
            },
            {
              "call": "str_count(\"aaabababab\", \"ab\")",
              "expected": "4"
            },
            {
              "call": "str_count(\"aaabababab\", \"aa\")",
              "expected": "1"
            },
            {
              "call": "str_count(\"aaabababab\", \"a\")",
              "expected": "6"
            },
            {
              "call": "str_count(\"aaabababab\", \"b\")",
              "expected": "4"
            }
          ]
        },
        {
          "id": "str_dist",
          "name": "str_dist",
          "description": "Given a string and a non-empty substringsub, compute recursively the largest substring which starts and ends with sub and return its length.",
          "stub": "def str_dist(str, str2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "str_dist(\"catcowcat\", \"cat\")",
              "expected": "9"
            },
            {
              "call": "str_dist(\"catcowcat\", \"cow\")",
              "expected": "3"
            },
            {
              "call": "str_dist(\"cccatcowcatxx\", \"cat\")",
              "expected": "9"
            },
            {
              "call": "str_dist(\"abccatcowcatcatxyz\", \"cat\")",
              "expected": "12"
            },
            {
              "call": "str_dist(\"xyx\", \"x\")",
              "expected": "3"
            },
            {
              "call": "str_dist(\"xyx\", \"y\")",
              "expected": "1"
            },
            {
              "call": "str_dist(\"xyx\", \"z\")",
              "expected": "0"
            },
            {
              "call": "str_dist(\"z\", \"z\")",
              "expected": "1"
            },
            {
              "call": "str_dist(\"x\", \"z\")",
              "expected": "0"
            },
            {
              "call": "str_dist(\"\", \"z\")",
              "expected": "0"
            },
            {
              "call": "str_dist(\"hiHellohihihi\", \"hi\")",
              "expected": "13"
            },
            {
              "call": "str_dist(\"hiHellohihihi\", \"hih\")",
              "expected": "5"
            },
            {
              "call": "str_dist(\"hiHellohihihi\", \"o\")",
              "expected": "1"
            },
            {
              "call": "str_dist(\"hiHellohihihi\", \"ll\")",
              "expected": "2"
            }
          ]
        },
        {
          "id": "string_clean",
          "name": "string_clean",
          "description": "Given a string, return recursively a \"cleaned\" string where adjacent chars that are the same have been reduced to a single char. So \"yyzzza\" yields \"yza\".",
          "stub": "def string_clean(str):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "string_clean(\"yyzzza\")",
              "expected": "\"yza\""
            },
            {
              "call": "string_clean(\"abbbcdd\")",
              "expected": "\"abcd\""
            },
            {
              "call": "string_clean(\"Hello\")",
              "expected": "\"Helo\""
            },
            {
              "call": "string_clean(\"XXabcYY\")",
              "expected": "\"XabcY\""
            },
            {
              "call": "string_clean(\"112ab445\")",
              "expected": "\"12ab45\""
            },
            {
              "call": "string_clean(\"Hello Bookkeeper\")",
              "expected": "\"Helo Bokeper\""
            }
          ]
        },
        {
          "id": "sum_digits",
          "name": "sum_digits",
          "description": "Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).",
          "stub": "def sum_digits(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "sum_digits(126)",
              "expected": "9"
            },
            {
              "call": "sum_digits(49)",
              "expected": "13"
            },
            {
              "call": "sum_digits(12)",
              "expected": "3"
            },
            {
              "call": "sum_digits(10)",
              "expected": "1"
            },
            {
              "call": "sum_digits(1)",
              "expected": "1"
            },
            {
              "call": "sum_digits(0)",
              "expected": "0"
            },
            {
              "call": "sum_digits(730)",
              "expected": "10"
            },
            {
              "call": "sum_digits(1111)",
              "expected": "4"
            },
            {
              "call": "sum_digits(11111)",
              "expected": "5"
            },
            {
              "call": "sum_digits(10110)",
              "expected": "3"
            },
            {
              "call": "sum_digits(235)",
              "expected": "10"
            }
          ]
        },
        {
          "id": "triangle",
          "name": "triangle",
          "description": "We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.",
          "stub": "def triangle(n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "triangle(0)",
              "expected": "0"
            },
            {
              "call": "triangle(1)",
              "expected": "1"
            },
            {
              "call": "triangle(2)",
              "expected": "3"
            },
            {
              "call": "triangle(3)",
              "expected": "6"
            },
            {
              "call": "triangle(4)",
              "expected": "10"
            },
            {
              "call": "triangle(5)",
              "expected": "15"
            },
            {
              "call": "triangle(6)",
              "expected": "21"
            },
            {
              "call": "triangle(7)",
              "expected": "28"
            }
          ]
        }
      ]
    },
    {
      "name": "Recursion-2",
      "problems": [
        {
          "id": "group_no_adj",
          "name": "group_no_adj",
          "description": "Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen. (No loops needed.)",
          "stub": "def group_no_adj(n, arr, n2, n3, n4, n5):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "group_no_adj(0, [2, 5, 10, 4], 12)",
              "expected": "True"
            },
            {
              "call": "group_no_adj(0, [2, 5, 10, 4], 14)",
              "expected": "False"
            },
            {
              "call": "group_no_adj(0, [2, 5, 10, 4], 7)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "group_sum",
          "name": "group_sum",
          "description": "Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking strategy in this problem, you can use the same pattern for many problems to search a space of choices. Rather than looking at the whole array, our convention is to consider the part of the array starting at indexstartand continuing to the end of the array. The caller can specify the whole array simply by passing start as 0. No loops are needed -- the recursive calls progress down the array.",
          "stub": "def group_sum(n, arr, n2, n3, n4):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "group_sum(0, [2, 4, 8], 10)",
              "expected": "True"
            },
            {
              "call": "group_sum(0, [2, 4, 8], 14)",
              "expected": "True"
            },
            {
              "call": "group_sum(0, [2, 4, 8], 9)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "group_sum5",
          "name": "group_sum5",
          "description": "Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with these additional constraints: all multiples of 5 in the array must be included in the group. If the value immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)",
          "stub": "def group_sum5(n, arr, n2, n3, n4, n5):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "group_sum5(0, [2, 5, 10, 4], 19)",
              "expected": "True"
            },
            {
              "call": "group_sum5(0, [2, 5, 10, 4], 17)",
              "expected": "True"
            },
            {
              "call": "group_sum5(0, [2, 5, 10, 4], 12)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "group_sum6",
          "name": "group_sum6",
          "description": "Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No loops needed.)",
          "stub": "def group_sum6(n, arr, n2, n3, n4):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "group_sum6(0, [5, 6, 2], 8)",
              "expected": "True"
            },
            {
              "call": "group_sum6(0, [5, 6, 2], 9)",
              "expected": "False"
            },
            {
              "call": "group_sum6(0, [5, 6, 2], 7)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "group_sum_clump",
          "name": "group_sum_clump",
          "description": "Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target, with this additional constraint: if there are numbers in the array that are adjacent and the identical value, they must either all be chosen, or none of them chosen. For example, with the array {1, 2, 2, 2, 5, 2}, either all three 2's in the middle must be chosen or not, all as a group. (one loop can be used to find the extent of the identical values).",
          "stub": "def group_sum_clump(n, arr, n2, n3, n4):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "group_sum_clump(0, [2, 4, 8], 10)",
              "expected": "True"
            },
            {
              "call": "group_sum_clump(0, [1, 2, 4, 8, 1], 14)",
              "expected": "True"
            },
            {
              "call": "group_sum_clump(0, [2, 4, 4, 8], 14)",
              "expected": "False"
            }
          ]
        },
        {
          "id": "split53",
          "name": "split53",
          "description": "Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups is the same, with these constraints: all the values that are multiple of 5 must be in one group, and all the values that are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)",
          "stub": "def split53(arr, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "split53([1, 1])",
              "expected": "True"
            },
            {
              "call": "split53([1, 1, 1])",
              "expected": "False"
            },
            {
              "call": "split53([2, 4, 2])",
              "expected": "True"
            }
          ]
        },
        {
          "id": "split_array",
          "name": "split_array",
          "description": "Given an array of ints, is it possible to divide the ints into two groups, so that the sums of the two groups are the same. Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitArray(). (No loops needed.)",
          "stub": "def split_array(arr, n):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "split_array([2, 2])",
              "expected": "True"
            },
            {
              "call": "split_array([2, 3])",
              "expected": "False"
            },
            {
              "call": "split_array([5, 2, 3])",
              "expected": "True"
            }
          ]
        },
        {
          "id": "split_odd10",
          "name": "split_odd10",
          "description": "Given an array of ints, is it possible to divide the ints into two groups, so that the sum of one group is a multiple of 10, and the sum of the other group is odd. Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitOdd10(). (No loops needed.)",
          "stub": "def split_odd10(arr, n, n2):\n    # TODO: implement\n    pass\n",
          "tests": [
            {
              "call": "split_odd10([5, 5, 5])",
              "expected": "True"
            },
            {
              "call": "split_odd10([5, 5, 6])",
              "expected": "False"
            },
            {
              "call": "split_odd10([5, 5, 6, 1])",
              "expected": "True"
            }
          ]
        }
      ]
    }
  ]
};
