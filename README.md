# reverse_regexp
reverse string from regexp, support try to embed a sequence inside generated string

if don't need embed sequence just set position and current_position_idx to None

# Example Usage:

```
if __name__ == '__main__':
    pattern_string = r"(a|b)*c[12345]{4}\w{3}"
    pattern_string = r"(_en|_fr){,3}"
    pattern_string = r"^/(?=.{6,20}$)\D*\d/"
    pattern_string = r"[qwrtpsdfghjklzxcvbnm]*\w*(\d{2,})\W*"
    pattern_string = r"\((?!2001)[0-9a-zA-z _\.\-:]*\)"
    pattern_string = r"^(feature|bugfix|hotfix|release)/[a-z0-9-]+(-\d+)?$"
    pattern_string = r"/\d+(?!\s*(kg|lb))/"
    pattern_string = r"[0-5]{2,5}(\d{3,})"
    pattern_string = r"^(feature|bugfix|hotfix|release)/[a-z0-9-]+(-\d+)?$"
    pattern_string = r"^[MJHDWTRPCN]{1}[aeiou]{1,2}[qsghjklxz]{1}[aeiouy]{1}[bhjdksapel]{1}[rstuvwxyz]+$"

    parsed_pattern = sre_parse.parse(pattern_string)
    # is_valid_manual = verify_generated_string(pattern_string, "100 dollars")
    # print(f"Is valid manual: {is_valid_manual}")

    print(f"Regex pattern: {pattern_string}")
    print(f"parsed_pattern: {parsed_pattern}")
    #print(sorted(list("qwrtpsdfghjklzxcvbnm")))

    position_accept_chars = get_all_accept_word_from_regex(parsed_pattern)
    print(f"position_accept_chars: {position_accept_chars}")
    r=[]
    rr=set()
    v=0
    for p in range(10000000, 10100000):
        generated_string, _ = generate_string_from_parsed_regex(parsed_pattern=parsed_pattern, position_accept_chars=position_accept_chars, position=p, current_position_idx=0)
        is_valid = verify_generated_string(pattern_string, generated_string.replace("|",""))
        r.append(generated_string)
        rr.add(generated_string)
        if is_valid:
            v+=1

    print("--------------------------------------------------------------------------")
    print(f"verified count[{v}] total generated[{len(r)}] unique generated[{len(rr)}]")
    print("--------------------------------------------------------------------------")
    print(f"{r[1]}\n{r[100]}\n{r[200]}\n{r[500]}\n{r[1000]}\n{r[1500]}\n{r[1999]}\n")
    print("--------------------------------------------------------------------------")

    for _r in r[:10]:
        print(_r)
    print("--------------------------------------------------------------------------")
```
