import random
from string import ascii_lowercase, ascii_uppercase, digits


class StringMapper:
    @staticmethod
    def _build_random_mapping(chars, th=0.8):
        max_retry = 100
        curr = 0

        if len(chars) == 0 or len(chars) == 1:
            return dict(zip(chars, chars))

        _th = th if (1 - 1/len(chars)) > th else (1 - 1/(len(chars) - 1) - 0.1)

        #print(f"len(chars)[{len(chars)}] max_th[{(1 - 1/len(chars))}] _th[{_th}]")
        """Create a random bijective mapping for given characters"""
        while curr < max_retry:
            shuffled = random.sample(chars, len(chars))
            is_valid = StringMapper.validate_shuffle(chars, shuffled, th=_th)

            if len(chars) < 3 or is_valid:
                return dict(zip(chars, shuffled))
            else:
                curr += 1
        raise Exception(f"can't generate random mapping,un-shuffled over th[{th}].")

    @staticmethod
    def validate_shuffle(chars, shuffled, th=0.8):
        d = 0
        for i, char in enumerate(chars):
            if shuffled[i] == char:
                d += 1
        #print(f"r[{(len(chars) - d) / len(chars) }] th[{th}]")
        return ((len(chars) - d) / len(chars)) >= th

    def __init__(self, skip_chars=None, static_words=None, min_mask_len=0, seed=None):
        """
        Initializes the Mappings object with random bijective mappings for lowercase,
        uppercase letters, and digits.  Uses a seed for reproducible mappings.

        Args:
            seed: An optional integer seed for the random number generator.
                  If provided, the mappings will be the same for the same seed.
                  If None, the mappings will be different each time.
        """
        if seed is not None:
            random.seed(seed)  # Seed the random number generator

        if skip_chars is None:
            skip_chars = []

        self.static_words = set([word.lower().strip() for word in static_words if word is not None]) if static_words else set()
        self.min_mask_len = min_mask_len

        self._ascii_lowercase = [c for c in ascii_lowercase if c not in skip_chars]
        self._ascii_uppercase = [c for c in ascii_uppercase if c not in skip_chars]
        self._digits = [c for c in digits if c not in skip_chars]

        self._az_len = len(self._ascii_lowercase)
        self._AZ_len = len(self._ascii_uppercase)
        self._oz_len = len(self._digits)

        self.az_mappings = {}
        self.AZ_mappings = {}
        self.oz_mappings = {}

        for i in range(len(self._ascii_lowercase)):
            self.az_mappings[i] = [StringMapper._build_random_mapping(self._ascii_lowercase) for _ in range(i+1)]

        for i in range(len(self._ascii_uppercase)):
            self.AZ_mappings[i] = [StringMapper._build_random_mapping(self._ascii_uppercase) for _ in range(i+1)]

        for i in range(len(self._digits)):
            self.oz_mappings[i] = [StringMapper._build_random_mapping(self._digits) for _ in range(i+1)]

        self.len_az_mappings = len(self.az_mappings)
        self.len_AZ_mappings = len(self.AZ_mappings)
        self.len_oz_mappings = len(self.oz_mappings)

    def map_string(self, s):
        if not s:
            return ""
        elif s.lower().strip() in self.static_words:
            return s
        elif len(s) <= self.min_mask_len:
            return s

        mapped = []
        p = 0
        len_s = len(s)

        for i, char in enumerate(s):
            if char not in self._ascii_lowercase + self._ascii_uppercase + self._digits:
                mapped.append(char)
                p = 0
                continue
            else:
                if char in self._ascii_lowercase:
                    # Use az_mappings based on position mod self._az_len
                    if len_s >= self.len_az_mappings:
                        mapping = self.az_mappings[self.len_az_mappings - 1][p % self._az_len]
                    else:
                        mapping = self.az_mappings[len_s % self.len_az_mappings][p % self._az_len]
                elif char in self._ascii_uppercase:
                    # Use AZ_mappings based on position mod self._AZ_len
                    if len_s >= self.len_AZ_mappings:
                        mapping = self.AZ_mappings[self.len_AZ_mappings - 1][p % self._AZ_len]
                    else:
                        mapping = self.AZ_mappings[len_s % self.len_AZ_mappings][p % self._AZ_len]
                else:
                    # Use oz_mappings based on position mod self._oz_len
                    if len_s >= self.len_oz_mappings:
                        mapping = self.oz_mappings[self.len_oz_mappings - 1][p % self._oz_len]
                    else:
                        mapping = self.oz_mappings[len_s % self.len_oz_mappings][p % self._oz_len]

                if p == 0:
                    mapped.append(mapping[char])
                else:
                    prev_char = mapped[-1]
                    if char in self._ascii_lowercase and prev_char in self._ascii_lowercase:
                        mapped.append(mapping[self._ascii_lowercase[(self._ascii_lowercase.index(prev_char) +
                                                                     self._ascii_lowercase.index(char)) % self._az_len]])
                    elif char in self._ascii_uppercase and prev_char in self._ascii_uppercase:
                        mapped.append(mapping[self._ascii_uppercase[(self._ascii_uppercase.index(prev_char) +
                                                                     self._ascii_uppercase.index(char)) % self._AZ_len]])
                    elif char in self._digits and prev_char in self._digits:
                        mapped.append(mapping[self._digits[(self._digits.index(prev_char) +
                                                            self._digits.index(char)) % self._oz_len]])
                    else:
                        mapped.append(mapping[char])

                p += 1

        return ''.join(mapped)

