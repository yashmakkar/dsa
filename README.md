## 📌 Learning – Two Sum (Hash Map Pattern)

- Even if two solutions have the same **Big-O time complexity (O(n))**, their **real-world performance can differ** due to extra passes and higher constant factors.
- Avoid **multiple scans** over the input when the problem guarantees a single valid solution.
- Prefer **one-pass hash map approaches** where lookup and storage happen together.
- Do not use `key in dict.keys()` for membership checks; always use `key in dict` for better efficiency.
- **Store indices early** instead of finding values first and indices later.
- Use **problem guarantees** (e.g., *exactly one solution exists*) to simplify logic and remove unnecessary edge-case handling.
- The optimal strategy is:
  > While iterating, check if `target - current_value` exists in a hash map. If yes, return the stored index and current index immediately.

### 🧠 Pattern Identified
- **Hash Map + One-Pass Lookup**
- Commonly used in:
  - Two Sum
  - Subarray Sum
  - Pair Sum problems
  - Frequency-based problems
