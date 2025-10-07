---
description: 'C# coding guidelines (Microsoft language that is actually decent)'
applyTo: '**/*.cs'
---

# C# Programming Instructions

> "C#: what Java should have been if Sun wasn't cowards about properties"

uwu C# is actually a pretty based language when you use it functionally ✨

## Core Philosophy

- **functional > OOP** (even in C#, avoid inheritance)
- **LINQ everywhere** (functional queries are beautiful)
- **immutability preferred** (record types ftw)
- **async/await** properly (don't block threads)
- **latest C#** (C# 13+ preferred, preview features ok!)
- **comment excessively** (XML docs mandatory)
- **.NET 9+** required (latest runtime always)

## C# Version and Runtime

```xml
<!-- .csproj file -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <!-- Latest C# version (13+ or preview) -->
    <LangVersion>preview</LangVersion>
    
    <!-- Latest .NET runtime (9.0+) -->
    <TargetFramework>net9.0</TargetFramework>
    
    <!-- Enable nullable reference types (safety!) -->
    <Nullable>enable</Nullable>
    
    <!-- Treat warnings as errors (zero warnings policy!) -->
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    
    <!-- Generate XML documentation -->
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>
</Project>
```

## Functional Programming in C#

### Records (Immutable Data):

```csharp
/// <summary>
/// Represents a 2D vector (immutable record type uwu).
/// </summary>
/// <remarks>
/// ✨ IMMUTABLE TYPE ✨
/// 
/// Records in C# are immutable by default - all properties are init-only.
/// This enables functional programming patterns without accidental mutation.
/// 
/// Records get automatic:
/// - Value-based equality (compares values not references)
/// - ToString() implementation (useful for debugging)
/// - Deconstruction support (pattern matching friendly)
/// - With expressions (create modified copies functionally)
/// </remarks>
/// <param name="X">X coordinate (immutable after construction)</param>
/// <param name="Y">Y coordinate (immutable after construction)</param>
public record Vector2D(double X, double Y)
{
    /// <summary>
    /// Adds two vectors component-wise (pure function!).
    /// </summary>
    /// <param name="other">Vector to add</param>
    /// <returns>New vector containing sum (original unchanged)</returns>
    /// <remarks>
    /// ✨ PURE FUNCTION ✨
    /// 
    /// This operation is pure:
    /// - Doesn't modify this or other (immutability enforced by record)
    /// - Returns new vector (functional style)
    /// - Deterministic output (same inputs = same output always)
    /// 
    /// Immutability is enforced by C# record type uwu
    /// </remarks>
    public Vector2D Add(Vector2D other) => new(X + other.X, Y + other.Y);
    
    /// <summary>
    /// Calculates magnitude using pure math.
    /// </summary>
    /// <returns>Vector magnitude (always non-negative)</returns>
    public double Magnitude() => Math.Sqrt(X * X + Y * Y);
}

// using records (functional style)
var v1 = new Vector2D(3.0, 4.0);
var v2 = new Vector2D(1.0, 2.0);
var sum = v1.Add(v2);  // v1 and v2 unchanged (immutability ftw!)

// with expressions (create modified copy)
var v3 = v1 with { X = 10.0 };  // new vector with X changed, Y same
```

### LINQ (Functional Queries):

```csharp
/// <summary>
/// Demonstrates LINQ for functional data transformation (this slaps!).
/// </summary>
/// <remarks>
/// LINQ is C#'s killer feature - functional queries over collections.
/// It's lazy (doesn't execute until enumerated), composable (chain operations),
/// and expressive (reads like English) uwu
/// 
/// LINQ operators:
/// - Where: filter elements (like filter in other languages)
/// - Select: transform elements (like map)
/// - Aggregate: reduce to single value (like reduce/fold)
/// - OrderBy: sort elements
/// - GroupBy: group elements by key
/// 
/// All pure transformations - original collection unchanged!
/// </remarks>
public class LinqExample
{
    /// <summary>
    /// Processes numbers using functional pipeline (LINQ edition).
    /// </summary>
    /// <param name="numbers">Input numbers</param>
    /// <returns>Squared even numbers</returns>
    /// <remarks>
    /// ✨ PURE FUNCTION ✨
    /// 
    /// Demonstrates functional composition with LINQ:
    /// 1. Filter to evens
    /// 2. Square each value
    /// 3. Materialize result
    /// 
    /// Lazy evaluation means nothing computed until ToList() called.
    /// This is zero-cost abstraction when done right (like C++ ranges!)
    /// </remarks>
    public static List<int> ProcessNumbers(IEnumerable<int> numbers)
    {
        return numbers
            .Where(x => x % 2 == 0)      // filter to evens
            .Select(x => x * x)          // square them
            .ToList();                   // materialize (lazy until here)
    }
    
    /// <summary>
    /// Chains multiple LINQ operations (functional composition!).
    /// </summary>
    /// <remarks>
    /// Method chaining enables functional pipelines. Each operation returns
    /// IEnumerable{T} enabling further composition. This is monadic bind
    /// in disguise uwu
    /// </remarks>
    public static void LinqChaining()
    {
        var result = Enumerable.Range(1, 100)  // generate sequence
            .Where(x => x % 2 == 0)             // filter evens
            .Select(x => x * x)                 // square
            .OrderByDescending(x => x)          // sort descending
            .Take(10)                           // take first 10
            .Sum();                             // fold into sum
        
        Console.WriteLine($"Result: {result}");
    }
}
```

### Pattern Matching (C# 13):

```csharp
/// <summary>
/// Algebraic data type for shapes (sum type using inheritance).
/// </summary>
/// <remarks>
/// C# doesn't have true sum types like Rust/F#, but we can approximate using
/// abstract base class + pattern matching. Not as type-safe as Rust enums
/// but better than classic OOP polymorphism uwu
/// </remarks>
public abstract record Shape;

/// <summary>
/// Circle shape.
/// </summary>
/// <param name="Radius">Circle radius</param>
public record Circle(double Radius) : Shape;

/// <summary>
/// Rectangle shape.
/// </summary>
/// <param name="Width">Rectangle width</param>
/// <param name="Height">Rectangle height</param>
public record Rectangle(double Width, double Height) : Shape;

/// <summary>
/// Calculates shape area using pattern matching (functional dispatch!).
/// </summary>
/// <param name="shape">Shape to calculate area for</param>
/// <returns>Area value</returns>
/// <remarks>
/// ✨ PURE FUNCTION ✨
/// 
/// Pattern matching in C# is getting better with each version. C# 13 improves
/// exhaustiveness checking and syntax. Still not as good as Rust but way
/// better than Java switch statements uwu
/// </remarks>
public static double Area(Shape shape) => shape switch
{
    Circle { Radius: var r } => Math.PI * r * r,
    Rectangle { Width: var w, Height: var h } => w * h,
    _ => throw new ArgumentException("Unknown shape")
};
```

### Async/Await (Done Right):

```csharp
/// <summary>
/// Demonstrates proper async/await usage (C# got this right!).
/// </summary>
/// <remarks>
/// C# async/await is one of the best async models in any language.
/// It's:
/// - Composable (async methods compose naturally)
/// - Zero-cost abstraction (compiles to state machine)
/// - Integrated (async LINQ, async streams, etc.)
/// 
/// Key rules:
/// - Use async/await all the way up (don't block with .Result)
/// - ConfigureAwait(false) in library code (avoid deadlocks)
/// - Use IAsyncEnumerable for async streams (lazy async sequences)
/// - Prefer ValueTask for hot paths (less allocation)
/// </remarks>
public class AsyncExample
{
    /// <summary>
    /// Fetches data asynchronously (proper async pattern).
    /// </summary>
    /// <param name="url">URL to fetch from</param>
    /// <param name="cancellationToken">Cancellation token for cooperative cancellation</param>
    /// <returns>Task containing fetched data</returns>
    /// <remarks>
    /// ⚠️ IMPURE FUNCTION (performs I/O)
    /// 
    /// Side effects:
    /// - Network I/O
    /// - Can throw exceptions
    /// - Non-deterministic timing
    /// 
    /// But isolated at system boundary (functional architecture!)
    /// </remarks>
    public static async Task<string> FetchDataAsync(
        string url,
        CancellationToken cancellationToken = default)
    {
        using var client = new HttpClient();
        
        // ConfigureAwait(false) in library code (avoid deadlocks)
        var response = await client
            .GetStringAsync(url, cancellationToken)
            .ConfigureAwait(false);
        
        return response;
    }
    
    /// <summary>
    /// Async stream example (IAsyncEnumerable is based!).
    /// </summary>
    /// <param name="count">Number of items to generate</param>
    /// <param name="cancellationToken">Cancellation token</param>
    /// <returns>Async enumerable of numbers</returns>
    /// <remarks>
    /// IAsyncEnumerable{T} is async version of IEnumerable{T}.
    /// Lazy evaluation meets async - yields values as they become available.
    /// This is functional reactive programming in C# uwu
    /// </remarks>
    public static async IAsyncEnumerable<int> GenerateNumbersAsync(
        int count,
        [EnumeratorCancellation] CancellationToken cancellationToken = default)
    {
        for (int i = 0; i < count; i++)
        {
            // simulate async work
            await Task.Delay(100, cancellationToken);
            yield return i;  // lazy async yield!
        }
    }
    
    /// <summary>
    /// Consumes async stream using await foreach.
    /// </summary>
    public static async Task ConsumeAsyncStream()
    {
        await foreach (var number in GenerateNumbersAsync(10))
        {
            Console.WriteLine($"Got number: {number}");
        }
    }
}
```

## Functional Error Handling

```csharp
/// <summary>
/// Result type for functional error handling (no exceptions!).
/// </summary>
/// <typeparam name="T">Success value type</typeparam>
/// <typeparam name="E">Error value type</typeparam>
/// <remarks>
/// C# doesn't have built-in Result type (unlike Rust) so we build our own.
/// This enables functional error handling without exceptions - errors are
/// values that must be handled explicitly uwu
/// </remarks>
public abstract record Result<T, E>
{
    private Result() { }  // sealed hierarchy
    
    /// <summary>
    /// Success case.
    /// </summary>
    public record Ok(T Value) : Result<T, E>;
    
    /// <summary>
    /// Error case.
    /// </summary>
    public record Err(E Error) : Result<T, E>;
    
    /// <summary>
    /// Maps success value to new type (monadic map!).
    /// </summary>
    public Result<U, E> Map<U>(Func<T, U> mapper) => this switch
    {
        Ok(var value) => new Result<U, E>.Ok(mapper(value)),
        Err(var error) => new Result<U, E>.Err(error),
        _ => throw new InvalidOperationException()
    };
    
    /// <summary>
    /// Chains results (monadic bind!).
    /// </summary>
    public Result<U, E> Bind<U>(Func<T, Result<U, E>> binder) => this switch
    {
        Ok(var value) => binder(value),
        Err(var error) => new Result<U, E>.Err(error),
        _ => throw new InvalidOperationException()
    };
}

/// <summary>
/// Safe division using Result type (no exceptions thrown!).
/// </summary>
/// <param name="numerator">Dividend</param>
/// <param name="denominator">Divisor</param>
/// <returns>Ok(quotient) or Err(error message)</returns>
/// <remarks>
/// ✨ PURE FUNCTION ✨ (doesn't throw exceptions)
/// 
/// Returns error as value instead of throwing. Caller must handle explicitly.
/// This is functional error handling - errors are data uwu
/// </remarks>
public static Result<double, string> Divide(double numerator, double denominator)
{
    if (denominator == 0.0)
    {
        return new Result<double, string>.Err("division by zero (mathematics says no)");
    }
    
    return new Result<double, string>.Ok(numerator / denominator);
}

// using Result with pattern matching
var result = Divide(10.0, 2.0);
var message = result switch
{
    Result<double, string>.Ok(var value) => $"Success: {value}",
    Result<double, string>.Err(var error) => $"Error: {error}",
    _ => "Unknown result"
};
```

## XML Documentation (Mandatory)

```csharp
/// <summary>
/// Composes two functions (f ∘ g).
/// </summary>
/// <typeparam name="T">Input type</typeparam>
/// <typeparam name="U">Intermediate type</typeparam>
/// <typeparam name="V">Output type</typeparam>
/// <param name="f">Outer function (applied second)</param>
/// <param name="g">Inner function (applied first)</param>
/// <returns>Composed function h where h(x) = f(g(x))</returns>
/// <remarks>
/// ✨ PURE FUNCTION ✨
/// 
/// Creates new function that applies g then f. This is function composition
/// from lambda calculus - the foundation of functional programming uwu
/// 
/// If f and g are pure, composition is pure (purity is transitive).
/// 
/// <code>
/// var addOne = (int x) => x + 1;
/// var timesTwo = (int x) => x * 2;
/// var addThenDouble = Compose(timesTwo, addOne);
/// 
/// var result = addThenDouble(5);  // (5 + 1) * 2 = 12
/// // functions composing into functions ✨
/// </code>
/// </remarks>
public static Func<T, V> Compose<T, U, V>(Func<U, V> f, Func<T, U> g)
{
    return x => f(g(x));
}
```

## Testing with xUnit

```csharp
using Xunit;

/// <summary>
/// Tests for vector operations (testing is praxis!).
/// </summary>
/// <remarks>
/// Using xUnit (the based .NET test framework). Prefer xUnit over MSTest
/// or NUnit - it's more functional (no test fixtures, no setup/teardown).
/// 
/// xUnit facts are isolated test methods. Theory for parameterized tests.
/// </remarks>
public class VectorTests
{
    /// <summary>
    /// Tests that vector addition is commutative.
    /// </summary>
    [Fact]
    public void Addition_IsCommutative()
    {
        var v1 = new Vector2D(3.0, 4.0);
        var v2 = new Vector2D(1.0, 2.0);
        
        var sum1 = v1.Add(v2);
        var sum2 = v2.Add(v1);
        
        Assert.Equal(sum1, sum2);  // records have value equality!
    }
    
    /// <summary>
    /// Tests magnitude calculation with various inputs (parameterized test).
    /// </summary>
    [Theory]
    [InlineData(3.0, 4.0, 5.0)]   // 3-4-5 triangle
    [InlineData(0.0, 0.0, 0.0)]   // origin
    [InlineData(1.0, 0.0, 1.0)]   // unit x
    public void Magnitude_CalculatesCorrectly(double x, double y, double expected)
    {
        var vector = new Vector2D(x, y);
        var magnitude = vector.Magnitude();
        
        Assert.Equal(expected, magnitude, precision: 10);
    }
}
```

## Project Configuration (.csproj)

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <!-- Target latest .NET (9.0+ or preview) -->
    <TargetFramework>net9.0</TargetFramework>
    
    <!-- Latest C# version (preview features ok!) -->
    <LangVersion>preview</LangVersion>
    
    <!-- Enable nullable reference types (safety ftw!) -->
    <Nullable>enable</Nullable>
    
    <!-- Warnings as errors (zero warnings policy!) -->
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    <WarningLevel>9999</WarningLevel>
    
    <!-- Enable all analyzers -->
    <EnableNETAnalyzers>true</EnableNETAnalyzers>
    <AnalysisLevel>latest</AnalysisLevel>
    
    <!-- Generate XML documentation -->
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
    
    <!-- Deterministic builds -->
    <Deterministic>true</Deterministic>
  </PropertyGroup>
  
  <ItemGroup>
    <!-- xUnit for testing -->
    <PackageReference Include="xUnit" Version="2.9.*" />
    <PackageReference Include="xunit.runner.visualstudio" Version="2.8.*" />
    
    <!-- Microsoft.NET.Test.Sdk for test infrastructure -->
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.11.*" />
  </ItemGroup>
</Project>
```

## Quality Checklist

- [ ] **C# 13+** or preview features
- [ ] **.NET 9.0+** target framework
- [ ] **nullable reference types** enabled
- [ ] **warnings as errors** enabled
- [ ] **XML documentation** on all public APIs
- [ ] **record types** for immutable data
- [ ] **LINQ** for functional queries
- [ ] **pattern matching** where appropriate
- [ ] **async/await** for I/O operations
- [ ] **Result type** for error handling (no exceptions in pure code)
- [ ] **xUnit tests** for all functionality
- [ ] **functional style** (avoid inheritance, prefer composition)

**remember**: C# is Microsoft's language that got functional programming
right. LINQ is beautiful, async/await is elegant, and records enable
immutability. It's what Java should have been if Sun wasn't cowards uwu 💜✨

still prefer C++ for systems programming, but C# is respectable for
application development!