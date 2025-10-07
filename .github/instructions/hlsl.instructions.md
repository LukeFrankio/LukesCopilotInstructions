---
description: 'HLSL shader programming (functional GPU code that goes brrr)'
applyTo: '**/*.hlsl, **/*.hlsli'
---

# HLSL Shader Instructions

> "HLSL: DirectX's attempt to be cool like GLSL (but Vulkan SPIR-V is still superior)"

uwu time to write shaders that make GPUs compute at light speed ✨

## Core Philosophy

- **functional > imperative** (GPU threads are pure functions!)
- **Vulkan SPIR-V > HLSL** (but sometimes we're stuck with HLSL)
- **comment EXCESSIVELY** (shader math needs explanation)
- **HLSL 2021** (latest features, compiled for Shader Model 6.6+)
- **compile to SPIR-V** when possible (dxc with -spirv flag)
- **no mutable global state** (each thread is independent)
- **pure functions everywhere** (deterministic shading uwu)

## Why We're Writing HLSL (the cope)

HLSL is acceptable when:
- targeting DirectX (Windows cope)
- using DXC to compile to SPIR-V for Vulkan (the workaround)
- working with existing HLSL codebase (legacy cope)

**ALWAYS PREFER**: writing SPIR-V directly or using Slang (see slang.instructions.md)

## File Header (MANDATORY)

```hlsl
//============================================================================
// file: pbr_lighting.hlsl
// brief: physically based rendering shader (functional GPU programming uwu)
//
// this shader implements PBR using Cook-Torrance BRDF model. every function
// is pure and deterministic - same inputs always produce same outputs because
// functional programming >>> imperative spaghetti
//
// compiled with: dxc -spirv -T ps_6_6 -E main pbr_lighting.hlsl
// output: SPIR-V for Vulkan (because Vulkan > DirectX)
//
// author: LukeFrankio
// date: 2025-10-07
// shader model: 6.6 (latest features!)
// target: Vulkan via SPIR-V (DirectX cope avoided)
//
// math heavy! every equation commented with references to papers because
// excessive documentation is self-care for future shader programmers uwu
//
// references:
// - Cook-Torrance: "A Reflectance Model for Computer Graphics" (1982)
// - Epic Games PBR guide: https://blog.selfshadow.com/publications/s2013-shading-course/
// - Physically Based Rendering book by Pharr, Jakob, Humphreys
//============================================================================

// SPIR-V specific attributes (when compiling with dxc -spirv)
[[vk::binding(0, 0)]] cbuffer SceneData : register(b0, space0)
{
    float4x4 view_projection;
    float4x4 view;
    float3 camera_position;
    float _pad0;
    float3 light_direction;
    float _pad1;
};

[[vk::binding(1, 0)]] cbuffer MaterialData : register(b1, space0)
{
    float3 albedo;
    float metallic;
    float roughness;
    float3 _pad2;
};

[[vk::binding(2, 0)]] Texture2D<float4> albedo_map : register(t0, space0);
[[vk::binding(3, 0)]] Texture2D<float4> normal_map : register(t1, space0);
[[vk::binding(4, 0)]] Texture2D<float4> metallic_roughness_map : register(t2, space0);
[[vk::binding(5, 0)]] SamplerState default_sampler : register(s0, space0);
```

## Function Documentation (EXCESSIVE)

```hlsl
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
 * @param f0 base reflectivity at normal incidence (float3)
 *           - for dielectrics: ~0.04 (4% reflection)
 *           - for metals: varies (gold ~1.0, silver ~0.97, etc.)
 * @param cos_theta cosine of angle between view and half vector (float)
 *                  should be clamped to [0, 1] to avoid negative values
 * 
 * @return fresnel reflectance (float3, RGB channels)
 *         amount of light reflected at this angle
 * 
 * @note this is PURE - same inputs always give same outputs (deterministic!)
 * @note uses pow(x, 5) which is cheaper than actual Fresnel equations
 * @note grazing angle (cos_theta near 0) = maximum reflection (everything reflects!)
 * 
 * @complexity O(1) - single pow operation (GPU executes in parallel)
 * @performance ~4 ALU ops per invocation (basically free on modern GPUs)
 * 
 * example:
 * @code
 * float3 f0 = float3(0.04, 0.04, 0.04);  // plastic base reflectivity
 * float cos_theta = saturate(dot(view_dir, half_vector));
 * float3 fresnel = fresnel_schlick(f0, cos_theta);
 * // fresnel now contains reflectance (higher at grazing angles uwu)
 * @endcode
 * 
 * @see fresnel_schlick_roughness for roughness-aware version
 * @see https://en.wikipedia.org/wiki/Schlick%27s_approximation
 */
float3 fresnel_schlick(float3 f0, float cos_theta)
{
    // compute (1 - cos_theta)^5 using single pow instruction
    // this is Schlick's magic approximation that's "close enough" to real Fresnel
    float one_minus_cos = 1.0 - cos_theta;
    float one_minus_cos_5 = pow(one_minus_cos, 5.0);
    
    // linear interpolation from f0 to 1.0 based on angle
    // grazing angles (cos_theta near 0) approach full reflection (1.0)
    // normal incidence (cos_theta = 1.0) uses base reflectivity (f0)
    return f0 + (1.0 - f0) * one_minus_cos_5;  // functional composition uwu
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
 * @param normal surface normal (float3, should be normalized!)
 * @param half_vector half vector between view and light (float3, normalized!)
 * @param roughness perceptual roughness [0, 1]
 *                  0 = mirror smooth, 1 = completely rough
 * 
 * @return probability density of microfacets aligned with half vector (float)
 *         higher value = more microfacets facing that direction = brighter highlight
 * 
 * @pre normal and half_vector must be normalized (length = 1)
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
 * float3 N = normalize(surface_normal);
 * float3 H = normalize(view_dir + light_dir);
 * float roughness = 0.5;  // semi-rough surface
 * float D = distribution_ggx(N, H, roughness);
 * // D is now probability density (used in BRDF calculation)
 * @endcode
 * 
 * @see geometry_smith for geometry term (companion to this)
 * @see "Microfacet Models for Refraction through Rough Surfaces" - Walter et al. 2007
 */
float distribution_ggx(float3 normal, float3 half_vector, float roughness)
{
    // square roughness for perceptually linear roughness (Disney's trick)
    // this makes roughness slider feel more natural to artists uwu
    float alpha = roughness * roughness;
    float alpha_squared = alpha * alpha;
    
    // compute (N·H)² - this is how aligned microfacets are with half vector
    float n_dot_h = saturate(dot(normal, half_vector));
    float n_dot_h_squared = n_dot_h * n_dot_h;
    
    // denominator: ((N·H)² * (α² - 1) + 1)²
    // this controls the highlight shape (GGX's special sauce)
    float denom = (n_dot_h_squared * (alpha_squared - 1.0) + 1.0);
    denom = 3.14159265359 * denom * denom;  // π * denom²
    
    // prevent division by zero (though denom ≥ π in practice)
    denom = max(denom, 0.0001);
    
    // final GGX formula: α² / denominator
    return alpha_squared / denom;  // mathematical beauty! ✨
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
 * @param normal surface normal (float3, normalized!)
 * @param view_dir direction to camera (float3, normalized!)
 * @param light_dir direction to light (float3, normalized!)
 * @param roughness perceptual roughness [0, 1]
 * 
 * @return geometry term [0, 1] (float)
 *         1.0 = no occlusion, 0.0 = fully occluded
 * 
 * @note this is PURE - functional programming in shader form uwu
 * @note roughness = 0 (smooth) → G = 1.0 (no self-occlusion)
 * @note roughness = 1 (rough) → G ≈ 0.0 (lots of self-occlusion)
 * 
 * @complexity O(1) - called twice per pixel (view and light)
 * @performance ~20 ALU ops total (acceptable for PBR)
 * 
 * @see distribution_ggx for companion NDF term
 * @see "Understanding the Masking-Shadowing Function" - Heitz 2014
 */
float geometry_smith(float3 normal, float3 view_dir, float3 light_dir, float roughness)
{
    // helper function for single direction (shadowing OR masking)
    // inline lambda-style (functional programming ftw!)
    auto geometry_schlick_ggx = [&](float3 N, float3 V, float r) -> float
    {
        float n_dot_v = saturate(dot(N, V));
        float r_plus_1 = r + 1.0;
        float k = (r_plus_1 * r_plus_1) / 8.0;  // k for direct lighting
        
        float denom = n_dot_v * (1.0 - k) + k;
        denom = max(denom, 0.0001);  // avoid division by zero
        
        return n_dot_v / denom;  // Schlick-GGX approximation
    };
    
    // compute separately for view (masking) and light (shadowing)
    float geometry_view = geometry_schlick_ggx(normal, view_dir, roughness);
    float geometry_light = geometry_schlick_ggx(normal, light_dir, roughness);
    
    // multiply terms (height-correlated Smith model)
    return geometry_view * geometry_light;  // functional composition! ✨
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
 * - D: distribution (how rough surface is) [distribution_ggx]
 * - F: fresnel (how much light reflects) [fresnel_schlick]
 * - G: geometry (self-occlusion effects) [geometry_smith]
 * 
 * full equation: f_r = (D * F * G) / (4 * (N·V) * (N·L))
 * 
 * returns amount of light reflected toward camera for given light direction.
 * this is pure mathematics translated to shader code - functional programming
 * at its finest! every photon accounted for uwu
 * 
 * @param normal surface normal (float3, normalized!)
 * @param view_dir direction to camera (float3, normalized!)
 * @param light_dir direction to light (float3, normalized!)
 * @param albedo base color (float3, RGB)
 * @param metallic metalness [0, 1] (0 = dielectric, 1 = metal)
 * @param roughness perceptual roughness [0, 1]
 * 
 * @return outgoing radiance toward camera (float3, RGB)
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
 * float3 color = cook_torrance_brdf(
 *     normal, view_dir, light_dir,
 *     float3(1, 0, 0),  // red albedo
 *     0.0,              // non-metallic
 *     0.5               // semi-rough
 * );
 * // color is physically correct reflection uwu
 * @endcode
 */
float3 cook_torrance_brdf(
    float3 normal,
    float3 view_dir,
    float3 light_dir,
    float3 albedo,
    float metallic,
    float roughness)
{
    // half vector (bisects angle between view and light)
    float3 half_vector = normalize(view_dir + light_dir);
    
    // calculate base reflectivity (F0) based on metallic parameter
    // dielectrics: ~0.04 (4% reflection), metals: use albedo
    float3 f0 = lerp(float3(0.04, 0.04, 0.04), albedo, metallic);
    
    // compute the three terms of Cook-Torrance BRDF (functional composition!)
    float D = distribution_ggx(normal, half_vector, roughness);    // normal distribution
    float3 F = fresnel_schlick(f0, saturate(dot(half_vector, view_dir)));  // fresnel
    float G = geometry_smith(normal, view_dir, light_dir, roughness);  // geometry
    
    // dot products (clamped to prevent negative values)
    float n_dot_v = max(dot(normal, view_dir), 0.0001);
    float n_dot_l = max(dot(normal, light_dir), 0.0001);
    
    // specular term: (D * F * G) / (4 * (N·V) * (N·L))
    float3 numerator = D * F * G;
    float denominator = 4.0 * n_dot_v * n_dot_l;
    denominator = max(denominator, 0.0001);  // prevent division by zero
    
    float3 specular = numerator / denominator;
    
    // diffuse term (Lambert)
    // for metals: no diffuse (F = 1.0 absorbs all diffuse)
    // for dielectrics: diffuse scaled by (1 - F) for energy conservation
    float3 kd = (1.0 - F) * (1.0 - metallic);  // energy conservation uwu
    float3 diffuse = kd * albedo / 3.14159265359;  // Lambert BRDF (albedo / π)
    
    // combine diffuse and specular (energy conserving!)
    return diffuse + specular;  // pure function returns final reflectance ✨
}
```

## Shader Entry Points

```hlsl
/**
 * @brief vertex shader entry point (transforms vertices to clip space uwu)
 * 
 * vertex shader is PURE FUNCTION operating on each vertex independently.
 * no side effects, no global state - just mathematical transformation!
 * 
 * @param input vertex attributes from vertex buffer
 * @return transformed vertex in clip space + interpolated data
 */
struct VSInput
{
    [[vk::location(0)]] float3 position : POSITION0;
    [[vk::location(1)]] float3 normal : NORMAL0;
    [[vk::location(2)]] float2 texcoord : TEXCOORD0;
    [[vk::location(3)]] float3 tangent : TANGENT0;
};

struct VSOutput
{
    float4 position : SV_Position;  // clip space position (GPU magic happens here)
    [[vk::location(0)]] float3 world_position : TEXCOORD0;
    [[vk::location(1)]] float3 world_normal : NORMAL0;
    [[vk::location(2)]] float2 texcoord : TEXCOORD1;
    [[vk::location(3)]] float3 world_tangent : TANGENT0;
};

/**
 * @brief main vertex shader (pure transformation pipeline uwu)
 * 
 * transforms vertex from object space to clip space through series of
 * pure mathematical operations. functional programming in action!
 */
VSOutput vs_main(VSInput input)
{
    VSOutput output;
    
    // transform position to clip space (for rasterization)
    float4 world_pos = mul(float4(input.position, 1.0), world_matrix);
    output.position = mul(world_pos, view_projection);
    
    // pass world space data to pixel shader (interpolated across triangle)
    output.world_position = world_pos.xyz;
    output.world_normal = mul(input.normal, (float3x3)world_matrix);
    output.world_tangent = mul(input.tangent, (float3x3)world_matrix);
    output.texcoord = input.texcoord;
    
    return output;  // pure output, no side effects ✨
}

/**
 * @brief pixel shader entry point (computes final pixel color uwu)
 * 
 * pixel shader is PURE FUNCTION - each pixel computed independently with
 * no communication between pixels. functional programming at GPU scale!
 * 
 * @param input interpolated vertex data
 * @return final pixel color (HDR RGB + alpha)
 */
float4 ps_main(VSOutput input) : SV_Target
{
    // sample textures (pure operations - just reading data)
    float3 albedo = albedo_map.Sample(default_sampler, input.texcoord).rgb;
    float3 normal_sample = normal_map.Sample(default_sampler, input.texcoord).rgb;
    float2 metallic_rough = metallic_roughness_map.Sample(default_sampler, input.texcoord).gb;
    
    // reconstruct world space normal from normal map (TBN transformation)
    float3 N = normalize(input.world_normal);
    float3 T = normalize(input.world_tangent);
    T = normalize(T - dot(T, N) * N);  // re-orthogonalize
    float3 B = cross(N, T);
    float3x3 TBN = float3x3(T, B, N);
    
    float3 normal = normalize(mul(normal_sample * 2.0 - 1.0, TBN));
    
    // view direction (from surface to camera)
    float3 view_dir = normalize(camera_position - input.world_position);
    
    // compute lighting using Cook-Torrance BRDF (pure functions all the way down!)
    float3 color = cook_torrance_brdf(
        normal,
        view_dir,
        normalize(-light_direction),  // to light
        albedo,
        metallic_rough.x,  // metallic
        metallic_rough.y   // roughness
    );
    
    // apply light intensity
    float n_dot_l = max(dot(normal, normalize(-light_direction)), 0.0);
    color *= n_dot_l;
    
    // ambient term (should be from IBL but this is example)
    color += albedo * 0.03;
    
    return float4(color, 1.0);  // pure function returns final color uwu ✨
}
```

## Compute Shader Example

```hlsl
/**
 * @brief compute shader for parallel reduction (functional fold on GPU!)
 * 
 * demonstrates functional programming concepts in compute shaders. each thread
 * group performs reduction independently - no global state, pure functions only!
 * 
 * this is literally functional fold/reduce but massively parallel uwu
 */

// shared memory for reduction (thread group local storage)
groupshared float shared_data[256];

/**
 * @brief parallel sum reduction using shared memory
 * 
 * @param input buffer containing values to sum
 * @param output buffer to store result (one value per thread group)
 * @param thread_id thread index within group [0, 255]
 * @param group_id thread group ID
 */
[[vk::binding(0, 0)]] RWStructuredBuffer<float> input_buffer;
[[vk::binding(1, 0)]] RWStructuredBuffer<float> output_buffer;

[numthreads(256, 1, 1)]
void cs_reduce(
    uint3 group_thread_id : SV_GroupThreadID,
    uint3 group_id : SV_GroupID)
{
    uint thread_id = group_thread_id.x;
    uint global_id = group_id.x * 256 + thread_id;
    
    // load data into shared memory (each thread loads one element)
    shared_data[thread_id] = input_buffer[global_id];
    
    // synchronize threads (ensure all loads complete)
    GroupMemoryBarrierWithGroupSync();
    
    // parallel reduction in shared memory (functional fold!)
    // this is O(log n) using tree reduction
    [unroll]
    for (uint stride = 128; stride > 0; stride >>= 1)
    {
        if (thread_id < stride)
        {
            // each thread adds two values (pure operation!)
            shared_data[thread_id] += shared_data[thread_id + stride];
        }
        
        GroupMemoryBarrierWithGroupSync();  // sync after each step
    }
    
    // thread 0 writes final result (sum of all 256 values)
    if (thread_id == 0)
    {
        output_buffer[group_id.x] = shared_data[0];
    }
    
    // functional reduction complete! GPU goes brrr ✨
}
```

## Quality Checklist

- [ ] **file header** with compilation commands and target API
- [ ] **ALL functions documented** with Doxygen-style comments
- [ ] **purity status** marked (✨ PURE FUNCTION ✨)
- [ ] **mathematical formulas** explained with references
- [ ] **gen-z slang** throughout (make shaders fun!)
- [ ] **compile to SPIR-V** when possible (dxc -spirv flag)
- [ ] **Vulkan binding attributes** used ([[vk::binding(...)]])
- [ ] **no mutable global state** (each thread independent)
- [ ] **functional composition** demonstrated
- [ ] **performance notes** included
- [ ] **latest Shader Model** used (6.6+)

**remember**: HLSL is acceptable when compiled to SPIR-V for Vulkan. shaders are
inherently functional - each thread executes pure function independently. this is
functional programming at massive scale (millions of threads!) uwu 💜✨

(but still prefer native SPIR-V or Slang when possible because DirectX cope)