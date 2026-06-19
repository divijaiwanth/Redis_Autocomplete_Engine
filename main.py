import redis
from pathlib import Path

WORDS_FILE = "words.txt"
REDIS_KEY = "autocomplete"

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


class AutoComplete:
    def __init__(self):
        self._load_words()

    def _load_words(self):
        """Load words from words.txt into Redis."""
        r.delete(REDIS_KEY)

        #If path doesnot exist, create it and return
        path = Path(WORDS_FILE)
        if not path.exists():
            path.touch()
            return

        with open(WORDS_FILE, "r", encoding="utf-8") as f:
            words = {
                line.strip().lower()
                for line in f
                if line.strip()
            }

        if words:
            mapping = {word: 0 for word in words}
            r.zadd(REDIS_KEY, mapping)

    def add_word(self, word: str):
        """Add a new word to both Redis and words.txt."""
        word = word.strip().lower()

        if not word:
            return

        # Prevent duplicates
        if r.zscore(REDIS_KEY, word) is not None:
            return

        # Add to Redis
        r.zadd(REDIS_KEY, {word: 0})

        # Append to file
        with open(WORDS_FILE, "a", encoding="utf-8") as f:
            f.write(f"{word}\n")

    def search(self, prefix: str, limit: int = 10):
        """Return autocomplete suggestions."""
        prefix = prefix.lower()

        return r.zrangebylex(
            REDIS_KEY,
            f"[{prefix}",
            f"[{prefix}\xff",
            0,
            limit,
        )


if __name__ == "__main__":
    ac = AutoComplete()

    while True:
        print("\n1. Search")
        print("2. Add word")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            prefix = input("Prefix: ")
            print(ac.search(prefix))

        elif choice == "2":
            word = input("New word: ")
            ac.add_word(word)
            print("Added.")

        elif choice == "3":
            break