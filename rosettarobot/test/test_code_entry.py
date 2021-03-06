import glob
import logging
from rosettarobot import robot


def test_extract_url_string():
    code = robot.CodeEntry("rosettarobot/test/github-rust-rosetta/src/24_game.rs")

    tests_failed = [
        "",
        " ",
        "//",
        "// http://google.com",
        "// http://rosettacode.org"
    ]

    for input in tests_failed:
        assert(code._extract_url_string(input) is None)

    tests_passed = [
        ("// Implements http://rosettacode.org/wiki/99_Bottles_of_Beer",
         "http://rosettacode.org/wiki/99_Bottles_of_Beer"),
        ("// Implements http://rosettacode.org/wiki/A%2BB",
         "http://rosettacode.org/wiki/A%2BB"),
        ("// Implements http://rosettacode.org/wiki/100_doors",
         "http://rosettacode.org/wiki/100_doors"),
        ("// Implements http://rosettacode.org/wiki/24_game",
         "http://rosettacode.org/wiki/24_game"),
        ("// Implements http://rosettacode.org/wiki/100_doors",
         "http://rosettacode.org/wiki/100_doors"),
        ("// http://rosettacode.org/wiki/24_game/Solve",
         "http://rosettacode.org/wiki/24_game/Solve"),
        ("// http://rosettacode.org/wiki/24_game/Solve#Scala",
         "http://rosettacode.org/wiki/24_game/Solve#Scala"),
        ("// http://rosettacode.org/wiki/AKS_test_for_primes",
         "http://rosettacode.org/wiki/AKS_test_for_primes"),
        ("//Implements http://rosettacode.org/wiki/9_billion_names_of_God_the_integer",
         "http://rosettacode.org/wiki/9_billion_names_of_God_the_integer"),
        ("// http://rosettacode.org/wiki/ABC_Problem",
         "http://rosettacode.org/wiki/ABC_Problem"),
        ("// Implements http://rosettacode.org/wiki/Ackermann_function",
         "http://rosettacode.org/wiki/Ackermann_function"),
        ("// Implements http://rosettacode.org/wiki/Almost_prime",
         "http://rosettacode.org/wiki/Almost_prime"),
        ("// Implements http://rosettacode.org/wiki/Arithmetic/Integer",
         "http://rosettacode.org/wiki/Arithmetic/Integer"),
        ("// Implements http://rosettacode.org/wiki/Anagrams",
         "http://rosettacode.org/wiki/Anagrams"),
        ("// Implements http://rosettacode.org/wiki/Averages/Arithmetic_mean",
         "http://rosettacode.org/wiki/Averages/Arithmetic_mean"),
        ("// Implements http://rosettacode.org/wiki/Arrays",
         "http://rosettacode.org/wiki/Arrays"),
        ("// http://rosettacode.org/wiki/Arithmetic/Rational",
         "http://rosettacode.org/wiki/Arithmetic/Rational"),
        ("// Implements http://rosettacode.org/wiki/Assertions",
         "http://rosettacode.org/wiki/Assertions"),
        ("// Implements http://rosettacode.org/wiki/Balanced_brackets",
         "http://rosettacode.org/wiki/Balanced_brackets"),
        ("// Implements http://rosettacode.org/wiki/Averages/Mean_angle",
         "http://rosettacode.org/wiki/Averages/Mean_angle"),
        ("// http://rosettacode.org/wiki/Binary_search",
         "http://rosettacode.org/wiki/Binary_search"),
        ("// Implements http://rosettacode.org/wiki/Binary_digits",
         "http://rosettacode.org/wiki/Binary_digits"),
        ("// http://rosettacode.org/wiki/Evaluate_binomial_coefficients",
         "http://rosettacode.org/wiki/Evaluate_binomial_coefficients"),
        ("// http://rosettacode.org/wiki/Bitwise_operations",
         "http://rosettacode.org/wiki/Bitwise_operations"),
        ("//Implements http://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort",
         "http://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort"),
        ("// Implements http://rosettacode.org/wiki/Call_a_foreign-language_function",
         "http://rosettacode.org/wiki/Call_a_foreign-language_function"),
        ("// Implements http://rosettacode.org/wiki/Apply_a_callback_to_an_array",
         "http://rosettacode.org/wiki/Apply_a_callback_to_an_array"),
        ("// Implements http://rosettacode.org/wiki/Check_that_file_exists",
         "http://rosettacode.org/wiki/Check_that_file_exists"),
        ("// Implements http://rosettacode.org/wiki/Arithmetic/Complex",
         "http://rosettacode.org/wiki/Arithmetic/Complex"),
        ("// Implements http://rosettacode.org/wiki/Concurrent_computing",
         "http://rosettacode.org/wiki/Concurrent_computing"),
        ("// Implements http://rosettacode.org/wiki/Create_a_file",
         "http://rosettacode.org/wiki/Create_a_file"),
        ("// Implements http://rosettacode.org/wiki/Count_in_octal",
         "http://rosettacode.org/wiki/Count_in_octal"),
        ("// Implements http://rosettacode.org/wiki/Empty_program",
         "http://rosettacode.org/wiki/Empty_program"),
        ("// Implements http://rosettacode.org/wiki/Dot_product",
         "http://rosettacode.org/wiki/Dot_product"),
        ("// Implements http://rosettacode.org/wiki/Entropy",
         "http://rosettacode.org/wiki/Entropy"),
        ("// http://rosettacode.org/wiki/Equilibrium_index",
         "http://rosettacode.org/wiki/Equilibrium_index"),
        ("// Implements http://rosettacode.org/wiki/Factorial",
         "http://rosettacode.org/wiki/Factorial"),
        ("// http://rosettacode.org/wiki/FASTA_format",
         "http://rosettacode.org/wiki/FASTA_format"),
        ("// Implements http://rosettacode.org/wiki/Fibonacci_sequence",
         "http://rosettacode.org/wiki/Fibonacci_sequence"),
        ("// Implements http://rosettacode.org/wiki/Fibonacci_word",
         "http://rosettacode.org/wiki/Fibonacci_word"),
        ("// Implements http://rosettacode.org/wiki/File_size",
         "http://rosettacode.org/wiki/File_size"),
        ("// Implements http://rosettacode.org/wiki/Four_bit_adder",
         "http://rosettacode.org/wiki/Four_bit_adder"),
        ("// http://rosettacode.org/wiki/Function_composition",
         "http://rosettacode.org/wiki/Function_composition"),
        ("// http://rosettacode.org/wiki/Greatest_element_of_a_list",
         "http://rosettacode.org/wiki/Greatest_element_of_a_list"),
        ("//http://rosettacode.org/wiki/Function_definition",
         "http://rosettacode.org/wiki/Function_definition"),
        ("// Implements http://rosettacode.org/wiki/Gray_code",
         "http://rosettacode.org/wiki/Gray_code"),
        ("// Implements http://rosettacode.org/wiki/Guess_the_number",
         "http://rosettacode.org/wiki/Guess_the_number"),
        ("// Implements http://rosettacode.org/wiki/Hailstone_sequence",
         "http://rosettacode.org/wiki/Hailstone_sequence"),
        ("// http://rosettacode.org/wiki/Hamming_numbers",
         "http://rosettacode.org/wiki/Hamming_numbers"),
        ("// Implements http://rosettacode.org/wiki/Hamming_numbers",
         "http://rosettacode.org/wiki/Hamming_numbers"),
        ("// Implements http://rosettacode.org/wiki/Happy_numbers",
         "http://rosettacode.org/wiki/Happy_numbers"),
        ("// http://rosettacode.org/wiki/Harshad_or_Niven_series",
         "http://rosettacode.org/wiki/Harshad_or_Niven_series"),
        ("// http://rosettacode.org/wiki/HTTP",
         "http://rosettacode.org/wiki/HTTP"),
        ("//   http://rosettacode.org/wiki/Huffman_coding",
         "http://rosettacode.org/wiki/Huffman_coding"),
        ("// Implements http://rosettacode.org/wiki/IBAN",
         "http://rosettacode.org/wiki/IBAN"),
        ("// Implements http://rosettacode.org/wiki/Infinity",
         "http://rosettacode.org/wiki/Infinity"),
        ("// Implements http://rosettacode.org/wiki/Input_loop",
         "http://rosettacode.org/wiki/Input_loop"),
        ("// Implements http://rosettacode.org/wiki/Check_input_device_is_a_terminal",
         "http://rosettacode.org/wiki/Check_input_device_is_a_terminal"),
        ("// Implements http://rosettacode.org/wiki/Integer_sequence",
         "http://rosettacode.org/wiki/Integer_sequence"),
        ("// Implements http://rosettacode.org/wiki/JSON",
         "http://rosettacode.org/wiki/JSON"),
        ("// Implements http://rosettacode.org/wiki/Letter_frequency",
         "http://rosettacode.org/wiki/Letter_frequency"),
        ("// http://rosettacode.org/wiki/Look-and-say_sequence",
         "http://rosettacode.org/wiki/Look-and-say_sequence"),
        ("// Implements http://rosettacode.org/wiki/Loops/For",
         "http://rosettacode.org/wiki/Loops/For"),
        ("// Implements http://rosettacode.org/wiki/Loops/Infinite",
         "http://rosettacode.org/wiki/Loops/Infinite"),
        ("// Implements http://rosettacode.org/wiki/Loops/For",
         "http://rosettacode.org/wiki/Loops/For"),
        ("// Implements http://rosettacode.org/wiki/Loops/While",
         "http://rosettacode.org/wiki/Loops/While"),
        ("// Implements http://rosettacode.org/wiki/Loops/N_plus_one_half",
         "http://rosettacode.org/wiki/Loops/N_plus_one_half"),
        ("// Implements http://rosettacode.org/wiki/LZW_compression",
         "http://rosettacode.org/wiki/LZW_compression"),
        ("// Solution for http://rosettacode.org/wiki/Execute_a_Markov_algorithm",
         "http://rosettacode.org/wiki/Execute_a_Markov_algorithm"),
        ("// http://rosettacode.org/wiki/Modular_exponentiation",
         "http://rosettacode.org/wiki/Modular_exponentiation"),
        ("// Implements http://rosettacode.org/wiki/MD5/Implementation",
         "http://rosettacode.org/wiki/MD5/Implementation"),
        ("// Implements http://rosettacode.org/wiki/Mutual_recursion",
         "http://rosettacode.org/wiki/Mutual_recursion"),
        ("// Implements http://rosettacode.org/wiki/N-queens_problem",
         "http://rosettacode.org/wiki/N-queens_problem"),
        ("// Implements http://rosettacode.org/wiki/Check_output_device_is_a_terminal",
         "http://rosettacode.org/wiki/Check_output_device_is_a_terminal"),
        ("// Implements http://rosettacode.org/wiki/Palindrome_detection",
         "http://rosettacode.org/wiki/Palindrome_detection"),
        ("// Implements http://rosettacode.org/wiki/Perfect_numbers",
         "http://rosettacode.org/wiki/Perfect_numbers"),
        ("// Implements http://rosettacode.org/wiki/Parallel_calculations",
         "http://rosettacode.org/wiki/Parallel_calculations"),
        ("// set: http://rosettacode.org/wiki/Power_set",
         "http://rosettacode.org/wiki/Power_set"),
        ("// Implements http://rosettacode.org/wiki/Prime_decomposition",
         "http://rosettacode.org/wiki/Prime_decomposition"),
        ("//Implements http://rosettacode.org/wiki/Primality_by_Trial_Division",
         "http://rosettacode.org/wiki/Primality_by_Trial_Division"),
        ("// http://rosettacode.org/wiki/Pythagorean_triples",
         "http://rosettacode.org/wiki/Pythagorean_triples"),
        ("//Implements http://rosettacode.org/wiki/Sorting_algorithms/Quicksort",
         "http://rosettacode.org/wiki/Sorting_algorithms/Quicksort"),
        ("// Implements http://rosettacode.org/wiki/Range_expansion",
         "http://rosettacode.org/wiki/Range_expansion"),
        ("// Implements http://rosettacode.org/wiki/Read_a_file_line_by_line",
         "http://rosettacode.org/wiki/Read_a_file_line_by_line"),
        ("// Implements http://rosettacode.org/wiki/Find_limit_of_recursion",
         "http://rosettacode.org/wiki/Find_limit_of_recursion"),
        ("// Implements http://rosettacode.org/wiki/Rename_a_file",
         "http://rosettacode.org/wiki/Rename_a_file"),
        ("// http://rosettacode.org/wiki/Repeat_a_string",
         "http://rosettacode.org/wiki/Repeat_a_string"),
        ("// Implements http://rosettacode.org/wiki/Reverse_words_in_a_string",
         "http://rosettacode.org/wiki/Reverse_words_in_a_string"),
        ("// http://rosettacode.org/wiki/Roots_of_a_function",
         "http://rosettacode.org/wiki/Roots_of_a_function"),
        ("// http://rosettacode.org/wiki/Roots_of_unity",
         "http://rosettacode.org/wiki/Roots_of_unity"),
        ("// Implements http://rosettacode.org/wiki/Rot-13",
         "http://rosettacode.org/wiki/Rot-13"),
        ("// http://rosettacode.org/wiki/Sequence_of_non-squares",
         "http://rosettacode.org/wiki/Sequence_of_non-squares"),
        ("// Implements http://rosettacode.org/wiki/Set",
         "http://rosettacode.org/wiki/Set"),
        ("// Implements http://rosettacode.org/wiki/SHA-1",
         "http://rosettacode.org/wiki/SHA-1"),
        ("// http://rosettacode.org/wiki/Run-length_encoding",
         "http://rosettacode.org/wiki/Run-length_encoding"),
        ("// http://rosettacode.org/wiki/Self-describing_numbers",
         "http://rosettacode.org/wiki/Self-describing_numbers"),
        ("// Implements http://rosettacode.org/wiki/SHA-256",
         "http://rosettacode.org/wiki/SHA-256"),
        ("// http://rosettacode.org/wiki/Sierpinski_triangle",
         "http://rosettacode.org/wiki/Sierpinski_triangle"),
        ("// Implements http://rosettacode.org/wiki/Short-circuit_evaluation",
         "http://rosettacode.org/wiki/Short-circuit_evaluation"),
        ("// Implements http://rosettacode.org/wiki/Sieve_of_Eratosthenes",
         "http://rosettacode.org/wiki/Sieve_of_Eratosthenes"),
        ("// Implements http://rosettacode.org/wiki/Sort_an_integer_array",
         "http://rosettacode.org/wiki/Sort_an_integer_array"),
        ("// Implements http://rosettacode.org/wiki/Stack",
         "http://rosettacode.org/wiki/Stack"),
        ("// http://rosettacode.org/wiki/String_concatenation",
         "http://rosettacode.org/wiki/String_concatenation"),
        ("// Implements http://rosettacode.org/wiki/Hello_world/Standard_error",
         "http://rosettacode.org/wiki/Hello_world/Standard_error"),
        ("// Implements http://rosettacode.org/wiki/String_interpolation",
         "http://rosettacode.org/wiki/String_interpolation"),
        ("// Implements http://rosettacode.org/wiki/String_matching",
         "http://rosettacode.org/wiki/String_matching"),
        ("// http://rosettacode.org/wiki/Strip_comments_from_a_string",
         "http://rosettacode.org/wiki/Strip_comments_from_a_string"),
        ("// Implements http://rosettacode.org/wiki/Generic_swap",
         "http://rosettacode.org/wiki/Generic_swap"),
        ("// http://rosettacode.org/wiki/Synchronous_concurrency",
         "http://rosettacode.org/wiki/Synchronous_concurrency"),
        ("// http://rosettacode.org/wiki/Taxicab_numbers",
         "http://rosettacode.org/wiki/Taxicab_numbers"),
        ("// http://rosettacode.org/wiki/Towers_of_Hanoi",
         "http://rosettacode.org/wiki/Towers_of_Hanoi"),
        ("// Implements http://rosettacode.org/wiki/Hello_world/Web_server",
         "http://rosettacode.org/wiki/Hello_world/Web_server"),
        ("// implements http://rosettacode.org/wiki/Zig-zag_matrix",
         "http://rosettacode.org/wiki/Zig-zag_matrix"),
        ("// http://rosettacode.org/wiki/Talk:Zig-zag_matrix",
         "http://rosettacode.org/wiki/Talk:Zig-zag_matrix")
    ]

    for input, expected in tests_passed:
        assert code._extract_url_string(input).group(1) == expected


def test_extract_url():
    for path in glob.glob("rosettarobot/test/github-rust-rosetta/src/*.rs"):
        code = robot.CodeEntry(path)
        url = code.extract_url()
        if url is None:
            logging.debug("Failed to extract url from {}".format(path))
            assert False
            break
    else:
        assert url.startswith('http://rosettacode.org/wiki')
