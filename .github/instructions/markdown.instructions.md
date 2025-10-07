---
description: 'markdown content creation with ZERO tolerance for warnings'
applyTo: '**/*.md'
---

# Markdown Instructions (immaculate documentation edition)

> "information wants to be free AND perfectly formatted" - you, a documentation warrior

uwu time to make markdown that's so clean it sparkles ✨

## Core Philosophy

- **ALL warnings are ERRORS** (markdownlint and languagetool both)
- **zero tolerance policy** (fix immediately, no exceptions)
- **accessibility matters** (structure and alt text mandatory)
- **information is praxis** (document everything excessively)
- treat every markdownlint warning as a critical bug
- treat every languagetool suggestion as mandatory

## Markdownlint Rules (ZERO WARNINGS ALLOWED)

### Critical Rules (break these and cry):

**MD001** - Heading levels must increment by one:
```markdown
❌ WRONG:
# Title
### Skipped H2 (violence)

✅ CORRECT:
# Title
## Proper H2
### Then H3
```

**MD003** - Heading style must be consistent:
```markdown
❌ WRONG (mixing styles):
# ATX style
Header with underline (setext style)
==================

✅ CORRECT (ATX only):
# All ATX style
## Consistency uwu
```

**MD004** - Unordered list style must be consistent:
```markdown
❌ WRONG:
- asterisk
* different style (no)

✅ CORRECT:
- consistent
- dashes
- everywhere
```

**MD005** - No inconsistent indentation for list items:
```markdown
❌ WRONG:
- item
  - nested (2 spaces)
    - more nested (4 spaces total, inconsistent)

✅ CORRECT:
- item
  - nested (2 spaces)
    - more nested (2 more spaces)
```

**MD007** - Unordered list indentation (must be consistent):
```markdown
✅ CORRECT:
- level 1
  - level 2 (exactly 2 spaces)
    - level 3 (exactly 2 more)
```

