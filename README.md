# reverse_regexp
reverse string from regexp, support try to embed a sequence inside generated string

if don't need embed sequence just set position and current_position_idx to None

"""
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
"""
