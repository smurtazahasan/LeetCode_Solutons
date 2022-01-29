# [Python Solutions to LeetCode](https://leetcode.com/problemset/all/)

![Language](https://img.shields.io/badge/language-Python%20%20%20-blue.svg)&nbsp;
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)&nbsp;
![Update](https://img.shields.io/badge/update-daily-green.svg)&nbsp;
![Progress](https://img.shields.io/badge/progress-7%20%2F%202147-ff69b4.svg)&nbsp;

## Objective
* This repo is to help me reach my objective of completing majority of leetcode questions and using this as a way for myself and others to track my progress 📈
* Alongside leetcode, I'm also doing CodeSignal challenges ⚙️
* Python is the first language I'm doing these questions in but I hope to expand into other languages 🐍
* Lastly, each solution file has different ways of doing the same questions from brute force to more elegant methods 🔁

---

## Easy

|#|Difficulty|Name|Solution|Time/Space|Technique Used|
|---|:------:|-----|------|------|-----|
|13|`Easy`|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|[Python](./easy/13romantointeger.py)|**O(n)**/**O(1)**|1. Iterate backwards and multiply<br>2. Use replace() and iterate through<br>3. Check if prev value for smaller|
|20|`Easy`|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|[Python](./easy/20validparentheses.py)|1.**O(n^3)**/**O(1)**<br>2.**O(n)**/**O(1)**|1. Use .replace inside loop<br>2. Check against dictionary|
|121|`Easy`|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|[Python](./easy/121besttimetobuyandsellstock.py)|1.**O(n)**/**O(1)**<br>2.**O(n^2)**/**O(1)**|1. Kadane's Algorithm<br>2. Brute Force - Nested For Loop|
|217|`Easy`|[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)|[Python](./easy/217containsduplicate.py)|**O(n)**/**O(n)**|1. Dictionary and iterate <br>2. Set the array and compare lengths<br>3. Sort, Set and zip through array|
|268|`Easy`|[Missing Number](https://leetcode.com/problems/missing-number/)|[Python](./easy/268missingnumber.py)|1.**O(n)**/**O(n)**<br>2.**O(n)**/**O(1)**<br>3.**O(n)**/**O(1)**|1. Dictionary and lookup<br>2. Return if not in range<br>3. Sum of 0->n minus sum of nums|
|448|`Easy`|[Find All Numbers Disappeared](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)|[Python](./easy/448findallnumbersdisappeared.py)|**O(n)**/**O(n)**|1. if not in list, return<br>2. Use numpy to create a compare list<br>3. Set(list) and return difference|
|1507|`Easy`|[Reformat Date](https://leetcode.com/problems/reformat-date/)|[Python](./easy/1507reformatdate.py)|**O(n)**/**O(1)**|1. Dictionary and lookup date <br>2. Use .format and dictionary|



<!-- ---|``|[]()|[Python]()|**O()**|**O()**|----Note---| -->
