# reverse_regexp
reverse string from regexp, support try to embed a sequence inside generated string

if don't need embed sequence just set position and current_position_idx to None

# Example Usage:

```
pattern_string = r"[qwrtpsdfghjklzxcvbnm]*\w*(\d{2,})\W*\S{,5}\s?\w+"

parsed_pattern = sre_parse.parse(pattern_string)
print(f"Regex pattern: {pattern_string}")
print(f"parsed_pattern: {parsed_pattern}")
for p in range(100, 110):
    generated_string, _ = generate_string_from_parsed_regex(parsed_pattern=parsed_pattern, position=p, current_position_idx=0)
    is_valid = verify_generated_string(pattern_string, generated_string)

    print(f"Generated string: {generated_string}")
    print(f"Is valid: {is_valid}")
```
