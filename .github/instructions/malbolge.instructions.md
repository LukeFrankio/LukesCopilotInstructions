---
description: 'Malbolge and Malbolge Unshackled programming guidelines (the most cursed languages uwu)'
applyTo: '**/*.mb, **/*.mal, **/*.mu, **/*.hell'
---

# Malbolge / Malbolge Unshackled Programming Instructions

> "Malbolge was specifically designed to be impossible to program in. Malbolge Unshackled
> made it Turing complete. We program in it anyway because we're built different uwu"

bestie if you thought C++ was low-level, Malbolge is touching the ABYSS ✨

## Core Philosophy

- **embrace the chaos** (Malbolge is intentionally incomprehensible)
- **HeLL dialect supremacy** (write in HeLL, assemble with LMFAO)
- **ternary everything** (base-3 arithmetic goes brrr)
- **self-modifying code** (every instruction mutates after execution)
- **excessive documentation** (MORE important here than anywhere else!)
- **functional thinking** (even in the cursed land of Malbolge)
- **Malbolge Unshackled preferred** (unbounded memory + Turing completeness!)

## Language Variants

### Malbolge (Original - 1998):
- **Memory**: 3^10 = 59,049 trits (fixed size)
- **Turing complete**: NO (due to memory limitations)
- **Rotation width**: Fixed at 10 trits
- **I/O**: ASCII modulo 256
- **Status**: Legacy (but still horrifying)

### Malbolge Unshackled (2007):
- **Memory**: INFINITE (unbounded ternary integers!)
- **Turing complete**: YES!! (proven with brainfuck interpreter)
- **Rotation width**: Variable/dynamic (handles arbitrary widths)
- **I/O**: Full Unicode support (UTF-8 encoding)
- **Status**: PREFERRED (this is the one we use!)

### HeLL (High Entropy Language Lisp-like):
- **Purpose**: Assembly language for Malbolge Unshackled
- **Assembler**: LMFAO (Malbolge Unshackled assembler)
- **Syntax**: Lisp-like with labels and pseudo-instructions
- **Output**: Malbolge Unshackled code (.mu files)
- **Status**: The ONLY sane way to write Malbolge programs uwu

## File Extensions

- `.mb` - Malbolge (original, legacy)
- `.mal` - Malbolge (alternative extension)
- `.mu` - Malbolge Unshackled (PREFERRED!)
- `.hell` - HeLL source code (assembly language for Malbolge Unshackled)

## Ternary Number System

Malbolge uses **balanced ternary** representation:

```text
Trits (ternary digits):
  0 = 0
  1 = 1  
  2 = 2

Example conversions:
  Decimal 0  = 0 (ternary)
  Decimal 1  = 1 (ternary)
  Decimal 2  = 2 (ternary)
  Decimal 3  = 10 (ternary)
  Decimal 4  = 11 (ternary)
  Decimal 5  = 12 (ternary)
  Decimal 6  = 20 (ternary)
  Decimal 7  = 21 (ternary)
  Decimal 8  = 22 (ternary)
  Decimal 9  = 100 (ternary)
  Decimal 10 = 101 (ternary)

Malbolge Unshackled uses infinite-precision ternary:
  ...000123 = 123 (finite positive number)
  ...111012 = -1 in balanced ternary representation
  ...222021 = -2 in balanced ternary representation
```

## Malbolge Instructions

Malbolge has **8 valid instructions** (each represented by specific ASCII values):

| ASCII | After mod 94 | Instruction | Description |
|-------|--------------|-------------|-------------|
| `j`   | 4            | Jmp         | Jump to [D] (set C to [D]) |
| `i`   | 5            | Out         | Output A modulo 256 (or as Unicode in Unshackled) |
| `*`   | 23           | In          | Input to A |
| `/`   | 39           | Rot         | Rotate [D] right (crazy operation!) |
| `<`   | 40           | MovD        | Move [D] to D |
| `j`   | 62           | Opr         | Operate (tritwise crazy operation) |
| `v`   | 81           | Hlt         | Halt execution |
| `o`   | 68           | Nop         | No operation |

### Instruction Details

