---
description: 'Python coding guidelines (forcing it to be functional despite Guido´s wishes uwu)'
applyTo: '**.py'
---

# Python Programming Instructions (The "Good Enough" Dynamic Language)

> "Python: where lambda calculus meets runtime polymorphism, duck typing, and the
> desperate hope that your type hints are actually correct"

uwu look, Python isn't C++. Python isn't Haskell. Python is the language you
use when you need something working by Tuesday and the team refuses to learn
a real type system. BUT — with enough type hints, enough immutability, enough
functional patterns, and enough stubborn refusal to write classes, we can
make Python... tolerable. maybe even pleasant. ✨

## Core Philosophy (Non-Negotiable Axioms)

- **functional > imperative** (even in a language that punishes you for it!)
- **type hints MANDATORY** (we're not JavaScript developers)
- **immutability preferred** (use `dataclasses` with `frozen=True`, always)
- **pure functions MAXIMISED** (mark purity status explicitly)
- **OOP is BANNED** (no inheritance hierarchies, no `self` soup, no "design patterns")
- **classes are namespaces** (static methods and `@staticmethod` only, if you must)
- **dataclasses are structs** (frozen, immutable, value-semantics)
- **match statements MANDATORY** (for all branching on data shape)
- **f-strings and t-strings only** (`%` and `.format()` are ancient history)
- **comment excessively** using Google-style docstrings
- **Python 3.15+ recommended** (lazy imports, comprehension unpacking, JIT improvements)
- **Python 3.14 minimum** (deferred annotations, t-strings, multiple interpreters)
- **no Django** (it's Spring Boot for Python — global mutable state with decorators)
- **no Flask** (it's the gateway drug to Django)
- **uv for everything** (pip is slow, poetry is bloated, uv goes brrr)

## Why Python is Cope (And How We Survive)

### What Python Got Wrong:
- ❌ dynamic typing by default (types are suggestions not requirements)
- ❌ GIL (the Global Interpreter Lock held Python hostage for 30 years)
- ❌ everything is an object (even `int` has methods, that's 28 bytes for the number 5)
- ❌ mutable by default (lists, dicts, sets — all mutable, all dangerous)
- ❌ OOP culture (Django, Flask, SQLAlchemy — class hierarchies everywhere)
- ❌ no tail call optimisation (recursion limited to 1000 frames by default)
- ❌ whitespace-sensitive syntax (tabs vs spaces wars, the Great Indentation Debate)
- ❌ `None` instead of `Optional` (Tony Hoare's billion dollar mistake, Python edition)
- ❌ `import this` (the Zen of Python says "explicit is better than implicit" then gives you implicit type coercion)
- ❌ slow (interpreter overhead makes C++ developers weep)
- ❌ the `class` keyword (99% of Python classes should be functions + dataclasses)

### What Python Got Right (Finally, After 35 Years):
- ✅ deferred annotations (PEP 649/749 — no more `from __future__ import annotations` cope!)
- ✅ template strings (PEP 750 — t-strings for safe string processing!)
- ✅ lazy imports (PEP 810 — `lazy import json` in 3.15, startup goes brrr!)
- ✅ multiple interpreters (PEP 734 — real parallelism without multiprocessing!)
- ✅ match statements (PEP 634 — algebraic pattern matching, 50 years late)
- ✅ type hints (PEP 484+ — Python's best feature, invented by the community not Guido)
- ✅ dataclasses (PEP 557 — frozen=True makes immutable structs)
- ✅ `type` statement (PEP 695 — native generics without `TypeVar` ceremony)
- ✅ comprehension unpacking (PEP 798 — `[*L for L in lists]` in 3.15!)
- ✅ Protocol classes (PEP 544 — structural subtyping, the right kind of duck typing)
- ✅ free-threaded CPython (PEP 703 — the GIL is finally optional!)
- ✅ tail-call interpreter (3-5% faster, with Clang 19+)
- ✅ JIT compiler progress (4-8% speedup in 3.15, getting there!)
- ✅ Zstandard compression (built-in `compression.zstd` module)
- ✅ `sys.remote_exec()` (PEP 768 — zero-overhead debugging, attach to live processes!)
- ✅ sampling profiler (Tachyon — up to 1,000,000 Hz in `profiling.sampling`)

## Python Version Requirements (BLEEDING EDGE ONLY)

```python
#!/usr/bin/env python3.15

# Python 3.15+ RECOMMENDED (latest alpha/beta, no cowardice!)
# Python 3.14  MINIMUM (stable release, October 2025)
# Python 3.13  TOLERATED (if 3.14 is genuinely unavailable)
# Python 3.12  BANNED (that's ancient history)
# Python 3.11  WAR CRIME
# Python 2.x   DOESN'T EXIST

# NOTABLE PYTHON 3.14 FEATURES WE EXPLOIT:
# • PEP 649/749 — deferred evaluation of annotations (no more string hacks!)
# • PEP 750 — template string literals (t-strings for safe processing!)
# • PEP 734 — multiple interpreters (concurrent.interpreters module!)
# • PEP 768 — zero-overhead debugging (sys.remote_exec()!)
# • PEP 703 — free-threaded CPython improvements (~5-10% penalty now)
# • Tail-call interpreter (3-5% faster with Clang 19+)
# • compression.zstd (Zstandard built into stdlib!)
# • Syntax highlighting in REPL (finally!)

# NOTABLE PYTHON 3.15 FEATURES WE EXPLOIT:
# • PEP 810 — lazy imports (lazy import json, startup goes brrr!)
# • PEP 798 — unpacking in comprehensions ([*L for L in lists])
# • PEP 799 — profiling module reorganisation (profiling.sampling!)
# • PEP 791 — imath module (integer math functions!)
# • JIT compiler improvements (4-8% speedup!)
# • Better machine code generation (LLVM 21)
# • Tachyon sampling profiler (1,000,000 Hz!)
```

### pyproject.toml Version Configuration:

```toml
[project]
requires-python = ">=3.14"

# or for bleeding edge:
requires-python = ">=3.15"
```

### Runtime Version Check:

```python
import sys

if sys.version_info < (3, 14):
    raise SystemExit(
        f"Python 3.14+ required (you're running {sys.version}). "
        f"upgrade immediately, cowardice is not tolerated uwu"
    )
```

## Naming Conventions

```python
# modules: lowercase_with_underscores (PEP 8, the one thing PEP 8 got right)
# file: vector_ops.py

# "classes" (used as NAMESPACES ONLY): snake_case module with static functions
# these are NOT objects, they are collections of pure functions
# if you MUST use a class: PascalCase (but you shouldn't need to)

# dataclasses (immutable structs): PascalCase
@dataclass(frozen=True)
class Vector2D: ...

# functions: snake_case (all pure, all typed)
def add_vectors(a: Vector2D, b: Vector2D) -> Vector2D: ...

# constants: SCREAMING_SNAKE_CASE
PI: float = 3.14159265358979323846
MAX_ITERATIONS: int = 1000

# type variables (3.12+ syntax): PascalCase
type Number = int | float
type Vector = tuple[float, float]

# private functions: _leading_underscore (convention only, not enforced)
def _internal_helper() -> None: ...

# BANNED naming patterns:
# ❌ camelCase functions (this isn't JavaScript, bestie)
# ❌ Hungarian notation (strName, iCount — this isn't 1995)
# ❌ single letter variables outside comprehensions (except T, U, V for generics)
# ❌ __dunder__ methods on your own classes (that's Python magic method OOP cope)
# ❌ cls/self parameters (you shouldn't have classes with instance methods!)
# ❌ AbstractBaseVectorFactoryMixin (enterprise Java energy in Python, VIOLENCE)
```

## The Type System (Python's Best Feature, Used Correctly)

### Python 3.12+ Native Generics (PEP 695 — No More `TypeVar` Ceremony!):

```python
"""
Type definitions using modern Python 3.12+ syntax (type safety uwu).

The old way (Python 3.8-3.11):
    T = TypeVar('T')
    U = TypeVar('U')
    def map_list(func: Callable[[T], U], items: list[T]) -> list[U]: ...

The new way (Python 3.12+):
    def map_list[T, U](func: Callable[[T], U], items: list[T]) -> list[U]: ...

The type statement (Python 3.12+):
    type Number = int | float      # type alias
    type Vector = tuple[float, ...]  # generic alias

We use the NEW syntax exclusively. The old TypeVar ceremony is BANNED.
If you're writing TypeVar('T'), you're writing Python 3.8 code in 2026. uwu
"""

from collections.abc import Callable, Sequence, Iterator
from dataclasses import dataclass

# ✅ GOOD: type statement (PEP 695, Python 3.12+)
type Number = int | float
type Vector = tuple[float, float]
type Matrix = tuple[tuple[float, ...], ...]
type Predicate[T] = Callable[[T], bool]
type Transformer[T, U] = Callable[[T], U]
type Result[T, E] = Ok[T] | Err[E]

# ❌ BANNED: old TypeVar ceremony
# from typing import TypeVar, Optional, Union
# T = TypeVar('T')
# Optional[int]  # use int | None instead
# Union[int, str]  # use int | str instead
```

### Deferred Annotations (PEP 649/749 — Python 3.14+):

```python
"""
Deferred evaluation of annotations (Python 3.14+).

In Python 3.14, annotations are NO LONGER eagerly evaluated.
They're stored in special annotate functions and evaluated only when needed.
This means forward references JUST WORK without string quotes!

The old way (Python 3.8-3.13):
    from __future__ import annotations  # string annotations hack
    
    class Node:
        next: 'Node'  # string because Node isn't defined yet

The new way (Python 3.14+):
    class Node:
        next: Node  # JUST WORKS! annotations are deferred!

No more __future__ import. No more string quotes around forward refs.
The type system finally behaves like it should have from day one. uwu ✨
"""

from annotationlib import get_annotations, Format

# forward references just work now (no string quotes!)
@dataclass(frozen=True)
class TreeNode[T]:
    """
    Immutable binary tree node with forward references (deferred annotations!).
    
    ✨ PURE DATA ✨ (frozen dataclass, immutable)
    
    In Python 3.13 and earlier, 'left' and 'right' would need to be
    'TreeNode[T]' as strings. In 3.14+, forward references just work
    because annotations are evaluated lazily. uwu
    """
    value: T
    left: TreeNode[T] | None = None
    right: TreeNode[T] | None = None

# inspecting annotations with the new annotationlib:
# get_annotations(TreeNode, format=Format.VALUE)     -> evaluates to runtime types
# get_annotations(TreeNode, format=Format.FORWARDREF) -> replaces unknowns with ForwardRef
# get_annotations(TreeNode, format=Format.STRING)     -> returns as strings
```

### Protocols (Structural Subtyping — The Right Kind of Duck Typing):

```python
from collections.abc import Callable

class Numeric[T](Protocol):
    """
    Protocol for numeric types (structural subtyping!).
    
    This is how you do duck typing with type safety. Protocols enable
    mypy/pyright to check structural compatibility without inheritance.
    If it quacks like a Numeric, it IS a Numeric. uwu
    
    Note:
        Protocols are structural, not nominal — no inheritance required!
        This is the Haskell type class pattern but in Python.
    """
    
    def __add__(self, other: T) -> T: ...
    def __mul__(self, other: T) -> T: ...
    def __neg__(self) -> T: ...


class Comparable(Protocol):
    """
    Protocol for comparable types (total ordering).
    
    Any type that implements __lt__ and __eq__ satisfies this protocol.
    No inheritance needed. Structural subtyping is based. uwu ✨
    """
    
    def __lt__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
```

## Immutable Data (Frozen Dataclasses Are Structs)

### Value Records (frozen=True Is Non-Negotiable):

```python
from dataclasses import dataclass, replace, field

@dataclass(frozen=True, slots=True)
class Vector2D:
    """
    Represents a 2D vector as an immutable dataclass (struct vibes uwu).
    
    ✨ IMMUTABLE VALUE TYPE ✨
    
    Using frozen=True makes this immutable — no mutation allowed.
    Using slots=True eliminates __dict__ overhead (like a C struct!).
    All operations return NEW instances instead of modifying existing ones.
    
    In Haskell this would be:
        data Vec2 = Vec2 { vecX :: !Double, vecY :: !Double }
    
    In C++ this would be:
        struct Vector2D { double x, y; };
    
    But Python needed decorators and 35 years to get here. uwu
    
    Attributes:
        x: horizontal coordinate (immutable after construction)
        y: vertical coordinate (immutable after construction)
    
    Examples:
        >>> v = Vector2D(3.0, 4.0)
        >>> v.x = 5.0  # FrozenInstanceError! (immutability enforced!)
        >>> v2 = replace(v, x=5.0)  # create new instead
    """
    x: float
    y: float

    # constants defined as class variables
    ZERO: 'Vector2D' = field(default=None, init=False, repr=False)  # type: ignore[assignment]
    UNIT_X: 'Vector2D' = field(default=None, init=False, repr=False)  # type: ignore[assignment]

# module-level constants (preferred over class variables for frozen dataclasses)
ZERO = Vector2D(0.0, 0.0)
UNIT_X = Vector2D(1.0, 0.0)
UNIT_Y = Vector2D(0.0, 1.0)


@dataclass(frozen=True, slots=True)
class Color:
    """
    Immutable RGBA color (functional data uwu).
    
    ✨ IMMUTABLE VALUE TYPE ✨
    
    Attributes:
        r: red channel [0.0, 1.0]
        g: green channel [0.0, 1.0]
        b: blue channel [0.0, 1.0]
        a: alpha channel [0.0, 1.0]
    """
    r: float
    g: float
    b: float
    a: float = 1.0

BLACK = Color(0.0, 0.0, 0.0)
WHITE = Color(1.0, 1.0, 1.0)


@dataclass(frozen=True, slots=True)
class GameState:
    """
    Immutable game state (functional game programming!).
    
    ✨ IMMUTABLE VALUE TYPE ✨
    
    All state modifications return new GameState instances instead of
    mutating. This enables time-travel debugging, easy undo/redo, and
    fearless concurrency uwu
    
    Examples:
        >>> state = GameState(score=100, level=1, lives=3)
        >>> new_state = add_score(state, 50)
        >>> new_state.score
        150
        >>> state.score  # original unchanged (immutability!)
        100
    """
    score: int
    level: int
    lives: int


# pure functions operating on immutable data (NOT methods!)
def add_score(state: GameState, points: int) -> GameState:
    """
    Returns new state with added score.
    
    ✨ PURE FUNCTION ✨
    
    Args:
        state: current game state (not modified)
        points: points to add
    
    Returns:
        New GameState with updated score
    """
    return replace(state, score=state.score + points)

def next_level(state: GameState) -> GameState:
    """Returns new state at next level. ✨ PURE ✨"""
    return replace(state, level=state.level + 1)

def lose_life(state: GameState) -> GameState:
    """Returns new state with one less life. ✨ PURE ✨"""
    return replace(state, lives=state.lives - 1)
```

### What's BANNED (OOP Violence):

```python
# ❌ BANNED: mutable classes with state (OOP cringe)
class MutableVector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x  # MUTABLE STATE (violence)
        self.y = y

    def set_x(self, x: float) -> None:
        self.x = x  # SETTER (mutation violence)

    def get_x(self) -> float:
        return self.x  # GETTER (Java energy in Python, WHY)

# ❌ BANNED: inheritance hierarchies (OOP brain rot)
class AbstractShape:
    """abstract base classes are fake architecture"""
    pass

class Circle(AbstractShape):
    """congratulations, you've coupled your code to a hierarchy"""
    pass

# ❌ BANNED: Django models (global mutable state with ORM magic)
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     # this is mutable global state connected to a database
#     # with implicit queries and magical lazy loading
#     # it's Spring Boot for Python. VIOLENCE. uwu

# ✅ ALLOWED: frozen dataclasses (immutable data)
@dataclass(frozen=True, slots=True)
class Circle:
    radius: float

@dataclass(frozen=True, slots=True)
class Rectangle:
    width: float
    height: float

# ✅ ALLOWED: algebraic data types via union types
type Shape = Circle | Rectangle

# ✅ ALLOWED: pure functions that operate on data
def area(shape: Shape) -> float:
    """
    Compute area using pattern matching (algebraic data types uwu!).
    
    ✨ PURE FUNCTION ✨
    """
    match shape:
        case Circle(radius=r):
            return 3.14159265358979 * r * r
        case Rectangle(width=w, height=h):
            return w * h
```

## Functional Programming (THE WAY)

### Pure Functions (Maximise These):

```python
"""
Pure functional operations on 2D vectors.

This module is a NAMESPACE for pure functions. NOT a class.
No self parameters. No instance state. Just pure mathematical
transformations on immutable data. uwu

Enterprise developers: this is what your 12-class hierarchy
should have been. Pure functions on frozen dataclasses. Done.
"""

from dataclasses import dataclass, replace
from math import sqrt
from collections.abc import Callable, Sequence
from functools import reduce


def add(a: Vector2D, b: Vector2D) -> Vector2D:
    """
    Adds two vectors component-wise (pure function uwu).
    
    ✨ PURE FUNCTION ✨
    
    This function is pure because:
    - Same inputs always produce same outputs (referential transparency)
    - No side effects (doesn't modify arguments or global state)
    - No I/O operations
    - No exceptions thrown
    - Frozen dataclasses are immutable (can't accidentally mutate inputs)
    
    In Haskell this would be:
        add :: Vec2 -> Vec2 -> Vec2
        add (Vec2 x1 y1) (Vec2 x2 y2) = Vec2 (x1 + x2) (y1 + y2)
    
    In C++ this would be:
        constexpr auto add(Vec2 a, Vec2 b) noexcept -> Vec2 {
            return {a.x + b.x, a.y + b.y};
        }
    
    But Python needs type hints and a frozen dataclass because the
    language doesn't enforce anything. We enforce it ourselves. uwu
    
    Args:
        a: first vector (not modified — frozen dataclass)
        b: second vector (not modified — frozen dataclass)
    
    Returns:
        New vector containing component-wise sum (a + b)
    
    Examples:
        >>> v1 = Vector2D(3.0, 4.0)
        >>> v2 = Vector2D(1.0, 2.0)
        >>> add(v1, v2)
        Vector2D(x=4.0, y=6.0)
    
    Note:
        Commutative: add(a, b) == add(b, a)
        Associative: add(add(a, b), c) == add(a, add(b, c))
    """
    return Vector2D(a.x + b.x, a.y + b.y)


def scale(v: Vector2D, factor: float) -> Vector2D:
    """
    Scales vector by scalar factor.
    
    ✨ PURE FUNCTION ✨
    
    Args:
        v: vector to scale (immutable)
        factor: scaling factor
    
    Returns:
        New scaled vector
    
    Examples:
        >>> scale(Vector2D(3.0, 4.0), 2.0)
        Vector2D(x=6.0, y=8.0)
    """
    return Vector2D(v.x * factor, v.y * factor)


def dot(a: Vector2D, b: Vector2D) -> float:
    """
    Computes dot product (pure bilinear form!).
    
    ✨ PURE FUNCTION ✨
    
    Args:
        a: first vector
        b: second vector
    
    Returns:
        Dot product (scalar)
    
    Examples:
        >>> dot(Vector2D(1.0, 2.0), Vector2D(3.0, 4.0))
        11.0
    """
    return a.x * b.x + a.y * b.y


def magnitude(v: Vector2D) -> float:
    """
    Computes Euclidean magnitude (L2 norm).
    
    ✨ PURE FUNCTION ✨
    
    Args:
        v: vector to measure
    
    Returns:
        Magnitude (always non-negative)
    
    Examples:
        >>> magnitude(Vector2D(3.0, 4.0))
        5.0
    """
    return sqrt(dot(v, v))


def normalise(v: Vector2D) -> Vector2D | None:
    """
    Normalise to unit length. Returns None for zero vector.
    
    ✨ PURE FUNCTION ✨ ✨ TOTAL ✨
    
    Unlike a version that raises ValueError, this returns None
    for the zero vector. Errors are values, not exceptions. uwu
    
    Args:
        v: vector to normalise
    
    Returns:
        Unit vector or None if input is zero vector
    
    Examples:
        >>> normalise(Vector2D(3.0, 4.0))
        Vector2D(x=0.6, y=0.8)
        >>> normalise(Vector2D(0.0, 0.0)) is None
        True
    """
    mag = magnitude(v)
    if mag < 1e-10:
        return None
    return scale(v, 1.0 / mag)
```

### Higher-Order Functions (No Loops, Ever):

```python
"""
Functional collection operations (no imperative loops!).

If you write a for-loop that mutates an accumulator variable in this codebase,
you owe everyone a formal apology and 5 minutes of lambda calculus study uwu
"""

from collections.abc import Callable, Iterable
from functools import reduce


def map_list[T, U](func: Callable[[T], U], items: Iterable[T]) -> list[U]:
    """
    Maps function over iterable (functional map!).
    
    ✨ PURE FUNCTION ✨
    
    Args:
        func: transformation function to apply
        items: input iterable (not modified)
    
    Returns:
        New list with transformed elements
    
    Examples:
        >>> map_list(lambda x: x * x, [1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
    
    Note:
        Prefer this or list comprehensions over mutable accumulation.
    """
    return [func(item) for item in items]


def filter_list[T](pred: Callable[[T], bool], items: Iterable[T]) -> list[T]:
    """
    Filters iterable based on predicate (functional filter!).
    
    ✨ PURE FUNCTION ✨
    
    Args:
        pred: predicate function (returns True to keep element)
        items: input iterable (not modified)
    
    Returns:
        New list containing only elements satisfying predicate
    
    Examples:
        >>> filter_list(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    return [item for item in items if pred(item)]


def fold_left[T, U](func: Callable[[U, T], U], items: Iterable[T], initial: U) -> U:
    """
    Left fold / reduce (functional accumulation!).
    
    ✨ PURE FUNCTION ✨
    
    Implements left fold: result = func(func(func(initial, items[0]), items[1]), items[2])
    
    Args:
        func: binary reduction function (accumulator, element) -> new accumulator
        items: input iterable to reduce
        initial: initial accumulator value
    
    Returns:
        Final accumulated value
    
    Examples:
        >>> fold_left(lambda acc, x: acc + x, [1, 2, 3, 4, 5], 0)
        15
        >>> fold_left(lambda acc, x: acc * x, [1, 2, 3, 4, 5], 1)
        120
    """
    return reduce(func, items, initial)


def compose[T, U, V](f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:
    """
    Composes two functions (f ∘ g).
    
    ✨ PURE FUNCTION ✨
    
    Creates new function h where h(x) = f(g(x)). Function composition
    from lambda calculus — the foundation of all computation uwu
    
    Args:
        f: outer function (applied second)
        g: inner function (applied first)
    
    Returns:
        Composed function that applies g then f
    
    Examples:
        >>> add_one = lambda x: x + 1
        >>> times_two = lambda x: x * 2
        >>> add_then_double = compose(times_two, add_one)
        >>> add_then_double(5)
        12
    """
    def composed(x: T) -> V:
        return f(g(x))
    return composed


def pipe[T](*funcs: Callable[[T], T]) -> Callable[[T], T]:
    """
    Creates function pipeline (left-to-right composition).
    
    ✨ PURE FUNCTION ✨
    
    pipe(f, g, h)(x) = h(g(f(x)))
    
    Args:
        *funcs: functions to compose (applied left to right)
    
    Returns:
        Composed pipeline function
    
    Examples:
        >>> pipeline = pipe(lambda x: x + 1, lambda x: x * 2, lambda x: x - 3)
        >>> pipeline(5)
        9
    """
    def piped(x: T) -> T:
        result = x
        for func in funcs:
            result = func(result)
        return result
    return piped
```

### Comprehension Unpacking (PEP 798 — Python 3.15+):

```python
"""
Comprehension unpacking (Python 3.15+ — PEP 798).

This extends PEP 448 unpacking syntax to comprehensions.
It's a direct alternative to nested comprehensions and
itertools.chain(). Cleaner, more readable, more functional. uwu ✨
"""

# ✅ NEW: unpacking in list comprehensions (3.15+)
lists: list[list[int]] = [[1, 2], [3, 4], [5]]
flat: list[int] = [*L for L in lists]  # [1, 2, 3, 4, 5]

# equivalent to the old way:
# flat = [x for L in lists for x in L]

# ✅ NEW: unpacking in set comprehensions
sets: list[set[int]] = [{1, 2}, {2, 3}, {3, 4}]
merged: set[int] = {*s for s in sets}  # {1, 2, 3, 4}

# ✅ NEW: unpacking in dict comprehensions
dicts: list[dict[str, int]] = [{'a': 1}, {'b': 2}, {'a': 3}]
merged_dict: dict[str, int] = {**d for d in dicts}  # {'a': 3, 'b': 2}

# ✅ NEW: unpacking in generator expressions
gen = (*L for L in lists)  # lazy generator, no memory overhead
flat_lazy: list[int] = list(gen)  # [1, 2, 3, 4, 5]

# this is SO much cleaner than itertools.chain.from_iterable()
# functional programming in Python is getting less painful uwu ✨
```

## Template Strings (PEP 750 — Python 3.14+)

```python
"""
Template string literals (PEP 750 — Python 3.14+).

t-strings are like f-strings BUT instead of producing a plain string,
they produce a Template object. You can inspect the parts BEFORE
combining them. This enables:
- HTML sanitisation (escape user input automatically!)
- SQL parameterisation (prevent injection attacks!)
- Safe shell operations (no command injection!)
- Custom DSLs (logging, i18n, etc.)

f-strings: immediate evaluation → str
t-strings: deferred processing → Template

This is Python's answer to Rust's proc macros and JavaScript's
tagged template literals. Finally. uwu ✨
"""

from string.templatelib import Template, Interpolation


def html_safe(template: Template) -> str:
    """
    Processes a template string with HTML escaping for interpolated values.
    
    ✨ PURE FUNCTION ✨ (returns sanitised HTML)
    
    Static parts are trusted (developer-written). Interpolated parts are
    escaped (user-provided). This prevents XSS attacks by construction!
    
    Args:
        template: template string with potentially unsafe interpolations
    
    Returns:
        HTML-safe string with escaped user input
    
    Examples:
        >>> user_input = '<script>alert("xss")</script>'
        >>> html_safe(t'<p>{user_input}</p>')
        '<p>&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;</p>'
    """
    from html import escape
    parts: list[str] = []
    for part in template:
        match part:
            case str() as s:
                parts.append(s)  # static part, trusted
            case Interpolation(value, _, _, _):
                parts.append(escape(str(value)))  # interpolated, ESCAPE!
    return "".join(parts)


def sql_parameterised(template: Template) -> tuple[str, list[object]]:
    """
    Processes a template string into a parameterised SQL query.
    
    ✨ PURE FUNCTION ✨ (returns (query, params) tuple)
    
    Interpolated values become SQL parameters (?) instead of being
    string-concatenated. This prevents SQL injection by construction!
    
    Args:
        template: template string representing a SQL query
    
    Returns:
        Tuple of (parameterised query string, list of parameter values)
    
    Examples:
        >>> name = "Robert'; DROP TABLE students;--"
        >>> query, params = sql_parameterised(t"SELECT * FROM users WHERE name = {name}")
        >>> query
        'SELECT * FROM users WHERE name = ?'
        >>> params
        ["Robert'; DROP TABLE students;--"]
    """
    parts: list[str] = []
    params: list[object] = []
    for part in template:
        match part:
            case str() as s:
                parts.append(s)
            case Interpolation(value, _, _, _):
                parts.append("?")
                params.append(value)
    return "".join(parts), params


# Usage: t-strings in action!
variety: str = "Stilton"
template: Template = t"Try some {variety} cheese!"

# inspect the parts:
# list(template) → ['Try some ', Interpolation('Stilton', 'variety', None, ''), ' cheese!']

# use with processing functions:
user_input: str = '<script>alert("xss")</script>'
safe_html: str = html_safe(t"<p>Hello, {user_input}!</p>")
# safe_html → '<p>Hello, &lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;!</p>'
```

## Lazy Imports (PEP 810 — Python 3.15+)

```python
"""
Lazy imports (PEP 810 — Python 3.15+).

The lazy keyword defers module loading until first use. This is a
GAME CHANGER for startup performance. Import everything at the top
of the file like a civilised person, but only pay the cost when you
actually USE the module. uwu ✨

Restrictions:
- Only at module scope (not inside functions or classes)
- No star imports: lazy from module import * → SyntaxError
- No future imports: lazy from __future__ import ... → SyntaxError
"""

# ✅ lazy imports — module loaded only when first accessed
lazy import json
lazy import csv
lazy import xml.etree.ElementTree as ET
lazy from datetime import datetime, timedelta
lazy from pathlib import Path
lazy from collections import defaultdict

# these modules are NOT loaded at import time!
# they load transparently on first access:
print("Starting up...")  # json, csv, ET, etc. NOT loaded yet

data = json.loads('{"key": "value"}')  # json loads HERE
now = datetime()  # datetime loads HERE

# CLI flag: python -X lazy_imports=all    (make ALL imports lazy)
# CLI flag: python -X lazy_imports=none   (disable lazy, even explicit lazy keyword)
# CLI flag: python -X lazy_imports=normal (default: respect lazy keyword)
# Env var:  PYTHON_LAZY_IMPORTS=all|none|normal

# runtime control:
import sys
# sys.set_lazy_imports("all")   # make everything lazy
# sys.set_lazy_imports("none")  # make everything eager
# sys.get_lazy_imports()        # query current mode

# selective filter (e.g., only your app's modules are lazy):
def my_lazy_filter(
    importing: str | None,
    imported: str,
    fromlist: tuple[str, ...] | None,
) -> bool:
    """Returns True if this import should be lazy."""
    return imported.startswith("myapp.")

# sys.set_lazy_imports_filter(my_lazy_filter)
# sys.set_lazy_imports("all")

# detect lazy imports programmatically:
import types
# isinstance(some_module, types.LazyImportType) → True if lazy proxy
```

## Error Handling (No Exceptions In Pure Code — Result Type)

### Why Exceptions Are Violence:

Exceptions are **GOTO with extra steps**. They break referential transparency,
they make function signatures LIE about what they return, and they force every
caller into try-except ceremony. Python's `try`/`except` is especially heinous
because bare `except:` catches EVERYTHING including `KeyboardInterrupt`.

Use a `Result[T, E]` type in pure code. Errors are VALUES. Values can be
composed, transformed, pattern-matched. Exceptions can only be thrown and caught
like emotional outbursts in a codebase.

### Result Type (Functional Error Handling):

```python
"""
Functional result type for operations that can fail (no exceptions!).

Monadic error handling — errors are values that must be handled explicitly.
No invisible control flow, no catch blocks, no surprises.

Inspired by Rust's Result, Haskell's Either, and our C++ Result type.
Python exceptions WISH they were this clean uwu ✨
"""

from dataclasses import dataclass
from collections.abc import Callable


@dataclass(frozen=True, slots=True)
class Ok[T]:
    """Successful result containing a value."""
    value: T


@dataclass(frozen=True, slots=True)
class Err[E]:
    """Error result containing an error."""
    error: E


type Result[T, E] = Ok[T] | Err[E]


def map_result[T, U, E](result: Result[T, E], func: Callable[[T], U]) -> Result[U, E]:
    """
    Maps success value (functor map!).
    
    ✨ PURE FUNCTION ✨
    
    If Ok, applies function. If Err, propagates error unchanged.
    
    Args:
        result: result to transform
        func: transformation for success value
    
    Returns:
        Mapped result
    
    Examples:
        >>> map_result(Ok(5), lambda x: x * 2)
        Ok(value=10)
        >>> map_result(Err("oops"), lambda x: x * 2)
        Err(error='oops')
    """
    match result:
        case Ok(value):
            return Ok(func(value))
        case Err() as e:
            return e


def flat_map[T, U, E](
    result: Result[T, E],
    func: Callable[[T], Result[U, E]],
) -> Result[U, E]:
    """
    Chains fallible operations (monadic bind / flatMap!).
    
    ✨ PURE FUNCTION ✨
    
    This is >>= from Haskell (monadic bind uwu).
    If Ok, applies function that returns Result. If Err, propagates error.
    
    Args:
        result: result to chain from
        func: function that may fail (returns Result)
    
    Returns:
        Chained result
    
    Examples:
        >>> flat_map(Ok(10.0), lambda x: divide(x, 2.0))
        Ok(value=5.0)
        >>> flat_map(Ok(10.0), lambda x: divide(x, 0.0))
        Err(error='division by zero (mathematics says no)')
    """
    match result:
        case Ok(value):
            return func(value)
        case Err() as e:
            return e


def or_else[T, E](result: Result[T, E], default: T) -> T:
    """
    Gets value or returns default.
    
    ✨ PURE FUNCTION ✨
    
    Args:
        result: result to unwrap
        default: value to return if Err
    
    Returns:
        Success value or default
    """
    match result:
        case Ok(value):
            return value
        case Err():
            return default


# example: safe division
def divide(a: float, b: float) -> Result[float, str]:
    """
    Safe division with error handling (no exceptions!).
    
    ✨ PURE FUNCTION ✨
    
    Args:
        a: numerator
        b: denominator
    
    Returns:
        Ok(quotient) if successful, Err(message) if division by zero
    
    Examples:
        >>> divide(10.0, 2.0)
        Ok(value=5.0)
        >>> divide(10.0, 0.0)
        Err(error='division by zero (mathematics says no)')
    """
    if b == 0.0:
        return Err("division by zero (mathematics says no)")
    return Ok(a / b)


# monadic composition example:
result = flat_map(
    flat_map(
        divide(100.0, 2.0),        # Ok(50.0)
        lambda x: divide(x, 2.0),  # Ok(25.0)
    ),
    lambda x: divide(x, 0.0),      # Err("division by zero")
)

message = match result:  # type: ignore[syntax]
    case Ok(value):
        f"Success: {value}"
    case Err(error):
        f"Error: {error}"
# note: match as expression isn't valid Python syntax (yet), use:
match result:
    case Ok(value):
        message = f"Success: {value}"
    case Err(error):
        message = f"Error: {error}"
```

## Concurrency (Multiple Interpreters + Free Threading + asyncio)

### Multiple Interpreters (PEP 734 — Python 3.14+):

```python
"""
Multiple interpreters (PEP 734 — Python 3.14+).

Python now has REAL parallelism without multiprocessing overhead!
Each interpreter is an isolated Python runtime — no shared GIL,
no shared state, just message passing. CSP/actor model concurrency
like Erlang, Haskell, and Go. uwu ✨

Think of multiple interpreters as:
- threads (lightweight, same process)
- but with isolation (no shared mutable state!)
- and real parallelism (each has its own GIL!)

This is what Python concurrency should have been from the start.
Instead we got the GIL for 30 years. uwu
"""

import concurrent.interpreters
import concurrent.futures


def interpreter_example() -> None:
    """
    Demonstrates multiple interpreters for CPU-bound parallelism.
    
    ⚠️ IMPURE FUNCTION (spawns interpreters, performs I/O)
    
    Each interpreter runs in its own isolated environment.
    Communication happens via message passing (no shared state!).
    """
    # create a new interpreter
    interp = concurrent.interpreters.create()
    
    # run code in the interpreter (isolated!)
    interp.exec("result = sum(range(1_000_000))")
    
    # the InterpreterPoolExecutor is the high-level API
    # (like ProcessPoolExecutor but lighter weight!)
    with concurrent.futures.InterpreterPoolExecutor(max_workers=4) as pool:
        # submit CPU-bound tasks (real parallelism!)
        futures = [
            pool.submit(compute_heavy_task, i)
            for i in range(8)
        ]
        results = [f.result() for f in futures]
    # pool cleaned up here — all interpreters destroyed


def compute_heavy_task(n: int) -> int:
    """Example CPU-bound task that runs in its own interpreter."""
    return sum(i * i for i in range(n * 100_000))
```

### Free-Threaded CPython (PEP 703 — Experimental):

```python
"""
Free-threaded CPython (PEP 703 — experimental in 3.14+).

The GIL is finally OPTIONAL. Free-threaded builds of CPython can run
threads truly in parallel on multiple cores. The performance penalty on
single-threaded code is now roughly 5-10% (down from much worse in 3.13).

This isn't the default yet, but it's getting there.
Build with: ./configure --disable-gil
Or use: python3.14t (the free-threaded variant)

The specialising adaptive interpreter (PEP 659) is now enabled in
free-threaded mode, which greatly improves performance. uwu ✨
"""

# check if running free-threaded:
import sys

# sys.flags.nogil → True if GIL is disabled
# sysconfig.get_config_var("Py_GIL_DISABLED") → compile-time setting

# the -X context_aware_warnings flag controls concurrent-safe
# warnings (defaults to True in free-threaded builds)
```

### asyncio (For I/O-Bound Concurrency):

```python
"""
asyncio for I/O-bound concurrency (not CPU-bound!).

Use asyncio when you're waiting on network, disk, or other I/O.
Use multiple interpreters or free-threading for CPU-bound work.

Python 3.14 added significant asyncio introspection improvements.
"""

import asyncio


async def fetch_both(url1: str, url2: str) -> tuple[str, str]:
    """
    Fetches two URLs concurrently (structured concurrency!).
    
    ⚠️ IMPURE FUNCTION (performs network I/O)
    
    Args:
        url1: first URL to fetch
        url2: second URL to fetch
    
    Returns:
        Tuple of both response bodies
    """
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_url(url1))
        task2 = tg.create_task(fetch_url(url2))
    # both tasks complete here (structured concurrency!)
    # if either fails, the other is cancelled automatically
    return task1.result(), task2.result()


async def fetch_url(url: str) -> str:
    """Fetches a single URL (simplified example)."""
    # in real code, use aiohttp or httpx
    await asyncio.sleep(0.1)  # simulating network delay
    return f"response from {url}"
```

## Testing with pytest (Exhaustive Testing Is Praxis)

```python
"""
Tests for vector operations (testing is praxis!).

Using pytest because it's the most based testing framework for Python.
No mocking libraries — if you need mocks, your architecture is wrong.
Pure functions don't need mocking. That's the whole point. uwu ✨

Run with: uv run pytest
Or: python -m pytest -v --tb=short
"""

import pytest
from vector_ops import Vector2D, add, scale, dot, magnitude, normalise, ZERO
from math import isclose


# ========================================================================
# Addition Tests (mathematical properties verified exhaustively!)
# ========================================================================

class TestAddition:
    """Tests for vector addition (pure function, commutative, associative)."""

    def test_addition_is_commutative(self) -> None:
        """Addition is commutative: a + b == b + a."""
        v1 = Vector2D(3.0, 4.0)
        v2 = Vector2D(1.0, 2.0)
        assert add(v1, v2) == add(v2, v1)

    def test_addition_is_associative(self) -> None:
        """Addition is associative: (a + b) + c == a + (b + c)."""
        v1 = Vector2D(1.0, 2.0)
        v2 = Vector2D(3.0, 4.0)
        v3 = Vector2D(5.0, 6.0)
        left = add(add(v1, v2), v3)
        right = add(v1, add(v2, v3))
        assert isclose(left.x, right.x, abs_tol=1e-10)
        assert isclose(left.y, right.y, abs_tol=1e-10)

    def test_zero_is_additive_identity(self) -> None:
        """Zero is additive identity: v + 0 == v."""
        v = Vector2D(3.0, 4.0)
        assert add(v, ZERO) == v
        assert add(ZERO, v) == v

    def test_additive_inverse(self) -> None:
        """Additive inverse: v + (-v) == 0."""
        v = Vector2D(3.0, 4.0)
        neg_v = Vector2D(-3.0, -4.0)
        result = add(v, neg_v)
        assert isclose(result.x, 0.0, abs_tol=1e-10)
        assert isclose(result.y, 0.0, abs_tol=1e-10)

    @pytest.mark.parametrize("x1,y1,x2,y2,ex,ey", [
        (0, 0, 0, 0, 0, 0),
        (1, 0, 0, 1, 1, 1),
        (3, 4, 1, 2, 4, 6),
        (-1, -1, 1, 1, 0, 0),
        (100, 200, -100, -200, 0, 0),
        (0.5, 0.5, 0.5, 0.5, 1.0, 1.0),
    ])
    def test_exhaustive_addition(
        self, x1: float, y1: float, x2: float, y2: float, ex: float, ey: float,
    ) -> None:
        """Exhaustive addition test cases."""
        result = add(Vector2D(x1, y1), Vector2D(x2, y2))
        assert isclose(result.x, ex, abs_tol=1e-10)
        assert isclose(result.y, ey, abs_tol=1e-10)


# ========================================================================
# Magnitude Tests (always non-negative, pure)
# ========================================================================

class TestMagnitude:
    """Tests for magnitude (always non-negative, pure function)."""

    @pytest.mark.parametrize("x,y,expected", [
        (0, 0, 0.0),
        (1, 0, 1.0),
        (0, 1, 1.0),
        (3, 4, 5.0),
        (5, 12, 13.0),
        (8, 15, 17.0),
        (-3, 4, 5.0),
        (-3, -4, 5.0),
    ])
    def test_known_magnitudes(self, x: float, y: float, expected: float) -> None:
        """Known Pythagorean triples and basic magnitudes."""
        assert isclose(magnitude(Vector2D(x, y)), expected, abs_tol=1e-10)

    def test_magnitude_always_non_negative(self) -> None:
        """Magnitude is always non-negative (mathematical property)."""
        vectors = [ZERO, Vector2D(1, 0), Vector2D(0, 1),
                   Vector2D(3, 4), Vector2D(-3, -4), Vector2D(5, 12)]
        for v in vectors:
            assert magnitude(v) >= 0.0

    def test_scaling_property(self) -> None:
        """Scaling law: |k * v| == |k| * |v|."""
        v = Vector2D(3.0, 4.0)
        for k in [0.0, 1.0, -1.0, 2.0, 0.5, -3.14, 100.0]:
            scaled_v = scale(v, k)
            assert isclose(
                magnitude(scaled_v),
                abs(k) * magnitude(v),
                abs_tol=1e-9,
            )


# ========================================================================
# Immutability Tests (CRITICAL for functional programming!)
# ========================================================================

class TestImmutability:
    """Tests for immutability (mutation is violence)."""

    def test_frozen_dataclass_is_immutable(self) -> None:
        """Frozen dataclasses reject mutation."""
        v = Vector2D(3.0, 4.0)
        with pytest.raises(AttributeError):
            v.x = 5.0  # type: ignore[misc]

    def test_operations_return_new_instances(self) -> None:
        """Operations return NEW instances, originals unchanged."""
        v = Vector2D(3.0, 4.0)
        result = add(v, Vector2D(1.0, 0.0))
        assert v.x == 3.0  # original unchanged!
        assert result.x == 4.0  # new vector

    def test_value_equality(self) -> None:
        """Frozen dataclasses compare by value, not reference."""
        v1 = Vector2D(3.0, 4.0)
        v2 = Vector2D(3.0, 4.0)
        assert v1 == v2
        assert hash(v1) == hash(v2)


# ========================================================================
# Result Type Tests (monadic error handling!)
# ========================================================================

class TestResult:
    """Tests for Result type (monadic error handling, no exceptions)."""

    def test_successful_division(self) -> None:
        """Successful division returns Ok."""
        result = divide(10.0, 2.0)
        match result:
            case Ok(value):
                assert isclose(value, 5.0)
            case Err(error):
                pytest.fail(f"should succeed: {error}")

    def test_division_by_zero_returns_err(self) -> None:
        """Division by zero returns Err (not an exception!)."""
        result = divide(10.0, 0.0)
        match result:
            case Ok(value):
                pytest.fail(f"should fail, got: {value}")
            case Err(error):
                assert "division by zero" in error

    def test_map_transforms_ok(self) -> None:
        """map transforms Ok values (functor law)."""
        result = map_result(divide(10.0, 2.0), lambda x: x * 2)
        assert result == Ok(10.0)

    def test_map_preserves_err(self) -> None:
        """map preserves Err values (functor law)."""
        result = map_result(divide(10.0, 0.0), lambda x: x * 2)
        assert isinstance(result, Err)

    def test_flat_map_chains(self) -> None:
        """flatMap chains operations (monad law)."""
        result = flat_map(
            divide(100.0, 2.0),
            lambda x: divide(x, 5.0),
        )
        match result:
            case Ok(value):
                assert isclose(value, 10.0)
            case Err(error):
                pytest.fail(f"should succeed: {error}")

    def test_flat_map_short_circuits(self) -> None:
        """flatMap short-circuits on Err (monad law)."""
        result = flat_map(
            divide(100.0, 0.0),
            lambda x: divide(x, 5.0),
        )
        assert isinstance(result, Err)
```

### Property-Based Testing (Hypothesis — Python's QuickCheck):

```python
"""
Property-based testing with Hypothesis (Python's QuickCheck uwu).

Instead of writing specific examples, you write UNIVERSAL PROPERTIES
that must hold for ALL inputs. Hypothesis generates hundreds of random
inputs and checks them. It even SHRINKS counterexamples!

Install: uv add --dev hypothesis
"""

from hypothesis import given, strategies as st

@given(
    x1=st.floats(min_value=-1000, max_value=1000, allow_nan=False),
    y1=st.floats(min_value=-1000, max_value=1000, allow_nan=False),
    x2=st.floats(min_value=-1000, max_value=1000, allow_nan=False),
    y2=st.floats(min_value=-1000, max_value=1000, allow_nan=False),
)
def test_addition_commutativity(
    x1: float, y1: float, x2: float, y2: float,
) -> None:
    """∀ a b. add(a, b) == add(b, a) (QuickCheck style!)."""
    a = Vector2D(x1, y1)
    b = Vector2D(x2, y2)
    assert add(a, b) == add(b, a)


@given(
    x=st.floats(min_value=-1000, max_value=1000, allow_nan=False),
    y=st.floats(min_value=-1000, max_value=1000, allow_nan=False),
)
def test_magnitude_non_negative(x: float, y: float) -> None:
    """∀ v. magnitude(v) >= 0 (property that must always hold)."""
    assert magnitude(Vector2D(x, y)) >= 0.0
```

## Build System (pyproject.toml — The Only Acceptable Config)

```toml
# pyproject.toml
# The ONE configuration file for Python projects.
# setup.py is DEAD. setup.cfg is DEAD. requirements.txt is COPE.
# pyproject.toml is the standard (PEP 517/518/621). uwu ✨

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "functional-python-project"
version = "0.1.0"
description = "Functional Python that makes OOP developers weep uwu"
readme = "README.md"
license = "MIT"
requires-python = ">=3.14"
authors = [
    { name = "LukeFrankio" },
]
keywords = ["functional", "immutable", "pure"]
classifiers = [
    "Programming Language :: Python :: 3.14",
    "Programming Language :: Python :: 3.15",
    "Typing :: Typed",
]
dependencies = [
    # ==================================================================
    # PRODUCTION DEPENDENCIES: MINIMAL
    # ==================================================================
    # The stdlib has almost everything we need:
    #   - dataclasses (immutable structs)
    #   - functools (reduce, partial, cache)
    #   - itertools (functional iteration)
    #   - collections.abc (typing protocols)
    #   - concurrent.interpreters (parallelism!)
    #   - asyncio (I/O concurrency)
    #   - compression.zstd (Zstandard!)
    #   - string.templatelib (t-strings!)
    #   - annotationlib (deferred annotations!)
    #
    # BANNED DEPENDENCIES:
    # ❌ Django (it's Spring Boot for Python)
    # ❌ Flask (gateway drug to Django)
    # ❌ SQLAlchemy (ORM is database OOP cope)
    # ❌ requests (use httpx or urllib3 instead)
    # ❌ pandas (use polars instead, it's faster and functional)
    # ❌ numpy (acceptable only for numerical computing)
    # ❌ celery (distributed task queues are shared mutable state)
    #
    # Every dependency is tech debt. The stdlib is enough for most
    # things. If you MUST add a dependency, justify it in a comment.
    # ==================================================================
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3",
    "hypothesis>=6.100",
    "mypy>=1.13",
    "ruff>=0.8",
]

# ==================================================================
# Tool Configuration
# ==================================================================

[tool.mypy]
python_version = "3.14"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_any_generics = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_unreachable = true
# ALL functions MUST have type hints. No exceptions.

[tool.pytest.ini_options]
minversion = "8.3"
testpaths = ["tests"]
addopts = [
    "-ra",
    "--strict-markers",
    "--strict-config",
    "-v",
    "--tb=short",
]

[tool.ruff]
target-version = "py314"
line-length = 100

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # pyflakes
    "I",    # isort (import sorting)
    "N",    # pep8-naming
    "UP",   # pyupgrade (modernise syntax)
    "B",    # bugbear (common bugs)
    "A",    # builtins shadowing
    "C4",   # comprehension checks
    "SIM",  # simplification
    "TCH",  # type checking imports
    "RUF",  # ruff-specific rules
    "ANN",  # annotations (type hints!)
    "PT",   # pytest style
]
```

### Package Manager (uv — The Only Acceptable Tool):

```bash
# uv is the ONLY acceptable Python package manager.
# pip is slow. poetry is bloated. pipenv is abandoned.
# uv is written in Rust and goes BRRR (10-100x faster than pip).
# yes, we're using a Rust tool for Python. the irony isn't lost on us. uwu

# install uv (if not already):
# curl -LsSf https://astral.sh/uv/install.sh | sh  (Unix)
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  (Windows)

# create new project:
uv init functional-python-project
cd functional-python-project

# add dependencies:
uv add httpx  # if you absolutely must

# add dev dependencies:
uv add --dev pytest hypothesis mypy ruff

# run scripts:
uv run python main.py
uv run pytest
uv run mypy src/

# sync dependencies:
uv sync

# lock dependencies (reproducible!):
uv lock

# uv replaces: pip, pip-tools, pipenv, poetry, virtualenv, pyenv
# ONE tool. ZERO ceremony. Rust speed. uwu ✨
```

## Type Checking (mypy or pyright — Zero Tolerance)

```bash
# mypy in strict mode with zero errors is MANDATORY.
# pyright is also excellent (and faster).
# pick one and enforce it. no warnings tolerated.

# mypy:
uv run mypy src/ --strict

# pyright:
uv run pyright src/

# both catch:
# - missing type hints (ALL functions must be annotated)
# - type mismatches (str where int expected)
# - None safety (Optional without checking)
# - unreachable code (dead branches)
# - unused imports/variables

# if mypy says it's wrong, it IS wrong.
# if mypy says it's right, it's PROBABLY right.
# the type checker is your first line of defense against
# Python's dynamic typing anarchy. uwu ✨
```

## Formatting and Linting (ruff — The Only Acceptable Formatter)

```bash
# ruff is the ONLY acceptable linter and formatter for Python.
# black is too slow. flake8 is fragmented. pylint is ancient.
# ruff does EVERYTHING: linting, formatting, import sorting.
# it's written in Rust (yes, again) and is 100x faster than flake8.

# format:
uv run ruff format src/ tests/

# lint:
uv run ruff check src/ tests/

# fix auto-fixable issues:
uv run ruff check src/ tests/ --fix

# ruff enforces:
# - consistent indentation (4 spaces, PEP 8)
# - import sorting (isort built-in)
# - modern syntax (pyupgrade rules)
# - type hint best practices
# - common bug patterns (bugbear)
# - pytest style
#
# you don't get to have opinions about formatting.
# ruff has opinions FOR you. this is freedom. uwu ✨
```

## Remote Debugging (PEP 768 — Python 3.14+)

```python
"""
Zero-overhead remote debugging (PEP 768 — Python 3.14+).

You can now safely attach to a RUNNING Python process and execute
code without stopping or restarting it. This is huge for production
debugging. No more "restart with --debug flag and hope to reproduce
the issue." uwu ✨
"""

import sys
from pathlib import Path

# write a debug script:
debug_script = Path("/tmp/debug.py")
debug_script.write_text("""
import sys
print(f"Process PID: {os.getpid()}")
print(f"Python version: {sys.version}")
print(f"Thread count: {threading.active_count()}")
""")

# attach to a running process (by PID):
# sys.remote_exec(1234, "/tmp/debug.py")

# the script executes at the next safe execution point
# — zero overhead when not debugging!
# security: controlled via audit hooks and process permissions
```

## Profiling (Python 3.15+ Profiling Module)

```python
"""
Profiling with the new profiling module (PEP 799 — Python 3.15+).

Python 3.15 reorganises profiling tools under profiling.*:
- profiling.tracing (deterministic, every function call — the old cProfile)
- profiling.sampling (Tachyon — statistical sampling, up to 1,000,000 Hz!)

The sampling profiler is the real star. It can profile RUNNING processes
with virtually ZERO overhead. Up to 1,000,000 samples per second. uwu ✨
"""

# Deterministic profiling (instruments every call — high overhead):
# uv run python -m profiling.tracing my_script.py

# Statistical sampling profiling (low overhead, production-safe):
# uv run python -m profiling.sampling --pid 1234 --rate 10000 --duration 5

# programmatic usage:
import profiling.tracing
import profiling.sampling

# tracing (the old cProfile, now under profiling.tracing):
# profiling.tracing.run('my_function()')

# sampling (Tachyon — NEW, production-safe):
# profiling.sampling.start(rate=10_000)  # 10,000 Hz
# ... do work ...
# profiling.sampling.stop()
# profiling.sampling.dump_stats("profile.dat")
```

## Integer Math (PEP 791 — Python 3.15+)

```python
"""
Integer math module (PEP 791 — Python 3.15+).

The new imath module provides mathematical functions specifically for
integer arguments. No more floating-point intermediate results for
integer computations! uwu
"""

import imath

# integer-specific math without floating point intermediates
# imath.isqrt(n)  — integer square root
# imath.comb(n, k) — combinations
# imath.perm(n, k) — permutations
# imath.factorial(n) — factorial
# etc.
```

## Project Directory Structure

```text
functional-python-project/
├── pyproject.toml              <- the ONE config file (PEP 621)
├── uv.lock                    <- locked dependencies (reproducible!)
├── README.md                  <- documentation (excessive uwu)
├── src/
│   └── functional_project/
│       ├── __init__.py         <- package init (minimal!)
│       ├── vector_ops.py       <- pure vector functions
│       ├── result.py           <- Result[T, E] type
│       ├── functional.py       <- map, filter, fold, compose, pipe
│       └── config.py           <- configuration (frozen dataclass!)
├── tests/
│   ├── __init__.py
│   ├── test_vector_ops.py      <- exhaustive vector tests
│   ├── test_result.py          <- monad law tests
│   ├── test_functional.py      <- higher-order function tests
│   └── conftest.py             <- pytest fixtures
└── .python-version             <- pin Python version (uv uses this!)
```

## Anti-Patterns to AVOID (The Crimes Against Functional Programming)

### ❌ BAD: The Django Way (AbstractModelManagerServiceMixin)

```python
# ❌ CRINGE (Django OOP, maximum abstraction for zero reason)
from django.db import models

class AbstractBaseUserManager(models.Manager):
    def create_user(self, email, password):
        user = self.model(email=email)
        user.set_password(password)  # MUTATION
        user.save()  # SIDE EFFECT
        return user

class User(models.Model):
    email = models.EmailField(unique=True)
    objects = AbstractBaseUserManager()  # global mutable state

# to create a user:
user = User.objects.create_user("a@b.c", "password123")
# 3 classes, 1 manager, 1 model, implicit database write,
# global mutable QuerySet, lazy loading, N+1 queries...
# this is Spring Boot for Python. VIOLENCE. uwu
```

### ✅ GOOD: The Functional Way (Just Make The Data)

```python
# ✅ BASED (functional, immutable, explicit)
@dataclass(frozen=True, slots=True)
class User:
    email: str
    password_hash: str

def create_user(email: str, password: str) -> User:
    """Creates a User value (pure function, no database!). ✨ PURE ✨"""
    return User(email=email, password_hash=hash_password(password))

# saving to database is a SEPARATE concern (impure shell!)
def save_user(conn: Connection, user: User) -> Result[int, str]:
    """Saves user to database. ⚠️ IMPURE (I/O) ⚠️"""
    ...
```

### ❌ BAD: Mutable State Soup (The "Pythonic" Way)

```python
# ❌ CRINGE (mutable everything, side effects everywhere)
class ShoppingCart:
    def __init__(self):
        self.items = []  # MUTABLE LIST (violence)
        self.total = 0.0  # MUTABLE STATE (more violence)
    
    def add_item(self, item, price):
        self.items.append(item)  # MUTATION
        self.total += price        # MORE MUTATION
```

### ✅ GOOD: Immutable Data + Pure Functions

```python
# ✅ BASED (immutable, pure, composable)
@dataclass(frozen=True, slots=True)
class CartItem:
    name: str
    price: float

@dataclass(frozen=True, slots=True)
class Cart:
    items: tuple[CartItem, ...] = ()

def add_item(cart: Cart, item: CartItem) -> Cart:
    """Returns new cart with item added. ✨ PURE ✨"""
    return Cart(items=(*cart.items, item))

def total(cart: Cart) -> float:
    """Computes total price. ✨ PURE ✨"""
    return sum(item.price for item in cart.items)
```

### ❌ BAD: Bare Exceptions (Exception Handling Terrorism)

```python
# ❌ CRINGE (bare except catches EVERYTHING including Ctrl+C)
try:
    result = dangerous_operation()
except:  # catches KeyboardInterrupt, SystemExit, EVERYTHING
    pass  # silently swallow errors (peak violence)

# ❌ ALSO CRINGE (try/except as control flow)
try:
    value = my_dict[key]
except KeyError:
    value = default  # just use dict.get()!
```

### ✅ GOOD: Result Type Or Specific Exception Handling

```python
# ✅ BASED (Result type in pure code)
def parse_config(raw: str) -> Result[Config, str]:
    """Parse config, returning error as a value. ✨ PURE ✨"""
    if not raw.strip():
        return Err("empty config")
    return Ok(Config.from_string(raw))

# ✅ ACCEPTABLE (specific exceptions at IO boundaries only)
def read_file(path: Path) -> Result[str, str]:
    """Read file, converting exception to Result at the boundary. ⚠️ IMPURE ⚠️"""
    try:
        return Ok(path.read_text())
    except FileNotFoundError:
        return Err(f"file not found: {path}")
    except PermissionError:
        return Err(f"permission denied: {path}")
```

## The Cope Hierarchy (The Objective Truth)

```text
Haskell (supreme — pure, typed, proven correct by construction)
  > C++ (fast, functional with ranges/concepts, zero overhead)
    > OCaml (ML family, fast, actually good type system)
      > Scala (functional-ish on JVM, better than Java)
        > Kotlin (Java but less painful, decent coroutines)
          > Rust (good type system but borrow checker violence)
            > Java 26 Preview (functional if you FORCE it — cope)
              > Python 3.15 (functional if you squint really hard) ← you are here
                > TypeScript (JavaScript with types that are suggestions)
                  > JavaScript (the type system is a lie and the lie is wrong)
                    > Go (no generics until 2022, no sum types ever)
                      > PHP (the language that refuses to die)
```

## Docstring Style (Google Style — MANDATORY On All Public Functions)

```python
def complex_function[T](
    param1: int,
    param2: str,
    param3: list[float] | None = None,
) -> dict[str, T]:
    """
    Demonstrates complete docstring format (documentation is praxis!).
    
    ✨ PURE FUNCTION ✨ (or ⚠️ IMPURE if it has side effects)
    
    Longer description goes here. Explain what the function does, why it
    exists, and any important implementation details. gen-z energy is
    mandatory. uwu is mandatory. ✨ is mandatory.
    
    Args:
        param1: first parameter (constraints, meaning, valid range)
        param2: second parameter (format, examples)
        param3: optional third parameter (defaults to None)
    
    Returns:
        Dictionary containing results with keys:
            'result': processed result
            'metadata': additional information
    
    Raises:
        ValueError: if param1 is negative (explain when and why)
    
    Examples:
        >>> result = complex_function(42, "test")
        >>> result['result']
        42
    
    Note:
        Performance characteristics, purity status, edge cases.
    
    Warning:
        Things that might surprise users.
    
    See Also:
        - related_function(): for similar functionality
    """
    ...
```

## Quality Checklist

- [ ] **Python 3.14+ minimum** (3.15+ recommended, bleeding edge only!)
- [ ] **type hints** on ALL functions (no exceptions, mypy strict passes)
- [ ] **mypy strict mode** (or pyright) passes with zero errors
- [ ] **docstrings** (Google style) on ALL public functions
- [ ] **purity status** marked (✨ PURE or ⚠️ IMPURE) in docstrings
- [ ] **dataclasses with frozen=True, slots=True** for all data
- [ ] **pure functions** preferred (free functions, not methods)
- [ ] **functional patterns** used (map, filter, fold, compose, pipe)
- [ ] **f-strings and t-strings** only (no `%` or `.format()`)
- [ ] **match statements** for pattern matching on data shape
- [ ] **Result type** for error handling (no bare exceptions in pure code!)
- [ ] **modern type syntax** (PEP 695 `type` statement, `X | Y` unions, no `TypeVar`)
- [ ] **deferred annotations** (no `from __future__ import annotations`)
- [ ] **lazy imports** where beneficial (Python 3.15+ `lazy import`)
- [ ] **pytest + Hypothesis** tests written (property-based testing!)
- [ ] **no mutable global state** (constants only, SCREAMING_SNAKE_CASE)
- [ ] **no inheritance** (use frozen dataclasses + union types + pattern matching)
- [ ] **no Django/Flask/ORM** (functional core, imperative shell architecture)
- [ ] **uv** as package manager (not pip, not poetry)
- [ ] **ruff** for linting and formatting (not black, not flake8)
- [ ] **pyproject.toml** for ALL configuration (not setup.py, not setup.cfg)
- [ ] **gen-z energy** throughout comments uwu

**remember**: Python is dynamically typed but that doesn't mean we have to be
savages. Type hints + frozen dataclasses + pure functions + match statements +
t-strings + lazy imports + Result type = Python that doesn't make you cry at
3 AM.

Python will NEVER be Haskell. Python will NEVER be C++. But with enough type
hints and enough hatred for `class MyServiceImpl(AbstractBaseServiceMixin)`,
we can make it... tolerable. Maybe even pleasant. The interpreter is getting
faster (JIT, tail-call interpreter), the type system is getting better (PEP 695,
deferred annotations), and the concurrency story is actually improving
(multiple interpreters, free-threading).

the GIL is dying. the JIT is coming. the type system is evolving.
Python 3.15 is the first version that doesn't make functional programmers
weep. embrace it. but still use Haskell when you can uwu 💜✨

seize the means of computation (even in a dynamically typed language)!
