# Strings and Numbers Challenges

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../07-problem-solving-patterns/README.md) · [Module index](../README.md) · [Next →](../09-collections/README.md)
<!-- /chapter-navigation:top -->

Review literal character membership, indexing, integer division and remainder. For the medium palindrome challenge, reuse the two-pointer pattern, comparing symmetric positions rather than a pair sum.

Read the contract and linked prerequisite lessons, predict results, attempt the starter in a personal file, and check boundaries. Open hints progressively; compare the reference only after your attempt. No browser runner is provided.

### Variable window with last-seen positions

A fixed window always has the same length; a variable window can shrink or grow as its constraint changes. For unique characters, maintain an inclusive left boundary and scan right one character at a time. A dictionary remembers the last index of each character. If that index is at least left, the old occurrence must leave the window: move left to that index plus one. Otherwise leave left unchanged. The valid window length is right - left + 1. Track the best length. For "abba", after the second b the window starts at index 2; at the final a, its earlier index 0 is outside the window, so do not move left backwards. The maximum is 2. Under ordinary hashing assumptions this uses expected linear time and space proportional to distinct characters. The rule is specific to uniqueness, not a universal variable-window rule.

## Available challenges

- [Vowel Counter](../../exercises/problem-solving/vowel-counter/README.md) · Easy · 10 min
- [ASCII Digit Counter](../../exercises/problem-solving/ascii-digit-counter/README.md) · Easy · 10 min
- [Sum of Digits](../../exercises/problem-solving/sum-digits/README.md) · Easy · 12 min
- [Literal Palindrome](../../exercises/problem-solving/literal-palindrome/README.md) · Medium · 18 min

- [Longest Distinct Substring](../../exercises/problem-solving/longest-distinct-substring/README.md) · Hard · 35 min

<!-- chapter-navigation:bottom -->
[← Previous](../07-problem-solving-patterns/README.md) · [Module index](../README.md) · [Next →](../09-collections/README.md)
<!-- /chapter-navigation:bottom -->