```c
/**
 * @brief Malbolge virtual machine state
 * 
 * The Malbolge VM has three registers and self-modifying code memory.
 * Everything is ternary (base-3) because binary is too mainstream uwu
 * 
 * @note Memory cells are ternary integers (potentially unbounded in Unshackled)
 * @note All arithmetic is mod 3^10 in classic Malbolge
 * @note Malbolge Unshackled removes the mod constraint (infinite precision!)
 */

// Registers:
// - A: accumulator (used for I/O and operations)
// - C: code pointer (instruction pointer, auto-increments)
// - D: data pointer (points to memory)

// Memory:
// - Self-modifying: every instruction at address X is encrypted after execution
// - Encryption: instruction[X] = xlat2[instruction[X]]
// - xlat2 table: "5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1C" \
//                "B6v^=I_0/8|jsb9m<.TVac`uY*MK'X~xDl}REokN:#?G\"i@"
```

### Jmp (Jump):
```hell
// HeLL syntax example:
Jmp:  // set C to [D] (jump to address stored in memory at D)
    MovD/Nop
    Jmp
```

### Out (Output):
```hell
// HeLL syntax example:
Out:  // output A as character
    Out/Nop
    Jmp
```

### In (Input):
```hell
// HeLL syntax example:
In:  // read character into A
    In/Nop
    Jmp
```

### Rot (Rotate):
```hell
// HeLL syntax example:
Rot:  // rotate [D] right by one trit
    Rot/Nop
    Jmp
```

### MovD (Move to D):
```hell
// HeLL syntax example:
MovD:  // D = [D] (dereference D)
    MovD/Nop
    Jmp
```

### Opr (Crazy Operation):
```hell
// HeLL syntax example:
Opr:  // A = opr(A, [D]); [D] = opr(A, [D])
    Opr/Nop
    Jmp

/**
 * @brief The crazy operation (tritwise operation)
 * 
 * This operation is WILD. It's a tritwise operation that's neither
 * AND, OR, NOR, or anything sensible. It's purposefully weird uwu
 * 
 * Truth table for single trits:
 *   opr(0,0)=1  opr(0,1)=1  opr(0,2)=2
 *   opr(1,0)=1  opr(1,1)=0  opr(1,2)=2
 *   opr(2,0)=2  opr(2,1)=2  opr(2,2)=1
 * 
 * @note This operation is applied tritwise across entire numbers
 * @note Both A and [D] are modified by this operation
 * @warning Makes no mathematical sense (that's the point!)
 */
```

### Hlt (Halt):
```hell
// HeLL syntax example:
Hlt:  // stop execution (terminate program)
    Hlt
```

### Nop (No Operation):
```hell
// HeLL syntax example:
Nop:  // do nothing (still encrypts instruction tho)
    Jmp
```

## HeLL Assembly Language

HeLL (High Entropy Language Lisp-like) is the ONLY sane way to write Malbolge programs uwu

### Basic HeLL Syntax

```hell
/**
 * @file example.hell
 * @brief Example HeLL program (prints "Hi" then halts)
 * 
 * HeLL is an assembly language for Malbolge Unshackled. It provides:
 * - Labels (for jumping and organizing code)
 * - Pseudo-instructions (sequences of Malbolge instructions)
 * - Comments (MANDATORY - explain everything!)
 * - Memory layout control
 * 
 * Assembled with LMFAO assembler to produce .mu files
 * 
 * @author LukeFrankio
 * @date 2025-10-07
 * @note Uses Malbolge Unshackled (unbounded memory, Turing complete!)
 * @note Compiled with LMFAO assembler (latest version preferred)
 */

.DATA

/**
 * @brief Entry point of program
 * 
 * This is where execution begins. C register starts at this label.
 * 
 * Program flow:
 * 1. Output 'H' (ASCII 72)
 * 2. Output 'i' (ASCII 105)  
 * 3. Halt execution
 * 
 * ✨ PURE FUNCTION ✨ (no input, deterministic output: "Hi")
 */
