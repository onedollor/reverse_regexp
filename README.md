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

#Regex pattern: [qwrtpsdfghjklzxcvbnm]*\w*(\d{2,})\W*\S{,5}\s?\w+
#parsed_pattern: [(MAX_REPEAT, (0, MAXREPEAT, [(IN, [(LITERAL, 113), (LITERAL, 119), (LITERAL, 114), (LITERAL, 116), (LITERAL, 112), (LITERAL, 115), (LITERAL, 100), (LITERAL, 102), (LITERAL, 103), (LITERAL, 104), (LITERAL, 106), (LITERAL, 107), (LITERAL, 108), (LITERAL, 122), (LITERAL, 120), (LITERAL, 99), (LITERAL, 118), (LITERAL, 98), (LITERAL, 110), (LITERAL, 109)])])), (MAX_REPEAT, (0, MAXREPEAT, [(IN, [(CATEGORY, CATEGORY_WORD)])])), (SUBPATTERN, (1, 0, 0, [(MAX_REPEAT, (2, MAXREPEAT, [(IN, [(CATEGORY, CATEGORY_DIGIT)])]))])), (MAX_REPEAT, (0, MAXREPEAT, [(IN, [(CATEGORY, CATEGORY_NOT_WORD)])])), (MAX_REPEAT, (0, 5, [(IN, [(CATEGORY, CATEGORY_NOT_SPACE)])])), (MAX_REPEAT, (0, 1, [(IN, [(CATEGORY, CATEGORY_SPACE)])])), (MAX_REPEAT, (1, MAXREPEAT, [(IN, [(CATEGORY, CATEGORY_WORD)])]))]
#Generated string: cbblcrjqvcphrqnhpnsjV6Z5cN51bhOwf769371669044862266!##$*&$)*@#%!+$(!#1hu6WU6G1wY6E
#Is valid: True
#Generated string: cbccbpqbrxhxltoh1pgWnI4xy943356894997048!#%$@&$@!*!%@-RY(-Z mpl7JNrH_tYhBuYhM5Nb8
#Is valid: True
#Generated string: cbdqxzhrdcvcdltvftmzk5te_vyOG2iFfymc5L8693028431343654$+&+(+($&&@-$0pI`s Nit77xtQLWwn65gVAfSH0
#Is valid: True
#Generated string: cbfgnqnlbrjV69_6bcaUr739421406025112&+&-((%)%&-\d>V_no3R77EwyB0ZnViSLrbH
#Is valid: True
#Generated string: cbgjpsvqfpwpnjtU4Z8da3FGKHHRRlo8051561580965949100)@#&*&)^$#&-@11?Q48iQ0mPjpp3lZ6UkvJMDB_H
#Is valid: True
#Generated string: cbhwlpxnlzvdvqnfnvj7PFF9Fxy0j0K2ipjaxGD838161424986854)$&++!)-@#&)%$!-#$)&@--d!c zHKy0YHOh7I_
#Is valid: True
#Generated string: cbjxnrhhtvhxhwddvzsbrw2FdlSe8JD8LzSdjXI02576091544448365600(-(+#!^%$#^@@@^((#($)%$KSE=EwiGbNOKf3SoxDNWZ5hohgf
#Is valid: True
#Generated string: cbklfxsvtvdlhDpG4nQdYgonwBC6367701318381724492-!!@#$$%^&##))<dy3 LZulheCZEu
#Is valid: True
#Generated string: cblzxwmxwjmdpmvqfrxkzrzgbnkObbkPd5sot7137036858019807996+)^^!&&^#%#^$)$^!#$06yMWesq4FN5nczf1Orcv
#Is valid: True
#Generated string: cbmlxtlftzqwhpftCF6gGBEmc319955787986814190*$&(@*-(&$%(+$##*+++)#xH$B nWKfxOovCoo
#Is valid: True
```
