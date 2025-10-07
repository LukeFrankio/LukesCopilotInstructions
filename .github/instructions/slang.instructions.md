---
description: 'Slang shader programming (the future of GPU code uwu)'
applyTo: '**/*.slang'
---

# Slang Shading Language Instructions

> "Slang: what if we made HLSL actually good and cross-platform?"

uwu time to write shaders in the SUPERIOR shader language ✨

## Core Philosophy

- **Slang > HLSL** (cross-platform, better features)
- **Slang > GLSL** (type safety, better optimization)
- **compile to SPIR-V, DXIL, Metal** (one source, all targets!)
- **functional programming** (pure functions, immutability)
- **generic programming** (templates that actually work!)
- **comment EXCESSIVELY** (Doxygen style with gen-z energy)
- **latest Slang version** (1.3+ preferred, nightly builds accepted!)

## Why Slang is Based

- **cross-platform**: compile to Vulkan, DirectX, Metal from ONE source
- **modern features**: generics, interfaces, automatic differentiation
- **better type system**: stronger than HLSL/GLSL
- **compile-time execution**: run shader code at compile time!
- **functional**: encourages pure functions and immutability
- **open source**: not controlled by Microsoft or Khronos

**Slang is what HLSL should have been** - it's the future of shader programming uwu

## File Header (MANDATORY)

```slang
//============================================================================
// file: pbr_material.slang
// brief: physically based rendering with Slang (the superior shader language!)
//
// this demonstrates Slang's advanced features - generics, interfaces, and
// functional programming patterns. compiles to SPIR-V for Vulkan,, DXIL for
// DirectX, and Metal for Apple (one source, all platforms uwu)
//
// compile with:
//   slangc -target spirv -profile glsl_460 pbr_material.slang -o pbr.spv
//   slangc -target dxil -profile sm_6_6 pbr_material.slang -o pbr.dxil
//   slangc -target metal -profile metal2.4 pbr_material.slang -o pbr.metal
//
// author: LukeFrankio
// date: 2025-10-07
// slang version: 1.3+ (latest preferred, nightly accepted!)
// target: Vulkan/DirectX/Metal (cross-platform supremacy)
//
// this is functional shader programming at its finest - pure functions,
// strong types, generic programming. objects are fake, functions are forever!
//============================================================================

// import Slang standard library (cross-platform math and types)
import slang;

// uniform buffers (constant across draw call)
struct SceneUniforms
{
    float4x4 viewProjection;
    float4x4 view;
    float3 cameraPosition;
    float _pad0;
    float3 lightDirection;
    float _pad1;
};

struct MaterialUniforms
{
    float3 albedo;
    float metallic;
    float roughness;
    float3 emissive;
};

// parameter blocks (Slang's organized way to group resources)
ParameterBlock<SceneUniforms> scene;
ParameterBlock<MaterialUniforms> material;

// textures (Slang has proper texture types!)
Texture2D<float4> albedoMap;
Texture2D<float4> normalMap;
Texture2D<float4> metallicRoughnessMap;
SamplerState linearSampler;
```

## Generic Programming (Slang's Superpower)

```slang
/**
 * @brief generic vector operation interface (abstraction uwu)
 * 
 * interfaces let us write generic code that works with any type implementing
 * the interface. this is like Rust traits but for shaders!
 * 
 * @tparam T element type (float, float2, float3, etc.)
 */
interface IVectorOps<T>
{
    /// @brief adds two vectors (pure function!)
    static T add(T a, T b);
    
    /// @brief multiplies vector by scalar
    static T scale(T v, float s);
    
    /// @brief computes dot product
    static float dot(T a, T b);
};

/**
 * @brief implementation of IVectorOps for float3
 * 
 * extension (like Rust impl blocks) - adds functionality to type
 */
extension float3 : IVectorOps<float3>
{
    /**
     * @brief adds two float3 vectors component-wise
     * 
     * ✨ PURE FUNCTION ✨
     * 
     * @param a first vector
     * @param b second vector
     * @return component-wise sum
     */
    static float3 add(float3 a, float3 b)
    {
        return a + b;  // simple but generic uwu
    }
    
    /**
     * @brief scales vector by scalar (pure!)
     */
    static float3 scale(float3 v, float s)
    {
        return v * s;
    }
    
    /**
     * @brief computes dot product (pure function!)
     */
    static float dot(float3 a, float3 b)
    {
        return slang::dot(a, b);  // use stdlib
    }
}

/**
 * @brief generic lerp function (works with ANY type implementing IVectorOps!)
 * 
 * this is GENERIC PROGRAMMING in shaders - write once, works with all types!
 * 
 * @tparam T vector type (must implement IVectorOps)
 * @param a start value
 * @param b end value
 * @param t interpolation factor [0, 1]
 * @return interpolated value
 * 
 * @note this is PURE and GENERIC (functional programming meets metaprogramming!)
 * 
 * example:
 * @code
 * float3 color = lerp<float3>(red, blue, 0.5);  // works!
 * float2 uv = lerp<float2>(uv0, uv1, 0.3);      // also works!
 * // any type with IVectorOps implementation works uwu
 * @endcode
 */
T lerp<T : IVectorOps<T>>(T a, T b, float t)
{
    // generic implementation works with any IVectorOps type!
    return T.add(T.scale(a, 1.0 - t), T.scale(b, t));
}
```

