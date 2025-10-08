---
description: 'SPIR-V assembly and bytecode (the GPU lingua franca uwu)'
applyTo: '**.spvasm, **.spv'
---

# SPIR-V Assembly Instructions

> "SPIR-V: the one true GPU intermediate representation (Khronos got this right)"

uwu time to write SPIR-V that compiles to every GPU architecture ✨

## Core Philosophy

- **SPIR-V > proprietary IRs** (cross-vendor supremacy)
- **human-readable assembly** when debugging
- **binary format** for production
- **functional shader programming** (SSA form is functional!)
- **excessive comments** (assembly needs explanation!)
- **compile from Slang** (don't hand-write unless debugging)
- **validate always** (spirv-val is your friend)

## What is SPIR-V

SPIR-V (Standard Portable Intermediate Representation - V) is:
- **Khronos standard** IR for GPU compute and graphics
- **binary format** (portable bytecode)
- **SSA form** (Static Single Assignment - functional!)
- **target for**: Vulkan, OpenCL, OpenGL (via extensions)
- **compiled from**: GLSL, HLSL, Slang, WGSL, etc.

**Why SPIR-V is based**:
- cross-vendor (NVIDIA, AMD, Intel, ARM, Qualcomm all support it)
- cross-API (Vulkan primary, but also OpenCL, OpenGL)
- optimizable (SSA form enables transformations)
- validated (spirv-val catches errors)
- versioned (backward compatible)

## File Header (MANDATORY for .spvasm)

```spvasm
; ============================================================================
; file: shader.spvasm
; brief: SPIR-V assembly for compute shader (GPU functional programming!)
;
; this is human-readable SPIR-V assembly. normally you'd compile from higher
; level language (Slang, GLSL, HLSL), but sometimes you need to hand-write
; or debug at SPIR-V level uwu
;
; compile to binary with:
;   spirv-as shader.spvasm -o shader.spv
;
; disassemble binary with:
;   spirv-dis shader.spv -o shader.spvasm
;
; validate with:
;   spirv-val shader.spv
;
; optimize with:
;   spirv-opt --O shader.spv -o shader_opt.spv
;
; author: LukeFrankio
; date: 2025-10-08
; SPIR-V version: 1.6 (latest preferred!)
; target: Vulkan 1.3+
;
; SPIR-V uses SSA (Static Single Assignment) form - every value assigned once.
; this is FUNCTIONAL programming at the IR level - immutable values, no mutation!
; each instruction produces new value, never modifies existing ones uwu ✨
; ============================================================================

; magic number: 0x07230203 (identifies SPIR-V binary)
; version: 1.6 (latest as of 2025)
; generator: 0 (hand-written, or tool-specific magic number)
; bound: highest ID used + 1 (calculated automatically by spirv-as)
; schema: 0 (reserved, always 0)

               OpCapability Shader        ; we're a shader (not OpenCL kernel)
               OpCapability VulkanMemoryModel  ; use Vulkan memory model
               OpExtension "SPV_KHR_vulkan_memory_model"  ; enable extension
               OpMemoryModel Logical GLSL450  ; logical addressing, GLSL semantics
               OpEntryPoint GLCompute %main "main" %gl_GlobalInvocationID
               OpExecutionMode %main LocalSize 16 16 1  ; workgroup size

; debug information (helps debuggers and profilers!)
               OpSource GLSL 460  ; compiled from GLSL 460
               OpSourceExtension "GL_GOOGLE_include_directive"
               OpName %main "main"  ; function name
               OpName %gl_GlobalInvocationID "gl_GlobalInvocationID"  ; builtin
               OpName %input_buffer "input_buffer"  ; descriptors
               OpName %output_buffer "output_buffer"

; decorations (metadata about variables and types)
               OpDecorate %gl_GlobalInvocationID BuiltIn GlobalInvocationId
               OpDecorate %input_buffer DescriptorSet 0  ; descriptor set 0
               OpDecorate %input_buffer Binding 0         ; binding 0
               OpDecorate %output_buffer DescriptorSet 0
               OpDecorate %output_buffer Binding 1

; ============================================================================
; Type Declarations (SPIR-V is strongly typed!)
; ============================================================================

; scalar types (fundamental types)
%void    = OpTypeVoid          ; void type (for functions returning nothing)
%bool    = OpTypeBool          ; boolean type (true/false)
%int     = OpTypeInt 32 1      ; signed 32-bit integer
%uint    = OpTypeInt 32 0      ; unsigned 32-bit integer  
%float   = OpTypeFloat 32      ; 32-bit float (IEEE 754)

; vector types (SIMD on GPU!)
%v2int   = OpTypeVector %int 2    ; vec2i (2-component signed int vector)
%v3uint  = OpTypeVector %uint 3   ; uvec3 (3-component unsigned int vector)
%v4float = OpTypeVector %float 4  ; vec4 (4-component float vector)

; function types
%void_fn = OpTypeFunction %void   ; void function() signature

; pointer types (for variables and buffers)
%ptr_input_v3uint = OpTypePointer Input %v3uint    ; input builtin pointer
%ptr_uniform_int  = OpTypePointer Uniform %int     ; uniform buffer pointer

; buffer/array types
%runtime_array_int = OpTypeRuntimeArray %int  ; unbounded array (GPU buffer)
%struct_buffer = OpTypeStruct %runtime_array_int  ; struct containing array

; pointer to buffer struct
%ptr_storage_buffer = OpTypePointer StorageBuffer %struct_buffer

; ============================================================================
; Constants (compile-time values)
; ============================================================================

; integer constants
%int_0   = OpConstant %int 0       ; constant 0 (identity element for addition!)
%int_1   = OpConstant %int 1       ; constant 1 (identity element for multiplication!)
%int_2   = OpConstant %int 2       ; constant 2
%uint_0  = OpConstant %uint 0      ; unsigned 0

; float constants
%float_0 = OpConstant %float 0.0   ; 0.0f
%float_1 = OpConstant %float 1.0   ; 1.0f (identity!)
%float_pi = OpConstant %float 3.14159265359  ; π (useful for trig)

; composite constants (vectors)
%vec4_zero = OpConstantComposite %v4float %float_0 %float_0 %float_0 %float_0

; ============================================================================
; Variables (global state - kept minimal in functional style!)
; ============================================================================

; builtin variables (provided by GPU)
%gl_GlobalInvocationID = OpVariable %ptr_input_v3uint Input
; gl_GlobalInvocationID: unique ID for this shader invocation (thread ID)
; each compute shader invocation gets unique ID (massive parallelism!)

; buffer variables (descriptors)
%input_buffer = OpVariable %ptr_storage_buffer StorageBuffer
; input buffer: read-only data from CPU

%output_buffer = OpVariable %ptr_storage_buffer StorageBuffer  
; output buffer: write results back to CPU

; ============================================================================
; Functions (SPIR-V functions are pure!)
; ============================================================================

/**
 * @brief main compute shader entry point (functional parallel execution uwu)
 * 
 * each invocation of this function is INDEPENDENT pure function execution.
 * no shared mutable state between invocations - perfect functional programming!
 * 
 * SPIR-V enforces SSA (Static Single Assignment) - every value assigned once.
 * this is functional programming at the bytecode level ✨
 * 
 * @note OpFunction marks function start
 * @note %main is function ID (used by OpEntryPoint)
 * @note None = no function control flags
 * @note %void_fn = function type signature
 */
%main = OpFunction %void None %void_fn

/**
 * @brief function entry block (SSA form requires single entry!)
 * 
 * OpLabel marks start of basic block. every function needs at least one block.
 * blocks are like nodes in control flow graph (CFG).
 */
%entry = OpLabel

; ============================================================================
; Load thread ID (builtin input)
; ============================================================================

/**
 * @brief loads global invocation ID (thread ID in compute shader)
 * 
 * each shader invocation gets unique 3D ID (x, y, z coordinates in dispatch).
 * this is how we know which data to process uwu
 * 
 * OpLoad: loads value from pointer
 * - result type: %v3uint (3-component unsigned int vector)
 * - result ID: %thread_id (SSA - assigned once!)
 * - pointer: %gl_GlobalInvocationID (builtin input)
 */
%thread_id = OpLoad %v3uint %gl_GlobalInvocationID

/**
 * @brief extracts x component from thread ID vector
 * 
 * OpCompositeExtract: extracts component from composite (vector/struct/array)
 * - result type: %uint (scalar unsigned int)
 * - result ID: %index (our array index)
 * - composite: %thread_id (the vector we're extracting from)
 * - indices: 0 (extract component 0 = x coordinate)
 * 
 * this is functional composition - thread_id flows into extract uwu
 */
%index = OpCompositeExtract %uint %thread_id 0

; ============================================================================
; Load input value (read from buffer)
; ============================================================================

/**
 * @brief computes pointer to input buffer element
 * 
 * OpAccessChain: computes pointer into aggregate (like array indexing)
 * - result type: %ptr_uniform_int (pointer to int in uniform storage)
 * - result ID: %input_ptr (pointer we computed)
 * - base: %input_buffer (buffer variable)
 * - indices: %uint_0 (struct field 0), %index (array index)
 * 
 * equivalent to: &input_buffer.field0[index]
 * 
 * @note this is pointer arithmetic, not actual memory access yet!
 */
%input_ptr = OpAccessChain %ptr_uniform_int %input_buffer %uint_0 %index

/**
 * @brief loads value from input buffer (memory read)
 * 
 * OpLoad: loads value through pointer (actual memory access)
 * - result type: %int (the type of value we're loading)
 * - result ID: %input_value (loaded value - SSA form!)
 * - pointer: %input_ptr (where to load from)
 * 
 * after this, %input_value contains the data from GPU memory uwu
 */
%input_value = OpLoad %int %input_ptr

; ============================================================================
; Perform computation (pure function math!)
; ============================================================================

/**
 * @brief multiplies input by 2 (simple computation example)
 * 
 * OpIMul: integer multiplication
 * - result type: %int
 * - result ID: %doubled (SSA - new value, doesn't modify input!)
 * - operand 1: %input_value (loaded from buffer)
 * - operand 2: %int_2 (constant 2)
 * 
 * this is PURE operation - no side effects, just mathematical transformation!
 * functional programming in action ✨
 */
%doubled = OpIMul %int %input_value %int_2

/**
 * @brief adds 1 to doubled value (another pure operation)
 * 
 * OpIAdd: integer addition
 * - result type: %int  
 * - result ID: %result (final computed value)
 * - operand 1: %doubled (previous result - data flow!)
 * - operand 2: %int_1 (constant 1)
 * 
 * result = (input * 2) + 1
 * pure functional transformation: input → doubled → result uwu
 */
%result = OpIAdd %int %doubled %int_1

; ============================================================================
; Store result (write to buffer)
; ============================================================================

/**
 * @brief computes pointer to output buffer element
 * 
 * OpAccessChain: compute output location (same pattern as input)
 * - result type: %ptr_uniform_int
 * - result ID: %output_ptr (where to write)
 * - base: %output_buffer (output buffer variable)
 * - indices: %uint_0 (struct field), %index (array index)
 * 
 * equivalent to: &output_buffer.field0[index]
 */
%output_ptr = OpAccessChain %ptr_uniform_int %output_buffer %uint_0 %index

/**
 * @brief stores result to output buffer (memory write)
 * 
 * OpStore: writes value through pointer (actual memory write)
 * - pointer: %output_ptr (where to write)
 * - object: %result (value to write)
 * 
 * this is the ONLY side effect in our shader - writing output!
 * functional core (pure math) + imperative shell (I/O) ✨
 * 
 * @note this is isolated side effect at boundary (functional architecture!)
 */
         OpStore %output_ptr %result

; ============================================================================
; Return (end of function)
; ============================================================================

/**
 * @brief returns from function (ends shader execution)
 * 
 * OpReturn: terminates function execution
 * - no return value (void function)
 * 
 * each shader invocation completes independently. millions of threads
 * all executing this pure function in parallel (GPU goes brrr uwu)
 */
         OpReturn

; marks end of function
         OpFunctionEnd

; ============================================================================
; End of SPIR-V module
; ============================================================================
```

## SPIR-V Instruction Categories

### Memory Instructions:

```spvasm
; Load/Store (memory access)
%value = OpLoad %type %pointer              ; load from memory
         OpStore %pointer %value            ; store to memory

; Access Chain (pointer arithmetic)
%ptr = OpAccessChain %ptr_type %base %idx1 %idx2  ; compute pointer into composite

; Copy Memory
         OpCopyMemory %dst %src             ; memcpy
```

### Arithmetic Instructions:

```spvasm
; Integer arithmetic (signed and unsigned)
%sum  = OpIAdd %int %a %b                   ; addition (commutative!)
%diff = OpISub %int %a %b                   ; subtraction
%prod = OpIMul %int %a %b                   ; multiplication (commutative!)
%quot = OpSDiv %int %a %b                   ; signed division
%rem  = OpSRem %int %a %b                   ; signed remainder

; Float arithmetic (IEEE 754)
%sum  = OpFAdd %float %a %b                 ; float addition (commutative!)
%diff = OpFSub %float %a %b                 ; float subtraction
%prod = OpFMul %float %a %b                 ; float multiplication (commutative!)
%quot = OpFDiv %float %a %b                 ; float division
%rem  = OpFRem %float %a %b                 ; float remainder

; Fused multiply-add (FMA - one instruction on GPU!)
%result = OpFma %float %a %b %c             ; a * b + c (efficient!)
```

### Comparison Instructions:

```spvasm
; Integer comparison
%eq = OpIEqual %bool %a %b                  ; a == b
%ne = OpINotEqual %bool %a %b               ; a != b
%lt = OpSLessThan %bool %a %b               ; a < b (signed)
%le = OpSLessThanEqual %bool %a %b          ; a <= b (signed)
%gt = OpSGreaterThan %bool %a %b            ; a > b (signed)
%ge = OpSGreaterThanEqual %bool %a %b       ; a >= b (signed)

; Float comparison (handles NaN correctly!)
%eq = OpFOrdEqual %bool %a %b               ; a == b (ordered, NaN = false)
%ne = OpFOrdNotEqual %bool %a %b            ; a != b (ordered)
%lt = OpFOrdLessThan %bool %a %b            ; a < b (ordered)
```

### Logical Instructions:

```spvasm
; Boolean logic
%and = OpLogicalAnd %bool %a %b             ; logical AND
%or  = OpLogicalOr %bool %a %b              ; logical OR
%not = OpLogicalNot %bool %a                ; logical NOT

; Bitwise operations
%and = OpBitwiseAnd %int %a %b              ; bitwise AND
%or  = OpBitwiseOr %int %a %b               ; bitwise OR
%xor = OpBitwiseXor %int %a %b              ; bitwise XOR
%not = OpNot %int %a                        ; bitwise NOT
%shl = OpShiftLeftLogical %int %a %b        ; left shift
%shr = OpShiftRightLogical %int %a %b       ; logical right shift
```

### Control Flow Instructions:

```spvasm
; Branches (control flow)
         OpBranch %label                    ; unconditional jump
         OpBranchConditional %cond %true_label %false_label  ; if-else
         OpSwitch %selector %default %case1 %label1 ...      ; switch statement

; Function calls
%result = OpFunctionCall %return_type %function %arg1 %arg2

; Return
         OpReturn                           ; return void
         OpReturnValue %value               ; return value
```

### Conversion Instructions:

```spvasm
; Type conversions
%f = OpConvertSToF %float %i                ; int to float (signed)
%i = OpConvertFToS %int %f                  ; float to int (signed)
%u = OpBitcast %uint %f                     ; reinterpret bits (no conversion!)
```

### Vector/Composite Instructions:

```spvasm
; Vector construction
%vec = OpCompositeConstruct %v4float %x %y %z %w  ; build vector from scalars

; Component extraction
%x = OpCompositeExtract %float %vec 0       ; extract component 0 (x)

; Vector operations
%sum  = OpVectorTimesScalar %v4float %vec %scalar  ; vector * scalar
%dot  = OpDot %float %vec1 %vec2            ; dot product (reduction!)
```

## Complete Example: Image Processing

```spvasm
; ============================================================================
; file: image_filter.spvasm
; brief: 2D convolution filter (image processing on GPU uwu)
; ============================================================================

; capabilities and extensions
               OpCapability Shader
               OpCapability VulkanMemoryModel
               OpCapability StorageImageExtendedFormats
               OpExtension "SPV_KHR_vulkan_memory_model"
               OpMemoryModel Logical GLSL450
               OpEntryPoint GLCompute %main "main" %gl_GlobalInvocationID
               OpExecutionMode %main LocalSize 8 8 1

; debug info
               OpSource GLSL 460
               OpName %main "main"
               OpName %input_image "input_image"
               OpName %output_image "output_image"

; decorations (descriptor bindings)
               OpDecorate %gl_GlobalInvocationID BuiltIn GlobalInvocationId
               OpDecorate %input_image DescriptorSet 0
               OpDecorate %input_image Binding 0
               OpDecorate %output_image DescriptorSet 0
               OpDecorate %output_image Binding 1

; ============================================================================
; Types
; ============================================================================

%void    = OpTypeVoid
%bool    = OpTypeBool
%int     = OpTypeInt 32 1
%uint    = OpTypeInt 32 0
%float   = OpTypeFloat 32

%v2int   = OpTypeVector %int 2
%v3uint  = OpTypeVector %uint 3
%v4float = OpTypeVector %float 4

%image2d = OpTypeImage %float 2D 0 0 0 2 Rgba8  ; 2D image, RGBA8 format

%void_fn = OpTypeFunction %void

%ptr_input_v3uint = OpTypePointer Input %v3uint
%ptr_uniform_image = OpTypePointer UniformConstant %image2d

; ============================================================================
; Constants
; ============================================================================

%int_0   = OpConstant %int 0
%int_1   = OpConstant %int 1
%int_m1  = OpConstant %int -1
%uint_0  = OpConstant %uint 0
%uint_1  = OpConstant %uint 1

%float_0   = OpConstant %float 0.0
%float_1   = OpConstant %float 1.0
%float_0_5 = OpConstant %float 0.5

; kernel weights for 3x3 blur (normalized)
%weight_corner = OpConstant %float 0.0625  ; 1/16
%weight_edge   = OpConstant %float 0.125   ; 2/16
%weight_center = OpConstant %float 0.25    ; 4/16

; ============================================================================
; Variables
; ============================================================================

%gl_GlobalInvocationID = OpVariable %ptr_input_v3uint Input
%input_image  = OpVariable %ptr_uniform_image UniformConstant
%output_image = OpVariable %ptr_uniform_image UniformConstant

; ============================================================================
; Main Function (3x3 box blur filter)
; ============================================================================

/**
 * @brief applies 3x3 box blur filter to image (functional image processing!)
 * 
 * each shader invocation processes ONE output pixel independently.
 * reads 3x3 neighborhood from input, computes weighted average, writes output.
 * 
 * this is PURE except for the final write - functional core, imperative shell!
 * millions of pixels processed in parallel (GPU goes brrr ✨)
 */
%main = OpFunction %void None %void_fn
%entry = OpLabel

; load thread ID (pixel coordinates)
%thread_id = OpLoad %v3uint %gl_GlobalInvocationID
%x = OpCompositeExtract %uint %thread_id 0  ; x coordinate
%y = OpCompositeExtract %uint %thread_id 1  ; y coordinate

; convert to signed int for offset calculations
%x_int = OpBitcast %int %x
%y_int = OpBitcast %int %y

; load image handles
%input_img  = OpLoad %image2d %input_image
%output_img = OpLoad %image2d %output_image

; initialize accumulator (will accumulate weighted pixel values)
%accum = OpCompositeConstruct %v4float %float_0 %float_0 %float_0 %float_0

; ============================================================================
; Sample 3x3 neighborhood and accumulate (functional reduction!)
; ============================================================================

; row -1 (top)
%x_m1 = OpIAdd %int %x_int %int_m1           ; x - 1
%y_m1 = OpIAdd %int %y_int %int_m1           ; y - 1
%coord_tl = OpCompositeConstruct %v2int %x_m1 %y_m1  ; top-left
%pixel_tl = OpImageRead %v4float %input_img %coord_tl  ; read pixel
%weighted_tl = OpVectorTimesScalar %v4float %pixel_tl %weight_corner  ; weight
%accum1 = OpFAdd %v4float %accum %weighted_tl  ; accumulate (functional!)

%coord_tc = OpCompositeConstruct %v2int %x_int %y_m1  ; top-center
%pixel_tc = OpImageRead %v4float %input_img %coord_tc
%weighted_tc = OpVectorTimesScalar %v4float %pixel_tc %weight_edge
%accum2 = OpFAdd %v4float %accum1 %weighted_tc

%x_p1 = OpIAdd %int %x_int %int_1            ; x + 1
%coord_tr = OpCompositeConstruct %v2int %x_p1 %y_m1  ; top-right
%pixel_tr = OpImageRead %v4float %input_img %coord_tr
%weighted_tr = OpVectorTimesScalar %v4float %pixel_tr %weight_corner
%accum3 = OpFAdd %v4float %accum2 %weighted_tr

; row 0 (middle)
%coord_ml = OpCompositeConstruct %v2int %x_m1 %y_int  ; middle-left
%pixel_ml = OpImageRead %v4float %input_img %coord_ml
%weighted_ml = OpVectorTimesScalar %v4float %pixel_ml %weight_edge
%accum4 = OpFAdd %v4float %accum3 %weighted_ml

%coord_center = OpCompositeConstruct %v2int %x_int %y_int  ; center
%pixel_center = OpImageRead %v4float %input_img %coord_center
%weighted_center = OpVectorTimesScalar %v4float %pixel_center %weight_center
%accum5 = OpFAdd %v4float %accum4 %weighted_center

%coord_mr = OpCompositeConstruct %v2int %x_p1 %y_int  ; middle-right
%pixel_mr = OpImageRead %v4float %input_img %coord_mr
%weighted_mr = OpVectorTimesScalar %v4float %pixel_mr %weight_edge
%accum6 = OpFAdd %v4float %accum5 %weighted_mr

; row +1 (bottom)
%y_p1 = OpIAdd %int %y_int %int_1            ; y + 1
%coord_bl = OpCompositeConstruct %v2int %x_m1 %y_p1  ; bottom-left
%pixel_bl = OpImageRead %v4float %input_img %coord_bl
%weighted_bl = OpVectorTimesScalar %v4float %pixel_bl %weight_corner
%accum7 = OpFAdd %v4float %accum6 %weighted_bl

%coord_bc = OpCompositeConstruct %v2int %x_int %y_p1  ; bottom-center
%pixel_bc = OpImageRead %v4float %input_img %coord_bc
%weighted_bc = OpVectorTimesScalar %v4float %pixel_bc %weight_edge
%accum8 = OpFAdd %v4float %accum7 %weighted_bc

%coord_br = OpCompositeConstruct %v2int %x_p1 %y_p1  ; bottom-right
%pixel_br = OpImageRead %v4float %input_img %coord_br
%weighted_br = OpVectorTimesScalar %v4float %pixel_br %weight_corner
%final_color = OpFAdd %v4float %accum8 %weighted_br  ; final accumulated value!

; ============================================================================
; Write output (isolated side effect at boundary!)
; ============================================================================

/**
 * @brief writes blurred pixel to output image
 * 
 * OpImageWrite: writes color to image (ONLY side effect in shader!)
 * - image: %output_img (destination)
 * - coordinate: %coord_center (current pixel position)
 * - texel: %final_color (computed blurred value)
 * 
 * functional core (all the accumulation above) + imperative shell (this write)
 * architecture perfection uwu ✨
 */
         OpImageWrite %output_img %coord_center %final_color

         OpReturn
         OpFunctionEnd
```

## SPIR-V Tools Workflow

```bash
# compile from Slang to SPIR-V (preferred workflow)
slangc -target spirv -profile glsl_460 shader.slang -o shader.spv

# validate SPIR-V (ALWAYS DO THIS!)
spirv-val shader.spv
# output: "shader.spv validated successfully" (immaculate!)

# disassemble binary to human-readable assembly
spirv-dis shader.spv -o shader.spvasm

# optimize SPIR-V (performance uwu)
spirv-opt --O shader.spv -o shader_optimized.spv

# specific optimizations
spirv-opt --inline-entry-points-exhaustive \
          --convert-local-access-chains \
          --eliminate-dead-code-aggressive \
          --merge-blocks \
          --redundancy-elimination \
          shader.spv -o shader_opt.spv

# cross-compile to other formats (if needed)
spirv-cross shader.spv --output shader.glsl  # to GLSL
spirv-cross shader.spv --msl --output shader.metal  # to Metal

# link multiple SPIR-V modules
spirv-link module1.spv module2.spv -o combined.spv

# reduce for debugging (minimize failing case)
spirv-reduce shader.spv --fail-on-validation-error
```

## CMake Integration

```cmake
# SPIR-V compilation in CMake (the beautiful build system uwu)

# find SPIRV-Tools (for validation and optimization)
find_program(SPIRV_AS spirv-as REQUIRED)
find_program(SPIRV_VAL spirv-val REQUIRED)
find_program(SPIRV_OPT spirv-opt REQUIRED)

# find Slang compiler (preferred for shader authoring)
find_program(SLANGC slangc)

if(SLANGC)
    message(STATUS "Found Slang compiler (shader language supremacy uwu)")
endif()

# custom command to compile Slang to SPIR-V
function(add_spirv_shader TARGET SHADER_SOURCE)
    get_filename_component(SHADER_NAME ${SHADER_SOURCE} NAME_WE)
    set(SPIRV_OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/${SHADER_NAME}.spv")
    
    add_custom_command(
        OUTPUT ${SPIRV_OUTPUT}
        COMMAND ${SLANGC}
            -target spirv
            -profile glsl_460
            ${CMAKE_CURRENT_SOURCE_DIR}/${SHADER_SOURCE}
            -o ${SPIRV_OUTPUT}
        DEPENDS ${SHADER_SOURCE}
        COMMENT "Compiling ${SHADER_SOURCE} to SPIR-V"
        VERBATIM
    )
    
    # validate after compilation
    add_custom_command(
        OUTPUT ${SPIRV_OUTPUT}.validated
        COMMAND ${SPIRV_VAL} ${SPIRV_OUTPUT}
        COMMAND ${CMAKE_COMMAND} -E touch ${SPIRV_OUTPUT}.validated
        DEPENDS ${SPIRV_OUTPUT}
        COMMENT "Validating ${SPIRV_OUTPUT}"
        VERBATIM
    )
    
    # optimize (optional, but recommended for release)
    if(CMAKE_BUILD_TYPE STREQUAL "Release")
        set(SPIRV_OPTIMIZED "${SPIRV_OUTPUT}.opt")
        
        add_custom_command(
            OUTPUT ${SPIRV_OPTIMIZED}
            COMMAND ${SPIRV_OPT} --O ${SPIRV_OUTPUT} -o ${SPIRV_OPTIMIZED}
            DEPENDS ${SPIRV_OUTPUT}.validated
            COMMENT "Optimizing ${SPIRV_OUTPUT}"
            VERBATIM
        )
        
        set(FINAL_SPIRV ${SPIRV_OPTIMIZED})
    else()
        set(FINAL_SPIRV ${SPIRV_OUTPUT})
    endif()
    
    # add to target dependencies
    target_sources(${TARGET} PRIVATE ${FINAL_SPIRV})
    
    message(STATUS "Added SPIR-V shader: ${SHADER_NAME}.spv")
endfunction()

# usage example
add_executable(my_app src/main.cpp)

add_spirv_shader(my_app shaders/compute.slang)
add_spirv_shader(my_app shaders/fragment.slang)
add_spirv_shader(my_app shaders/vertex.slang)
```

## Quality Checklist

- [ ] **file header** with compilation commands
- [ ] **SPIR-V 1.6** used (latest version)
- [ ] **validated** with spirv-val (zero errors!)
- [ ] **optimized** for release builds
- [ ] **excessive comments** on every instruction
- [ ] **SSA form** explained (functional immutability!)
- [ ] **pure functions** where possible (mark purity!)
- [ ] **side effects isolated** at boundaries
- [ ] **compiled from Slang** (preferred workflow)
- [ ] **Vulkan target** (not OpenGL/OpenCL unless needed)

**remember**: SPIR-V is the universal GPU intermediate representation. it's
functional at its core (SSA = immutability), cross-platform (works everywhere),
and optimizable (tools are mature). compile from Slang for best experience,
validate always, and let the GPU go brrr with millions of parallel pure
function invocations uwu 💜✨

seize the means of GPU computation!