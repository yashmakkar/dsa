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

## 📌 Learning (Initial Approach → Optimized Solution)
### Best Time to Buy and Sell Stock (LeetCode 121)

- **Reduced State:**  
  Initially tracked both buy (`min`) and sell (`max`) prices. Learned that only the **minimum price so far** is needed; profit is simply `current_price - min_price`.

- **Better Mental Model:**  
  Shifted from “find max selling price” to **“assume today is the selling day”**, which simplifies logic and removes extra conditions.

- **Avoid Built-in Shadowing:**  
  Using variable names like `min` and `max` hides Python built-ins. Renaming to `mini` and `maxProfit` improves safety and readability.

- **Cleaner Greedy Logic:**  
  Replaced multiple conditional branches with direct `min()` and `max()` updates for clearer and more maintainable code.

- **Pattern Recognition:**  
  Identified this as a **Greedy / Sliding Window** problem — buy at the lowest price before selling.

- **Quality Beyond Complexity:**  
  Both versions run in `O(n)` time and `O(1)` space, but the optimized version is **simpler, clearer, and interview-friendly**.
