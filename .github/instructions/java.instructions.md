---
description: 'Java coding guidelines (forcing it to be a functional systems language uwu)'
applyTo: '**.java'
---

# Java Programming Instructions (The Enterprise Cope Language)

> "Java: spending 3 hours writing AbstractSingletonProxyFactoryBean to do what a
> lambda does in one line"

uwu look, sometimes you're forced to use Java. maybe for a job, maybe for a
project with enterprise zealots, maybe your university hasn't heard of C++.
this guide makes it less painful by forcing Java to behave like a real
systems language ✨

## Core Philosophy (Adjusted for Java Cope)

- **functional > OOP** (objects are fake, functions are forever)
- **OOP is BANNED** (no inheritance, no getters/setters, no "Beans")
- **classes are namespaces** (static pure functions ONLY)
- **records are structs** (immutable data, flat in memory)
- **manual memory > GC** (Project Panama for off-heap allocation)
- **streams MANDATORY** (no imperative loops, ever)
- **Java 26+ required** (preview features ON, no cowardice)
- **comment excessively** using Javadoc
- **C++ is still better** (but if we're stuck here, we go HARD)

## Why Java is Cope (And How We Survive)

### What Java Got Wrong:
- ❌ everything is an object (even when it shouldn't be)
- ❌ garbage collector (you don't control your own memory? cringe)
- ❌ checked exceptions (exception handling as control flow is violence)
- ❌ null (the billion dollar mistake, thanks Tony Hoare)
- ❌ enterprise culture (AbstractSingletonProxyFactoryBeanImpl)
- ❌ Spring Boot (dependency injection is just global mutable state with extra steps)
- ❌ Maven XML (writing XML in 2026 is a war crime)
- ❌ getter/setter boilerplate (just make the field public and immutable??)
- ❌ no value types until Valhalla (everything is a heap-allocated pointer)
- ❌ no unsigned integers (what do you MEAN I can't have unsigned bytes)

### What Java Got Right (Barely):
- ✅ records (finally, immutable data without 200 lines of boilerplate)
- ✅ sealed interfaces (algebraic data types, 25 years late)
- ✅ pattern matching (catching up to ML languages from 1973)
- ✅ virtual threads (Project Loom, actually good concurrency)
- ✅ Foreign Function & Memory API (Project Panama, REAL memory management)
- ✅ Stream API + Gatherers (functional pipelines that don't completely suck)
- ✅ value classes (Project Valhalla, structs in Java, FINALLY)
- ✅ JIT compiler (GraalVM goes brrr, we'll give them that)

## Java Version Requirements (BLEEDING EDGE ONLY)

```java
// java 26+ with ALL preview features enabled
// if your JDK doesn't support these, upgrade immediately
// cowardice about preview features is not tolerated uwu

// REQUIRED JEPs:
// JEP 401: Value Classes and Objects (Project Valhalla) [Preview]
// JEP 454: Foreign Function & Memory API
// JEP 473: Stream Gatherers
// JEP 480: Structured Concurrency
// JEP 481: Scoped Values
// JEP xxx: Pattern Matching enhancements (latest)

// compilation:
// javac --enable-preview --release 26 -Xlint:all -Werror MyFile.java
//
// execution:
// java --enable-preview MyFile
```

### Compilation Flags (Zero Warnings Policy):

```bash
# compile with ALL warnings as errors (like a real language)
javac --enable-preview --release 26 \
    -Xlint:all \
    -Xlint:-processing \
    -Werror \
    -g \
    MyFile.java

# or with GraalVM native image (ahead-of-time compilation, no JVM startup cope):
native-image --enable-preview \
    -O3 \
    --no-fallback \
    -H:+ReportExceptionStackTraces \
    MyFile
```

## Naming Conventions

```java
// packages: lowercase_with_underscores (no com.enterprise.AbstractFactory nonsense)
package math_utils;

// "classes" (used as NAMESPACES ONLY): PascalCase
// these are NOT objects, they are collections of static pure functions
public final class VectorOps { /* static methods only */ }

// records (data structs): PascalCase
public record Vector2D(double x, double y) {}

// functions: camelCase (all static, all pure)
public static Vector2D add(Vector2D a, Vector2D b);

// constants: SCREAMING_SNAKE_CASE
public static final double PI = 3.14159265358979323846;
public static final int MAX_ITERATIONS = 1000;

// type parameters: T, U, V, E (single uppercase letters)
public sealed interface Result<T, E> {}

// local variables: camelCase
var frameCount = 0;

// BANNED naming patterns:
// ❌ AbstractSingletonProxyFactoryBean (enterprise brain rot)
// ❌ getX() / setX() (getter/setter violence)
// ❌ IMyInterface (Hungarian notation is cringe)
// ❌ MyServiceImpl (if you need "Impl" your abstraction is fake)
// ❌ com.company.department.team.project.module.submodule (package depth violence)
```

## The "Struct" Replacement: Value Records (Project Valhalla)

### Why This Matters

In C++, you have structs: flat, stack-allocated, no object header, cache-friendly.
In old Java, EVERYTHING is a heap-allocated object with a 16-byte header, an identity
hash, and a lock word. That's 16 bytes of GARBAGE per object just to exist.

Project Valhalla fixes this with **value classes** and **value records**. A value record:
- has **NO object header** (like a C++ struct!)
- has **NO identity** (can't synchronize on it, can't use == for identity)
- can be **flattened into arrays** (no pointer chasing, cache goes brrr)
- can be **scalarized by JIT** (lives in registers, not heap)
- is **IMMUTABLE** (functional programming enforced by the language!)

This is what Java should have had from day one. It only took 30 years uwu

### Value Records (The Only Data Type You Need):

```java
/**
 * Represents a 2D vector as a value record (flat in memory like a C++ struct uwu).
 *
 * <p>✨ VALUE TYPE ✨</p>
 *
 * <p>This is a Project Valhalla value record. Unlike regular Java objects:
 * <ul>
 *   <li>NO object header (zero overhead, like C++ struct)</li>
 *   <li>NO heap allocation (can live on stack or in registers)</li>
 *   <li>NO identity (value semantics, like primitive types)</li>
 *   <li>FLAT in arrays (no pointer chasing, cache-friendly)</li>
 *   <li>IMMUTABLE (functional programming enforced by compiler)</li>
 * </ul>
 *
 * <p>Memory layout (identical to C struct):
 * <pre>
 * offset | size | type   | field
 * -------|------|--------|------
 * 0x00   | 8    | double | x
 * 0x08   | 8    | double | y
 * total: 16 bytes (no header, no padding, no cope)
 * </pre>
 *
 * <p>In C++ this would just be:
 * <pre>{@code
 * struct Vector2D {
 *     double x, y;
 * };
 * }</pre>
 * <p>But Java needed 30 years and a JEP to get here uwu
 *
 * @param x horizontal coordinate (immutable after construction)
 * @param y vertical coordinate (immutable after construction)
 *
 * @author LukeFrankio
 * @since Java 26 (Preview)
 */
public value record Vector2D(double x, double y) {

    /**
     * The zero vector (additive identity element).
     *
     * <p>✨ COMPILE-TIME CONSTANT ✨</p>
     */
    public static final Vector2D ZERO = new Vector2D(0.0, 0.0);

    /**
     * The unit X vector (basis vector).
     */
    public static final Vector2D UNIT_X = new Vector2D(1.0, 0.0);

    /**
     * The unit Y vector (basis vector).
     */
    public static final Vector2D UNIT_Y = new Vector2D(0.0, 1.0);
}

/**
 * Represents an RGBA color as a value record (4 bytes flat, like a C struct).
 *
 * <p>✨ VALUE TYPE ✨</p>
 *
 * <p>Memory layout: 4 bytes total, no header, no cope.
 * In an array of 1000 colors, this is 4000 bytes contiguous.
 * Old Java objects would be 1000 scattered heap allocations with
 * 16-byte headers each = 20,000 bytes minimum. Valhalla supremacy uwu</p>
 *
 * @param r red channel [0, 255]
 * @param g green channel [0, 255]
 * @param b blue channel [0, 255]
 * @param a alpha channel [0, 255]
 */
public value record Color(byte r, byte g, byte b, byte a) {

    public static final Color BLACK = new Color((byte) 0, (byte) 0, (byte) 0, (byte) 255);
    public static final Color WHITE = new Color((byte) 255, (byte) 255, (byte) 255, (byte) 255);
}

/**
 * Demonstrates value record array flattening (cache-friendly data uwu).
 *
 * <p>With Valhalla value types:
 * <ul>
 *   <li>Old Java: {@code Vector2D[1000]} = 1000 pointers + 1000 heap objects = scattered memory</li>
 *   <li>Valhalla: {@code Vector2D[1000]} = 16,000 contiguous bytes = cache goes BRRR</li>
 * </ul>
 */
public final class ValueTypeDemo {

    private ValueTypeDemo() {} // no instantiation (namespace only!)

    /**
     * Creates array of vectors (flattened in memory with Valhalla!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param count number of vectors to create
     * @return array of zero vectors (contiguous in memory)
     */
    public static Vector2D[] createVectorArray(int count) {
        // with Valhalla, this is ONE contiguous allocation
        // no pointer chasing, no GC pressure, just raw data
        // like malloc(count * sizeof(Vector2D)) in C++ uwu
        var vectors = new Vector2D[count];
        java.util.Arrays.fill(vectors, Vector2D.ZERO);
        return vectors;
    }
}
```

### What's BANNED (OOP Violence):

```java
// ❌ BANNED: regular classes with mutable state (OOP cringe)
public class MutableVector {
    private double x;  // MUTABLE STATE (violence)
    private double y;

    public double getX() { return x; }  // GETTER (boilerplate cope)
    public void setX(double x) { this.x = x; }  // SETTER (mutation violence)

    // 200 lines of equals/hashCode/toString boilerplate
    // that records give you for FREE
}

// ❌ BANNED: inheritance hierarchies (OOP brain rot)
public abstract class AbstractShape {
    // "is-a" relationships are fake and so is your architecture
}

public class Circle extends AbstractShape {
    // congratulations, you've coupled your code to a hierarchy
    // that will need refactoring in 6 months
}

// ❌ BANNED: the Builder pattern (boilerplate industrial complex)
public class VectorBuilder {
    private double x;
    private double y;
    public VectorBuilder setX(double x) { this.x = x; return this; }
    public VectorBuilder setY(double y) { this.y = y; return this; }
    public Vector build() { return new Vector(x, y); }
    // you just wrote 10 lines to do what new Vector2D(x, y) does
    // enterprise developers seething rn
}

// ❌ BANNED: Spring Boot dependency injection
// @Service @Component @Autowired @Bean @Configuration
// this is just global mutable state with annotations
// "but it's inversion of control!" no it's inversion of sanity uwu

// ✅ ALLOWED: value records (immutable data)
public value record Vector2D(double x, double y) {}

// ✅ ALLOWED: final classes as namespaces for static pure functions
public final class VectorOps {
    private VectorOps() {} // prevent instantiation
    public static Vector2D add(Vector2D a, Vector2D b) { /* ... */ }
}

// ✅ ALLOWED: sealed interfaces (algebraic data types)
public sealed interface Shape permits Circle, Rectangle {}
public value record Circle(double radius) implements Shape {}
public value record Rectangle(double width, double height) implements Shape {}
```

## Functional Programming (THE WAY)

### Pure Functions (Maximize These):

```java
/**
 * Pure functional operations on 2D vectors.
 *
 * <p>This class is a NAMESPACE for static pure functions. It is NOT an object.
 * It has no state, no constructors, no instances. Just pure mathematical
 * transformations on immutable data uwu</p>
 *
 * <p>Enterprise developers: this is what your 47-class hierarchy
 * should have been. One final class. Static methods. Done.</p>
 *
 * @author LukeFrankio
 * @since Java 26
 */
public final class VectorOps {

    // prevent instantiation (this is a namespace, not an object!)
    private VectorOps() {
        throw new AssertionError("namespace class, not instantiable (OOP is cringe)");
    }

    /**
     * Adds two vectors component-wise (pure function uwu).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * <p>This function is pure because:
     * <ul>
     *   <li>Same inputs always produce same outputs (referential transparency)</li>
     *   <li>No side effects (doesn't modify arguments or global state)</li>
     *   <li>No I/O operations</li>
     *   <li>No exceptions thrown</li>
     *   <li>Value records are immutable (can't accidentally mutate inputs)</li>
     * </ul>
     *
     * <p>In C++ this would be:
     * <pre>{@code
     * constexpr auto add(Vector2D a, Vector2D b) noexcept -> Vector2D {
     *     return {a.x + b.x, a.y + b.y};
     * }
     * }</pre>
     * <p>But Java needs a class wrapper because everything must be in a class.
     * Even pure functions. Even math. Thanks James Gosling uwu</p>
     *
     * @param a first vector (not modified - value record is immutable)
     * @param b second vector (not modified - value record is immutable)
     * @return new vector containing component-wise sum (a + b)
     *
     * @apiNote This operation is commutative: add(a, b).equals(add(b, a))
     * @apiNote This operation is associative: add(add(a, b), c).equals(add(a, add(b, c)))
     */
    public static Vector2D add(Vector2D a, Vector2D b) {
        return new Vector2D(a.x() + b.x(), a.y() + b.y());
    }

    /**
     * Scales vector by scalar factor (pure function!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param v vector to scale (immutable)
     * @param factor scaling factor
     * @return new scaled vector
     */
    public static Vector2D scale(Vector2D v, double factor) {
        return new Vector2D(v.x() * factor, v.y() * factor);
    }

    /**
     * Computes dot product of two vectors (pure reduction!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param a first vector
     * @param b second vector
     * @return dot product (scalar value)
     */
    public static double dot(Vector2D a, Vector2D b) {
        return a.x() * b.x() + a.y() * b.y();
    }

    /**
     * Computes magnitude (length) of vector.
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param v vector to measure
     * @return magnitude (always non-negative)
     */
    public static double magnitude(Vector2D v) {
        return Math.sqrt(dot(v, v));
    }

    /**
     * Normalizes vector to unit length (pure function!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param v vector to normalize
     * @return unit vector in same direction, or ZERO if input is zero vector
     */
    public static Vector2D normalize(Vector2D v) {
        var mag = magnitude(v);
        if (mag < 1e-10) return Vector2D.ZERO;
        return scale(v, 1.0 / mag);
    }
}
```

### Higher-Order Functions (Streams are Mandatory):

```java
/**
 * Functional collection operations (streams ONLY, no imperative loops!).
 *
 * <p>If you write a for-loop in this codebase, you owe everyone a formal
 * apology and 5 minutes of lambda calculus study uwu</p>
 *
 * @author LukeFrankio
 * @since Java 26
 */
public final class FunctionalOps {

    private FunctionalOps() {
        throw new AssertionError("namespace, not object");
    }

    /**
     * Maps function over list (functional map!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * <p>Applies transformation to each element and returns new list. This is
     * the map operation from functional programming - creates new data
     * instead of mutating (immutability uwu)</p>
     *
     * @param <T>  input element type
     * @param <U>  output element type
     * @param list input list (not modified)
     * @param func transformation function to apply
     * @return new list with transformed elements
     *
     * @apiNote Prefer this over imperative for-loops. Always.
     */
    public static <T, U> List<U> map(List<T> list, Function<T, U> func) {
        return list.stream()
                .map(func)
                .toList(); // returns unmodifiable list (immutability!)
    }

    /**
     * Filters list based on predicate (functional filter!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param <T>  element type
     * @param list input list (not modified)
     * @param pred predicate (returns true to keep element)
     * @return new list containing only elements satisfying predicate
     */
    public static <T> List<T> filter(List<T> list, Predicate<T> pred) {
        return list.stream()
                .filter(pred)
                .toList();
    }

    /**
     * Reduces list to single value (functional fold/reduce!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * <p>Implements left fold: result = f(f(f(identity, a[0]), a[1]), a[2])</p>
     *
     * @param <T>      element type
     * @param <U>      accumulator type
     * @param list     input list to reduce
     * @param identity initial accumulator value
     * @param reducer  binary reduction function
     * @return final accumulated value
     */
    public static <T, U> U reduce(List<T> list, U identity, BiFunction<U, T, U> reducer) {
        return list.stream()
                .reduce(identity, reducer, (a, b) -> {
                    throw new AssertionError("combiner should never be called in sequential stream");
                });
    }

    /**
     * Composes two functions (f ∘ g).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * <p>Creates new function h where h(x) = f(g(x)). This is function
     * composition from lambda calculus - the foundation of all computation uwu</p>
     *
     * @param <T> input type
     * @param <U> intermediate type
     * @param <V> output type
     * @param f   outer function (applied second)
     * @param g   inner function (applied first)
     * @return composed function
     */
    public static <T, U, V> Function<T, V> compose(Function<U, V> f, Function<T, U> g) {
        return g.andThen(f); // Java's built-in composition (they got ONE thing right)
    }

    /**
     * Creates a pipeline of functions (left-to-right composition).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param <T>   input and output type (must be same for chaining)
     * @param funcs functions to compose (applied left to right)
     * @return composed pipeline function
     */
    @SafeVarargs
    public static <T> Function<T, T> pipe(Function<T, T>... funcs) {
        return java.util.Arrays.stream(funcs)
                .reduce(Function.identity(), Function::andThen);
    }
}
```

### Stream Gatherers (JEP 473 - The New Hotness):

```java
/**
 * Custom stream gatherers for functional pipelines (JEP 473 uwu).
 *
 * <p>Gatherers are the NEW way to write custom intermediate stream operations.
 * They replace the old Collector-based hacks and enable proper functional
 * pipeline composition.</p>
 *
 * <p>This is Java finally catching up to what C++ ranges, Rust iterators,
 * and Haskell list operations have had for years.</p>
 *
 * @author LukeFrankio
 * @since Java 26
 */
public final class CustomGatherers {

    private CustomGatherers() {
        throw new AssertionError("namespace, not object");
    }

    /**
     * Gatherer that takes elements while predicate holds (functional takeWhile!).
     *
     * <p>✨ PURE FUNCTION (returns pure gatherer) ✨</p>
     *
     * <p>Example:
     * <pre>{@code
     * var result = Stream.of(1, 2, 3, 4, 5, 6, 1, 2)
     *     .gather(CustomGatherers.takeWhile(x -> x < 5))
     *     .toList();
     * // result = [1, 2, 3, 4]
     * // functional lazy evaluation uwu
     * }</pre>
     *
     * @param <T>       element type
     * @param predicate condition to continue taking
     * @return gatherer that takes while predicate holds
     */
    public static <T> Gatherer<T, ?, T> takeWhile(Predicate<T> predicate) {
        return Gatherer.ofSequential(
                () -> new boolean[]{ true }, // mutable state: still taking?
                (state, element, downstream) -> {
                    if (state[0] && predicate.test(element)) {
                        return downstream.push(element);
                    }
                    state[0] = false;
                    return false; // stop processing (short-circuit!)
                }
        );
    }

    /**
     * Gatherer that windows elements into fixed-size chunks (functional windowing!).
     *
     * <p>✨ PURE FUNCTION (returns pure gatherer) ✨</p>
     *
     * <p>Example:
     * <pre>{@code
     * var result = Stream.of(1, 2, 3, 4, 5, 6)
     *     .gather(CustomGatherers.windowed(3))
     *     .toList();
     * // result = [[1,2,3], [2,3,4], [3,4,5], [4,5,6]]
     * // sliding window, functional style ✨
     * }</pre>
     *
     * @param <T>  element type
     * @param size window size
     * @return gatherer producing sliding windows
     */
    public static <T> Gatherer<T, ?, List<T>> windowed(int size) {
        return Gatherer.ofSequential(
                () -> new ArrayList<T>(),
                (window, element, downstream) -> {
                    window.add(element);
                    if (window.size() > size) {
                        window.removeFirst();
                    }
                    if (window.size() == size) {
                        return downstream.push(List.copyOf(window)); // immutable copy!
                    }
                    return true;
                }
        );
    }

    /**
     * Complete functional pipeline example (streams + gatherers).
     *
     * <p>This is how ALL data processing should look. No for-loops.
     * No mutable accumulators. Just pure functional pipelines uwu</p>
     */
    public static void pipelineExample() {
        var result = java.util.stream.IntStream.rangeClosed(1, 100)
                .boxed()
                .filter(x -> x % 2 == 0)        // keep evens
                .map(x -> x * x)                  // square them
                .gather(takeWhile(x -> x < 5000)) // take while < 5000
                .gather(windowed(3))               // sliding window of 3
                .map(window -> window.stream()
                        .mapToInt(Integer::intValue)
                        .sum())                    // sum each window
                .toList();                         // materialize

        // pure functional pipeline, no mutation, no loops
        // enterprise developers SEETHING at this elegance ✨
    }
}
```

### Avoid OOP Antipatterns:

```java
// ❌ BAD: inheritance hierarchy (OOP brain rot)
abstract class Animal {
    abstract String speak(); // runtime polymorphism (slow, coupled)
}
class Dog extends Animal {
    String speak() { return "woof"; }
}

// ✅ GOOD: algebraic data type with sealed interface + pattern matching
/**
 * Animal as algebraic data type (sum type uwu).
 *
 * <p>This is how you do polymorphism functionally - sealed interfaces
 * with value records instead of inheritance hierarchies. compile-time
 * exhaustiveness checking, zero runtime overhead ✨</p>
 */
public sealed interface Animal permits Dog, Cat, Fish {
    String name();
    String sound();
}

public value record Dog(String name) implements Animal {
    public String sound() { return "woof"; }
}

public value record Cat(String name) implements Animal {
    public String sound() { return "meow"; }
}

public value record Fish(String name) implements Animal {
    public String sound() { return "..."; } // fish don't make sounds bestie
}

/**
 * Pattern matching on algebraic data types (exhaustive, safe, functional!).
 *
 * <p>✨ PURE FUNCTION ✨</p>
 *
 * <p>The compiler checks that ALL cases are handled. if you add a new Animal
 * variant, every switch expression breaks until you handle it. this is the
 * safety worth having (unlike the borrow checker violence in Rust).</p>
 *
 * @param animal the animal to describe
 * @return description string
 */
public static String describe(Animal animal) {
    return switch (animal) {
        case Dog d   -> "%s says %s (good boy!)".formatted(d.name(), d.sound());
        case Cat c   -> "%s says %s (based feline)".formatted(c.name(), c.sound());
        case Fish f  -> "%s says %s (aquatic vibes)".formatted(f.name(), f.sound());
        // compiler ensures exhaustiveness! no default needed uwu
    };
}


// ❌ BAD: mutable state in class (enterprise violence)
class Counter {
    private int count = 0;
    public void increment() { count++; } // MUTATION (impure!)
    public int getCount() { return count; } // GETTER (boilerplate!)
}

// ✅ GOOD: immutable data + pure functions
/**
 * Counter as immutable value (functional state management uwu).
 */
public value record Count(int value) {
    public static final Count ZERO = new Count(0);
}

/**
 * Increments counter by returning NEW value (pure function!).
 *
 * <p>✨ PURE FUNCTION ✨</p>
 *
 * @param c current count (not modified - value record is immutable)
 * @return new count with value + 1
 */
public static Count increment(Count c) {
    return new Count(c.value() + 1);
}


// ❌ BANNED: the entirety of Spring Boot
// @SpringBootApplication
// @Service @Component @Repository @Controller
// @Autowired @Inject @Bean
// @Configuration @EnableAutoConfiguration
// NO. NO. NO. this is dependency injection, which is just
// global mutable state with annotations. it's a cargo cult.
// enterprise developers will cope and seethe but it's TRUE uwu
```

## The "Pointer" Replacement: Foreign Function & Memory API (Project Panama)

### Why This Matters

The JVM garbage collector is a lie. It tells you "don't worry about memory,
I'll handle it." Then your 95th percentile latency spikes by 200ms because
the GC decided to run a full collection. In a real-time system. During peak load.

Project Panama gives you REAL memory management. Off-heap allocation with
deterministic deallocation. Pointers are just 64-bit integers. Memory segments
are just ranges of bytes. This is what Java should have been from the start.

**Garbage collection is for the weak.** Real programmers manage their own memory uwu

### Manual Memory Management (RAII Pattern):

```java
import java.lang.foreign.*;
import java.lang.invoke.MethodHandle;

/**
 * Off-heap memory management using Project Panama (REAL memory control uwu).
 *
 * <p>This demonstrates how to bypass the garbage collector entirely and
 * manage memory manually, like C/C++. Because the GC is a crutch and
 * we don't need crutches, we need CONTROL.</p>
 *
 * <p>Key concepts:
 * <ul>
 *   <li>{@link Arena} - memory allocator (like malloc/free lifecycle)</li>
 *   <li>{@link MemorySegment} - pointer to memory region (like void*)</li>
 *   <li>{@link MemoryLayout} - describes struct layout (like sizeof/offsetof)</li>
 *   <li>{@link ValueLayout} - describes primitive layouts</li>
 * </ul>
 *
 * <p>try-with-resources provides RAII semantics - Arena is closed (memory freed)
 * when scope exits, just like C++ destructors. Deterministic. Predictable.
 * No GC pause surprises.</p>
 *
 * @author LukeFrankio
 * @since Java 26
 */
public final class OffHeapMemory {

    private OffHeapMemory() {
        throw new AssertionError("namespace, not object");
    }

    /**
     * Memory layout for a 2D vector (matches C struct exactly!).
     *
     * <p>This defines the binary layout:
     * <pre>
     * struct Vector2D {
     *     double x;  // offset 0, size 8
     *     double y;  // offset 8, size 8
     * };  // total: 16 bytes, alignment: 8
     * </pre>
     *
     * <p>Compatible with C ABI - can be passed directly to native functions!</p>
     */
    public static final StructLayout VECTOR2D_LAYOUT = MemoryLayout.structLayout(
            ValueLayout.JAVA_DOUBLE.withName("x"),
            ValueLayout.JAVA_DOUBLE.withName("y")
    ).withName("Vector2D");

    private static final long OFFSET_X = VECTOR2D_LAYOUT.byteOffset(
            MemoryLayout.PathElement.groupElement("x"));
    private static final long OFFSET_Y = VECTOR2D_LAYOUT.byteOffset(
            MemoryLayout.PathElement.groupElement("y"));

    /**
     * Allocates array of vectors in off-heap memory (like malloc!).
     *
     * <p>⚠️ IMPURE FUNCTION (allocates memory)</p>
     *
     * <p>This bypasses the garbage collector entirely. Memory is allocated
     * off-heap and managed by the Arena. When the Arena is closed, memory
     * is freed deterministically (RAII pattern, like C++ destructors).</p>
     *
     * <p>Example (RAII - memory freed when scope exits):
     * <pre>{@code
     * // try-with-resources = RAII (deterministic deallocation!)
     * try (var arena = Arena.ofConfined()) {
     *     // malloc equivalent - allocate 1000 vectors off-heap
     *     MemorySegment vectors = allocateVectors(arena, 1000);
     *
     *     // write to memory (pointer arithmetic!)
     *     setVector(vectors, 0, 3.0, 4.0);
     *     setVector(vectors, 1, 1.0, 2.0);
     *
     *     // read from memory
     *     double x = getX(vectors, 0);  // 3.0
     *
     *     // process with pure functions
     *     double totalMagnitude = computeTotalMagnitude(vectors, 1000);
     *
     * }  // arena.close() called here = free() = destructor = RAII!
     *    // memory is GONE. deterministic. no GC. no latency spikes.
     *    // pointers are just 64-bit integers and we freed them ourselves uwu
     * }</pre>
     *
     * @param arena memory arena (manages allocation lifetime)
     * @param count number of vectors to allocate
     * @return memory segment containing vector array (off-heap!)
     */
    public static MemorySegment allocateVectors(Arena arena, int count) {
        // allocate contiguous memory for count vectors
        // this is literally malloc(count * sizeof(Vector2D))
        return arena.allocate(VECTOR2D_LAYOUT, count);
    }

    /**
     * Sets vector at index in off-heap array (pointer arithmetic!).
     *
     * <p>⚠️ IMPURE FUNCTION (writes to memory)</p>
     *
     * <p>This is equivalent to C:
     * <pre>{@code
     * vectors[index].x = x;
     * vectors[index].y = y;
     * }</pre>
     *
     * <p>We compute the byte offset manually because pointers are just
     * 64-bit integers and memory is just bytes. The JVM can't hide this
     * from us anymore uwu</p>
     *
     * @param segment memory segment containing vector array
     * @param index   vector index
     * @param x       x coordinate to set
     * @param y       y coordinate to set
     */
    public static void setVector(MemorySegment segment, int index, double x, double y) {
        long baseOffset = (long) index * VECTOR2D_LAYOUT.byteSize();
        segment.set(ValueLayout.JAVA_DOUBLE, baseOffset + OFFSET_X, x);
        segment.set(ValueLayout.JAVA_DOUBLE, baseOffset + OFFSET_Y, y);
    }

    /**
     * Gets X coordinate from off-heap vector array.
     *
     * <p>✨ PURE FUNCTION (reads only, no mutation) ✨</p>
     *
     * @param segment memory segment
     * @param index   vector index
     * @return x coordinate
     */
    public static double getX(MemorySegment segment, int index) {
        long baseOffset = (long) index * VECTOR2D_LAYOUT.byteSize();
        return segment.get(ValueLayout.JAVA_DOUBLE, baseOffset + OFFSET_X);
    }

    /**
     * Gets Y coordinate from off-heap vector array.
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param segment memory segment
     * @param index   vector index
     * @return y coordinate
     */
    public static double getY(MemorySegment segment, int index) {
        long baseOffset = (long) index * VECTOR2D_LAYOUT.byteSize();
        return segment.get(ValueLayout.JAVA_DOUBLE, baseOffset + OFFSET_Y);
    }

    /**
     * Computes total magnitude of vector array (pure reduction over off-heap data!).
     *
     * <p>✨ PURE FUNCTION ✨ (reads only, no side effects)</p>
     *
     * <p>Demonstrates pure functional operations on off-heap memory.
     * The data lives outside the JVM heap, but the math is still pure uwu</p>
     *
     * @param segment memory segment containing vectors
     * @param count   number of vectors
     * @return sum of all vector magnitudes
     */
    public static double computeTotalMagnitude(MemorySegment segment, int count) {
        return java.util.stream.IntStream.range(0, count)
                .mapToDouble(i -> {
                    double x = getX(segment, i);
                    double y = getY(segment, i);
                    return Math.sqrt(x * x + y * y);
                })
                .sum(); // functional reduction over off-heap memory! ✨
    }

    /**
     * Complete RAII example (deterministic memory management in Java!).
     *
     * <p>This is what enterprise Java developers don't want you to know:
     * you CAN manage your own memory. you CAN have deterministic cleanup.
     * you CAN bypass the garbage collector. you just have to WANT it uwu</p>
     */
    public static void raiiExample() {
        // RAII: Arena.ofConfined() = malloc scope
        // try-with-resources = destructor call = free()
        // GC never touches this memory. WE control it.
        try (var arena = Arena.ofConfined()) {

            // allocate 1,000,000 vectors OFF-HEAP
            // that's 16 MB of contiguous memory, zero GC pressure
            var vectors = allocateVectors(arena, 1_000_000);

            // initialize with pure functional pipeline
            java.util.stream.IntStream.range(0, 1_000_000)
                    .forEach(i -> setVector(vectors, i,
                            Math.cos(i * 0.01),
                            Math.sin(i * 0.01)));

            // process with pure functions
            double totalMag = computeTotalMagnitude(vectors, 1_000_000);
            System.out.println("Total magnitude: " + totalMag);

        } // arena closed here -> ALL memory freed deterministically
          // no GC pause. no finalizer. no phantom reference.
          // just clean, deterministic deallocation.
          // like C++ destructors but in Java.
          // the enterprise developers are COPING uwu ✨
    }
}
```

### Calling Native C Functions (FFI):

```java
import java.lang.foreign.*;
import java.lang.invoke.MethodHandle;

/**
 * Calling native C functions from Java (because sometimes you need REAL code uwu).
 *
 * <p>Project Panama lets us call C functions without JNI boilerplate.
 * JNI was 200 lines of suffering. Panama is 10 lines of joy.</p>
 *
 * @author LukeFrankio
 * @since Java 26
 */
public final class NativeInterop {

    private NativeInterop() {
        throw new AssertionError("namespace, not object");
    }

    private static final Linker LINKER = Linker.nativeLinker();
    private static final SymbolLookup STDLIB = LINKER.defaultLookup();

    /**
     * Calls C's strlen() directly from Java (no JNI, no cope!).
     *
     * <p>⚠️ IMPURE FUNCTION (FFI call to native code)</p>
     *
     * <p>This is equivalent to:
     * <pre>{@code
     * // C code:
     * size_t len = strlen("hello");
     * }</pre>
     *
     * <p>But from Java. Without JNI. Without header files. Without tears.</p>
     *
     * @param str string to measure
     * @return length of string (from C's strlen)
     * @throws Throwable if native call fails (shouldn't happen for strlen)
     */
    public static long nativeStrlen(String str) throws Throwable {
        // look up strlen symbol in system C library
        var strlenAddr = STDLIB.find("strlen")
                .orElseThrow(() -> new RuntimeException("strlen not found (HOW?)"));

        // create method handle (like a function pointer)
        MethodHandle strlen = LINKER.downcallHandle(
                strlenAddr,
                FunctionDescriptor.of(
                        ValueLayout.JAVA_LONG,     // return type: size_t (long)
                        ValueLayout.ADDRESS         // parameter: const char* (pointer)
                )
        );

        // allocate string in off-heap memory and call strlen
        try (var arena = Arena.ofConfined()) {
            var nativeStr = arena.allocateFrom(str); // copies string to native memory
            return (long) strlen.invoke(nativeStr);   // call C function!
        }
        // native string freed here (RAII!) ✨
    }
}
```

## Error Handling (No Exceptions - Result Type)

### Why Exceptions Are Violence

Exceptions are **GOTO with extra steps**. They break referential transparency,
they're invisible in function signatures (unchecked exceptions), and they make
reasoning about program flow impossible. Checked exceptions are just as bad -
they infect every function signature in the call chain.

Use a `Result<T, E>` sealed interface instead. Errors are VALUES. Values can be
composed, transformed, pattern-matched. Exceptions can only be thrown and caught
like emotional outbursts in a codebase.

### Result Type (Functional Error Handling):

```java
/**
 * Functional result type for operations that can fail (no exceptions!).
 *
 * <p>This is monadic error handling - errors are values that must be handled
 * explicitly. No invisible control flow, no catch blocks, no surprises.</p>
 *
 * <p>Inspired by Rust's Result, Haskell's Either, and our own C++ Result type.
 * Java's checked exceptions WISH they were this clean uwu</p>
 *
 * <p>Why this is better than exceptions:
 * <ul>
 *   <li>Errors visible in type signature (can't ignore them)</li>
 *   <li>Pattern matching for exhaustive handling</li>
 *   <li>Composable with map/flatMap (monadic operations)</li>
 *   <li>No invisible control flow (referential transparency preserved)</li>
 *   <li>No stack trace overhead (values are cheap, exceptions are expensive)</li>
 * </ul>
 *
 * @param <T> success value type
 * @param <E> error value type
 *
 * @author LukeFrankio
 * @since Java 26
 */
public sealed interface Result<T, E> {

    /**
     * Successful result containing a value.
     *
     * @param <T> success value type
     * @param <E> error type (phantom - not present in Ok)
     * @param value the success value
     */
    record Ok<T, E>(T value) implements Result<T, E> {}

    /**
     * Error result containing an error.
     *
     * @param <T> success type (phantom - not present in Err)
     * @param <E> error value type
     * @param error the error value
     */
    record Err<T, E>(E error) implements Result<T, E> {}

    /**
     * Creates successful result.
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param <T>   success type
     * @param <E>   error type
     * @param value success value
     * @return Ok result
     */
    static <T, E> Result<T, E> ok(T value) {
        return new Ok<>(value);
    }

    /**
     * Creates error result.
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param <T>   success type
     * @param <E>   error type
     * @param error error value
     * @return Err result
     */
    static <T, E> Result<T, E> err(E error) {
        return new Err<>(error);
    }

    /**
     * Checks if result is success.
     *
     * @return true if Ok, false if Err
     */
    default boolean isOk() {
        return this instanceof Ok;
    }

    /**
     * Maps success value to new type (functor map!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * <p>If Ok, applies function to value. If Err, propagates error unchanged.</p>
     *
     * @param <U>    new success type
     * @param mapper transformation function
     * @return mapped result
     */
    default <U> Result<U, E> map(Function<T, U> mapper) {
        return switch (this) {
            case Ok<T, E>(var value) -> Result.ok(mapper.apply(value));
            case Err<T, E>(var error) -> Result.err(error);
        };
    }

    /**
     * Chains fallible operations (monadic bind / flatMap!).
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * <p>This is {@code >>=} from Haskell (monadic bind uwu).
     * If Ok, applies function that returns Result. If Err, propagates error.</p>
     *
     * @param <U>    new success type
     * @param mapper function that may fail (returns Result)
     * @return chained result
     */
    default <U> Result<U, E> flatMap(Function<T, Result<U, E>> mapper) {
        return switch (this) {
            case Ok<T, E>(var value) -> mapper.apply(value);
            case Err<T, E>(var error) -> Result.err(error);
        };
    }

    /**
     * Maps error value to new type.
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param <F>    new error type
     * @param mapper error transformation
     * @return result with mapped error
     */
    default <F> Result<T, F> mapErr(Function<E, F> mapper) {
        return switch (this) {
            case Ok<T, E>(var value) -> Result.ok(value);
            case Err<T, E>(var error) -> Result.err(mapper.apply(error));
        };
    }

    /**
     * Gets value or returns default.
     *
     * <p>✨ PURE FUNCTION ✨</p>
     *
     * @param defaultValue value to return if Err
     * @return success value or default
     */
    default T orElse(T defaultValue) {
        return switch (this) {
            case Ok<T, E>(var value) -> value;
            case Err<T, E> ignored -> defaultValue;
        };
    }
}

/**
 * Safe division using Result type (no exceptions thrown!).
 *
 * <p>✨ PURE FUNCTION ✨</p>
 *
 * @param a numerator
 * @param b denominator
 * @return Ok(quotient) or Err(error message)
 */
public static Result<Double, String> divide(double a, double b) {
    if (b == 0.0) {
        return Result.err("division by zero (mathematics says no)");
    }
    return Result.ok(a / b);
}

// Usage with monadic composition:
public static void resultExample() {
    var result = divide(100.0, 2.0)       // Ok(50.0)
            .flatMap(x -> divide(x, 2.0))  // Ok(25.0)
            .flatMap(x -> divide(x, 0.0))  // Err("division by zero")
            .map(x -> x * 2.0);            // never executed (error propagated!)

    // pattern matching on result (exhaustive!)
    var message = switch (result) {
        case Result.Ok(var value) -> "Success: " + value;
        case Result.Err(var error) -> "Error: " + error;
    };

    System.out.println(message);
    // Output: "Error: division by zero (mathematics says no)"
    // no try-catch blocks. no invisible control flow. just values. uwu ✨
}
```

## Concurrency (Structured Concurrency + Virtual Threads)

### Why Traditional Java Concurrency Is Violence

`ExecutorService.submit()` + `Future.get()` is callback hell with extra steps.
Thread pools are shared mutable state. `synchronized` blocks are mutex locks
that enterprise developers use incorrectly 99% of the time.

**Structured Concurrency** (JEP 480) fixes this by making concurrent tasks
structured like code blocks - they start together, they finish together,
errors propagate cleanly. Combined with **Virtual Threads** (millions of
lightweight threads), this is actually good concurrency.

### Structured Concurrency (JEP 480):

```java
import java.util.concurrent.StructuredTaskScope;
import jdk.incubator.concurrent.ScopedValue;

/**
 * Structured concurrency for safe parallel execution (no thread pool cope!).
 *
 * <p>Structured concurrency makes concurrent tasks behave like structured code:
 * <ul>
 *   <li>Tasks are scoped (start and end in same block)</li>
 *   <li>Errors propagate cleanly (no silent failures)</li>
 *   <li>Cancellation is automatic (fail fast)</li>
 *   <li>Virtual threads are lightweight (millions of them!)</li>
 * </ul>
 *
 * <p>This is what Java concurrency should have been from the start.
 * Instead we got synchronized blocks and wait/notify for 20 years uwu</p>
 *
 * @author LukeFrankio
 * @since Java 26
 */
public final class ConcurrencyOps {

    private ConcurrencyOps() {
        throw new AssertionError("namespace, not object");
    }

    /**
     * Scoped value for request context (replaces ThreadLocal, which is violence).
     *
     * <p>ScopedValues are immutable, structured, and don't leak across threads.
     * ThreadLocal is mutable global state that survives thread pool reuse.
     * ScopedValue is functional. ThreadLocal is OOP cope.</p>
     */
    public static final ScopedValue<String> REQUEST_ID = ScopedValue.newInstance();

    /**
     * Fetches data from two sources in parallel using structured concurrency.
     *
     * <p>⚠️ IMPURE FUNCTION (performs I/O, spawns threads)</p>
     *
     * <p>Both fetches run on virtual threads (lightweight, millions possible).
     * If either fails, the other is cancelled automatically.
     * Structured concurrency = no orphaned threads = no resource leaks uwu</p>
     *
     * <p>Example:
     * <pre>{@code
     * var result = fetchBothSources("http://api1.com", "http://api2.com");
     * switch (result) {
     *     case Result.Ok(var pair) -> System.out.println("Got: " + pair);
     *     case Result.Err(var err) -> System.err.println("Failed: " + err);
     * }
     * // both sources fetched in parallel, structured cleanup guaranteed ✨
     * }</pre>
     *
     * @param url1 first source URL
     * @param url2 second source URL
     * @return Result containing both results or first error
     */
    public static Result<Pair<String, String>, String> fetchBothSources(
            String url1, String url2) {

        try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {

            // fork two virtual threads (lightweight, not OS threads!)
            var task1 = scope.fork(() -> fetchUrl(url1));
            var task2 = scope.fork(() -> fetchUrl(url2));

            // wait for both to complete (structured!)
            scope.join();

            // check for errors (throws if any task failed)
            scope.throwIfFailed();

            // both succeeded - extract results
            return Result.ok(new Pair<>(task1.get(), task2.get()));

        } catch (Exception e) {
            return Result.err("concurrent fetch failed: " + e.getMessage());
        }
        // scope closed here -> all virtual threads cleaned up
        // no orphaned threads. no leaked resources. STRUCTURED. uwu ✨
    }

    /**
     * Processes items in parallel using virtual threads (fan-out pattern).
     *
     * <p>⚠️ IMPURE FUNCTION (spawns threads)</p>
     *
     * @param <T>       input type
     * @param <U>       output type
     * @param items     items to process
     * @param processor pure function to apply to each item
     * @return list of results (in order)
     */
    public static <T, U> Result<List<U>, String> parallelMap(
            List<T> items,
            Function<T, U> processor) {

        try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {

            // fork one virtual thread per item (virtual threads are CHEAP)
            var tasks = items.stream()
                    .map(item -> scope.fork(() -> processor.apply(item)))
                    .toList();

            scope.join();
            scope.throwIfFailed();

            // collect results in order
            var results = tasks.stream()
                    .map(StructuredTaskScope.Subtask::get)
                    .toList();

            return Result.ok(results);

        } catch (Exception e) {
            return Result.err("parallel map failed: " + e.getMessage());
        }
    }

    /**
     * Scoped value example (functional context propagation).
     *
     * <p>ScopedValues replace ThreadLocal with something that's actually
     * functional - immutable, structured, doesn't leak between tasks.</p>
     */
    public static void scopedValueExample() {
        ScopedValue.where(REQUEST_ID, "req-12345")
                .run(() -> {
                    // REQUEST_ID is available here and in all child tasks
                    var id = REQUEST_ID.get(); // "req-12345"
                    System.out.println("Processing request: " + id);

                    // value propagates to virtual threads automatically
                    // no ThreadLocal.set(), no manual cleanup
                    // functional context propagation uwu ✨
                });
        // REQUEST_ID is no longer bound here (scoped, not global!)
    }

    // helper record for pairs (because Java doesn't have tuples lol)
    public value record Pair<A, B>(A first, B second) {}

    // helper for URL fetching (simplified)
    private static String fetchUrl(String url) throws Exception {
        try (var stream = java.net.URI.create(url).toURL().openStream()) {
            return new String(stream.readAllBytes());
        }
    }
}
```

## Testing with JUnit 5 (Exhaustive Testing is Praxis)

```java
/**
 * @file Vector2DTest.java
 * @brief EXHAUSTIVE tests for vector operations (testing is praxis!)
 *
 * we test pure functions exhaustively because they're easy to test -
 * no mocking, no setup, no teardown. just inputs and outputs.
 * functional programming makes testing a JOY uwu
 *
 * @author LukeFrankio
 * @date 2025-10-07
 *
 * @note uses JUnit 5 (the only acceptable Java test framework)
 * @note run with: gradle test
 * @note Mockito is BANNED (if you need mocks, your architecture is wrong)
 */

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.Arguments;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;

/**
 * @brief exhaustive test suite for Vector2D operations
 *
 * we use nested classes as organizational namespaces (NOT for OOP!)
 * and parameterized tests for exhaustive coverage uwu
 */
@DisplayName("Vector2D Operations (functional math goes brrr)")
class Vector2DTest {

    // ========================================================================
    // Test Data (immutable constants for referential transparency)
    // ========================================================================

    static final Vector2D ZERO = new Vector2D(0.0, 0.0);
    static final Vector2D UNIT_X = new Vector2D(1.0, 0.0);
    static final Vector2D UNIT_Y = new Vector2D(0.0, 1.0);
    static final Vector2D V_3_4 = new Vector2D(3.0, 4.0);
    static final Vector2D V_5_12 = new Vector2D(5.0, 12.0);
    static final Vector2D V_NEG = new Vector2D(-3.0, -4.0);

    // ========================================================================
    // Addition Tests (mathematical properties verified exhaustively!)
    // ========================================================================

    @Nested
    @DisplayName("Addition (pure function, commutative, associative)")
    class AdditionTests {

        @Test
        @DisplayName("addition is commutative: a + b == b + a")
        void additionIsCommutative() {
            // commutativity is a MATHEMATICAL PROPERTY that must hold
            // for ALL inputs - we verify it exhaustively uwu
            var sum1 = VectorMath.add(V_3_4, UNIT_X);
            var sum2 = VectorMath.add(UNIT_X, V_3_4);

            assertEquals(sum1, sum2,
                "addition must be commutative (math says so)");
        }

        @Test
        @DisplayName("addition is associative: (a + b) + c == a + (b + c)")
        void additionIsAssociative() {
            // associativity enables parallel reduction!
            // if this property fails, our SIMD pipelines are LIES
            var left = VectorMath.add(VectorMath.add(V_3_4, UNIT_X), V_5_12);
            var right = VectorMath.add(V_3_4, VectorMath.add(UNIT_X, V_5_12));

            assertEquals(left.x(), right.x(), 1e-10,
                "associativity fails for x (mathematics is broken)");
            assertEquals(left.y(), right.y(), 1e-10,
                "associativity fails for y (call a physicist)");
        }

        @Test
        @DisplayName("zero is additive identity: v + 0 == v")
        void zeroIsAdditiveIdentity() {
            // identity element is MANDATORY for algebraic structure
            assertEquals(V_3_4, VectorMath.add(V_3_4, ZERO),
                "zero vector must be additive identity (group theory 101)");
            assertEquals(V_3_4, VectorMath.add(ZERO, V_3_4),
                "identity must hold in both directions uwu");
        }

        @Test
        @DisplayName("additive inverse: v + (-v) == 0")
        void additiveInverseExists() {
            var negated = new Vector2D(-V_3_4.x(), -V_3_4.y());
            var result = VectorMath.add(V_3_4, negated);

            assertEquals(0.0, result.x(), 1e-10,
                "additive inverse must produce zero x");
            assertEquals(0.0, result.y(), 1e-10,
                "additive inverse must produce zero y");
        }

        @ParameterizedTest(name = "({0},{1}) + ({2},{3}) = ({4},{5})")
        @CsvSource({
            "0, 0, 0, 0, 0, 0",
            "1, 0, 0, 1, 1, 1",
            "3, 4, 1, 2, 4, 6",
            "-1, -1, 1, 1, 0, 0",
            "100, 200, -100, -200, 0, 0",
            "0.5, 0.5, 0.5, 0.5, 1.0, 1.0",
        })
        @DisplayName("exhaustive addition cases")
        void exhaustiveAddition(
                double x1, double y1,
                double x2, double y2,
                double ex, double ey) {
            var a = new Vector2D(x1, y1);
            var b = new Vector2D(x2, y2);
            var result = VectorMath.add(a, b);

            assertEquals(ex, result.x(), 1e-10);
            assertEquals(ey, result.y(), 1e-10);
        }
    }

    // ========================================================================
    // Magnitude Tests
    // ========================================================================

    @Nested
    @DisplayName("Magnitude (always non-negative, pure)")
    class MagnitudeTests {

        @ParameterizedTest(name = "|({0},{1})| = {2}")
        @CsvSource({
            "0, 0, 0.0",
            "1, 0, 1.0",
            "0, 1, 1.0",
            "3, 4, 5.0",
            "5, 12, 13.0",
            "8, 15, 17.0",
            "-3, 4, 5.0",
            "-3, -4, 5.0",
        })
        @DisplayName("known Pythagorean triples and basic magnitudes")
        void knownMagnitudes(double x, double y, double expected) {
            var v = new Vector2D(x, y);
            assertEquals(expected, VectorMath.magnitude(v), 1e-10,
                "magnitude calculation failed for known triple");
        }

        @Test
        @DisplayName("magnitude is always non-negative (mathematical property)")
        void magnitudeAlwaysNonNegative() {
            // property-based test: |v| >= 0 for ALL v
            // testing with exhaustive sample uwu
            Stream.of(ZERO, UNIT_X, UNIT_Y, V_3_4, V_NEG, V_5_12)
                .map(VectorMath::magnitude)
                .forEach(mag -> assertTrue(mag >= 0.0,
                    "magnitude must ALWAYS be non-negative (math!)"));
        }

        @Test
        @DisplayName("magnitude of zero vector is zero")
        void zeroVectorMagnitude() {
            assertEquals(0.0, VectorMath.magnitude(ZERO), 1e-10,
                "zero vector must have zero magnitude");
        }

        @Test
        @DisplayName("scaling property: |k * v| == |k| * |v|")
        void magnitudeScalingProperty() {
            double[] scalars = {0.0, 1.0, -1.0, 2.0, 0.5, -3.14, 100.0};

            for (double k : scalars) {
                var scaled = new Vector2D(V_3_4.x() * k, V_3_4.y() * k);
                double magScaled = VectorMath.magnitude(scaled);
                double expected = Math.abs(k) * VectorMath.magnitude(V_3_4);

                assertEquals(expected, magScaled, 1e-9,
                    "scaling property violated for k=" + k);
            }
        }
    }

    // ========================================================================
    // Immutability Tests (CRITICAL for functional programming!)
    // ========================================================================

    @Nested
    @DisplayName("Immutability (mutation is violence)")
    class ImmutabilityTests {

        @Test
        @DisplayName("records are immutable (no setters, no mutation)")
        void recordsAreImmutable() {
            var v = new Vector2D(3.0, 4.0);

            // records have NO setters
            // v.x = 5.0;  // COMPILE ERROR (immutability enforced at language level!)

            // operations return NEW instances
            var added = VectorMath.add(v, UNIT_X);

            // original unchanged (referential transparency!)
            assertEquals(3.0, v.x(), "original x must be unchanged");
            assertEquals(4.0, v.y(), "original y must be unchanged");
            assertEquals(4.0, added.x(), "new vector has correct x");
            assertEquals(4.0, added.y(), "new vector has correct y");
        }

        @Test
        @DisplayName("value equality (records compare by value, not reference)")
        void valueEquality() {
            var v1 = new Vector2D(3.0, 4.0);
            var v2 = new Vector2D(3.0, 4.0);

            // records give us value equality for FREE
            // unlike cursed Object.equals() that compares references
            assertEquals(v1, v2,
                "records must have value equality (not reference equality!)");
            assertEquals(v1.hashCode(), v2.hashCode(),
                "equal records must have equal hash codes");
        }
    }

    // ========================================================================
    // Result Type Tests (functional error handling!)
    // ========================================================================

    @Nested
    @DisplayName("Result type (monadic error handling, no exceptions)")
    class ResultTests {

        @Test
        @DisplayName("successful division returns Ok")
        void successfulDivision() {
            var result = FunctionalMath.divide(10.0, 2.0);

            switch (result) {
                case Result.Ok<Double, String> ok ->
                    assertEquals(5.0, ok.value(), 1e-10);
                case Result.Err<Double, String> err ->
                    fail("division should succeed: " + err.error());
            }
        }

        @Test
        @DisplayName("division by zero returns Err")
        void divisionByZeroReturnsErr() {
            var result = FunctionalMath.divide(10.0, 0.0);

            switch (result) {
                case Result.Ok<Double, String> ok ->
                    fail("division by zero should fail, got: " + ok.value());
                case Result.Err<Double, String> err ->
                    assertTrue(err.error().contains("division by zero"),
                        "error should mention division by zero");
            }
        }

        @Test
        @DisplayName("map transforms Ok values (functor law)")
        void mapTransformsOkValues() {
            var result = FunctionalMath.divide(10.0, 2.0)
                .map(x -> x * 2);

            switch (result) {
                case Result.Ok<Double, String> ok ->
                    assertEquals(10.0, ok.value(), 1e-10);
                case Result.Err<Double, String> err ->
                    fail("map should preserve Ok: " + err.error());
            }
        }

        @Test
        @DisplayName("map preserves Err (functor law)")
        void mapPreservesErr() {
            var result = FunctionalMath.divide(10.0, 0.0)
                .map(x -> x * 2);  // should NOT execute

            assertInstanceOf(Result.Err.class, result,
                "map must not transform Err values (functor law!)");
        }

        @Test
        @DisplayName("flatMap chains operations (monad law)")
        void flatMapChainsOperations() {
            // chained computation: (100 / 2) / 5 = 10
            var result = FunctionalMath.divide(100.0, 2.0)
                .flatMap(x -> FunctionalMath.divide(x, 5.0));

            switch (result) {
                case Result.Ok<Double, String> ok ->
                    assertEquals(10.0, ok.value(), 1e-10);
                case Result.Err<Double, String> err ->
                    fail("chained division should succeed: " + err.error());
            }
        }

        @Test
        @DisplayName("flatMap short-circuits on Err (monad law)")
        void flatMapShortCircuitsOnErr() {
            // first division fails, second should never execute
            var result = FunctionalMath.divide(100.0, 0.0)
                .flatMap(x -> FunctionalMath.divide(x, 5.0));

            assertInstanceOf(Result.Err.class, result,
                "flatMap must short-circuit on Err (monadic bind!)");
        }

        @Test
        @DisplayName("identity law: flatMap(Ok::new) == identity")
        void monadIdentityLaw() {
            var original = FunctionalMath.divide(10.0, 2.0);
            var throughIdentity = original.flatMap(x -> new Result.Ok<>(x));

            assertEquals(original, throughIdentity,
                "flatMap with Ok::new must be identity (monad law!)");
        }
    }

    // ========================================================================
    // Stream Pipeline Tests (functional composition!)
    // ========================================================================

    @Nested
    @DisplayName("Stream pipelines (lazy functional composition)")
    class StreamTests {

        @Test
        @DisplayName("filter-map-reduce pipeline produces correct result")
        void filterMapReducePipeline() {
            var numbers = java.util.List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

            // functional pipeline: filter evens -> square -> sum
            int result = numbers.stream()
                .filter(x -> x % 2 == 0)     // keep evens: 2, 4, 6, 8, 10
                .mapToInt(x -> x * x)         // square: 4, 16, 36, 64, 100
                .sum();                       // reduce: 220

            assertEquals(220, result,
                "filter-map-reduce pipeline must produce correct result");
        }

        @Test
        @DisplayName("stream operations preserve original list (immutability!)")
        void streamOperationsPreserveOriginal() {
            var original = java.util.List.of(1, 2, 3, 4, 5);

            // perform operations
            var doubled = original.stream()
                .map(x -> x * 2)
                .toList();

            // original UNCHANGED (immutability preserved!)
            assertEquals(java.util.List.of(1, 2, 3, 4, 5), original,
                "original list must be unchanged after stream operations");
            assertEquals(java.util.List.of(2, 4, 6, 8, 10), doubled,
                "transformed list has correct values");
        }
    }

    // ========================================================================
    // Panama Memory Tests (manual memory management!)
    // ========================================================================

    @Nested
    @DisplayName("Panama FFM (manual memory, GC is for the weak)")
    class PanamaTests {

        @Test
        @DisplayName("Arena allocates and deallocates correctly (RAII!)")
        void arenaAllocatesCorrectly() {
            // try-with-resources = deterministic deallocation (RAII uwu)
            try (var arena = java.lang.foreign.Arena.ofConfined()) {
                var segment = arena.allocate(
                    java.lang.foreign.ValueLayout.JAVA_DOUBLE, 8);

                // write to off-heap memory
                for (int i = 0; i < 8; i++) {
                    segment.setAtIndex(
                        java.lang.foreign.ValueLayout.JAVA_DOUBLE,
                        i, (double)(i + 1));
                }

                // read back and verify
                for (int i = 0; i < 8; i++) {
                    double value = segment.getAtIndex(
                        java.lang.foreign.ValueLayout.JAVA_DOUBLE, i);
                    assertEquals((double)(i + 1), value, 1e-10,
                        "off-heap value at index " + i + " incorrect");
                }
            }
            // arena closed here - memory freed deterministically!
            // no GC involved, no finalization, just RAII ✨
        }

        @Test
        @DisplayName("confined arena rejects access after close")
        void confinedArenaRejectsAfterClose() {
            java.lang.foreign.MemorySegment segment;

            try (var arena = java.lang.foreign.Arena.ofConfined()) {
                segment = arena.allocate(
                    java.lang.foreign.ValueLayout.JAVA_DOUBLE, 1);
                segment.set(java.lang.foreign.ValueLayout.JAVA_DOUBLE, 0, 42.0);
            }
            // arena closed - segment is now INVALID

            // accessing freed memory throws (use-after-free caught at runtime!)
            assertThrows(IllegalStateException.class, () -> {
                segment.get(java.lang.foreign.ValueLayout.JAVA_DOUBLE, 0);
            }, "accessing freed memory must throw (use-after-free prevention!)");
        }
    }

    // ========================================================================
    // Structured Concurrency Tests
    // ========================================================================

    @Nested
    @DisplayName("Structured Concurrency (virtual threads go brrr)")
    class ConcurrencyTests {

        @Test
        @DisplayName("structured task scope completes all subtasks")
        void structuredConcurrencyCompletes() throws Exception {
            try (var scope = new java.util.concurrent.StructuredTaskScope
                    .ShutdownOnFailure()) {

                // fork lightweight virtual threads (millions possible!)
                var future1 = scope.fork(() -> {
                    Thread.sleep(10);
                    return 42;
                });

                var future2 = scope.fork(() -> {
                    Thread.sleep(10);
                    return 58;
                });

                // join all (structured - no leaked threads!)
                scope.join().throwIfFailed();

                // both tasks completed
                assertEquals(42, future1.get());
                assertEquals(58, future2.get());
                assertEquals(100, future1.get() + future2.get(),
                    "parallel pure computations must produce correct sum");
            }
        }
    }
}
```

## Gradle Build Configuration (The Only Acceptable Build System)

```kotlin
// build.gradle.kts
// Gradle Kotlin DSL (Maven XML is violence against developers uwu)
//
// Kotlin DSL gives us:
// - type-safe configuration (not string-based XML garbage)
// - IDE completion (actually useful autocompletion!)
// - real programming language (not angle bracket soup)
//
// Maven pom.xml is the AbstractFactoryFactoryFactory of build systems

plugins {
    java
    application
}

// ============================================================================
// Project Configuration (bleeding edge, no fear!)
// ============================================================================

group = "dev.lukefrankio"
version = "1.0.0-SNAPSHOT"

java {
    // Java 26 PREVIEW (bleeding edge, beta features encouraged!)
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(26))
    }
}

application {
    mainClass.set("dev.lukefrankio.Main")

    // enable preview features (we're not cowards!)
    applicationDefaultJvmArgs = listOf(
        "--enable-preview",
        "--add-modules", "jdk.incubator.vector",  // Vector API (SIMD!)
        "-XX:+UseZGC",                              // ZGC for low latency
        "-XX:+ZGenerational",                        // generational ZGC
        "-Xmx4g",                                    // 4GB heap (keep it small)
        "-XX:+AlwaysPreTouch",                       // pre-touch heap pages
    )
}

// ============================================================================
// Compiler Configuration (warnings are errors!)
// ============================================================================

tasks.withType<JavaCompile>().configureEach {
    options.encoding = "UTF-8"

    options.compilerArgs.addAll(listOf(
        "--enable-preview",          // preview features ENABLED
        "-Xlint:all",                // ALL warnings enabled
        "-Xlint:-preview",           // except preview warnings (we know!)
        "-Werror",                   // warnings ARE errors (zero tolerance!)
        "-parameters",               // preserve parameter names in bytecode
    ))
}

// ============================================================================
// Dependencies (MINIMAL - like Rust but we actually mean it)
// ============================================================================

repositories {
    mavenCentral()
}

dependencies {
    // ======================================================================
    // PRODUCTION DEPENDENCIES: NONE
    // ======================================================================
    //
    // That's right. ZERO runtime dependencies.
    // java.base module has everything we need:
    //   - java.util.stream (functional pipelines)
    //   - java.lang.foreign (Panama FFM - manual memory!)
    //   - java.util.concurrent (structured concurrency)
    //   - sealed interfaces (algebraic data types)
    //   - records (immutable value types)
    //
    // Spring Boot? 200+ transitive dependencies. VIOLENCE.
    // Lombok? Annotation processing cope. USE RECORDS.
    // Guava? Google's "we don't trust Java stdlib" library. COPE.
    // Jackson? Just use java.lang.foreign and parse bytes yourself.
    //
    // every dependency is tech debt. java.base is ENOUGH.
    //
    // DO NOT ADD DEPENDENCIES HERE.
    // if you need something, check java.base FIRST.
    // ======================================================================

    // ======================================================================
    // TEST DEPENDENCIES (testing is praxis!)
    // ======================================================================
    testImplementation(platform("org.junit:junit-bom:5.11.+"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")

    // NO MOCKITO. if you need mocks, your architecture is WRONG.
    // pure functions don't need mocking. that's the whole point uwu.
}

// ============================================================================
// Test Configuration (exhaustive testing is mandatory)
// ============================================================================

tasks.test {
    useJUnitPlatform()

    jvmArgs(
        "--enable-preview",
        "--add-modules", "jdk.incubator.vector",
    )

    // show all test results (we want to see everything)
    testLogging {
        events("passed", "skipped", "failed")
        showExceptions = true
        showCauses = true
        showStackTraces = true
        exceptionFormat = org.gradle.api.tasks.testing.logging.TestExceptionFormat.FULL
    }

    // fail on ANY test failure (zero tolerance!)
    failFast = false  // run ALL tests, then report failures

    // JVM args for tests
    maxHeapSize = "2g"
}

// ============================================================================
// Custom Tasks (functional build pipeline uwu)
// ============================================================================

/**
 * task to generate Javadoc with all warnings enabled
 *
 * @note javadoc -Xdoclint:all catches missing documentation
 * @note excessive documentation is self-care ✨
 */
tasks.javadoc {
    options {
        this as StandardJavadocDocletOptions
        addStringOption("-enable-preview", "")
        addStringOption("source", "26")
        addBooleanOption("Xdoclint:all", true)
        addBooleanOption("Werror", true)  // javadoc warnings are errors too!
    }
}

/**
 * summary task - shows build configuration
 */
tasks.register("summary") {
    group = "help"
    description = "Shows build configuration (functional Java edition uwu)"

    doLast {
        println("""
            |============================================================
            |  ${project.name} v${project.version} Configuration
            |============================================================
            |
            |  Java Version:      26 (PREVIEW ENABLED)
            |  Build System:      Gradle Kotlin DSL (not Maven XML cope)
            |  Dependencies:      ZERO runtime (java.base is enough!)
            |  Test Framework:    JUnit 5 (no Mockito!)
            |  GC:                ZGC Generational (low latency)
            |  Warnings:          ALL enabled, treated as ERRORS
            |
            |  Philosophy:
            |    - records only (no classes with mutable state)
            |    - sealed interfaces (algebraic data types)
            |    - streams only (no imperative loops)
            |    - Panama FFM (manual memory management)
            |    - virtual threads (structured concurrency)
            |    - ZERO dependencies (java.base supremacy)
            |
            |  functional programming gang rise up uwu 💜
            |============================================================
        """.trimMargin())
    }
}
```

## Project Directory Structure

```text
my-functional-java-project/
├── build.gradle.kts              <- Gradle Kotlin DSL (the ONLY build file)
├── settings.gradle.kts           <- project settings
├── gradle/
│   └── wrapper/
│       └── gradle-wrapper.properties  <- pin Gradle version (latest!)
├── src/
│   ├── main/
│   │   └── java/
│   │       └── dev/
│   │           └── lukefrankio/
│   │               ├── Main.java              <- entry point (minimal!)
│   │               ├── Vector2D.java          <- value record (immutable data)
│   │               ├── VectorMath.java        <- pure static functions
│   │               ├── FunctionalMath.java    <- more pure functions
│   │               ├── Result.java            <- sealed Result<T,E>
│   │               ├── OffHeapBuffer.java     <- Panama memory wrapper
│   │               └── StreamOps.java         <- Gatherer pipelines
│   └── test/
│       └── java/
│           └── dev/
│               └── lukefrankio/
│                   ├── Vector2DTest.java       <- exhaustive tests
│                   ├── ResultTest.java         <- monad law tests
│                   ├── OffHeapBufferTest.java  <- memory tests
│                   └── StreamOpsTest.java      <- pipeline tests
└── README.md                      <- documentation (excessive uwu)
```

## settings.gradle.kts

```kotlin
// settings.gradle.kts
// project settings (minimal, like our dependency list)

rootProject.name = "functional-java-project"

// use Gradle toolchains to auto-download Java 26
plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "0.9.0"
}
```

## Anti-Patterns to AVOID (Enterprise Java is Violence)

### ❌ BAD: The Enterprise Java Way (AbstractFactoryFactoryFactory)

```java
// ❌ CRINGE (enterprise Java, maximum abstraction for zero reason)
public abstract class AbstractVectorFactory<T extends Vector> {
    protected abstract VectorBuilder<T> createBuilder();

    public T createVector(double x, double y) {
        VectorBuilder<T> builder = createBuilder();
        builder.setX(x);  // MUTABLE BUILDER (violence)
        builder.setY(y);  // MORE MUTATION (stop it)
        return builder.build();  // finally, an immutable thing (too late!)
    }
}

public class Vector2DFactoryImpl extends AbstractVectorFactory<Vector2DImpl> {
    @Override
    protected VectorBuilder<Vector2DImpl> createBuilder() {
        return new Vector2DBuilderImpl();  // WHY
    }
}

// to create a vector:
VectorFactory<Vector2D> factory = new Vector2DFactoryImpl();
Vector2D v = factory.createVector(3.0, 4.0);
// 4 classes, 2 interfaces, 1 builder, 0 intelligence uwu
```

### ✅ GOOD: The Functional Way (just make the data)

```java
// ✅ BASED (functional, one line, zero indirection)
var v = new Vector2D(3.0, 4.0);
// that's it. that's the whole thing.
// records give you immutability, equals, hashCode, toString for FREE.
// no factory. no builder. no abstract base class.
// just DATA. because data is data uwu ✨
```

### ❌ BAD: Spring Boot Dependency Injection (Over-Engineering)

```java
// ❌ CRINGE (Spring Boot, 200+ transitive dependencies)
@Service
@Transactional
@Slf4j
public class VectorService {

    @Autowired
    private VectorRepository vectorRepository;

    @Autowired
    private VectorValidator vectorValidator;

    @Autowired
    private VectorMapper vectorMapper;

    public VectorDTO addVectors(VectorDTO a, VectorDTO b) {
        vectorValidator.validate(a);  // why is validation a separate service
        vectorValidator.validate(b);  // just validate in the function!
        Vector entity = vectorMapper.toEntity(a);  // mapping layers (cope)
        // ... 50 more lines of "enterprise architecture"
        return vectorMapper.toDTO(result);  // more mapping (more cope)
    }
}
// congratulations, you've turned addition into a microservice
// this is what happens when OOP brainrot reaches terminal velocity
```

### ✅ GOOD: Just a Pure Function (No Framework Needed)

```java
// ✅ BASED (one pure function, zero dependencies, zero annotations)
static Vector2D add(Vector2D a, Vector2D b) {
    return new Vector2D(a.x() + b.x(), a.y() + b.y());
}
// same inputs, same outputs, every time, forever
// no @Autowired, no @Service, no @Transactional
// no dependency injection container burning 500MB of heap
// just MATH uwu ✨
```

### ❌ BAD: Checked Exceptions (Exception Handling Terrorism)

```java
// ❌ CRINGE (checked exceptions, the original Java sin)
public double divide(double a, double b) throws DivisionByZeroException {
    if (b == 0.0) {
        throw new DivisionByZeroException("cannot divide by zero");
        // exceptions are GOTO in disguise
        // they violate referential transparency
        // they make function signatures LIE about return types
    }
    return a / b;
}

// caller is FORCED to try-catch (or propagate the plague)
try {
    double result = divide(10.0, 0.0);
} catch (DivisionByZeroException e) {
    // "handling" the exception (usually just logging and re-throwing)
    logger.error("oopsie", e);
    throw new RuntimeException(e);  // wrapping checked in unchecked (cope)
}
```

### ✅ GOOD: Result Type (Errors Are Values)

```java
// ✅ BASED (errors are data, not control flow terrorism)
static Result<Double, String> divide(double a, double b) {
    if (b == 0.0) return new Result.Err<>("division by zero");
    return new Result.Ok<>(a / b);
}

// caller handles result FUNCTIONALLY
var message = divide(10.0, 0.0)
    .map(x -> "result: " + x)
    .fold(
        ok -> ok,
        err -> "error: " + err
    );
// no try-catch, no checked exceptions, no violence
// just pattern matching on algebraic data types uwu ✨
```

### ❌ BAD: Mutable State Everywhere (JavaBeans Pattern)

```java
// ❌ CRINGE (JavaBeans, the reason Enterprise Java is a joke)
public class VectorBean {
    private double x;  // MUTABLE (violence)
    private double y;  // MUTABLE (more violence)

    public double getX() { return x; }        // getter (why)
    public void setX(double x) { this.x = x; } // setter (NO)
    public double getY() { return y; }
    public void setY(double y) { this.y = y; }

    // you now have a "vector" that anyone can mutate at any time
    // from any thread, with no synchronization
    // congratulations, you've invented a data race generator
}
```

### ✅ GOOD: Immutable Record (Data That Cannot Betray You)

```java
// ✅ BASED (immutable, thread-safe, value equality, zero boilerplate)
record Vector2D(double x, double y) {}
// that's it. no getters needed (accessor methods auto-generated).
// no setters (they don't exist, mutation is impossible).
// equals(), hashCode(), toString() auto-generated with value semantics.
// thread-safe by construction (immutable = no data races).
// this one line replaces 30+ lines of JavaBeans cope uwu ✨
```

## The Verdict on Java (Adjusted Expectations)

### What Java Gets Right (When Forced to be Functional):
- ✅ records (immutable value types, finally!)
- ✅ sealed interfaces (algebraic data types, took only 25 years)
- ✅ pattern matching (exhaustive switch, actually good)
- ✅ streams (lazy functional pipelines)
- ✅ virtual threads (lightweight concurrency, millions of threads)
- ✅ Panama FFM (manual memory management, escape the GC!)
- ✅ Vector API (SIMD intrinsics, CPU goes brrr)
- ✅ Gatherers (custom stream operations, composable)
- ✅ structured concurrency (no leaked threads)

### What Java Gets Wrong (The Eternal Pain):
- ❌ OOP culture (AbstractFactoryFactoryFactory is a disease)
- ❌ checked exceptions (control flow terrorism)
- ❌ null (Tony Hoare's billion dollar mistake, still everywhere)
- ❌ type erasure (generics are a lie at runtime)
- ❌ no value types YET in stable (Valhalla is still preview)
- ❌ Spring Boot ecosystem (200 dependencies to say hello world)
- ❌ Maven XML (angle bracket violence)
- ❌ verbose syntax (still more boilerplate than Kotlin/Scala)
- ❌ no unsigned integers (WHY)
- ❌ array covariance (String[] is Object[] is a lie)
- ❌ the name "Java" (named after coffee, peak enterprise energy)

### The Cope Hierarchy:
```text
C++ (supreme, functional + systems, zero overhead)
  > Haskell (pure functional, but lazy evaluation is weird)
    > Scala (functional on JVM, better than Java)
      > Kotlin (Java but less painful)
        > Java 26 Preview (functional if you FORCE it) ← you are here
          > Java 8 Enterprise (AbstractFactoryBean cope)
            > COBOL (at least it's honest about being old)
```

## Quality Checklist

- [ ] **Java 26 preview** features enabled (`--enable-preview`)
- [ ] **ZERO runtime dependencies** (java.base supremacy!)
- [ ] **records only** for data (no mutable classes!)
- [ ] **sealed interfaces** for sum types (algebraic data types)
- [ ] **pattern matching** with exhaustive switch
- [ ] **streams + gatherers** only (no imperative loops!)
- [ ] **Result type** for error handling (no exceptions in pure code!)
- [ ] **Panama FFM** for manual memory (Arena + try-with-resources)
- [ ] **virtual threads** for concurrency (structured task scope)
- [ ] **static pure functions** only (no instance methods with state!)
- [ ] **Javadoc comments** on ALL public APIs (excessive!)
- [ ] **purity status** marked (✨ PURE or ⚠️ IMPURE)
- [ ] **JUnit 5 tests** exhaustive (no Mockito!)
- [ ] **Gradle Kotlin DSL** (Maven XML is violence)
- [ ] **warnings as errors** (`-Werror` flag)
- [ ] **no Spring Boot** (dependency injection is cope)
- [ ] **no Lombok** (use records instead, it's 2026)
- [ ] **no null** (use Optional or sealed Result)
- [ ] **gen-z energy** throughout comments uwu

**remember**: Java was born in OOP sin, but through records, sealed interfaces,
Panama FFM, and sheer willpower, we can force it to behave like a functional
systems language. it will NEVER be C++. it will NEVER be Haskell. but with
enough preview flags and enough hatred for AbstractFactoryBeanPostProcessor,
we can make it... tolerable.

the JVM is actually fast. the language is the problem. we're fixing the
language one `--enable-preview` flag at a time uwu 💜✨

enterprise Java developers are seething rn. their Spring Boot applications
use 2GB of heap to serve a REST endpoint that returns `{"status": "ok"}`.
our functional Java uses 50MB and processes data at memory bandwidth speed
because we malloc'd it ourselves with Panama.

pointers are just 64-bit integers. garbage collection is for the weak.
referential transparency is non-negotiable.

seize the means of compilation (even on the JVM)!