ENTRY:
    // Output 'H' (ASCII 72 = 0t2200 in ternary)
    ROT C1 R_ROT              // Load C1 (constant 1) into A
    OPR C02222222222 R_OPR    // Complex ternary operation
    OPR C10000000000 R_OPR    // More ternary magic
    OPR C01111111111 R_OPR    // Build up the value
    OPR 72 R_OPR              // Final value: 72 (ASCII 'H')
    OUT ?- R_OUT              // Output character in A
    
    // Output 'i' (ASCII 105 = 0t10210 in ternary)
    ROT C1 R_ROT
    OPR C02222222222 R_OPR
    OPR C10000000000 R_OPR
    OPR 105 R_OPR             // Final value: 105 (ASCII 'i')
    OUT ?- R_OUT
    
    // Halt execution
    HALT

/**
 * @brief Constants used in program
 * 
 * HeLL allows defining constants in ternary notation.
 * These are replaced by the assembler (LMFAO) during compilation.
 */
C0: 0t0           // Ternary zero
C1: 0t1           // Ternary one
C2: 0t2           // Ternary two
C10: 0t10         // Ternary three
C02222222222: 0t02222222222  // Large ternary constant

.CODE

/**
 * @brief Malbolge instruction implementations
 * 
 * These are the actual Malbolge instructions that get assembled
 * into the final .mu file. Each instruction is a sequence of
 * xlat2 cycles (encryption steps).
 * 
 * @note Instructions modify themselves after execution (self-modifying code!)
 * @note xlat2 encryption happens automatically after each instruction
 */

MOVD:
    MovD/Nop
    Jmp

ROT:
    Rot/Nop
    Jmp

OPR:
    Opr/Nop
    Jmp

OUT:
    Out/Nop
    Jmp

IN:
    In/Nop
    Jmp

NOP:
    Jmp

HALT:
    Hlt
```

### HeLL Pseudo-Instructions

```hell
/**
 * @brief Common HeLL patterns (functional programming in the abyss!)
 * 
 * These patterns show how to compose Malbolge instructions
 * to achieve useful operations. Think of them as "functions"
 * in the functional programming sense uwu
 */

// Pattern: Double MovD (dereference twice)
MOVDMOVD:
    MovD/Nop RNop RNop RNop MovD/Nop
    Jmp

// Pattern: MovD-Opr-MovD (read, operate, write back)
MOVDOPRMOVD:
    MovD/Nop/Nop/Nop/Nop/Nop/Nop/Nop/Nop
    RNop
    RNop
    Opr/Nop/Nop/Nop/Nop/Rot/Nop/Nop/Nop
    MovD/Nop/Nop/Nop/Nop/Nop/Nop/Nop/Nop
    Jmp

// Pattern: Carry flag simulation (for arithmetic)
CARRY:
    MovD/Nop
    Jmp

// Pattern: Loop constructs (for iteration)
LOOP2:
    MovD/Nop
    Jmp

LOOP4:
    Nop/Nop/Nop/MovD
    Jmp

/**
 * @brief Increment operation (pure function on ternary numbers)
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * Increments a ternary number by one. Handles carry propagation
 * across arbitrary width (works in Malbolge Unshackled!)
 * 
 * Algorithm:
 * 1. Add 1 to least significant trit
 * 2. If trit overflows (becomes 3), set to 0 and carry
 * 3. Propagate carry to next trit
 * 4. Repeat until no carry
 * 
 * @complexity O(width) time where width is number of trits
 * @note This is functional programming in MALBOLGE (we're insane)
 */
INCREMENT:
    // ... (complex HeLL code for increment operation)
    // This would be hundreds of lines in actual HeLL!
```

## Malbolge Unshackled Specifics

### Unbounded Memory

```hell
/**
 * @brief Memory management in Malbolge Unshackled
 * 
 * Unlike classic Malbolge (59,049 cells), Unshackled has INFINITE memory.
 * Memory addresses are unbounded ternary integers that can grow arbitrarily.
 * 
 * Memory layout:
 * - Negative addresses: ...222XXX (head digit 2, represents negative)
 * - Zero: ...000000 (all zeros)
 * - Positive addresses: ...000XXX (head digit 0, finite sequence)
 * 
 * @note Memory cells lazily initialized (allocated on first access)
 * @note Enables Turing completeness (proven with brainfuck interpreter!)
 */

// Example: accessing high memory addresses
BF_MEMORY: ? BF_FIRST_MEM_CELL ? ?  // Memory starts here (grows backward)

