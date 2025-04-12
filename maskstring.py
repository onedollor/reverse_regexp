import random
from string import ascii_lowercase, ascii_uppercase, digits


def _build_random_mapping(chars):
    """Create a random bijective mapping for given characters"""
    shuffled = random.sample(chars, len(chars))
    return dict(zip(chars, shuffled))


class StringMapper:
    def __init__(self, skip_chars=None, seed=None):
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

        self._ascii_lowercase = [c for c in ascii_lowercase if c not in skip_chars]
        self._ascii_uppercase = [c for c in ascii_uppercase if c not in skip_chars]
        self._digits = [c for c in digits if c not in skip_chars]

        self._az_len = len(self._ascii_lowercase)
        self._AZ_len = len(self._ascii_uppercase)
        self._oz_len = len(self._digits)

        self.az_mappings = [_build_random_mapping(self._ascii_lowercase) for _ in range(len(self._ascii_lowercase))]
        self.AZ_mappings = [_build_random_mapping(self._ascii_uppercase) for _ in range(len(self._ascii_lowercase))]
        self.oz_mappings = [_build_random_mapping(self._digits) for _ in range(len(self._digits))]

    def map_string(self, s):
        if not s:
            return ""

        mapped = []
        p = 0
        for i, char in enumerate(s):
            if char not in self._ascii_lowercase + self._ascii_uppercase + self._digits:
                mapped.append(char)
                p = 0
                continue
            else:
                if char in self._ascii_lowercase:
                    # Use az_mappings based on position mod self._az_len
                    mapping = self.az_mappings[p % self._az_len]
                elif char in self._ascii_uppercase:
                    # Use AZ_mappings based on position mod self._AZ_len
                    mapping = self.AZ_mappings[p % self._AZ_len]
                else:
                    # Use oz_mappings based on position mod self._oz_len
                    mapping = self.oz_mappings[p % self._oz_len]

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