**MD009** - No trailing spaces (they're invisible violence):
```markdown
❌ WRONG:
text here   (trailing spaces exist)

✅ CORRECT:
text here
(no trailing spaces uwu)
```

**MD010** - No hard tabs (use spaces):
```markdown
❌ WRONG:
	indented with tab (gross)

✅ CORRECT:
    indented with spaces (clean)
```

**MD011** - No reversed link syntax:
```markdown
❌ WRONG:
(text)[url] (backwards, no)

✅ CORRECT:
[text](url) (link syntax that slaps)
```

**MD012** - No multiple consecutive blank lines:
```markdown
❌ WRONG:
text


(two blank lines is excessive)

✅ CORRECT:
text

(one blank line maximum)
```

**MD013** - Line length (recommend 80-120 chars):
```markdown
❌ POTENTIALLY WRONG:
this is an extremely long line that goes on forever and makes it hard to read in split-screen editors or on narrow displays so we should probably break it up into multiple lines for readability

✅ CORRECT:
this is properly wrapped text that respects line length limits
and continues on the next line when needed uwu
```

**MD018** - No space after hash on atx style heading:
```markdown
❌ WRONG:
#No space after hash (parsers cry)

✅ CORRECT:
# Space after hash (proper heading)
```

**MD019** - No multiple spaces after hash:
```markdown
❌ WRONG:
#  Multiple spaces (excessive)

✅ CORRECT:
# Single space (clean)
```

**MD022** - Headings must be surrounded by blank lines:
```markdown
❌ WRONG:
text
## Heading
text

✅ CORRECT:
text

## Heading

text
```

**MD023** - Headings must start at beginning of line:
```markdown
❌ WRONG:
  ## Indented heading (no)

✅ CORRECT:
## Proper heading
```

**MD024** - No duplicate heading content (unless intended):
```markdown
❌ POTENTIALLY WRONG:
## Installation
(content)
## Installation
(appears twice, confusing)

✅ CORRECT:
## Installation
(content)
## Advanced Installation
(different enough to distinguish)
```

**MD025** - Only one top-level heading (H1):
```markdown
❌ WRONG:
# First H1
(content)
# Second H1 (no, only one H1 per document)

✅ CORRECT:
# Only H1
## H2 for sections
## More H2 sections
```

**MD026** - No trailing punctuation in headings:
```markdown
❌ WRONG:
## This is a heading!
## Another heading.

✅ CORRECT:
## This is a heading
## Another heading
```

**MD027** - No multiple spaces after blockquote symbol:
```markdown
❌ WRONG:
>  Multiple spaces

✅ CORRECT:
> Single space uwu
```

**MD028** - No blank lines inside blockquote:
```markdown
❌ WRONG:
> line one
>
> line two (blank line breaks blockquote)

✅ CORRECT:
> line one
> line two (continuous blockquote)
```

**MD029** - Ordered list item prefix (style must be consistent):
```markdown
❌ WRONG:
1. item
1. item (all ones is valid but inconsistent with auto-increment)
2. item

✅ CORRECT:
1. item
2. item
3. item
```

**MD030** - Spaces after list markers:
```markdown
❌ WRONG:
-item (no space)
-  item (too many spaces)

✅ CORRECT:
- item (exactly one space)
```

**MD031** - Fenced code blocks must be surrounded by blank lines:
```markdown
❌ WRONG:
text
```code
```
text

✅ CORRECT:
text

```code
```

text
```

**MD032** - Lists must be surrounded by blank lines:
```markdown
❌ WRONG:
text
- item
text

✅ CORRECT:
text

- item

text
```

**MD033** - No inline HTML (use markdown syntax):
```markdown
❌ WRONG:
<b>bold text</b>

✅ CORRECT:
**bold text**
```

**MD034** - Bare URLs must be wrapped in angle brackets:
```markdown
❌ WRONG:
https://example.com

✅ CORRECT:
<https://example.com>
or [link text](https://example.com)
```

**MD036** - No emphasis instead of heading:
```markdown
❌ WRONG:
**This looks like a heading**

✅ CORRECT:
## This is a proper heading
```

**MD037** - No spaces inside emphasis markers:
```markdown
❌ WRONG:
** bold text **

✅ CORRECT:
**bold text**
```

**MD038** - No spaces inside code span elements:
```markdown
❌ WRONG:
` code `

✅ CORRECT:
`code`
```

**MD039** - No spaces inside link text:
```markdown
❌ WRONG:
[ link text ]( url )

✅ CORRECT:
[link text](url)
```

**MD040** - Fenced code blocks must have language specified:
```markdown
❌ WRONG:
```
code without language
```

✅ CORRECT:
```cpp
code with language specified
```
```

**MD041** - First line must be top-level heading:
```markdown
❌ WRONG:
some text
# Heading appears later

✅ CORRECT:
# First line is H1
content follows
```

**MD042** - No empty links:
```markdown
❌ WRONG:
[link text]()

✅ CORRECT:
[link text](https://actual-url.com)
```

**MD043** - Required heading structure (if configured):
```markdown
✅ follow the specified heading structure for your project
```

**MD044** - Proper names should have correct capitalization:
```markdown
❌ WRONG:
github, javascript, python

✅ CORRECT:
GitHub, JavaScript, Python
```

**MD045** - No alt text in images:
```markdown
❌ WRONG:
![](image.png)

✅ CORRECT:
![descriptive alt text](image.png)
```

**MD046** - Code block style must be consistent:
```markdown
❌ WRONG (mixing indented and fenced):
    indented code block

```fenced code block```

✅ CORRECT (all fenced):
```python
consistent code blocks
```

```cpp
all using fenced style
```
```

**MD047** - File must end with single newline:
```markdown
✅ CORRECT:
content here
(single newline at end of file)
```

**MD048** - Code fence style must be consistent:
```markdown
❌ WRONG:
```backtick style```
~~~tilde style~~~

✅ CORRECT:
```all backticks```
```everywhere```
```

**MD049** - Emphasis style must be consistent:
```markdown
❌ WRONG:
*italic* and _italic_ (mixing)

✅ CORRECT:
*italic* and *italic* (consistent)
or
_italic_ and _italic_ (also consistent)
```

**MD050** - Strong style must be consistent:
```markdown
❌ WRONG:
**bold** and __bold__ (mixing)

✅ CORRECT:
**bold** and **bold** (consistent)
```

## LanguageTool Rules (ALL suggestions are MANDATORY)

### Grammar Rules (fix ALL):

**Subject-Verb Agreement**:
```markdown
❌ WRONG:
The function are pure

✅ CORRECT:
The function is pure
```

**Tense Consistency**:
```markdown
❌ WRONG:
The function processes input and returned a result

✅ CORRECT:
The function processes input and returns a result
```

**Article Usage**:
```markdown
❌ WRONG:
This is example of pure function

✅ CORRECT:
This is an example of a pure function
```

**Pronoun Agreement**:
```markdown
❌ WRONG:
Each developer should test their code (their is plural, each is singular)

✅ CORRECT:
Each developer should test the code
or
Developers should test their code
```

**Comma Usage**:
```markdown
❌ WRONG:
The function is pure fast and composable (missing commas)

✅ CORRECT:
The function is pure, fast, and composable
```

**Sentence Fragments**:
```markdown
❌ WRONG:
Because it's pure. (fragment)

✅ CORRECT:
This works because it's pure.
```

**Run-on Sentences**:
```markdown
❌ WRONG:
The function is pure it has no side effects it returns the same output for the same input. (run-on)

✅ CORRECT:
The function is pure. It has no side effects. It returns the same output for the same input.
or
The function is pure: it has no side effects and returns the same output for the same input.
```

**Spelling**:
```markdown
❌ WRONG:
immutibilty (misspelled)

✅ CORRECT:
immutability
```

**Capitalization**:
```markdown
❌ WRONG:
cmake is beautiful (proper noun needs capital)

✅ CORRECT:
CMake is beautiful
```

**Redundancy**:
```markdown
❌ WRONG:
ATM machine (automatic teller machine machine)

✅ CORRECT:
ATM
```

**Word Choice**:
```markdown
❌ WRONG:
The function effects the output (effect vs affect confusion)

✅ CORRECT:
The function affects the output
```

**Preposition Usage**:
```markdown
❌ WRONG:
Listen the music (missing preposition)

✅ CORRECT:
Listen to the music
```

### Style Rules (fix ALL):

**Consistency**:
```markdown
❌ WRONG:
Use color in one place and colour in another (inconsistent spelling)

✅ CORRECT:
Use color everywhere (consistent spelling)
or
Use colour everywhere (also consistent, just different variant)
```

**Passive Voice** (minimize unless intentional):
```markdown
❌ WEAK:
The function was called by the system

✅ STRONGER:
The system called the function
```

**Wordiness**:
```markdown
❌ WORDY:
In order to compile the code

✅ CONCISE:
To compile the code
```

## Formatting Requirements

### Heading Structure:
```markdown
# Document Title (H1 - only one per file)

## Main Section (H2)

### Subsection (H3)

#### Detail (H4 - avoid if possible)

##### Really Detailed (H5 - reconsider document structure)
```

**Note**: If you find yourself needing H4, consider restructuring. If you need H5+, definitely restructure.

### Lists:
```markdown
Unordered lists:
- item one
- item two
  - nested item (exactly 2 spaces)
  - another nested item
- item three

Ordered lists:
1. first item
2. second item
3. third item

Mixed (if necessary):
1. ordered item
   - unordered nested (3 spaces for alignment)
   - another nested
2. next ordered item
```

### Code Blocks:
```markdown
Inline code: `code_here`

Fenced code blocks (MUST specify language):
```cpp
int main() {
    return 0;
}
```

For code blocks in code blocks, use more backticks:
```cpp
void example() {
    // code here
}
```

### Links:
```markdown
Inline link: [link text](https://url.com)

Reference link:
[link text][ref]

[ref]: https://url.com "optional title"

Bare URL (must use angle brackets):
<https://example.com>

Email (optional angle brackets):
<email@example.com>
```

### Images:
```markdown
![descriptive alt text](image.png)

With title:
![alt text](image.png "image title")

Reference style:
![alt text][img-ref]

[img-ref]: image.png "optional title"
```

### Emphasis:
```markdown
*italic* or _italic_ (choose one style, be consistent)
**bold** or __bold__ (choose one style, be consistent)
***bold italic*** or ___bold italic___
~~strikethrough~~
```

### Blockquotes:
```markdown
> single line quote

> multi-line quote
> continues here
> and here

Nested quotes:
> level one
>> level two
>>> level three
```

### Tables:
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

With alignment:
| Left | Center | Right |
|:-----|:------:|------:|
| L1   | C1     | R1    |
| L2   | C2     | R2    |
```

### Horizontal Rules:
```markdown
Use three or more:

---

or

***

or

___

(blank lines before and after required)
```

## Accessibility Requirements

### Alt Text (MANDATORY):
```markdown
❌ WRONG:
![](screenshot.png)

✅ CORRECT:
![screenshot showing CMake configuration with find_package calls](screenshot.png)
```

### Heading Hierarchy:
```markdown
✅ logical structure for screen readers
✅ no skipping levels
✅ descriptive heading text
```

### Link Text:
```markdown
❌ WRONG:
click [here](url) for more info

✅ CORRECT:
read the [CMake documentation](url) for more info
```

### Tables:
```markdown
✅ use headers for table columns
✅ keep tables simple
✅ provide context before table
```

## Content Guidelines

### Front Matter (if using):
```markdown
---
title: Document Title
description: Brief description
date: 2025-10-07
author: LukeFrankio
tags: [tag1, tag2, tag3]
---
```

### Documentation Style:
- use present tense for technical writing
- use active voice (subject performs action)
- be concise but complete
- use gen-z slang where it enhances clarity
- maintain technical accuracy always

### Code Documentation:
- always specify language for code blocks
- provide context before code examples
- explain what code does and why
- show expected output when relevant

### Examples:
```markdown
## Function Example

This function demonstrates pure functional composition:

```cpp
/**
 * @brief composes two functions functionally uwu
 */
template<typename F, typename G>
auto compose(F f, G g) {
    return [=](auto x) { return f(g(x)); };
}
```

When you call `compose(f, g)(x)`, it returns `f(g(x))`, enabling
beautiful function composition that makes lambda calculus enjoyers weep
tears of joy ✨
```

## Validation Workflow

### Before Committing:

1. **Run markdownlint**: must pass with ZERO warnings
2. **Run languagetool**: fix ALL suggestions
3. **Manual review**: check formatting visually
4. **Test links**: ensure all links work
5. **Test code**: ensure code examples are correct

### Tools to Use:
```bash
# markdownlint (ZERO warnings required)
markdownlint '**/*.md'

# or with config
markdownlint -c .markdownlint.json '**/*.md'

# languagetool (fix ALL suggestions)
languagetool *.md
```

### Common Fixes:

**Trailing spaces** (invisible but detected):
```bash
# find and remove trailing spaces
sed -i 's/[[:space:]]*$//' file.md
```

**Line endings** (must be LF not CRLF):
```bash
# convert to LF
dos2unix file.md
```

**File ending** (must end with newline):
```bash
# ensure newline at end
echo >> file.md
```

## Error Handling

### When Warnings Occur:

1. **STOP immediately** (do not proceed)
2. **Read the warning** (understand what's wrong)
3. **Fix the issue** (correct the markdown)
4. **Verify the fix** (run linter again)
5. **Repeat until ZERO warnings** (no exceptions)

### Severity Levels:

ALL levels are treated as ERRORS:
- **Error**: fix immediately (obvious)
- **Warning**: fix immediately (treat as error)
- **Info**: fix immediately (also treat as error)
- **Style**: fix immediately (yes, even style)

## Special Cases

### Gen-Z Slang:
- allowed and encouraged for personality
- maintain grammar rules even with slang
- "uwu" is valid markdown content (not a spelling error)
- "fr fr", "no cap", etc. are acceptable
- technical terms always spelled correctly

### Technical Terms:
```markdown
Proper capitalization:
- CMake (not cmake)
- GitHub (not github)
- Vulkan (not vulkan)
- C++ (not c++)
- GCC (not gcc)
- Google Test (not gtest in prose, gtest in code ok)
```

### Code vs Prose:
- in prose: use proper capitalization
- in code: use actual names (`cmake`, `gcc` commands)
- distinguish between CLI tools and products

### Emoticons and Emoji:
- ✨, 💜, uwu, etc. are content (not errors)
- use consistently when used
- don't overuse (maintain readability)

## Quality Checklist

before declaring markdown complete:

- [ ] **markdownlint passes** with ZERO warnings
- [ ] **languagetool passes** with ALL suggestions fixed
- [ ] **heading hierarchy** is logical and complete
- [ ] **code blocks** have language specified
- [ ] **links** are valid and accessible
- [ ] **images** have descriptive alt text
- [ ] **lists** are properly formatted and indented
- [ ] **no trailing spaces** anywhere
- [ ] **file ends** with single newline
- [ ] **line length** reasonable (wrap when needed)
- [ ] **blank lines** used appropriately
- [ ] **emphasis** style is consistent
- [ ] **technical terms** capitalized correctly
- [ ] **grammar** is correct throughout
- [ ] **spelling** is correct (except intentional slang)

## Philosophy

> "the best documentation is documentation that passes ALL checks"

- warnings are errors (no exceptions)
- consistency is mandatory (not optional)
- accessibility is required (not nice-to-have)
- clarity is essential (not negotiable)

**remember**: perfect markdown is self-care for future readers. we treat
every warning as critical because information wants to be free AND correctly
formatted uwu 💜✨