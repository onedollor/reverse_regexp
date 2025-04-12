from maskstring import StringMapper
skip_chars = 'aeiounrtuAEIOUNRTU'

# Example usage
mapper = StringMapper(skip_chars=skip_chars, seed=23713613163291)

# Test with different strings
print(mapper.map_string("abc123ABC"))  # Example: "xzv709QWE"
print(mapper.map_string("helloWORLD123"))  # Example: "mjqauVKXGB384"

print("Static mapping:")
print("ab →", mapper.map_string("ab"))
print("ba →", mapper.map_string("ba"))

print("abab →", mapper.map_string("abab"))
print("abaab →", mapper.map_string("abaab"))

print("aba →", mapper.map_string("aba"))
print("abn →", mapper.map_string("abn"))

r = set()
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
c = 0

for i in range(0,len(letters)):
    for j in range(0,len(letters)):
        s = mapper.map_string(f"{letters[i]}{letters[j]}")
        if s=='my':
            print(f"{letters[i]}{letters[j]} => s[{s}]")

        if s in r:
            pass
            #print(f"{letters[i]}{letters[j]} => s[{s}]")
        else:
            r.add(s)
        c+=1

print(f"{len(r)} {c}")

for i in range(0,len(letters)):
    for j in range(0,len(letters)):
        for k in range(0, len(letters)):
            for l in range(0, len(letters)):
                s = mapper.map_string(f"{letters[i]}{letters[j]}{letters[k]}{letters[l]}")
                # if s in r:
                #     print(f"{letters[i]}{letters[j]}{letters[k]}{letters[l]} => s[{s}]")
                # else:
                r.add(s)
                c+=1

print(f"{len(r)} {c}")