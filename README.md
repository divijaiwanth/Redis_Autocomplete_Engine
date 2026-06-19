# Redis Autocomplete Engine - Lightning Fast Prefix Search with Redis

A small Implementation Understanding of how Typeahead/Autocomplete works in production level products

Redis Autocomplete Engine is a lightweight, high-performance autocomplete system built in Python using Redis Sorted Sets and lexicographical range queries. It demonstrates how modern backend services can deliver instant search suggestions with minimal latency while keeping the implementation simple and easy to understand.

The project uses a plain `words.txt` file as its persistent dictionary and automatically indexes all words into Redis on startup. Any new word added through the application is immediately written to both Redis and `words.txt`, ensuring fast searches and persistence across restarts.

### this setup can also be upgraded by using Popularity Scoring and degradation techiniques
---

# System Architecture

```text
                 +----------------------+
                 |      words.txt       |
                 +----------+-----------+
                            |
                    Load on Startup
                            |
                            v
                 +----------------------+
                 |      main.py         |
                 +----------+-----------+
                            |
            +---------------+----------------+
            |                                |
            v                                v
   +------------------+             +------------------+
   |  Redis Sorted Set |             |   Add New Word   |
   | Lexicographic     |             | Update Redis +   |
   | Prefix Search     |             | Append to File   |
   +------------------+             +------------------+
                            |
                            v
                   Autocomplete Results
```

---

# ✨ Key Features

* **⚡ Fast Prefix Search** — Uses Redis Sorted Sets and lexicographical ordering for efficient autocomplete.
* **💾 Persistent Storage** — Stores all words in `words.txt` while Redis acts as a high-speed index.
* **➕ Dynamic Updates** — New words become searchable instantly and are automatically persisted.
* **🧩 Simple & Extendable** — Clean architecture that's easy to build upon with ranking, APIs, or fuzzy search.

---

# Project Structure

```text
redis-autocomplete/
├── main.py
├── words.txt
├── requirements.txt
└── README.md
```

---

# Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/redis-autocomplete.git
cd redis-autocomplete
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Start Redis (Linux / WSL)

Ensure Redis is installed on your machine.

### Option 1: Start Redis directly

```bash
redis-server
```

Open another terminal and verify it is running:

```bash
redis-cli ping
```

Expected output:

```text
PONG
```

### Option 2: If Redis is installed as a service

```bash
sudo service redis-server start
```

or on systems using `systemd`:

```bash
sudo systemctl start redis-server
```

Verify:

```bash
redis-cli ping
```

You should again receive:

```text
PONG
```

## 4. Prepare `words.txt`

Create a `words.txt` file in the project root with one word per line:

```text
apple
application
apply
banana
band
bandwidth
cat
catalog
```

## 5. Run the Project

```bash
python main.py
```

The application will:

* Load all words from `words.txt` into Redis.
* Perform instant prefix-based searches.
* Save newly added words to both Redis and `words.txt`.

---

# Technology Stack

| Component              | Technology                    |
| ---------------------- | ----------------------------- |
| **Language**           | Python                        |
| **Database / Cache**   | Redis                         |
| **Persistent Storage** | `words.txt`                   |
| **Data Structure**     | Redis Sorted Sets (`ZSET`)    |
| **Search Method**      | Lexicographical Range Queries |

---

# How It Works

### 1. Load Dictionary

When the application starts, it reads every entry from `words.txt` and inserts it into a Redis Sorted Set using a uniform score.

### 2. Prefix Search

When the user types a prefix such as `app`, Redis performs a lexicographical range query to retrieve matching words extremely quickly.

### 3. Add New Words

Any newly inserted word is:

* Added to the Redis index immediately.
* Appended to `words.txt`.
* Available for future searches without restarting the application.

---

# Why Redis Autocomplete Engine?

This project demonstrates practical backend engineering techniques used in real-world systems:

* Efficient autocomplete using Redis Sorted Sets.
* Prefix searching via lexicographical ordering.
* Separation of persistent storage and in-memory indexing.
* Clean, modular Python implementation suitable for extension into larger services.

It showcases knowledge of:

* Redis
* Data structures and algorithms
* Backend system design
* Low-latency search techniques

---

# Future Improvements

* Popularity-based ranking of suggestions.
* REST API using FastAPI or Flask.
* Fuzzy matching for typo tolerance.
* Docker support.
* Benchmarking with million-word datasets.
* Unit and integration tests.
* Database-backed persistence instead of a text file.

---

# ❤️ Made With Passion

Made with ❤️ by **Divi Jaiwanth**