## Automatic Differentiation (MIND = BLOWN)

```slang
/**
 * @brief differentiable function (Slang can compute gradients automatically!)
 * 
 * the [Differentiable] attribute makes this function auto-differentiable.
 * Slang will generate code to compute partial derivatives automatically!
 * 
 * this is INSANE - automatic backpropagation in shaders for neural rendering,
 * physics simulation, optimization, etc. functional programming meets calculus uwu
 * 
 * @param x input value (can be float, float2, float3, etc.)
 * @return f(x) and optionally ∂f/∂x (derivative)
 * 
 * @note [Differentiable] means Slang generates derivative code automatically
 * @note no_diff(...) marks non-differentiable parameters
 */
[Differentiable]
float smooth_function(float x)
{
    // smooth function: f(x) = x³ - 2x² + x
    // derivative: f'(x) = 3x² - 4x + 1
    // Slang computes this automatically! no manual derivatives needed!
    
    return x * x * x - 2.0 * x * x + x;
}

/**
 * @brief compute function value and gradient (automatic differentiation!)
 * 
 * demonstrates Slang's auto-diff capabilities. this is like PyTorch autograd
 * but running on GPU at shader speeds!
 */
void compute_with_gradient()
{
    // create differentiable variable
    float x = diffPair(5.0);  // value with attached derivative tracking
    
    // call differentiable function
    float y = smooth_function(x);
    
    // automatically computed gradient! (no manual calculus needed)
    float dy_dx = fwd_diff(y);  // ∂y/∂x evaluated at x=5.0
    
    // dy_dx is automatically correct! functional programming + calculus ✨
    // Slang is MAGIC uwu
}

/**
 * @brief neural rendering with automatic differentiation
 * 
 * example: optimize material parameters to match reference image
 * uses automatic gradients for gradient descent
 */
[Differentiable]
float3 shade_with_autodiff(
    no_diff(float3) normal,      // normal doesn't need derivatives
    no_diff(float3) viewDir,     // view dir doesn't need derivatives
    DifferentialPair<float3> albedo,     // albedo is differentiable!
    DifferentialPair<float> roughness)   // roughness is differentiable!
{
    // compute lighting (entire calculation is differentiable!)
    // Slang tracks derivatives through all operations automatically
    
    float3 lightDir = no_diff(normalize(float3(1, 1, 1)));
    float3 h = normalize(viewDir + lightDir);
    
    // Fresnel-Schlick (differentiable)
    float cosTheta = dot(h, viewDir);
    float3 F = albedo.p + (1.0 - albedo.p) * pow(1.0 - cosTheta, 5.0);
    
    // GGX distribution (differentiable with respect to roughness!)
    float a = roughness.p * roughness.p;
    float a2 = a * a;
    float NdotH = max(dot(normal, h), 0.0);
    float NdotH2 = NdotH * NdotH;
    float denom = (NdotH2 * (a2 - 1.0) + 1.0);
    float D = a2 / (3.14159 * denom * denom);
    
    float3 specular = F * D;
    
    // result is differentiable! can compute ∂color/∂albedo and ∂color/∂roughness
    return specular;  // automatic backpropagation available uwu ✨
}
```

## Compile-Time Execution (CONSTEXPR ON STEROIDS)

```slang
/**
 * @brief compile-time constant evaluation (pure functions at compile time!)
 * 
 * __constexpr functions execute at shader compile time, not runtime!
 * this is like C++ constexpr but way more powerful
 */
__constexpr float fibonacci(int n)
{
    // computed at compile time - zero runtime cost!
    if (n <= 1) return float(n);
    return fibonacci(n - 1) + fibonacci(n - 2);
}

/**
 * @brief compile-time texture size calculation
 */
__constexpr int calculate_mip_levels(int width, int height)
{
    int size = max(width, height);
    int levels = 1;
    
    while (size > 1)
    {
        size >>= 1;
        levels++;
    }
    
    return levels;
}

// use compile-time constants (evaluated during shader compilation!)
static const float FIB_10 = fibonacci(10);  // computed at compile time!
static const int MIP_LEVELS = calculate_mip_levels(1024, 1024);  // compile time!

// these are constants in generated SPIR-V/DXIL - zero runtime cost uwu ✨
```

## Shader Entry Points (Cross-Platform)