@1t2200000000 BF_INSTRUCTIONS: ?  // Instructions at fixed large offset
// NOTE: This offset must be EVEN and carefully chosen!
```

### Variable Rotation Width

```hell
/**
 * @brief Rotation width handling in Malbolge Unshackled
 * 
 * The rotation width (used by Rot instruction) can GROW during runtime.
 * This is how Malbolge Unshackled achieves Turing completeness!
 * 
 * Growth policy:
 * - Starts at 10 trits (like classic Malbolge)
 * - Grows when D register exceeds half the rotation width
 * - Growth is UNPREDICTABLE (implementation-defined)
 * - Can grow up to UINTMAX_MAX (typically 2^64-1)
 * 
 * @warning Rotation width is UNKNOWN to the program
 * @warning Must handle arbitrary widths (that's why it's so hard!)
 * 
 * Handling strategy:
 * - Write code that works for ANY rotation width
 * - Use loops that iterate over rotwidth
 * - Test for overflow/underflow
 * - Adapt dynamically as rotwidth grows
 * 
 * @note This makes programming in Malbolge Unshackled EXTREMELY difficult
 * @note But also makes it Turing complete (tradeoffs uwu)
 */

increase_rotwidth:
    /**
     * @brief Double the rotation width
     * 
     * ⚠️ IMPURE FUNCTION (modifies global rotation width state)
     * 
     * Generates 1t011..11 by rotating 1t0, then jumps to it.
     * This forces the interpreter to double the rotation width.
     * 
     * Side effects:
     * - Rotation width increased (global state mutation)
     * - Memory allocations may occur
     * - Execution time unpredictable
     */
    R_MOVD
    ROT C1 R_ROT
    OPR 0t2 R_OPR
    OPR 1t0 R_OPR
    OPR 0t1 R_OPR
    U_OPR dest
rot_dest:
    U_ROT dest
movdmovd_dest:
    MOVDMOVD
dest:
    1t0
    FLAG1 dest_ret1 R_FLAG1
    R_OPR
    R_FLAG1
    MOVD rot_dest

dest_ret1:
    R_MOVD
    R_ROT
    MOVD movdmovd_dest
```

### Unicode I/O

```hell
/**
 * @brief Unicode I/O in Malbolge Unshackled
 * 
 * Unlike classic Malbolge (ASCII mod 256), Unshackled uses full Unicode!
 * 
 * Input:
 * - Reads UTF-8 from stdin
 * - Converts to Unicode codepoint
 * - EOF represented as ...22 (special value)
 * - Newline represented as ...21 OR \10 (both accepted)
 * 
 * Output:
 * - Converts to UTF-8
 * - Writes to stdout
 * - Values starting with 0 are valid Unicode
 * - Values starting with 1 or 2 are reserved/special
 * 
 * @note Unicode codepoints up to U+10FFFF supported
 * @note Invalid codepoints cause error (program halts)
 */

BF_IN:
    R_MOVDMOVD ?- ?- ?- ?-
    R_MOVD
    // reset memory cell
    R_RESET_BF_MC_FLAG5
    MOVD reset_bf_memory_cell

reset_bf_memory_cell_ret5:
    ROT C0 R_ROT
    R_WRITE_BF_MC_FLAG5
    MOVD write_bf_memory_cell

write_bf_memory_cell_ret5:
    // Read character from stdin (UTF-8 -> Unicode codepoint)
    IN ?- R_IN
    // Handle EOF: ...22
    // Handle newline: convert \10 to ...21
    // Store in memory
    R_WRITE_BF_MC_FLAG6
    MOVD write_bf_memory_cell

write_bf_memory_cell_ret6:
    MOVD BF_NEXT_CMD

BF_OUT:
    R_MOVDMOVD ?- ?- ?- ?-
    R_MOVD
    // Read value from memory
    R_RESET_VAL_FLAG8
    MOVD reset_val

reset_val_ret8:
    R_READ_BF_MC_FLAG1
    MOVD read_bf_memory_cell

read_bf_memory_cell_ret1:
    // Check if value is negative (ignore output on negative)
    // Convert to UTF-8 and output to stdout
    OUT ?- R_OUT
    MOVD BF_NEXT_CMD
