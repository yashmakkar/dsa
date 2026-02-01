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

---
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


---
### Subarray Sum Equals K – (LeetCode 560)

**Pattern:** Prefix Sum + Hash Map

**Key Idea:**
If  
`prefix_sum[j] - prefix_sum[i] = k`  
→ subarray `nums[i+1 ... j]` sums to `k`

**Core Logic:**
- Maintain running prefix sum
- Store prefix sum frequencies in a hash map
- For each index, add `freq[prefix_sum - k]` to result

**Important Initialization:**
```python
d = {0: 1}
```
- **Handles subarrays starting at index `0`**

### Why Not Sliding Window?
- Fails with negative numbers  
- Prefix sum works for all integers  

### Complexity
- **Time:** `O(n)`  
- **Space:** `O(n)`  

### Interview Trigger
> Subarray sum + negatives → **Prefix Sum + Hash Map**


---
### Intersection of Two Arrays – (LeetCode 349)

**Pattern:** Hash Set  

**Approach:**
- Convert both arrays to sets to remove duplicates
- Iterate over the smaller set
- Check membership in the other set

**Why Hash Set?**
- Constant-time lookup `O(1)`
- Eliminates duplicate elements automatically

**Complexity:**
- **Time:** `O(n + m)`
- **Space:** `O(n + m)`

**Interview Trigger:**
> Unique intersection → **Set / Hashing**
