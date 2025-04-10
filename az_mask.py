import random
from string import ascii_lowercase, ascii_uppercase, digits


class CharMapper:
    def __init__(self):
        # Initialize all mappings
        self.az_mappings = [self._build_random_mapping(ascii_lowercase) for _ in range(26)]
        self.AZ_mappings = [self._build_random_mapping(ascii_uppercase) for _ in range(26)]
        self.oz_mappings = [self._build_random_mapping(digits) for _ in range(10)]

    def _build_random_mapping(self, chars):
        """Create a random bijective mapping for given characters"""
        shuffled = random.sample(chars, len(chars))
        return dict(zip(chars, shuffled))


    def map_string(self, s):
        if not s:
            return ""

        mapped = []
        p = 0
        for i, char in enumerate(s):
            if char not in ascii_lowercase + ascii_uppercase + digits:
                mapped.append(char)
                p = 0
                continue
            else:
                if char in ascii_lowercase:
                    # Use az_mappings based on position mod 26
                    mapping = self.az_mappings[p % 26]
                elif char in ascii_uppercase:
                    # Use AZ_mappings based on position mod 26
                    mapping = self.AZ_mappings[p % 26]
                else:
                    # Use oz_mappings based on position mod 10
                    mapping = self.oz_mappings[p % 10]

                if p == 0:
                    mapped.append(mapping[char])
                else:
                    prev_char = mapped[-1]
                    if (char in ascii_lowercase and prev_char in ascii_lowercase)\
                            or (char in ascii_uppercase and prev_char in ascii_uppercase)\
                            or (char in digits and prev_char in digits):
                        if char in ascii_lowercase:
                            mapped.append(mapping[chr(97 + (ord(prev_char)+ord(char)) % 26)])
                        elif char in ascii_uppercase:
                            mapped.append(mapping[chr(65 + (ord(prev_char)+ord(char)) % 26)])
                        else:
                            mapped.append(mapping[chr(48 + (ord(prev_char)+ord(char)) % 10)])
                    else:
                        mapped.append(mapping[char])
                p += 1


        return ''.join(mapped)


# Example usage
mapper = CharMapper()

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

for i in range(0,62):
    for j in range(0,62):
        for k in range(0, 62):
            for l in range(0, 62):
                s = mapper.map_string(f"{letters[i]}{letters[j]}{letters[k]}{letters[l]}")
                if s in r:
                    print(f"{letters[i]}{letters[j]}{letters[k]}{letters[l]} => s[{s}]")
                else:
                    r.add(s)

                c+=1

print(f"{len(r)} {c}")