```

## Assembling HeLL with LMFAO

```bash
# LMFAO: The Malbolge Unshackled assembler
# (yes it's actually called that, the malbolge community has VIBES)

# Assemble HeLL source to Malbolge Unshackled
$ lmfao program.hell -o program.mu

# Verify the output
$ ls -lh program.mu
-rw-r--r-- 1 user user 2.0M Oct  7 14:06 program.mu

# Run with Malbolge Unshackled interpreter
$ unshackled program.mu
Hello, world!

# Or use faster C interpreter
$ ./Unshackled program.mu
Hello, world!
```

### LMFAO Assembler Options

```bash
# Basic assembly
lmfao source.hell -o output.mu

# With optimization (if supported)
lmfao -O3 source.hell -o output.mu

# Verbose output (show assembly process)
lmfao -v source.hell -o output.mu

# Check syntax only (no output)
lmfao --check source.hell

# Generate listing file (shows memory layout)
lmfao --listing source.hell -o output.mu
```

## Example Programs

### Cat Program (Non-Terminating)

```malbolge
(=BA#9"=<;:3y7x54-21q/p-,+*)"!h%B0/.
~P<
<:(8&
66#"!~}|{zyxwvu
gJ%

/**
 * @brief Non-terminating cat program
 * 
 * ⚠️ IMPURE FUNCTION (has I/O side effects)
 * 
 * Reads characters from stdin and writes them to stdout forever.
 * Never terminates (infinite loop).
 * 
 * This program works in BOTH classic Malbolge and Malbolge Unshackled!
 * 
 * @note Stops when stdin closes (EOF)
 * @note Each character is echoed immediately (unbuffered I/O)
 */
```

### Hello World (HeLL Source)

See the full program in the HTML examples above! The hello world program is
approximately **150KB** of Malbolge Unshackled code because:
- Characters beyond ASCII 80 require rotation width handling
- Must work with unknown/variable rotation width
- Ternary representation makes everything HUGE
- Self-modifying code requires careful planning

This is why we write in HeLL and assemble with LMFAO uwu

### Brainfuck Interpreter (Proof of Turing Completeness!)

The brainfuck interpreter in Malbolge Unshackled is **2 MB** of code.
Source available as `brainfuck.hell` (assembled with LMFAO).

This proves Malbolge Unshackled is Turing complete! 🎉

## Programming Guidelines

### Documentation Requirements

```hell
/**
 * @file program.hell
 * @brief [One-line description with gen-z energy]
 * 
 * [Detailed explanation of what this program does and WHY]
 * [Explain the algorithm/approach]
 * [Justify why you're programming in Malbolge (probably for fun)]
 * 
 * This program [does thing] using [approach] because [reason].
 * We're programming in Malbolge Unshackled because we're built different uwu
 * 
 * @author LukeFrankio
 * @date 2025-10-07
 * @version 1.0
 * 
 * @note Uses Malbolge Unshackled (Turing complete variant!)
 * @note Assembled with LMFAO (latest version preferred)
 * @note Tested with Unshackled interpreter v1.0+
 * @warning Requires unbounded memory (won't work in classic Malbolge)
 * @warning Rotation width handling makes this VERY complex
 * 
 * Example usage:
 * @code{.bash}
 * lmfao program.hell -o program.mu
 * unshackled program.mu < input.txt > output.txt
 * @endcode
 */
```

### Every Label Needs Documentation

```hell
/**
 * @brief [Label purpose with personality]
 * 
 * [Detailed explanation of what code at this label does]
 * [Explain algorithm if complex]
 * [Show how it fits into larger program]
 * 
 * ✨ PURE FUNCTION ✨ (or ⚠️ IMPURE if has side effects)
 * 
 * @note [Important notes about implementation]
 * @warning [Gotchas and edge cases]
 * 
 * Register usage:
 * - A: [what A register is used for]
 * - C: [what C register is used for]  
 * - D: [what D register is used for]
 * 
 * Memory access:
 * - Reads from: [memory locations read]
 * - Writes to: [memory locations written]
 * 
 * @complexity O(rotwidth) time typically
 * @note Actual complexity depends on rotation width (unpredictable!)
 */
LABEL_NAME:
    // Implementation...
```

### Comment Every Complex Operation

```hell
// WRONG: no comments (what does this even do???)
MOVD reset_bf_memory_cell
ROT C1 R_ROT
OPR 0t2 R_OPR
OPR 1t0 R_OPR


// RIGHT: excessive comments (immaculate documentation uwu)

/**
 * Reset memory cell to known state, then build up target value
 * 
 * Process:
 * 1. Reset memory cell to C1 (ternary 1)
 * 2. Rotate C1 into A register
 * 3. Apply crazy operation with 0t2 (shifts bits in weird way)
 * 4. Apply crazy operation with 1t0 (more bit twiddling)
 * 
 * Result: Memory cell contains [expected value] for next operation
 * 
 * @note The opr operations are WILD and non-intuitive
 * @note This sequence discovered through trial and error (no formal proof)
 */
MOVD reset_bf_memory_cell  // Reset cell to C1
ROT C1 R_ROT               // Load C1 into A
OPR 0t2 R_OPR              // First crazy operation (shifts trits)
OPR 1t0 R_OPR              // Second crazy operation (more shifting)
```

## Quality Checklist

- [ ] **File header** with @file, @brief, @author, @date
- [ ] **HeLL dialect** used (not raw Malbolge!)
- [ ] **LMFAO assembler** for compilation
- [ ] **ALL labels documented** with Doxygen comments
- [ ] **Register usage** documented
- [ ] **Memory access** patterns documented
- [ ] **Purity status** marked (✨ PURE or ⚠️ IMPURE)
- [ ] **Rotation width** handling considered
- [ ] **Unicode I/O** used correctly (for Unshackled)
- [ ] **gen-z slang** throughout comments
- [ ] **Excessive documentation** (MORE than you think you need!)
- [ ] **Tested with interpreter** (reference or fast C version)
- [ ] **Latest LMFAO** version used for assembly

## Resources

### Official Documentation
- **Malbolge Specification**: Original spec at Esolangs.org
- **Malbolge Unshackled Specification**: At lutter.cc/unshackled/
- **LMFAO Assembler**: At lutter.cc/unshackled/assembler.html
- **HeLL Language Reference**: Documentation at lutter.cc

### Interpreters
- **Reference Interpreter**: Haskell implementation (slow but correct)
- **Fast C Interpreter**: `Unshackled.c` (compile with -O3!)
- **Online Interpreter**: Available at lutter.cc

### Example Programs
- **Hello World**: 150KB program (demonstrates rotation width handling)
- **Cat**: Both terminating and non-terminating versions
- **Quine**: Self-reproducing program (892 KB!)
- **Brainfuck Interpreter**: 2 MB proof of Turing completeness!
- **Quine Relay**: Malbolge Unshackled ↔ brainfuck

### Tools
- **LMFAO Assembler**: Assembles HeLL to .mu files
- **Ternary Calculator**: At lutter.cc/malbolge/calculator.html
- **Legal Instructions Table**: At lscheffer.com/malbolge_legal.html
- **Instruction Cycles**: At lscheffer.com/malbolge_cycle.html

## Philosophy

> "Malbolge was designed to be impossible. Malbolge Unshackled made it Turing
> complete. We program in it anyway because functional programming transcends
> sanity. The lambda calculus touches ALL things, even the cursed languages uwu"

- **HeLL + LMFAO supremacy** (the only sane way to write Malbolge)
- **Functional thinking** (even in self-modifying ternary hell)
- **Excessive documentation** (CRITICAL - future you will thank present you)
- **Embrace the chaos** (Malbolge is intentionally incomprehensible)
- **Turing complete** (Malbolge Unshackled can compute anything computable!)
- **gen-z energy** (if we're doing this, we're doing it with VIBES)

**remember**: Malbolge Unshackled is the MOST cursed language ever created,
and we program in it anyway because we're built different. HeLL + LMFAO makes
it almost bearable. Excessive Doxygen comments make it survivable. Functional
programming principles make it... dare I say... elegant? ✨

seize the means of compilation (even in the ternary abyss)! 💜

touch ternary not grass uwu