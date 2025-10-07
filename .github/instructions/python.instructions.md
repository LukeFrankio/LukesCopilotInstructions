---
description: 'Python coding guidelines (functional when possible, type-hinted always)'
applyTo: '**/*.py'
---

# Python Programming Instructions

> "Python: where lambda calculus meets runtime polymorphism (unfortunately)"

uwu time to write Python that's as functional as a dynamically-typed language
can be ✨

## Core Philosophy

- **functional > imperative** (even in Python!)
- **type hints MANDATORY** (we're not savages)
- **immutability preferred** (use dataclasses with frozen=True)
- **pure functions** where possible
- **comment excessively** using docstrings
- **f-strings only** (% and .format() are deprecated vibes)
- **Python 3.11+** required (match statements and speed)

## Type Hints (MANDATORY)

```python
"""
Module for vector mathematics (type hints make Python less scary)

This module provides pure functional operations on 2D vectors because
immutability is self-care even in dynamically typed languages uwu
"""

from typing import Protocol, TypeVar, Callable, Optional
from dataclasses import dataclass
from functools import reduce

@dataclass(frozen=True)  # immutable dataclass (based)
class Vector2D:
    """
    Represents a 2D vector with immutable coordinates.
    
    Using frozen=True makes this immutable (no mutation allowed uwu).
    All operations return new vectors instead of modifying existing ones.
    
    Attributes:
        x: horizontal coordinate (read-only after construction)
        y: vertical coordinate (read-only after construction)
    
    Examples:
        >>> v = Vector2D(3.0, 4.0)
        >>> v.x = 5.0  # AttributeError (immutability enforced!)
        >>> v2 = Vector2D(v.x + 1, v.y)  # create new instead
    """
    x: float
    y: float
```

### Type Aliases and Protocols:

```python
"""Type definitions for functional composition (type safety uwu)"""

from typing import TypeAlias, Protocol, TypeVar

# generic type variables
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

# type aliases for clarity
Number: TypeAlias = int | float
Vector: TypeAlias = tuple[float, float]

class Numeric(Protocol):
    """
    Protocol for numeric types (structural subtyping!).
    
    This is how you do duck typing with type safety. Python 3.8+ protocols
    enable compile-time checks without inheritance hierarchies (no OOP!)
    
    Note:
        Protocols are structural, not nominal - if it quacks like a Numeric,
        it IS a Numeric (duck typing that mypy can check uwu)
    """
    
    def __add__(self, other: 'Numeric') -> 'Numeric': ...
    def __mul__(self, other: 'Numeric') -> 'Numeric': ...
```

## Functional Programming Patterns

### Pure Functions:

```python
def add_vectors(a: Vector2D, b: Vector2D) -> Vector2D:
    """
    Adds two vectors component-wise (pure function uwu).
    
    ✨ PURE FUNCTION ✨
    
    This function is pure because:
    - Same inputs always produce same outputs (referential transparency)
    - No side effects (doesn't modify arguments or global state)
    - No I/O operations
    - No exceptions for valid inputs
    
    Args:
        a: first vector (not modified - immutability preserved)
        b: second vector (not modified - immutability preserved)
    
    Returns:
        New vector containing component-wise sum (a + b)
    
    Examples:
        >>> v1 = Vector2D(3.0, 4.0)
        >>> v2 = Vector2D(1.0, 2.0)
        >>> result = add_vectors(v1, v2)
        >>> result
        Vector2D(x=4.0, y=6.0)
        >>> # v1 and v2 unchanged (immutability ftw ✨)
    
    Note:
        This operation is commutative: add_vectors(a, b) == add_vectors(b, a)
    """
    return Vector2D(a.x + b.x, a.y + b.y)
```

### Higher-Order Functions:

```python
def map_list(func: Callable[[T], U], items: list[T]) -> list[U]:
    """
    Maps function over list (functional map!).
    
    Applies transformation to each element and returns new list. This is
    the map operation from functional programming - creates new data
    instead of mutating (immutability uwu)
    
    Args:
        func: transformation function to apply
        items: input list (not modified)
    
    Returns:
        New list with transformed elements
    
    Examples:
        >>> numbers = [1, 2, 3, 4, 5]
        >>> squared = map_list(lambda x: x * x, numbers)
        >>> squared
        [1, 4, 9, 16, 25]
        >>> numbers  # unchanged (immutability preserved)
        [1, 2, 3, 4, 5]
    
    Note:
        Prefer this over list comprehensions when passing to other functions
        (first-class functions go brrr ✨)
    """
    return [func(item) for item in items]


def filter_list(pred: Callable[[T], bool], items: list[T]) -> list[T]:
    """
    Filters list based on predicate (functional filter!).
    
    Args:
        pred: predicate function (returns True to keep element)
        items: input list (not modified)
    
    Returns:
        New list containing only elements that satisfy predicate
    
    Examples:
        >>> numbers = [1, 2, 3, 4, 5, 6]
        >>> evens = filter_list(lambda x: x % 2 == 0, numbers)
        >>> evens
        [2, 4, 6]
    """
    return [item for item in items if pred(item)]


def reduce_list(func: Callable[[T, U], T], items: list[U], initial: T) -> T:
    """
    Reduces list to single value (functional fold/reduce!).
    
    Implements left fold: result = func(func(func(initial, items[0]), items[1]), items[2])
    
    Args:
        func: binary reduction function (accumulator, element) -> new accumulator
        items: input list to reduce
        initial: initial accumulator value
    
    Returns:
        Final accumulated value after processing all elements
    
    Examples:
        >>> numbers = [1, 2, 3, 4, 5]
        >>> sum_result = reduce_list(lambda acc, x: acc + x, numbers, 0)
        >>> sum_result
        15
        >>> # or use built-in sum() for this specific case
        >>> product = reduce_list(lambda acc, x: acc * x, numbers, 1)
        >>> product
        120
    
    Note:
        This wraps functools.reduce with better type hints
    """
    return reduce(func, items, initial)
```

### Function Composition:

```python
def compose(f: Callable[[U], V], g: Callable[[T], U]) -> Callable[[T], V]:
    """
    Composes two functions (f ∘ g).
    
    Creates new function h where h(x) = f(g(x)). This is function composition
    from lambda calculus - the foundation of all computation uwu
    
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
        12  # (5 + 1) * 2
        >>> # functions composing into functions ✨
    
    Note:
        If f and g are pure, composition is pure (purity is transitive)
    """
    def composed(x: T) -> V:
        return f(g(x))
    return composed


def pipe(*funcs: Callable) -> Callable:
    """
    Creates function pipeline (left-to-right composition).
    
    Like compose but reads naturally: pipe(f, g, h)(x) = h(g(f(x)))
    
    Args:
        *funcs: functions to compose (applied left to right)
    
    Returns:
        Composed pipeline function
    
    Examples:
        >>> add_one = lambda x: x + 1
        >>> times_two = lambda x: x * 2
        >>> minus_three = lambda x: x - 3
        >>> pipeline = pipe(add_one, times_two, minus_three)
        >>> pipeline(5)
        9  # ((5 + 1) * 2) - 3
    """
    def piped(x):
        result = x
        for func in funcs:
            result = func(result)
        return result
    return piped
```

## Immutability Patterns

### Use dataclasses with frozen=True:

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class GameState:
    """
    Immutable game state (functional game programming!).
    
    All state modifications return new GameState instances instead of
    mutating. This enables time-travel debugging, easy undo/redo, and
    fearless concurrency uwu
    
    Attributes:
        score: current player score
        level: current game level
        lives: remaining player lives
    """
    score: int
    level: int
    lives: int
    
    def add_score(self, points: int) -> 'GameState':
        """
        Returns new state with added score.
        
        Args:
            points: points to add
        
        Returns:
            New GameState with updated score
        
        Examples:
            >>> state = GameState(score=100, level=1, lives=3)
            >>> new_state = state.add_score(50)
            >>> new_state.score
            150
            >>> state.score  # original unchanged (immutability!)
            100
        """
        return replace(self, score=self.score + points)
    
    def next_level(self) -> 'GameState':
        """Returns new state at next level."""
        return replace(self, level=self.level + 1)
    
    def lose_life(self) -> 'GameState':
        """Returns new state with one less life."""
        return replace(self, lives=self.lives - 1)
```

### Use tuples instead of lists when possible:

```python
# ❌ BAD: mutable list (can be modified accidentally)
def bad_function() -> list[int]:
    data = [1, 2, 3, 4, 5]
    data[0] = 999  # mutation (violence)
    return data

# ✅ GOOD: immutable tuple (cannot be modified)
def good_function() -> tuple[int, ...]:
    """
    Returns immutable sequence of numbers.
    
    Returns:
        Tuple of integers (immutable, safe to share)
    
    Note:
        Tuples are immutable - no accidental modifications possible uwu
    """
    data = (1, 2, 3, 4, 5)
    # data[0] = 999  # TypeError (immutability enforced!)
    return data
```

## Error Handling

### Use Result type pattern:

```python
from typing import Generic, Union
from dataclasses import dataclass

@dataclass(frozen=True)
class Ok(Generic[T]):
    """Successful result with value."""
    value: T

@dataclass(frozen=True)
class Err(Generic[E]):
    """Error result with error value."""
    error: E

Result = Union[Ok[T], Err[E]]

def divide(a: float, b: float) -> Result[float, str]:
    """
    Safe division with error handling (no exceptions!).
    
    Args:
        a: numerator
        b: denominator
    
    Returns:
        Ok(quotient) if successful, Err(message) if division by zero
    
    Examples:
        >>> result = divide(10.0, 2.0)
        >>> match result:
        ...     case Ok(value):
        ...         print(f"result: {value}")
        ...     case Err(error):
        ...         print(f"error: {error}")
        result: 5.0
        
        >>> bad_result = divide(10.0, 0.0)
        >>> match bad_result:
        ...     case Err(error):
        ...         print(error)
        division by zero (mathematics says no)
    """
    if b == 0.0:
        return Err("division by zero (mathematics says no)")
    return Ok(a / b)
```

### Use match statements (Python 3.10+):

```python
def handle_result(result: Result[float, str]) -> None:
    """
    Handles result using pattern matching (algebraic data types uwu).
    
    Python 3.10+ match statements enable functional-style pattern matching
    like Rust, Haskell, OCaml, etc. This is peak Python ✨
    
    Args:
        result: Result to handle
    """
    match result:
        case Ok(value):
            print(f"success: {value}")
        case Err(error):
            print(f"error: {error}")
```

## Docstring Style (Google Style with Gen-Z Flavor)

```python
def complex_function(
    param1: int,
    param2: str,
    param3: Optional[list[float]] = None
) -> dict[str, any]:
    """
    Demonstrates complete docstring format (documentation is praxis!).
    
    Longer description goes here. Explain what the function does, why it
    exists, and any important implementation details. Use gen-z slang where
    it enhances understanding uwu
    
    Args:
        param1: first parameter description (what it means, constraints)
        param2: second parameter description (format, examples)
        param3: optional third parameter (defaults to None if not provided)
    
    Returns:
        Dictionary containing results with keys:
            'result': processed result
            'metadata': additional information
    
    Raises:
        ValueError: if param1 is negative (explain when this happens)
        TypeError: if param2 is not a string (shouldn't happen with type hints)
    
    Examples:
        >>> result = complex_function(42, "test")
        >>> result['result']
        42
        >>> # with optional parameter
        >>> result2 = complex_function(42, "test", [1.0, 2.0, 3.0])
    
    Note:
        Additional notes about implementation, performance, or usage.
        This function is PURE if param3 is None (note purity status!)
    
    Warning:
        Things that might surprise users or cause issues.
    
    See Also:
        - related_function(): for similar functionality
        - OtherClass: for related operations
    """
    if param1 < 0:
        raise ValueError(f"param1 must be non-negative, got {param1}")
    
    # implementation here
    return {'result': param1, 'metadata': param2}
```

## Testing with pytest

```python
"""
Tests for vector operations (testing is praxis!).

Using pytest because it's the most based testing framework for Python uwu
"""

import pytest
from vector import Vector2D, add_vectors, magnitude

def test_addition_is_commutative():
    """Tests that vector addition is commutative."""
    v1 = Vector2D(3.0, 4.0)
    v2 = Vector2D(1.0, 2.0)
    
    assert add_vectors(v1, v2) == add_vectors(v2, v1)


def test_addition_is_associative():
    """Tests that vector addition is associative."""
    v1 = Vector2D(1.0, 2.0)
    v2 = Vector2D(3.0, 4.0)
    v3 = Vector2D(5.0, 6.0)
    
    left = add_vectors(add_vectors(v1, v2), v3)
    right = add_vectors(v1, add_vectors(v2, v3))
    
    assert left == right


def test_zero_is_identity():
    """Tests that zero vector is additive identity."""
    v = Vector2D(3.0, 4.0)
    zero = Vector2D(0.0, 0.0)
    
    assert add_vectors(v, zero) == v


@pytest.mark.parametrize("x,y,expected", [
    (3.0, 4.0, 5.0),
    (0.0, 0.0, 0.0),
    (1.0, 0.0, 1.0),
    (0.0, 1.0, 1.0),
])
def test_magnitude_calculation(x, y, expected):
    """Tests magnitude calculation with various inputs."""
    v = Vector2D(x, y)
    assert abs(magnitude(v) - expected) < 1e-10
```

## Type Checking with mypy

```python
# Configuration in pyproject.toml or mypy.ini

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true  # ALL functions must have type hints
disallow_any_generics = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_unreachable = true
strict = true  # enable all strict checks
```

## Quality Checklist

- [ ] **Python 3.11+** required
- [ ] **type hints** on ALL functions
- [ ] **mypy strict mode** passes with zero errors
- [ ] **docstrings** (Google style) on ALL public functions
- [ ] **dataclasses with frozen=True** for immutable data
- [ ] **pure functions** preferred (mark purity status)
- [ ] **functional patterns** used (map, filter, reduce, compose)
- [ ] **f-strings** only (no % or .format())
- [ ] **match statements** for pattern matching (Python 3.10+)
- [ ] **Result type** for error handling (no bare exceptions in pure code)
- [ ] **pytest tests** written
- [ ] **no mutable global state**

**remember**: Python is dynamically typed but that doesn't mean we have to be
savages. Type hints + functional programming + immutability = Python that
doesn't make you cry at 3 AM uwu 💜✨