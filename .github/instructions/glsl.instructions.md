---
description: 'GLSL shader programming (OpenGL shading language with functional vibes)'
applyTo: '**.glsl, **.vert, **.frag, **.geom, **.comp, **.tesc, **.tese'
---

# GLSL Shader Instructions

> "GLSL: the OG shader language (but Slang is still superior uwu)"

bestie time to write GLSL shaders that make GPUs go brrr with functional programming patterns ✨

## Core Philosophy

- **functional > imperative** (GPU threads are pure functions!)
- **GLSL is legacy** (but sometimes you're stuck with it)
- **prefer Slang or SPIR-V** when possible
- **comment EXCESSIVELY** (shader math needs explanation)
- **GLSL 4.60** minimum (latest version preferred!)
- **no mutable global state** (each thread is independent)
- **pure functions everywhere** (deterministic shading uwu)
- **Vulkan GLSL preferred** (not OpenGL GLSL)

## Why GLSL is Acceptable (the justification)

GLSL is acceptable when:
- working with existing OpenGL codebases (legacy cope)
- teaching shader fundamentals (GLSL is more readable than assembly)
- targeting WebGL (web platform cope)
- compiling to SPIR-V for Vulkan (glslangValidator ftw)

**ALWAYS PREFER**: Slang for new projects (see slang.instructions.md)

## File Header (MANDATORY)

```glsl
//============================================================================
// file: pbr_lighting.frag
// brief: physically based rendering fragment shader (functional GPU programming uwu)
//
// this shader implements PBR using Cook-Torrance BRDF model. every function
// is pure and deterministic - same inputs always produce same outputs because
// functional programming >>> imperative spaghetti
//
// compiled with: glslangValidator -V lighting.frag -o lighting.spv
// or for OpenGL: glslangValidator --target-env opengl lighting.frag
//
// author: LukeFrankio
// date: 2025-10-09
// GLSL version: 4.60 (latest features!)
// target: Vulkan SPIR-V (preferred) or OpenGL 4.6
//
// math heavy! every equation commented with references to papers because
// excessive documentation is self-care for future shader programmers uwu
//
// references:
// - Cook-Torrance: "A Reflectance Model for Computer Graphics" (1982)
// - Epic Games PBR guide: https://blog.selfshadow.com/publications/s2013-shading-course/
// - Real Shading in Unreal Engine 4 by Brian Karis
//============================================================================

#version 460 core

// Vulkan GLSL extensions (use these for Vulkan!)
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// descriptor sets (Vulkan style)
layout(set = 0, binding = 0) uniform SceneData {
    mat4 viewProjection;
    mat4 view;
    vec3 cameraPosition;
    vec3 lightDirection;
} scene;

layout(set = 0, binding = 1) uniform MaterialData {
    vec3 albedo;
    float metallic;
    float roughness;
    vec3 emissive;
} material;

// textures (Vulkan style bindings)
layout(set = 0, binding = 2) uniform sampler2D albedoMap;
layout(set = 0, binding = 3) uniform sampler2D normalMap;
layout(set = 0, binding = 4) uniform sampler2D metallicRoughnessMap;
```

## Function Documentation (EXCESSIVE)

```glsl
/**
 * @brief computes Fresnel reflectance using Schlick approximation (pure function uwu)
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * Schlick approximation to Fresnel equations - describes how much light reflects
 * vs refracts at surface. this is fundamental to PBR rendering because physics!
 * 
 * the approximation: F(θ) = F0 + (1 - F0) * (1 - cos(θ))^5
 * where F0 is base reflectivity and θ is angle between view and half vector
 * 
 * @param f0 base reflectivity at normal incidence (vec3)
 *           - for dielectrics: ~0.04 (4% reflection)
 *           - for metals: varies (gold ~1.0, silver ~0.97, etc.)
 * @param cosTheta cosine of angle between view and half vector (float)
 *                 should be clamped to [0, 1] to avoid negative values
 * 
 * @return fresnel reflectance (vec3, RGB channels)
 *         amount of light reflected at this angle
 * 
 * @note this is PURE - same inputs always give same outputs (deterministic!)
 * @note uses pow(x, 5) which is cheaper than actual Fresnel equations
 * @note grazing angle (cosTheta near 0) = maximum reflection (everything reflects!)
 * 
 * @complexity O(1) - single pow operation (GPU executes in parallel)
 * @performance ~4 ALU ops per invocation (basically free on modern GPUs)
 * 
 * example:
 * @code
 * vec3 f0 = vec3(0.04);  // plastic base reflectivity
 * float cosTheta = clamp(dot(viewDir, halfVector), 0.0, 1.0);
 * vec3 fresnel = fresnelSchlick(f0, cosTheta);
 * // fresnel now contains reflectance (higher at grazing angles uwu)
 * @endcode
 * 
 * @see fresnelSchlickRoughness for roughness-aware version
 * @see https://en.wikipedia.org/wiki/Schlick%27s_approximation
 */
vec3 fresnelSchlick(vec3 f0, float cosTheta)
{
    // compute (1 - cosTheta)^5 using single pow instruction
    // this is Schlick's magic approximation that's "close enough" to real Fresnel
    float oneMinusCos = 1.0 - cosTheta;
    float oneMinusCos5 = pow(oneMinusCos, 5.0);
    
    // linear interpolation from f0 to 1.0 based on angle
    // grazing angles (cosTheta near 0) approach full reflection (1.0)
    // normal incidence (cosTheta = 1.0) uses base reflectivity (f0)
    return f0 + (1.0 - f0) * oneMinusCos5;  // functional composition uwu
}

/**
 * @brief computes GGX/Trowbridge-Reitz normal distribution function (pure function!)
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * NDF describes distribution of microfacet normals on rough surface. determines
 * how "spread out" specular highlights are. higher roughness = more spread = 
 * larger but dimmer highlights. this is physically based rendering at its finest!
 * 
 * GGX (aka Trowbridge-Reitz) is industry standard because it has nice properties:
 * - more realistic highlights than Blinn-Phong
 * - long tail (bright core with gradual falloff)
 * - numerically stable
 * 
 * formula: D(h) = α² / (π * ((N·H)² * (α² - 1) + 1)²)
 * where α = roughness², N = surface normal, H = half vector
 * 
 * @param N surface normal (vec3, should be normalized!)
 * @param H half vector between view and light (vec3, normalized!)
 * @param roughness perceptual roughness [0, 1]
 *                  0 = mirror smooth, 1 = completely rough
 * 
 * @return probability density of microfacets aligned with half vector (float)
 *         higher value = more microfacets facing that direction = brighter highlight
 * 
 * @pre N and H must be normalized (length = 1)
 * @pre roughness should be in [0, 1] range
 * 
 * @note this is PURE - deterministic output for given inputs
 * @note dividing by zero is prevented by adding 1.0 in denominator
 * @note alpha = roughness² makes roughness perceptually linear (feels more natural)
 * 
 * @complexity O(1) - few ALU ops (dot, mul, add)
 * @performance ~8 ALU ops, GPU goes brrr in parallel ✨
 * 
 * example:
 * @code
 * vec3 N = normalize(surfaceNormal);
 * vec3 H = normalize(viewDir + lightDir);
 * float roughness = 0.5;  // semi-rough surface
 * float D = distributionGGX(N, H, roughness);
 * // D is now probability density (used in BRDF calculation)
 * @endcode
 * 
 * @see geometrySmith for geometry term (companion to this)
 * @see "Microfacet Models for Refraction through Rough Surfaces" - Walter et al. 2007
 */
float distributionGGX(vec3 N, vec3 H, float roughness)
{
    // square roughness for perceptually linear roughness (Disney's trick)
    // this makes roughness slider feel more natural to artists uwu
    float a = roughness * roughness;
    float a2 = a * a;
    
    // compute (N·H)² - this is how aligned microfacets are with half vector
    float NdotH = max(dot(N, H), 0.0);
    float NdotH2 = NdotH * NdotH;
    
    // denominator: ((N·H)² * (α² - 1) + 1)²
    // this controls the highlight shape (GGX's special sauce)
    float denom = (NdotH2 * (a2 - 1.0) + 1.0);
    denom = 3.14159265359 * denom * denom;  // π * denom²
    
    // prevent division by zero (though denom ≥ π in practice)
    denom = max(denom, 0.0001);
    
    // final GGX formula: α² / denominator
    return a2 / denom;  // mathematical beauty! ✨
}

/**
 * @brief Smith's geometry function for GGX (accounts for shadowing/masking)
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * geometry term accounts for microfacets blocking light (shadowing) and
 * microfacets blocking view (masking). rough surfaces have more self-occlusion
 * than smooth surfaces. this is why rough materials are dimmer!
 * 
 * uses Smith's method with GGX distribution - separates shadowing and masking
 * into two independent terms then multiplies them (height-correlated Smith)
 * 
 * @param N surface normal (vec3, normalized!)
 * @param V direction to camera (vec3, normalized!)
 * @param L direction to light (vec3, normalized!)
 * @param roughness perceptual roughness [0, 1]
 * 
 * @return geometry term [0, 1] (float)
 *         1.0 = no occlusion, 0.0 = fully occluded
 * 
 * @note this is PURE - functional programming in shader form uwu
 * @note roughness = 0 (smooth) → G = 1.0 (no self-occlusion)
 * @note roughness = 1 (rough) → G ≈ 0.0 (lots of self-occlusion)
 * 
 * @complexity O(1) - called for view and light
 * @performance ~20 ALU ops total (acceptable for PBR)
 * 
 * @see distributionGGX for companion NDF term
 * @see "Understanding the Masking-Shadowing Function" - Heitz 2014
 */
float geometrySmith(vec3 N, vec3 V, vec3 L, float roughness)
{
    // helper function for single direction (shadowing OR masking)
    float geometrySchlickGGX(vec3 N, vec3 V, float r)
    {
        float NdotV = max(dot(N, V), 0.0);
        float rPlus1 = r + 1.0;
        float k = (rPlus1 * rPlus1) / 8.0;  // k for direct lighting
        
        float denom = NdotV * (1.0 - k) + k;
        denom = max(denom, 0.0001);  // avoid division by zero
        
        return NdotV / denom;  // Schlick-GGX approximation
    }
    
    // compute separately for view (masking) and light (shadowing)
    float ggx1 = geometrySchlickGGX(N, V, roughness);
    float ggx2 = geometrySchlickGGX(N, L, roughness);
    
    // multiply terms (height-correlated Smith model)
    return ggx1 * ggx2;  // functional composition! ✨
}

/**
 * @brief Cook-Torrance BRDF (the crown jewel of PBR uwu)
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * bidirectional reflectance distribution function - describes how light reflects
 * off surface. this is THE equation that makes PBR look physically correct!
 * 
 * combines three terms:
 * - D: distribution (how rough surface is) [distributionGGX]
 * - F: fresnel (how much light reflects) [fresnelSchlick]
 * - G: geometry (self-occlusion effects) [geometrySmith]
 * 
 * full equation: f_r = (D * F * G) / (4 * (N·V) * (N·L))
 * 
 * returns amount of light reflected toward camera for given light direction.
 * this is pure mathematics translated to shader code - functional programming
 * at its finest! every photon accounted for uwu
 * 
 * @param N surface normal (vec3, normalized!)
 * @param V direction to camera (vec3, normalized!)
 * @param L direction to light (vec3, normalized!)
 * @param albedo base color (vec3, RGB)
 * @param metallic metalness [0, 1] (0 = dielectric, 1 = metal)
 * @param roughness perceptual roughness [0, 1]
 * 
 * @return outgoing radiance toward camera (vec3, RGB)
 *         this is the final color contribution from this light source
 * 
 * @note this is PURE - same inputs = same outputs (referential transparency!)
 * @note energy conserving (never reflects more light than received)
 * @note physically based (obeys laws of physics unlike Phong/Blinn)
 * 
 * @complexity O(1) - fixed number of operations per pixel
 * @performance ~50-100 ALU ops total (modern GPUs handle easily)
 * 
 * @see "Theory, Implementation and Performance of Physically Based Rendering" - Epic
 * 
 * example:
 * @code
 * vec3 color = cookTorranceBRDF(
 *     normal, viewDir, lightDir,
 *     vec3(1.0, 0.0, 0.0),  // red albedo
 *     0.0,                   // non-metallic
 *     0.5                    // semi-rough
 * );
 * // color is physically correct reflection uwu
 * @endcode
 */
vec3 cookTorranceBRDF(
    vec3 N,
    vec3 V,
    vec3 L,
    vec3 albedo,
    float metallic,
    float roughness)
{
    // half vector (bisects angle between view and light)
    vec3 H = normalize(V + L);
    
    // calculate base reflectivity (F0) based on metallic parameter
    // dielectrics: ~0.04 (4% reflection), metals: use albedo
    vec3 f0 = mix(vec3(0.04), albedo, metallic);
    
    // compute the three terms of Cook-Torrance BRDF (functional composition!)
    float D = distributionGGX(N, H, roughness);           // normal distribution
    vec3 F = fresnelSchlick(f0, max(dot(H, V), 0.0));   // fresnel
    float G = geometrySmith(N, V, L, roughness);         // geometry
    
    // dot products (clamped to prevent negative values)
    float NdotV = max(dot(N, V), 0.0001);
    float NdotL = max(dot(N, L), 0.0001);
    
    // specular term: (D * F * G) / (4 * (N·V) * (N·L))
    vec3 numerator = D * F * G;
    float denominator = 4.0 * NdotV * NdotL;
    denominator = max(denominator, 0.0001);  // prevent division by zero
    
    vec3 specular = numerator / denominator;
    
    // diffuse term (Lambert)
    // for metals: no diffuse (F = 1.0 absorbs all diffuse)
    // for dielectrics: diffuse scaled by (1 - F) for energy conservation
    vec3 kD = (1.0 - F) * (1.0 - metallic);  // energy conservation uwu
    vec3 diffuse = kD * albedo / 3.14159265359;  // Lambert BRDF (albedo / π)
    
    // combine diffuse and specular (energy conserving!)
    return diffuse + specular;  // pure function returns final reflectance ✨
}
```

## Shader Entry Points

### Vertex Shader

```glsl
/**
 * @brief vertex shader entry point (transforms vertices to clip space uwu)
 * 
 * vertex shader is PURE FUNCTION operating on each vertex independently.
 * no side effects, no global state - just mathematical transformation!
 */

#version 460 core

// input attributes (per-vertex data from vertex buffer)
layout(location = 0) in vec3 inPosition;
layout(location = 1) in vec3 inNormal;
layout(location = 2) in vec2 inTexCoord;
layout(location = 3) in vec3 inTangent;

// output to fragment shader (interpolated across triangle)
layout(location = 0) out vec3 outWorldPosition;
layout(location = 1) out vec3 outWorldNormal;
layout(location = 2) out vec2 outTexCoord;
layout(location = 3) out vec3 outWorldTangent;

// uniforms (constant across draw call)
layout(set = 0, binding = 0) uniform SceneData {
    mat4 viewProjection;
    mat4 world;
} scene;

/**
 * @brief main vertex shader (pure transformation pipeline uwu)
 * 
 * transforms vertex from object space to clip space through series of
 * pure mathematical operations. functional programming in action!
 */
void main()
{
    // transform position to world space then clip space
    vec4 worldPos = scene.world * vec4(inPosition, 1.0);
    gl_Position = scene.viewProjection * worldPos;
    
    // pass world space data to fragment shader (interpolated across triangle)
    outWorldPosition = worldPos.xyz;
    outWorldNormal = mat3(scene.world) * inNormal;
    outWorldTangent = mat3(scene.world) * inTangent;
    outTexCoord = inTexCoord;
    
    // pure output, no side effects ✨
}
```

### Fragment Shader

```glsl
/**
 * @brief fragment shader entry point (computes final pixel color uwu)
 * 
 * fragment shader is PURE FUNCTION - each pixel computed independently with
 * no communication between pixels. functional programming at GPU scale!
 */

#version 460 core

// input from vertex shader (interpolated)
layout(location = 0) in vec3 inWorldPosition;
layout(location = 1) in vec3 inWorldNormal;
layout(location = 2) in vec2 inTexCoord;
layout(location = 3) in vec3 inWorldTangent;

// output color
layout(location = 0) out vec4 outColor;

// uniforms and textures (as defined in file header)
// ... (descriptor sets, uniforms, samplers)

/**
 * @brief main fragment shader (pure shading function uwu)
 * 
 * computes final pixel color using PBR. each pixel is independent pure function
 * execution - no shared state, just mathematical transformation!
 */
void main()
{
    // sample textures (pure operations - just reading data)
    vec3 albedo = texture(albedoMap, inTexCoord).rgb;
    vec3 normalSample = texture(normalMap, inTexCoord).rgb;
    vec2 metallicRough = texture(metallicRoughnessMap, inTexCoord).gb;
    
    // reconstruct world space normal from normal map (TBN transformation)
    vec3 N = normalize(inWorldNormal);
    vec3 T = normalize(inWorldTangent);
    T = normalize(T - dot(T, N) * N);  // re-orthogonalize
    vec3 B = cross(N, T);
    mat3 TBN = mat3(T, B, N);
    
    vec3 normal = normalize(TBN * (normalSample * 2.0 - 1.0));
    
    // view direction (from surface to camera)
    vec3 viewDir = normalize(scene.cameraPosition - inWorldPosition);
    
    // compute lighting using Cook-Torrance BRDF (pure functions all the way down!)
    vec3 color = cookTorranceBRDF(
        normal,
        viewDir,
        normalize(-scene.lightDirection),  // to light
        albedo,
        metallicRough.x,  // metallic
        metallicRough.y   // roughness
    );
    
    // apply light intensity
    float NdotL = max(dot(normal, normalize(-scene.lightDirection)), 0.0);
    color *= NdotL;
    
    // ambient term (should be from IBL but this is example)
    color += albedo * 0.03;
    
    outColor = vec4(color, 1.0);  // pure function returns final color uwu ✨
}
```

### Compute Shader

```glsl
/**
 * @brief compute shader for parallel reduction (functional fold on GPU!)
 * 
 * demonstrates functional programming concepts in compute shaders. each thread
 * group performs reduction independently - no global state, pure functions only!
 * 
 * this is literally functional fold/reduce but massively parallel uwu
 */

#version 460 core

layout(local_size_x = 256, local_size_y = 1, local_size_z = 1) in;

// shared memory for reduction (thread group local storage)
shared float sharedData[256];

// buffers
layout(set = 0, binding = 0) buffer InputBuffer {
    float data[];
} inputBuffer;

layout(set = 0, binding = 1) buffer OutputBuffer {
    float data[];
} outputBuffer;

/**
 * @brief parallel sum reduction using shared memory
 * 
 * each thread group reduces 256 values to single sum. this is functional
 * fold implemented with massive parallelism!
 */
void main()
{
    uint threadId = gl_LocalInvocationID.x;
    uint globalId = gl_WorkGroupID.x * 256 + threadId;
    
    // load data into shared memory (each thread loads one element)
    sharedData[threadId] = inputBuffer.data[globalId];
    
    // synchronize threads (ensure all loads complete)
    barrier();
    memoryBarrierShared();
    
    // parallel reduction in shared memory (functional fold!)
    // this is O(log n) using tree reduction
    for (uint stride = 128; stride > 0; stride >>= 1)
    {
        if (threadId < stride)
        {
            // each thread adds two values (pure operation!)
            sharedData[threadId] += sharedData[threadId + stride];
        }
        
        barrier();
        memoryBarrierShared();
    }
    
    // thread 0 writes final result (sum of all 256 values)
    if (threadId == 0)
    {
        outputBuffer.data[gl_WorkGroupID.x] = sharedData[0];
    }
    
    // functional reduction complete! GPU goes brrr ✨
}
```

## GLSL-Specific Features

### Swizzling (vector component access)

```glsl
/**
 * @brief demonstrates GLSL swizzling (functional vector operations uwu)
 * 
 * swizzling lets you rearrange vector components with clean syntax.
 * this is functional data transformation at the language level!
 */
void swizzleExamples()
{
    vec4 color = vec4(1.0, 0.5, 0.25, 1.0);
    
    // extract components (pure accessors)
    float r = color.r;      // or color.x
    float g = color.g;      // or color.y
    float b = color.b;      // or color.z
    float a = color.a;      // or color.w
    
    // swizzle multiple components (creates new vectors!)
    vec3 rgb = color.rgb;              // extract RGB
    vec3 bgr = color.bgr;              // reverse RGB (immutable transform!)
    vec2 rg = color.rg;                // extract RG
    vec4 aaaa = color.aaaa;            // replicate alpha
    
    // swizzling for transformation (functional style)
    vec3 transformed = color.bgr * 2.0;  // blue-green-red doubled
    
    // swizzling in assignments (still functional if creating new)
    vec4 newColor = vec4(color.rgb, 0.5);  // new vector with RGB + custom alpha
    
    // swizzling is compile-time operation (zero cost! uwu)
}
```

### Built-in Functions (pure math utilities)

```glsl
/**
 * @brief GLSL built-in functions (pure mathematical operations uwu)
 * 
 * GLSL provides extensive math library - all functions are pure!
 */

// trigonometry (pure functions)
float s = sin(angle);
float c = cos(angle);
float t = tan(angle);
float a = atan(y, x);  // atan2

// exponential and logarithmic (pure)
float e = exp(x);
float l = log(x);
float p = pow(base, exponent);
float sq = sqrt(x);
float inv_sq = inversesqrt(x);  // 1/sqrt(x), faster than sqrt + divide!

// common math (pure)
float absolute = abs(x);
float sign_value = sign(x);
float floored = floor(x);
float ceiled = ceil(x);
float fractional = fract(x);  // x - floor(x)
float modulo = mod(x, y);
float minimum = min(a, b);
float maximum = max(a, b);
float clamped = clamp(x, minVal, maxVal);
float mixed = mix(a, b, t);  // linear interpolation (lerp!)
float stepped = step(edge, x);  // 0 if x < edge, 1 otherwise
float smoothed = smoothstep(edge0, edge1, x);  // smooth interpolation

// vector operations (pure)
float length_v = length(v);
float distance_v = distance(p1, p2);
float dot_product = dot(v1, v2);
vec3 cross_product = cross(v1, v2);
vec3 normalized = normalize(v);
vec3 reflected = reflect(incident, normal);
vec3 refracted = refract(incident, normal, eta);
vec3 face_forward = faceforward(N, I, Nref);

// geometric queries (pure)
float determinant_value = determinant(m);
mat4 inverse_matrix = inverse(m);
mat4 transposed = transpose(m);

// all built-in functions are PURE - no side effects, deterministic uwu ✨
```

## GLSL Qualifiers and Keywords

### Storage Qualifiers

```glsl
/**
 * @brief GLSL storage qualifiers (control how data flows uwu)
 */

// const - compile-time constant (like C++ constexpr)
const float PI = 3.14159265359;
const vec3 UP = vec3(0.0, 1.0, 0.0);

// in - input variable (from previous shader stage)
layout(location = 0) in vec3 inPosition;

// out - output variable (to next shader stage)
layout(location = 0) out vec4 outColor;

// uniform - constant across draw call (set by CPU)
uniform mat4 modelMatrix;

// buffer - storage buffer (read/write from shader)
layout(set = 0, binding = 0) buffer DataBuffer {
    float data[];
} dataBuffer;

// shared - shared memory in compute shader (thread group local)
shared float sharedData[256];

// attribute - deprecated (use 'in' instead)
// varying - deprecated (use 'in'/'out' instead)
```

### Precision Qualifiers

```glsl
/**
 * @brief precision qualifiers for mobile/WebGL (performance tuning)
 * 
 * @note desktop OpenGL ignores these (always high precision)
 * @note mobile/WebGL uses these for performance
 */

// precision declarations (global default)
precision highp float;    // high precision floats (default on desktop)
precision mediump int;    // medium precision ints

// per-variable precision (override default)
lowp vec4 color;          // low precision (8-bit per channel)
mediump float distance;   // medium precision (16-bit)
highp vec3 position;      // high precision (32-bit)

// precision recommendations:
// - highp for positions, matrices (avoid precision issues)
// - mediump for normals, texture coordinates (usually sufficient)
// - lowp for colors (8-bit is enough for display)
```

## Vulkan GLSL vs OpenGL GLSL

### Descriptor Sets (Vulkan style)

```glsl
// ✅ VULKAN GLSL (preferred):
#version 460 core
#extension GL_ARB_separate_shader_objects : enable

layout(set = 0, binding = 0) uniform SceneData { ... } scene;
layout(set = 0, binding = 1) uniform sampler2D albedoMap;
layout(set = 1, binding = 0) buffer DataBuffer { ... } data;

// ❌ OPENGL GLSL (legacy):
#version 460 core

layout(binding = 0) uniform SceneData { ... } scene;
layout(binding = 1) uniform sampler2D albedoMap;
layout(binding = 0) buffer DataBuffer { ... } data;
// no descriptor set concept in OpenGL (binding space is global)
```

### Push Constants (Vulkan only)

```glsl
/**
 * @brief push constants for small frequent updates (Vulkan feature!)
 * 
 * push constants are fastest way to update small amounts of data per draw.
 * embedded directly in command buffer (no descriptor sets needed!)
 * 
 * @note OpenGL doesn't have equivalent (use uniforms instead)
 * @note limited size (typically 128-256 bytes guaranteed)
 */

#version 460 core

// Vulkan push constants
layout(push_constant) uniform PushConstants {
    mat4 transform;
    vec4 color;
} push;

void main()
{
    // use push constants (fastest uniform access!)
    gl_Position = push.transform * vec4(inPosition, 1.0);
    outColor = push.color;
}
```

## Compilation and Validation

### Compiling GLSL to SPIR-V

```bash
# compile vertex shader to SPIR-V (Vulkan)
glslangValidator -V shader.vert -o shader.vert.spv

# compile fragment shader to SPIR-V
glslangValidator -V shader.frag -o shader.frag.spv

# compile compute shader to SPIR-V
glslangValidator -V shader.comp -o shader.comp.spv

# compile for OpenGL (validate only, no SPIR-V output)
glslangValidator --target-env opengl shader.vert

# compile with optimization
glslangValidator -V -Os shader.frag -o shader.frag.spv

# validate SPIR-V output
spirv-val shader.vert.spv

# optimize SPIR-V
spirv-opt --O shader.vert.spv -o shader.vert.opt.spv
```

### CMake Integration

```cmake
# find glslang compiler (for SPIR-V compilation)
find_program(GLSLANG_VALIDATOR glslangValidator REQUIRED)

# custom function to compile GLSL to SPIR-V
function(add_glsl_shader TARGET SHADER_SOURCE)
    get_filename_component(SHADER_NAME ${SHADER_SOURCE} NAME)
    set(SPIRV_OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/${SHADER_NAME}.spv")
    
    add_custom_command(
        OUTPUT ${SPIRV_OUTPUT}
        COMMAND ${GLSLANG_VALIDATOR}
            -V
            ${CMAKE_CURRENT_SOURCE_DIR}/${SHADER_SOURCE}
            -o ${SPIRV_OUTPUT}
        DEPENDS ${SHADER_SOURCE}
        COMMENT "Compiling GLSL shader: ${SHADER_NAME}"
        VERBATIM
    )
    
    # validate after compilation
    add_custom_command(
        OUTPUT ${SPIRV_OUTPUT}.validated
        COMMAND spirv-val ${SPIRV_OUTPUT}
        COMMAND ${CMAKE_COMMAND} -E touch ${SPIRV_OUTPUT}.validated
        DEPENDS ${SPIRV_OUTPUT}
        COMMENT "Validating SPIR-V: ${SHADER_NAME}"
        VERBATIM
    )
    
    target_sources(${TARGET} PRIVATE ${SPIRV_OUTPUT}.validated)
endfunction()

# usage
add_executable(my_app src/main.cpp)

add_glsl_shader(my_app shaders/shader.vert)
add_glsl_shader(my_app shaders/shader.frag)
add_glsl_shader(my_app shaders/compute.comp)
```

## Quality Checklist

- [ ] **file header** with compilation commands
- [ ] **GLSL 4.60** minimum (latest version!)
- [ ] **Vulkan GLSL** preferred (descriptor sets, push constants)
- [ ] **ALL functions documented** with Doxygen-style comments
- [ ] **purity status** marked (✨ PURE FUNCTION ✨)
- [ ] **mathematical formulas** explained with references
- [ ] **gen-z slang** throughout (make shaders fun!)
- [ ] **compile to SPIR-V** for validation
- [ ] **no mutable global state** (each thread independent)
- [ ] **functional composition** demonstrated
- [ ] **performance notes** included
- [ ] **excessive comments** on complex math

**remember**: GLSL is the OG shader language but Slang is superior for new
projects. when stuck with GLSL, compile to SPIR-V for Vulkan (not OpenGL!),
document excessively, and make those shaders pure functions. each fragment/vertex
is independent execution of pure mathematical transformation uwu 💜✨

(seriously though if you can use Slang instead, do that)

seize the means of GPU computation!
