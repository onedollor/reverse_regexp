import sre_parse
import sre_compile
import random
import string
import re


def generate_string_from_parsed_regex(parsed_pattern: sre_parse.SubPattern, position : int = None, current_position_idx : int = None):
    """
    Generates a string that matches the regular expression represented by the parsed pattern.

    Args:
        parsed_pattern: The parsed regular expression pattern (output of sre_parse.parse()).

    Returns:
        str: A string that matches the regular expression, or None if generation fails.
    """

    def generate_from_token(token, position, current_position_idx):
        """Generates a string segment based on a specific token from the parsed regex."""
        op, args = token

        if op == sre_parse.LITERAL:
            return chr(args), current_position_idx  # LITERAL = Character literal

        elif op == sre_parse.MAX_REPEAT:
            min_repeat, max_repeat, subpattern = args
            result = ""

            if 10 < max_repeat:
                min_repeat = 10
            elif max_in_position < max_repeat:
                min_repeat = max_in_position
            elif position_len < max_repeat:
                min_repeat = position_len

            num_repeats = random.randint(min_repeat, max_repeat if max_repeat < (min_repeat + 10) else (min_repeat + 10) + max_repeat % (min_repeat + 1))  # Limit max repeat to avoid very long strings

            for _ in range(num_repeats - len(result)):
                gs, current_position_idx = generate_string_from_parsed_regex(subpattern, position, current_position_idx)
                result += gs
            return result, current_position_idx

        elif op == sre_parse.SUBPATTERN:
            # Handle cases where args has more than 3 elements
            for subpattern in args:
                if isinstance(subpattern, sre_parse.SubPattern):
                    return generate_string_from_parsed_regex(subpattern, position, current_position_idx)
                else:
                    #print(type(subpattern))
                    pass

        elif op == sre_parse.BRANCH:  # OR operator
            _, alternatives = args
            chosen_alternative = random.choice(alternatives)
            return generate_string_from_parsed_regex(chosen_alternative, position, current_position_idx)

        elif op == sre_parse.IN: #Character Sets ([abc], [a-z])
            char_set = ""
            for sub_token in args: #Iterate over character set elements
                sub_op, sub_args = sub_token

                if sub_op == sre_parse.LITERAL:
                    char_set += chr(sub_args)
                elif sub_op == sre_parse.CATEGORY:
                    category = sub_args
                    if category == sre_parse.CATEGORY_DIGIT:
                        char_set += string.digits
                    elif category == sre_parse.CATEGORY_WORD:
                        char_set += string.ascii_letters + string.digits + "_"
                    elif category == sre_parse.CATEGORY_SPACE:
                        char_set += ' ' #string.whitespace
                    elif category == sre_parse.CATEGORY_NOT_WORD:
                        char_set += "!@#$%^&*()-+"
                    elif category == sre_parse.ANY:
                        char_set += random.choice(string.printable[:-5]) #Placeholder until better logic
                    elif category == sre_parse.NOT_LITERAL:
                        for i in range(32, 127):  # printable ascii range
                            if i != args:
                                char_set += chr(i)
                    elif category == sre_parse.CATEGORY_NOT_DIGIT:
                        char_set += string.ascii_letters + string.punctuation + ' '
                    elif category == sre_parse.CATEGORY_NOT_SPACE:
                        char_set += string.ascii_letters + string.punctuation + string.digits
                    else:
                        print(f"Unsupported category: {category}")

                elif sub_op == sre_parse.RANGE:
                    start, end = sub_args
                    for i in range(start, end + 1):
                        char_set += chr(i)

            if char_set:
                if len(char_set) > max_in_position:
                    if current_position_idx is not None \
                            and position is not None \
                            and current_position_idx < position_len:
                        _c = sorted(char_set)[int(str(position)[current_position_idx])]
                        current_position_idx += 1
                        return _c, current_position_idx
                    else:
                        return random.choice(char_set), current_position_idx
                else:
                    return random.choice(char_set), current_position_idx
            else:
                return "" #Handle edge case where character set is empty

        elif op == sre_parse.ANY:
            return random.choice(string.printable[:-5]), current_position_idx #Any character except newline and some others

        elif op == sre_parse.NOT_LITERAL:
           possible_chars = ""
           for i in range(32, 127): #printable ascii range
               if i != args:
                   possible_chars += chr(i)
           return random.choice(possible_chars), current_position_idx


        elif op == sre_parse.NEGATE:
          #Handle NEGATE outside of character class (generally not supported)
          return "", current_position_idx

        elif op == sre_parse.AT:
            # ^, $, \A, \Z, \b, \B (Position assertions) - Skip these
            return "", current_position_idx

        elif op in [sre_parse.CATEGORY, sre_parse.CATEGORY_DIGIT, sre_parse.CATEGORY_SPACE, sre_parse.CATEGORY_WORD, sre_parse.CATEGORY_NOT_WORD]:  # Character categories (\d, \w, \s)
            category = args
            if category == sre_parse.CATEGORY_DIGIT:
                return random.choice(string.digits), current_position_idx
            elif category == sre_parse.CATEGORY_WORD:
                return random.choice(string.ascii_letters + string.digits + "_"), current_position_idx
            elif category == sre_parse.CATEGORY_SPACE:
                return ' ', current_position_idx
            elif category == sre_parse.CATEGORY_NOT_WORD:
                return random.choice("!@#$%^&*()-+"), current_position_idx #Placeholder until better logic

            else:
                return "", current_position_idx #Unsupported category


        else:
            print(f"Unsupported token: {op}")
            return "", current_position_idx #Ignore unhandled token


    generated_string = ""
    position_len = len(str(position))
    max_in_position = max([int(c) for c in str(position)])
    for token in parsed_pattern:
        gs, current_position_idx = generate_from_token(token, position, current_position_idx)
        generated_string += gs
        #print(f"parsed_pattern: {parsed_pattern} generated_string: {generated_string}")

    return generated_string, current_position_idx


def verify_generated_string(pattern_string, generated_string):
    """
    Verifies that the generated string matches the original regular expression.

    Args:
        pattern_string (str): The original regular expression pattern.
        generated_string (str): The string generated by the function.

    Returns:
        bool: True if the generated string matches the pattern, False otherwise.
    """
    try:
        compiled_pattern = re.compile(pattern_string)
        match = compiled_pattern.fullmatch(generated_string)  # Use fullmatch for exact matching
        return match is not None
    except re.error as e:
        print(f"Regex compilation error: {e}")
        return False


# Example Usage:
if __name__ == '__main__':
    pattern_string = r"(a|b)*c[12345]{4}\w{3}"
    pattern_string = r"(_en|_fr){,3}"
    pattern_string = r"^/(?=.{6,20}$)\D*\d/"
    pattern_string = r"[0-5]{2,5}(\d{3,})"
    pattern_string = r"[qwrtpsdfghjklzxcvbnm]*\w*(\d{2,})\W*"


    parsed_pattern = sre_parse.parse(pattern_string)
    is_valid_manual = verify_generated_string(pattern_string, "/uMkYaaD6/")
    print(f"Regex pattern: {pattern_string}")
    print(f"parsed_pattern: {parsed_pattern}")
    #print(sorted(list("qwrtpsdfghjklzxcvbnm")))
    for p in range(100, 110):
        generated_string, _ = generate_string_from_parsed_regex(parsed_pattern=parsed_pattern, position=p, current_position_idx=0)
        is_valid = verify_generated_string(pattern_string, generated_string)

        print(f"Generated string: {generated_string}")
        #print(f"Is valid: {is_valid} {is_valid_manual}")
        print(f"Is valid: {is_valid}")