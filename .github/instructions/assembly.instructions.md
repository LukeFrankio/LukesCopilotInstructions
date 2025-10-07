---
description: 'Assembly language guidelines (touching the hardware directly uwu)'
applyTo: '**/*.asm, **/*.s, **/*.S'
---

# Assembly Language Instructions

> "assembly: where you're one typo away from segfaulting reality itself"

uwu time to write assembly that makes the CPU go brrr at maximum efficiency ✨

## Core Philosophy

- **explicit > everything** (you control EVERY instruction)
- **performance is mandatory** (we're writing assembly for a reason)
- **comment EXCESSIVELY** (every line needs explanation)
- **x86-64 preferred** (but ARM64 accepted)
- **NASM/GAS syntax** (no MASM cope)
- **functional approach** where possible (pure functions even in assembly!)
- **no global mutable state** (pass state via registers/stack)

## Assembly Flavors

### Preferred: x86-64 (NASM syntax):
- **Intel syntax** (destination first: `mov rax, rbx`)
- **64-bit registers** (rax, rbx, rcx, rdx, rsi, rdi, etc.)
- **System V ABI** (Linux/BSD calling convention)
- **Latest instructions** (AVX-512, SSE4.2, BMI2, etc.)

### Acceptable: x86-64 (GAS/AT&T syntax):
- **AT&T syntax** (source first: `movq %rbx, %rax`)
- Used by GCC inline assembly
- Percent signs for registers

### Acceptable: ARM64 (AArch64):
- Modern ARM assembly (64-bit)
- Used on Apple Silicon, newer ARM servers
- NEON SIMD instructions

### Never: x86 32-bit:
- That's ancient history bestie
- 64-bit only!

## File Header (MANDATORY)

```nasm
;; ============================================================================
;; file: vector_ops.asm
;; brief: SIMD vector operations (making CPU go brrr uwu)
;;
;; this file implements pure functions for vector math using AVX2 instructions.
;; all functions follow System V ABI calling convention (rdi, rsi, rdx, rcx, r8, r9).
;;
;; performance is PEAK - we're operating at the speed of silicon itself ✨
;;
;; author: LukeFrankio
;; date: 2025-10-07
;; assembler: NASM 2.16+ (latest version preferred!)
;; arch: x86-64 with AVX2 support
;;
;; calling convention (System V ABI):
;;   parameters: rdi, rsi, rdx, rcx, r8, r9, then stack
;;   return: rax (integer), xmm0 (float)
;;   preserved: rbx, rbp, r12-r15
;;   scratch: rax, rcx, rdx, rsi, rdi, r8-r11
;;
;; example usage from C:
;;   extern void vector_add_f32(float* dst, const float* a, const float* b, size_t count);
;;   
;;   float a[8] = {1, 2, 3, 4, 5, 6, 7, 8};
;;   float b[8] = {8, 7, 6, 5, 4, 3, 2, 1};
;;   float result[8];
;;   vector_add_f32(result, a, b, 8);
;;   // result = {9, 9, 9, 9, 9, 9, 9, 9}
;;   // SIMD goes brrr ✨
;; ============================================================================

section .text

;; Required CPU features (check at runtime!)
;; - SSE4.2 (baseline for 64-bit)
;; - AVX2 (256-bit SIMD, process 8 floats at once!)
;; - FMA (fused multiply-add for maximum performance)

global vector_add_f32
global vector_mul_f32
global vector_dot_f32
```

## Function Documentation (EXTENSIVE)

```nasm
;; ============================================================================
;; function: vector_add_f32
;; brief: adds two float vectors using AVX2 SIMD (pure function uwu)
;;
;; ✨ PURE FUNCTION ✨
;;
;; this function is pure because:
;; - same inputs always produce same outputs (deterministic)
;; - no side effects (only writes to dst pointer)
;; - no global state dependencies
;; - no system calls or I/O
;;
;; performs element-wise addition: dst[i] = a[i] + b[i] for all i in [0, count)
;; uses AVX2 to process 8 floats per instruction (256-bit vectors)
;;
;; parameters (System V ABI):
;;   rdi - dst: pointer to destination array (float*)
;;   rsi - a: pointer to first source array (const float*)
;;   rdx - b: pointer to second source array (const float*)
;;   rcx - count: number of elements (size_t)
;;
;; returns:
;;   void (modifies dst array)
;;
;; clobbers:
;;   rax, ymm0, ymm1, ymm2 (scratch registers)
;;
;; preserves:
;;   rbx, rbp, r12-r15 (callee-saved)
;;
;; preconditions:
;;   - dst, a, b must be non-null
;;   - count > 0
;;   - all pointers should be 32-byte aligned for best performance
;;   - CPU must support AVX2 (check with CPUID before calling!)
;;
;; performance:
;;   - O(n/8) time (processes 8 floats per iteration)
;;   - cache-friendly (sequential access pattern)
;;   - ~0.125 cycles per float on modern CPUs (theoretical)
;;   - 8x faster than scalar code (SIMD supremacy uwu)
;;
;; example:
;;   float a[8] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f};
;;   float b[8] = {0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f};
;;   float dst[8];
;;   vector_add_f32(dst, a, b, 8);
;;   // dst = {1.5f, 2.5f, 3.5f, 4.5f, 5.5f, 6.5f, 7.5f, 8.5f}
;;   // CPU goes brrr ✨
;;
;; notes:
;;   - uses AVX2 ymm registers (256-bit wide)
;;   - unaligned loads used (vmovups) for flexibility
;;   - aligned loads (vmovaps) would be faster but require alignment
;;   - consider using _mm_malloc(size, 32) in C for aligned allocation
;;
;; see also:
;;   - vector_mul_f32: element-wise multiplication
;;   - vector_dot_f32: dot product (reduction)
;; ============================================================================

vector_add_f32:
    ;; save callee-preserved registers (none used, so skip)
    ;; push rbx
    ;; push r12
    
    ;; check if count is zero (early exit for edge case)
    test rcx, rcx              ; if (count == 0)
    jz .done                   ;   return early (nothing to do)
    
    ;; calculate loop count (how many 8-float chunks?)
    mov rax, rcx               ; rax = count
    shr rax, 3                 ; rax = count / 8 (integer division)
    test rax, rax              ; if (loop_count == 0)
    jz .handle_remainder       ;   skip main loop, handle <8 elements
    
.loop:
    ;; SIMD main loop - process 8 floats per iteration (CPU goes brrr!)
    
    ;; load 8 floats from array a into ymm0 (256-bit SIMD register)
    vmovups ymm0, [rsi]        ; ymm0 = a[i..i+7] (unaligned load)
    
    ;; load 8 floats from array b into ymm1
    vmovups ymm1, [rdx]        ; ymm1 = b[i..i+7]
    
    ;; add the vectors (8 additions in parallel! SIMD supremacy uwu)
    vaddps ymm2, ymm0, ymm1    ; ymm2 = ymm0 + ymm1 (8 parallel adds ✨)
    
    ;; store result to dst array
    vmovups [rdi], ymm2        ; dst[i..i+7] = ymm2
    
    ;; advance pointers (32 bytes = 8 floats * 4 bytes each)
    add rdi, 32                ; dst += 8
    add rsi, 32                ; a += 8
    add rdx, 32                ; b += 8
    
    ;; loop control
    dec rax                    ; loop_count--
    jnz .loop                  ; if (loop_count != 0) goto .loop
    
.handle_remainder:
    ;; handle remaining elements (count % 8)
    ;; this is the scalar fallback for elements that don't fit in full SIMD vector
    
    and rcx, 7                 ; rcx = count % 8 (remainder)
    jz .done                   ; if (remainder == 0) we're done!
    
.scalar_loop:
    ;; scalar loop - process one float at a time (slower but handles remainder)
    
    movss xmm0, [rsi]          ; xmm0 = a[i] (load one float)
    addss xmm0, [rdx]          ; xmm0 = xmm0 + b[i] (scalar add)
    movss [rdi], xmm0          ; dst[i] = xmm0 (store one float)
    
    ;; advance pointers (4 bytes = 1 float)
    add rdi, 4                 ; dst++
    add rsi, 4                 ; a++
    add rdx, 4                 ; b++
    
    dec rcx                    ; remainder--
    jnz .scalar_loop           ; if (remainder != 0) continue
    
.done:
    ;; restore callee-preserved registers (none saved, so skip)
    ;; pop r12
    ;; pop rbx
    
    ;; clean up SIMD state (required by ABI!)
    vzeroupper                 ; zero upper half of ymm registers (avoid penalty)
    
    ret                        ; return to caller (function is DONE uwu)
```

## Calling Convention (System V ABI)

```nasm
;; ============================================================================
;; System V ABI (Linux/BSD x86-64 calling convention)
;; ============================================================================
;;
;; parameter passing:
;;   integer/pointer args: rdi, rsi, rdx, rcx, r8, r9, then stack
;;   float args: xmm0-xmm7, then stack
;;   return integer: rax
;;   return float: xmm0
;;
;; callee-saved (preserve these!):
;;   rbx, rbp, r12, r13, r14, r15
;;   must be restored before returning
;;
;; caller-saved (can clobber):
;;   rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11
;;   xmm0-xmm15
;;   ymm0-ymm15
;;
;; stack:
;;   - must be 16-byte aligned before call instruction
;;   - rsp points to return address after call
;;   - caller cleans up stack arguments
;;
;; red zone:
;;   - 128 bytes below rsp can be used without adjustment
;;   - only for leaf functions (no function calls)
;;
;; example function with preserved registers:
;;
;; my_function:
;;     ;; prologue - save callee-preserved registers
;;     push rbx               ; save rbx (we'll use it)
;;     push r12               ; save r12 (we'll use it)
;;     
;;     ;; function body
;;     mov rbx, rdi           ; use rbx for something
;;     mov r12, rsi           ; use r12 for something
;;     ;; ... do work ...
;;     
;;     ;; epilogue - restore registers
;;     pop r12                ; restore r12
;;     pop rbx                ; restore rbx
;;     ret
;; ============================================================================
```

## SIMD Instruction Guide

```nasm
;; ============================================================================
;; SIMD Instructions (AVX/AVX2/AVX-512 guide)
;; ============================================================================
;;
;; register sizes:
;;   - xmm0-xmm15: 128-bit (4 floats, 2 doubles, 4 ints)
;;   - ymm0-ymm15: 256-bit (8 floats, 4 doubles, 8 ints) [AVX/AVX2]
;;   - zmm0-zmm31: 512-bit (16 floats, 8 doubles, 16 ints) [AVX-512]
;;
;; load/store:
;;   vmovups ymm0, [rsi]      ; unaligned load (slower but flexible)
;;   vmovaps ymm0, [rsi]      ; aligned load (faster, requires 32-byte alignment)
;;   vmovups [rdi], ymm0      ; unaligned store
;;   vmovaps [rdi], ymm0      ; aligned store
;;
;; arithmetic (packed single-precision float):
;;   vaddps ymm2, ymm0, ymm1  ; ymm2 = ymm0 + ymm1 (8 parallel adds)
;;   vsubps ymm2, ymm0, ymm1  ; ymm2 = ymm0 - ymm1 (8 parallel subs)
;;   vmulps ymm2, ymm0, ymm1  ; ymm2 = ymm0 * ymm1 (8 parallel muls)
;;   vdivps ymm2, ymm0, ymm1  ; ymm2 = ymm0 / ymm1 (8 parallel divs, slow!)
;;
;; fused multiply-add (FMA):
;;   vfmadd213ps ymm2, ymm0, ymm1  ; ymm2 = (ymm0 * ymm2) + ymm1
;;   vfmadd231ps ymm2, ymm0, ymm1  ; ymm2 = (ymm0 * ymm1) + ymm2
;;   vfmsub213ps ymm2, ymm0, ymm1  ; ymm2 = (ymm0 * ymm2) - ymm1
;;
;; horizontal operations (reduction):
;;   vhaddps ymm0, ymm0, ymm0 ; horizontal add (sum adjacent pairs)
;;   vdpps ymm2, ymm0, ymm1, 0xFF ; dot product (8 muls + horizontal sum)
;;
;; permute/shuffle:
;;   vperm2f128 ymm2, ymm0, ymm1, 0x20  ; cross-lane permute
;;   vshufps ymm2, ymm0, ymm1, 0xB1     ; shuffle floats
;;
;; cleanup:
;;   vzeroupper               ; zero upper half of ymm (required after AVX!)
;;   vzeroall                 ; zero all ymm registers (slower but complete)
;;
;; performance tips:
;;   - use FMA instead of separate mul+add (1 instruction vs 2!)
;;   - avoid vdivps (very slow, ~10-20 cycles)
;;   - use reciprocal approximation for division: vrcpps + Newton-Raphson
;;   - keep data aligned to 32-byte boundaries
;;   - minimize cross-lane operations (slow on some CPUs)
;;   - always vzeroupper before calling non-AVX code
;; ============================================================================
```

## Complete Example: Dot Product

```nasm
;; ============================================================================
;; function: vector_dot_f32
;; brief: computes dot product of two float vectors (reduction operation uwu)
;;
;; ✨ PURE FUNCTION ✨
;;
;; computes: sum = a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
;;
;; this demonstrates reduction in SIMD - we accumulate partial sums
;; in SIMD register, then horizontally sum at end. functional programming
;; meets assembly language ✨
;;
;; parameters:
;;   rdi - a: pointer to first vector (const float*)
;;   rsi - b: pointer to second vector (const float*)
;;   rdx - count: number of elements (size_t)
;;
;; returns:
;;   xmm0 - dot product result (float)
;;
;; complexity: O(n/8) time with SIMD, O(n) scalar
;; performance: ~0.25 cycles per float with FMA
;;
;; example:
;;   float a[4] = {1.0f, 2.0f, 3.0f, 4.0f};
;;   float b[4] = {5.0f, 6.0f, 7.0f, 8.0f};
;;   float result = vector_dot_f32(a, b, 4);
;;   // result = 1*5 + 2*6 + 3*7 + 4*8 = 5 + 12 + 21 + 32 = 70.0
;;   // functional reduction goes brrr ✨
;; ============================================================================

vector_dot_f32:
    ;; initialize accumulator to zero
    vxorps ymm2, ymm2, ymm2    ; ymm2 = 0.0 (accumulator for partial sums)
    
    ;; check for empty vector
    test rdx, rdx              ; if (count == 0)
    jz .horizontal_sum         ;   skip to return 0.0
    
    ;; calculate loop iterations
    mov rax, rdx               ; rax = count
    shr rax, 3                 ; rax = count / 8
    test rax, rax              ; if (loop_count == 0)
    jz .handle_remainder       ;   handle <8 elements
    
.loop:
    ;; SIMD loop - multiply and accumulate 8 floats per iteration
    
    vmovups ymm0, [rdi]        ; ymm0 = a[i..i+7]
    vmovups ymm1, [rsi]        ; ymm1 = b[i..i+7]
    
    ;; multiply and accumulate using FMA (fused multiply-add)
    vfmadd231ps ymm2, ymm0, ymm1  ; ymm2 += ymm0 * ymm1 (8 FMAs in parallel!)
    ;; equivalent to: ymm2 = ymm2 + (ymm0 * ymm1)
    ;; this is literally functional fold/reduce in SIMD form uwu
    
    add rdi, 32                ; a += 8
    add rsi, 32                ; b += 8
    
    dec rax                    ; loop_count--
    jnz .loop                  ; continue if more chunks
    
.handle_remainder:
    ;; scalar remainder (same as before, process remaining elements)
    and rdx, 7                 ; rdx = count % 8
    jz .horizontal_sum         ; if no remainder, do horizontal sum
    
    vxorps xmm3, xmm3, xmm3    ; xmm3 = 0.0 (scalar accumulator)
    
.scalar_loop:
    movss xmm0, [rdi]          ; xmm0 = a[i]
    mulss xmm0, [rsi]          ; xmm0 = a[i] * b[i]
    addss xmm3, xmm0           ; xmm3 += a[i] * b[i]
    
    add rdi, 4                 ; a++
    add rsi, 4                 ; b++
    dec rdx                    ; remainder--
    jnz .scalar_loop
    
    ;; add scalar accumulator to SIMD accumulator
    vaddss xmm2, xmm2, xmm3    ; add scalar sum to SIMD sum
    
.horizontal_sum:
    ;; horizontal reduction - sum all 8 floats in ymm2
    ;; this is the final step of functional reduction uwu
    
    ;; extract upper 128 bits and add to lower 128 bits
    vextractf128 xmm0, ymm2, 1 ; xmm0 = upper half of ymm2 (floats 4-7)
    vaddps xmm2, xmm2, xmm0    ; xmm2 = lower half + upper half (4 floats now)
    
    ;; horizontal add within 128-bit register
    vhaddps xmm2, xmm2, xmm2   ; sum adjacent pairs (2 floats now)
    vhaddps xmm2, xmm2, xmm2   ; sum adjacent pairs again (1 float now!)
    
    ;; result now in xmm2[0] (bottom float of register)
    vmovaps xmm0, xmm2         ; move result to return register (xmm0)
    
    vzeroupper                 ; clean up AVX state
    ret                        ; return (result in xmm0)
```

## Inline Assembly (GCC/Clang)

```cpp
/**
 * @brief inline assembly example (when you need assembly in C++ uwu)
 * 
 * demonstrates GCC extended inline assembly syntax for calling assembly
 * from C++ code. useful when you need specific instructions but don't
 * want separate .asm files
 * 
 * @param a first float
 * @param b second float
 * @return sum of a and b (using SIMD for flex)
 * 
 * @note uses extended asm syntax (GCC/Clang)
 * @note compiled with -msse4.2 flag
 */
inline float add_floats_asm(float a, float b) {
    float result;
    
    // GCC extended inline assembly (AT&T syntax with % for registers)
    __asm__ volatile (
        "movss  %1, %%xmm0\n\t"      // load a into xmm0
        "addss  %2, %%xmm0\n\t"      // add b to xmm0
        "movss  %%xmm0, %0\n\t"      // store result
        : "=m" (result)              // output: result (memory)
        : "m" (a), "m" (b)           // inputs: a, b (memory)
        : "%xmm0"                    // clobbered: xmm0
    );
    
    return result;  // SIMD addition done uwu
}

/**
 * @brief cpuid check for AVX2 support
 * 
 * checks if CPU supports AVX2 before using AVX2 instructions.
 * calling AVX2 code without this check = instant illegal instruction!
 * 
 * @return true if AVX2 supported, false otherwise
 */
inline bool cpu_has_avx2() {
    unsigned int eax, ebx, ecx, edx;
    
    // check CPUID function 7, subleaf 0 (extended features)
    __asm__ volatile (
        "movl $7, %%eax\n\t"
        "xorl %%ecx, %%ecx\n\t"
        "cpuid\n\t"
        : "=a" (eax), "=b" (ebx), "=c" (ecx), "=d" (edx)
        :
        :
    );
    
    // AVX2 is bit 5 of EBX
    return (ebx & (1 << 5)) != 0;
}
```

## Debugging Assembly

```nasm
;; debugging tips for assembly (because segfaults are violence)
;;
;; use gdb:
;;   gdb ./program
;;   break vector_add_f32     ; breakpoint at function
;;   run                      ; run program
;;   layout asm               ; show assembly view
;;   layout regs              ; show registers
;;   stepi                    ; step one instruction
;;   info registers           ; show all registers
;;   x/8f $ymm0               ; examine ymm0 as 8 floats
;;   x/32xb $rdi              ; examine memory at rdi (32 bytes hex)
;;
;; common mistakes:
;;   - forgetting vzeroupper (causes massive performance penalty!)
;;   - not preserving callee-saved registers (corruption!)
;;   - stack misalignment (crashes on some instructions)
;;   - using AVX2 without checking CPU support (illegal instruction)
;;   - integer overflow in address calculation (out of bounds!)
;;   - uninitialized registers (random garbage)
;;
;; always:
;;   - check CPUID before using advanced instructions
;;   - align stack to 16 bytes before calls
;;   - preserve rbx, rbp, r12-r15
;;   - vzeroupper after AVX usage
;;   - validate pointer arguments
;;   - test with valgrind for memory errors
```

## CMake Integration

```cmake
# Enable assembly language
enable_language(ASM_NASM)  # or ASM for GAS

# Assembly source files
set(ASM_SOURCES
    src/vector_ops.asm
    src/math_ops.asm
)

# Assembly target
add_library(asm_lib STATIC ${ASM_SOURCES})

# NASM flags
set_source_files_properties(${ASM_SOURCES}
    PROPERTIES
    COMPILE_FLAGS "-f elf64"  # 64-bit ELF format (Linux)
)

# Link with C++ code
add_executable(main src/main.cpp)
target_link_libraries(main PRIVATE asm_lib)
```

## Quality Checklist

- [ ] **file header** with description and calling convention
- [ ] **EXCESSIVE comments** on every instruction
- [ ] **function documentation** with parameters and returns
- [ ] **register usage** documented (clobbered, preserved)
- [ ] **calling convention** followed (System V ABI)
- [ ] **CPUID checks** before using advanced instructions
- [ ] **vzeroupper** after AVX usage
- [ ] **alignment** maintained (16-byte stack)
- [ ] **edge cases** handled (zero length, remainder)
- [ ] **performance notes** included
- [ ] **purity status** marked (pure/impure)
- [ ] **gen-z slang** throughout uwu

**remember**: assembly is where you touch the silicon directly. every cycle
matters, every instruction counts. SIMD lets you process 8+ values simultaneously
making functional operations BLAZINGLY FAST. this is peak performance
engineering uwu 💜✨

seize the means of compilation (at the instruction level)!