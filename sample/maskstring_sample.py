from maskstring import StringMapper
skip_chars = '01enrtuENRTU'
#skip_chars = '01abcdefghijklmnopqrstuvwx'
min_mask_len = 1
# Example usage
mapper = StringMapper(skip_chars=skip_chars, static_words=None, min_mask_len=min_mask_len, seed=23713613163291)

print(f"skip_chars[{skip_chars}]")
print(f"min_mask_len[{min_mask_len}]")
# Test with different strings
print(mapper.map_string("abc123ABC"))  # Example: "xzv709QWE"
print(mapper.map_string("helloWORLD123"))  # Example: "mjqauVKXGB384"
print(mapper.map_string("""Data masking is a security technique that protects sensitive data by replacing it with fake or randomized values, making it unrecognizable to unauthorized users while preserving its functionality for authorized users. This process allows data to be used for purposes like testing, training, and development without exposing sensitive information. """))

print("Static mapping:")
print("x →", mapper.map_string("x"))
print("y →", mapper.map_string("y"))
print("ab →", mapper.map_string("ab"))
print("ba →", mapper.map_string("ba"))

print("abab →", mapper.map_string("abab"))
print("abacb →", mapper.map_string("abacb"))

print("aba →", mapper.map_string("aba"))
print("abn →", mapper.map_string("abn"))

r = set()
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
c = 0

for i in range(0,len(letters)):
    for j in range(0,len(letters)):
        s = f"{letters[i]}{letters[j]}"
        ms = mapper.map_string(s)
        #print(f"s[{s}] => ms[{ms}]")

        if ms in r:
            pass
            #print(f"{s} => ms[{ms}]")
        else:
            r.add(ms)
        c+=1

print(f"{len(r)} {c}")

# for i in range(0,len(letters)):
#     for j in range(0,len(letters)):
#         for k in range(0, len(letters)):
#             for l in range(0, len(letters)):
#                 s = mapper.map_string(f"{letters[i]}{letters[j]}{letters[k]}{letters[l]}")
#                 # if s in r:
#                 #     print(f"{letters[i]}{letters[j]}{letters[k]}{letters[l]} => s[{s}]")
#                 # else:
#                 r.add(s)
#                 c+=1
#
# print(f"{len(r)} {c}")