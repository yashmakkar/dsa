### Valid Anagram – (LeetCode 42)

**Pattern:** Frequency Array / Counting  

**Core Idea:**
- Use fixed array of size 26 for letters
- Increment for `s`, decrement for `t`
- All zeros → anagram

**Why It Works:**
- Anagrams have identical character frequencies
- Constant space due to fixed alphabet size

**Complexity:**
- **Time:** `O(n)`
- **Space:** `O(1)`

**Interview Trigger:**
> String frequency match → **Counting Array**

---
### Contains Duplicate – (LeetCode 217)

**Pattern:** Hash Set  

**Core Idea:**
- Store elements in a set
- Compare set size with array size

**Why It Works:**
- Sets keep only unique values
- Size mismatch indicates duplicates

**Complexity:**
- **Time:** `O(n)`
- **Space:** `O(n)`

**Interview Trigger:**
> Duplicate detection → **Set / Hashing**

---
## Group Anagrams – (LeetCode 49)

**Pattern:** Hash Map + Frequency Array  

**Core Idea:**
- Represent each word by 26-length character count
- Use frequency tuple as dictionary key
- Group words with same counts

**Why It Works:**
- Anagrams share identical character frequencies
- Order doesn’t matter, only counts do

**Complexity:**
- **Time:** `O(n · k)`
- **Space:** `O(n · k)`

**Interview Trigger:**
> Anagram grouping → **Frequency Array as Hash Key**