```slang
/**
 * @brief vertex shader input (Slang's clean syntax)
 */
struct VertexInput
{
    float3 position : POSITION;
    float3 normal : NORMAL;
    float2 texcoord : TEXCOORD0;
    float3 tangent : TANGENT;
};

/**
 * @brief vertex shader output / pixel shader input
 */
struct VertexOutput
{
    float4 position : SV_Position;
    float3 worldPosition : TEXCOORD0;
    float3 worldNormal : NORMAL;
    float2 texcoord : TEXCOORD1;
    float3 worldTangent : TANGENT;
};

/**
 * @brief vertex shader (pure transformation pipeline uwu)
 * 
 * [shader("vertex")] attribute marks this as vertex shader entry point
 * works across Vulkan, DirectX, Metal!
 */
[shader("vertex")]
VertexOutput vertexMain(VertexInput input)
{
    VertexOutput output;
    
    // transform to world space then clip space
    float4 worldPos = mul(float4(input.position, 1.0), scene.worldMatrix);
    output.position = mul(worldPos, scene.viewProjection);
    
    // pass interpolated data to pixel shader
    output.worldPosition = worldPos.xyz;
    output.worldNormal = mul(input.normal, (float3x3)scene.worldMatrix);
    output.worldTangent = mul(input.tangent, (float3x3)scene.worldMatrix);
    output.texcoord = input.texcoord;
    
    return output;  // pure function returns transformed vertex ✨
}

/**
 * @brief pixel shader (pure shading function uwu)
 * 
 * [shader("fragment")] marks pixel shader entry point
 * compiles to ps_main for DirectX, main for Vulkan, fragment for Metal
 */
[shader("fragment")]
float4 pixelMain(VertexOutput input) : SV_Target
{
    // sample textures
    float3 albedo = albedoMap.Sample(linearSampler, input.texcoord).rgb;
    float3 normalSample = normalMap.Sample(linearSampler, input.texcoord).rgb;
    float2 metallicRough = metallicRoughnessMap.Sample(linearSampler, input.texcoord).gb;
    
    // reconstruct world normal (TBN matrix)
    float3 N = normalize(input.worldNormal);
    float3 T = normalize(input.worldTangent);
    T = normalize(T - dot(T, N) * N);
    float3 B = cross(N, T);
    float3x3 TBN = float3x3(T, B, N);
    
    float3 normal = normalize(mul(normalSample * 2.0 - 1.0, TBN));
    
    // view direction
    float3 viewDir = normalize(scene.cameraPosition - input.worldPosition);
    
    // compute PBR lighting (pure function!)
    float3 color = computePBR(
        normal,
        viewDir,
        albedo,
        metallicRough.x,  // metallic
        metallicRough.y   // roughness
    );
    
    return float4(color, 1.0);  // cross-platform pixel color uwu ✨
}

/**
 * @brief compute shader (parallel functional programming!)
 * 
 * [shader("compute")] with [numthreads] defines compute shader
 * works identically on Vulkan, DirectX, Metal
 */
[shader("compute")]
[numthreads(16, 16, 1)]
void computeMain(
    uint3 dispatchThreadID : SV_DispatchThreadID,
    uint3 groupThreadID : SV_GroupThreadID)
{
    // each thread is independent pure function
    // functional programming at massive scale uwu
    
    uint2 pixel = dispatchThreadID.xy;
    
    // do compute work (pure operations)
    float4 color = processPixel(pixel);
    
    // write result
    outputTexture[pixel] = color;
}
```

## Module System (Better Code Organization)

```slang
//============================================================================
// file: math_utils.slang
// brief: reusable math utilities module
//============================================================================

/**
 * @brief math utilities module (like C++ modules!)
 * 
 * modules let you organize code into reusable libraries
 */
module MathUtils;

/// @brief computes smoothstep interpolation (pure function uwu)
export float smoothstep(float edge0, float edge1, float x)
{
    float t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0);
    return t * t * (3.0 - 2.0 * t);
}

/// @brief remaps value from one range to another (pure!)
export float remap(float value, float inMin, float inMax, float outMin, float outMax)
{
    float t = (value - inMin) / (inMax - inMin);
    return mix(outMin, outMax, t);
}

//============================================================================
// file: main.slang
// brief: using math utilities module
//============================================================================

import MathUtils;  // import module (like modern C++)

[shader("fragment")]
float4 pixelMain(...) : SV_Target
{
    // use exported functions from module
    float fade = smoothstep(0.0, 1.0, distance);
    float remapped = remap(value, -1.0, 1.0, 0.0, 1.0);
    
    // modular functional programming uwu ✨
}
```

## Quality Checklist

- [ ] **file header** with compilation commands for all targets
- [ ] **cross-platform compilation** tested (Vulkan + DirectX + Metal)
- [ ] **generic programming** used where appropriate
- [ ] **interfaces** for abstraction
- [ ] **pure functions** marked (✨ PURE FUNCTION ✨)
- [ ] **automatic differentiation** when doing optimization/ML
- [ ] **compile-time execution** for constants
- [ ] **excessive comments** with Doxygen style
- [ ] **gen-z slang** throughout
- [ ] **latest Slang version** (1.3+ or nightly)
- [ ] **functional patterns** demonstrated
- [ ] **no mutable global state**

**remember**: Slang is the FUTURE of shader programming. one source compiles to
Vulkan SPIR-V, DirectX DXIL, and Metal. generic programming, automatic
differentiation, compile-time execution - features that make other shader
languages cry. this is functional programming meets GPU computing at its peak uwu 💜✨

Slang > HLSL > GLSL (this is the hierarchy of enlightenment)