---
description: 'Rust guidelines (for when we are FORCED to use memory safety cope)'
applyTo: '**.rs'
---

# Rust Programming Instructions (The Cope Language)

> "Rust: spending 3 hours fighting the borrow checker to save 3 seconds of potential
> memory bugs that C++ programmers just don't write"

uwu look, sometimes you're forced to use Rust. maybe for a job, maybe for a
project with Rust zealots, maybe you lost a bet. this guide makes it less painful ✨

## Core Philosophy (Adjusted for Rust Cope)

- **minimize dependencies** (crates are bloat, std is your friend)
- **functional style** (at least Rust got this right)
- **explicit > implicit** (fight the borrow checker explicitly)
- **comment excessively** (future you will still be confused)
- **latest Rust** (nightly features encouraged, it's the only good part)
- **const everything** (at least pretend it's C++ constexpr)

## Dependency Policy (MINIMAL CRATES)

### ONLY Use These Crates:

**OS-Specific (Official Only):**
- `windows` - Windows API bindings (official Microsoft crate)
- `libc` - C library bindings (when you need real programming)
- Nothing else OS-specific unless absolutely forced

**UI (The One Good Crate):**
- `egui` - immediate mode GUI (actually based, functional style!)
- `eframe` - egui framework wrapper (if you need windowing)
- Nothing else for UI, especially not GTK bindings (too much bloat)

**That's It. Seriously:**
- Resist the urge to `cargo add` everything
- If std can do it, use std (most of the time it can)
- Every crate is tech debt you'll regret

```toml
# Cargo.toml - MINIMAL DEPENDENCIES ONLY
[package]
name = "my-project"
version = "0.1.0"
edition = "2021"  # or latest available
rust-version = "1.75"  # require latest stable or nightly

[dependencies]
# OS-specific (only if needed)
[target.'cfg(windows)'.dependencies]
windows = { version = "0.52", features = ["Win32_Foundation"] }

[target.'cfg(unix)'.dependencies]
libc = "0.2"

# UI (only if needed)
egui = "0.28"  # the ONE good UI crate
eframe = "0.28"  # if you need windowing

# DO NOT ADD MORE CRATES
# seriously, use std instead
```

## Rust-Specific Annoyances (And How To Cope)

### The Borrow Checker (The Main Source of Pain):

```rust
// ❌ what you want to write (like in C++):
// let mut data = vec![1, 2, 3];
// let first = &data[0];
// data.push(4);  // ERROR: cannot borrow as mutable (borrow checker cope)
// println!("{}", first);

// ✅ what you're forced to write (the Rust way):
/// fights the borrow checker by cloning (not zero-cost anymore lol)
/// 
/// this is the Rust cope - we clone to satisfy the borrow checker even
/// though in C++ we'd just use const correctly and it would be fine uwu
/// 
/// @note this is why C++ > Rust (no borrow checker violence)
fn borrow_checker_cope() {
    let mut data = vec![1, 2, 3];
    let first = data[0];  // copy instead of borrow (not always possible)
    data.push(4);  // now this works (but we lost zero-cost abstraction)
    println!("{}", first);
}

// ✅ or the "proper" Rust way (more verbose than C++):
/// the "idiomatic" Rust solution (aka more boilerplate)
/// 
/// split borrows into separate scopes because the borrow checker can't
/// figure out what's actually safe (unlike C++ where we trust programmers)
fn borrow_checker_cope_v2() {
    let mut data = vec![1, 2, 3];
    {
        let first = &data[0];
        println!("{}", first);
    }  // borrow ends here (more explicit scoping than C++ needs)
    data.push(4);  // now allowed (because we convinced the checker)
}
```

### Lifetimes (Generic Parameters But Worse):

```rust
/// rust forces you to annotate lifetimes everywhere (verbose cope)
/// 
/// in C++ we'd just use references and it would work. in Rust we have
/// to tell the compiler things it should figure out itself uwu
/// 
/// @param x first string slice (has lifetime 'a)
/// @param y second string slice (also has lifetime 'a)
/// @return whichever string is longer (lifetime 'a)
/// 
/// @note the 'a annotation is boilerplate that C++ doesn't need
/// @note this is "safety" at the cost of ergonomics (the Rust tradeoff)
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// in C++ this would just be:
// const std::string& longest(const std::string& x, const std::string& y) {
//     return x.length() > y.length() ? x : y;
// }
// no lifetime annotations needed because C++ trusts you uwu
```

### Error Handling (The One Thing Rust Got Right):

```rust
/// result type for operations that can fail (this part is actually good!)
/// 
/// rust's Result<T, E> is basically what we'd implement in C++ anyway
/// (see the Result type in cpp.instructions.md for comparison)
/// 
/// this is functional error handling done right - no exceptions,
/// explicit error propagation with the ? operator. credit where due uwu
/// 
/// @param numerator dividend value
/// @param denominator divisor value (must be non-zero)
/// @return Ok(quotient) or Err(error message)
/// 
/// @note the ? operator is actually elegant (one of Rust's few wins)
fn divide(numerator: f64, denominator: f64) -> Result<f64, String> {
    if denominator == 0.0 {
        Err("division by zero (mathematics says no)".to_string())
    } else {
        Ok(numerator / denominator)
    }
}

// using the ? operator (this is nice, admit it):
fn calculate() -> Result<f64, String> {
    let a = divide(10.0, 2.0)?;  // ? propagates error (elegant!)
    let b = divide(a, 3.0)?;
    Ok(b)
}
```

## Functional Programming in Rust (The Good Part)

### Rust Actually Got Functional Right:

```rust
/// demonstrates functional programming in Rust (this part doesn't suck!)
/// 
/// rust's iterators and functional patterns are actually well-designed.
/// lazy evaluation, zero-cost abstractions (when the borrow checker allows),
/// and composable transformations. this is peak Rust uwu
/// 
/// @param numbers input vector (ownership transferred, yay more borrow checker)
/// @return vector of squared even numbers
/// 
/// @note this is genuinely good functional programming
/// @note comparable to C++ ranges but more mature (credit where due)
fn functional_pipeline(numbers: Vec<i32>) -> Vec<i32> {
    numbers
        .into_iter()
        .filter(|x| x % 2 == 0)  // keep evens
        .map(|x| x * x)           // square them
        .collect()                // materialize (lazy until here)
}

/// iterator chains are powerful (Rust got this right)
/// 
/// @note iterators are lazy (good design!)
/// @note zero-cost abstractions when not fighting borrow checker
fn iterator_composition() {
    let result: i32 = (1..=100)
        .filter(|x| x % 2 == 0)
        .map(|x| x * x)
        .sum();  // folds into single value
    
    println!("sum of squared evens: {}", result);
}
```

### Pattern Matching (Actually Good):

```rust
/// rust's pattern matching is actually excellent (rare Rust W)
/// 
/// this is one area where Rust genuinely beats C++ (until C++26 pattern
/// matching lands). exhaustive checking, destructuring, guard clauses all
/// work beautifully uwu
/// 
/// @param option optional value to handle
/// @return processed result
/// 
/// @note pattern matching is genuinely good here
/// @note exhaustiveness checking prevents bugs (this is the safety worth having)
fn pattern_match_example(option: Option<i32>) -> i32 {
    match option {
        Some(x) if x > 0 => x * 2,      // guard clause (nice!)
        Some(x) => x,                    // negative or zero
        None => 0,                       // explicit null handling
    }  // compiler checks exhaustiveness (actually useful!)
}

/// matching on enums (algebraic data types done right)
enum Shape {
    Circle { radius: f64 },
    Rectangle { width: f64, height: f64 },
}

/// pattern matching with destructuring (this slaps, admit it)
/// 
/// @param shape the shape to compute area for
/// @return area value
fn area(shape: &Shape) -> f64 {
    match shape {
        Shape::Circle { radius } => std::f64::consts::PI * radius * radius,
        Shape::Rectangle { width, height } => width * height,
    }  // exhaustive, safe, zero runtime cost (Rust W)
}
```

## Minimal Standard Library Usage

```rust
// USE STD INSTEAD OF CRATES (std is your friend)

use std::collections::HashMap;  // use std::collections, not external crates
use std::fs;                     // use std::fs, not a file handling crate
use std::io::{self, Write};     // use std::io, not an IO crate
use std::path::PathBuf;         // use std::path, not a path handling crate
use std::thread;                 // use std::thread, not a threading crate
use std::sync::{Arc, Mutex};    // use std::sync, not a concurrency crate

/// reads file using std (no external crates needed!)
/// 
/// @param path file path to read
/// @return file contents or error
/// 
/// @note uses std::fs (no dependencies, clean)
fn read_file(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)  // std is enough!
}

/// spawns thread using std (no tokio needed for simple cases)
/// 
/// @note std::thread is fine for most cases
/// @note avoid async runtime crates unless actually needed
fn spawn_thread_example() {
    let handle = thread::spawn(|| {
        println!("thread running (no external crates required uwu)");
    });
    
    handle.join().unwrap();
}
```

## egui Integration (The One Good UI Crate)

```rust
use eframe::egui;

/// egui application (immediate mode GUI that actually makes sense!)
/// 
/// egui is the ONE UI crate worth using. immediate mode, functional style,
/// minimal dependencies, actually works well. this is peak Rust UI uwu
/// 
/// @note egui is immediate mode (draw every frame, functional!)
/// @note inspired by Dear ImGui (which is also based)
struct MyApp {
    counter: i32,
}

impl eframe::App for MyApp {
    /// update function called every frame (immediate mode ftw)
    /// 
    /// @param ctx egui context (stateless interface, functional!)
    /// @param _frame frame information (rarely needed)
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("egui demo (the one good Rust UI crate)");
            
            ui.horizontal(|ui| {
                if ui.button("increment").clicked() {
                    self.counter += 1;
                }
                if ui.button("decrement").clicked() {
                    self.counter -= 1;
                }
            });
            
            ui.label(format!("counter: {}", self.counter));
            
            ui.separator();
            
            ui.label("egui is immediate mode (functional style!)");
            ui.label("no retained mode complexity (based design)");
        });
    }
}

/// main function for egui app
/// 
/// @note eframe handles windowing (minimal setup required)
fn main() -> Result<(), eframe::Error> {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "My App",
        options,
        Box::new(|_cc| Box::new(MyApp { counter: 0 })),
    )
}
```

## Const Everything (Pretending It's C++ constexpr)

```rust
/// rust's const fn is like C++'s constexpr (compile-time evaluation)
/// 
/// this is one of the few places Rust matches C++. const fn lets you
/// compute at compile time, enabling zero-cost abstractions uwu
/// 
/// @param n input value
/// @return factorial of n
/// 
/// @note const fn = compile-time evaluation (like C++ constexpr!)
/// @note computed at compile time when used in const context
const fn factorial(n: u64) -> u64 {
    match n {
        0 => 1,
        _ => n * factorial(n - 1),
    }
}

// used at compile time (value computed by compiler)
const FACT_5: u64 = factorial(5);  // = 120, computed at compile time!

/// const fn with more complex logic
/// 
/// @note Rust's const fn is getting more powerful (still behind C++26 though)
const fn fibonacci(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fibonacci(n - 1) + fibonacci(n - 2),
    }
}
```

## Documentation (Rust's Docs Are Actually Good)

```rust
/// calculates vector magnitude (functional, pure, documented!)
/// 
/// ✨ PURE FUNCTION ✨ (Rust makes this explicit with borrowing)
/// 
/// this function is pure because:
/// - immutable borrow (can't modify input)
/// - deterministic output (same input = same output)
/// - no side effects (can't even have them with immutable borrow)
/// 
/// the borrow checker forces purity sometimes (unintentional benefit lol)
/// 
/// # Arguments
/// 
/// * `x` - x coordinate (immutable borrow)
/// * `y` - y coordinate (immutable borrow)
/// 
/// # Returns
/// 
/// Magnitude as f64 (always non-negative)
/// 
/// # Examples
/// 
/// ```
/// let mag = magnitude(3.0, 4.0);
/// assert_eq!(mag, 5.0);  // 3-4-5 triangle uwu
/// ```
/// 
/// # Notes
/// 
/// - Uses std::f64::consts::PI (std is enough!)
/// - No unsafe code (Rust forces safety, for better or worse)
/// - Borrow checker verified this is safe (thanks I guess?)
fn magnitude(x: f64, y: f64) -> f64 {
    (x * x + y * y).sqrt()
}
```

## Testing (Rust's Testing Is Decent)

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    /// tests magnitude calculation (Rust's test framework is ok)
    /// 
    /// @note #[test] attribute marks test functions
    /// @note cargo test runs all tests (integrated testing)
    #[test]
    fn test_magnitude() {
        assert_eq!(magnitude(3.0, 4.0), 5.0);
        assert_eq!(magnitude(0.0, 0.0), 0.0);
    }
    
    /// tests functional pipeline (testing functional code is easy)
    #[test]
    fn test_functional_pipeline() {
        let input = vec![1, 2, 3, 4, 5, 6];
        let result = functional_pipeline(input);
        assert_eq!(result, vec![4, 16, 36]);  // squared evens
    }
    
    /// tests pattern matching exhaustiveness
    #[test]
    fn test_pattern_matching() {
        assert_eq!(pattern_match_example(Some(5)), 10);
        assert_eq!(pattern_match_example(Some(-5)), -5);
        assert_eq!(pattern_match_example(None), 0);
    }
}
```

## Cargo.toml Best Practices

```toml
[package]
name = "my-rust-project"
version = "0.1.0"
edition = "2021"  # or latest
rust-version = "1.75"  # require recent Rust
authors = ["LukeFrankio"]

[dependencies]
# MINIMAL DEPENDENCIES ONLY!
# seriously, use std wherever possible

# OS-specific (only if absolutely needed)
[target.'cfg(windows)'.dependencies]
windows = { version = "0.52", features = ["Win32_Foundation"], optional = true }

[target.'cfg(unix)'.dependencies]
libc = { version = "0.2", optional = true }

# UI (only if building GUI)
egui = { version = "0.28", optional = true }
eframe = { version = "0.28", optional = true }

[features]
default = []
gui = ["egui", "eframe"]  # enable with --features gui
windows-specific = ["windows"]
unix-specific = ["libc"]

[profile.release]
opt-level = 3  # maximum optimization
lto = true     # link-time optimization (slower builds, faster runtime)
codegen-units = 1  # better optimization, slower builds
strip = true   # strip symbols (smaller binary)

[profile.dev]
opt-level = 0  # fast compilation for development
```

## The Verdict on Rust

### What Rust Got Right:
- ✅ functional programming patterns (iterators, pattern matching)
- ✅ Result type for error handling (no exceptions!)
- ✅ exhaustive pattern matching (actually prevents bugs)
- ✅ const fn (compile-time evaluation like C++ constexpr)
- ✅ trait system (better than inheritance)
- ✅ cargo (integrated build system, less magic than CMake)
- ✅ documentation system (rust doc is actually good)

### What Rust Got Wrong:
- ❌ borrow checker (spending hours fighting compiler)
- ❌ lifetime annotations everywhere (verbose boilerplate)
- ❌ compile times (waiting forever for the checker)
- ❌ crate ecosystem (dependency hell, supply chain risk)
- ❌ async/await complexity (just use threads!)
- ❌ community (holier-than-thou attitude about memory safety)
- ❌ the name "Rust" (oxide is cope, steel is cope, just use C++)

## Quality Checklist

- [ ] **latest Rust** (stable or nightly)
- [ ] **MINIMAL dependencies** (std first, crates last)
- [ ] **only use**: windows/libc (OS), egui/eframe (UI)
- [ ] **functional style** (iterators, pattern matching)
- [ ] **excessive comments** (explain why Rust forced this approach)
- [ ] **const fn** where possible (compile-time evaluation)
- [ ] **exhaustive patterns** (let compiler check)
- [ ] **Result types** for errors (no panic! in libraries)
- [ ] **tests** for all public functions
- [ ] **documentation** (rust doc comments ///)

**remember**: Rust is memory safety cope. C++ with proper coding practices
achieves the same safety without the borrow checker violence. but if you're
forced to use Rust, at least do it functionally and minimize the crate bloat.

the borrow checker is not your friend, it's a cop that thinks you're guilty
until proven innocent uwu 💜

(still prefer C++ tho)