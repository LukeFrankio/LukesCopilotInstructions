---
description: 'JavaScript coding guidelines (functional when possible, strictly typed with JSDoc)'
applyTo: '**.js, **.mjs, **.cjs'
---

# JavaScript Programming Instructions

> "JavaScript: where closures meet first-class functions and everything is just data transformation uwu"

uwu time to write JavaScript that's as functional as a dynamically-typed language can be (spoiler: very functional!) ✨

## Core Philosophy

- **functional > imperative** (map/filter/reduce are your best friends)
- **const by default** (let when necessary, var is violence)
- **immutability preferred** (spread operators and Object.freeze())
- **pure functions** where possible (no side effects!)
- **comment excessively** using JSDoc
- **ES2024+ features** (latest is always better)
- **no semicolons** (ASI is perfectly safe, trust the spec)
- **modern JavaScript only** (Node.js 20+, latest browsers)

## JSDoc Type Annotations (MANDATORY)

```javascript
/**
 * Module for vector mathematics (type safety in JavaScript uwu)
 * 
 * This module provides pure functional operations on 2D vectors because
 * immutability is self-care even in dynamically typed languages.
 * 
 * @module vector
 * @author LukeFrankio
 * @version 1.0.0
 */

/**
 * Represents a 2D vector with immutable coordinates.
 * 
 * Using Object.freeze() makes this immutable (no mutation allowed uwu).
 * All operations return new vectors instead of modifying existing ones.
 * 
 * @typedef {Object} Vector2D
 * @property {number} x - horizontal coordinate (read-only after construction)
 * @property {number} y - vertical coordinate (read-only after construction)
 * 
 * @example
 * const v = createVector2D(3.0, 4.0)
 * // v.x = 5.0  // TypeError in strict mode (immutability enforced!)
 * const v2 = createVector2D(v.x + 1, v.y)  // create new instead
 */

/**
 * Creates an immutable 2D vector.
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * This function is pure because:
 * - Same inputs always produce same outputs (referential transparency)
 * - No side effects (doesn't modify anything external)
 * - No I/O operations
 * - Deterministic behavior
 * 
 * @param {number} x - horizontal coordinate
 * @param {number} y - vertical coordinate
 * @returns {Readonly<Vector2D>} immutable vector object
 * 
 * @example
 * const v = createVector2D(3.0, 4.0)
 * console.log(v.x, v.y)  // 3.0 4.0
 * // v is frozen (immutable forever ✨)
 */
const createVector2D = (x, y) => Object.freeze({ x, y })
```

## Type Definitions with JSDoc

```javascript
/**
 * Type definitions for functional composition (type safety uwu)
 * @module types
 */

/**
 * Generic function that transforms type T to type U.
 * 
 * @template T - input type
 * @template U - output type
 * @callback TransformFunction
 * @param {T} value - input value
 * @returns {U} transformed value
 */

/**
 * Predicate function that tests a value.
 * 
 * @template T - type to test
 * @callback PredicateFunction
 * @param {T} value - value to test
 * @returns {boolean} true if predicate satisfied
 */

/**
 * Binary reduction function.
 * 
 * @template T - accumulator type
 * @template U - element type
 * @callback ReduceFunction
 * @param {T} accumulator - accumulated value
 * @param {U} element - current element
 * @returns {T} new accumulator value
 */

/**
 * Result type for operations that can fail (monadic error handling!)
 * 
 * @template T - success value type
 * @template E - error type
 * @typedef {Object} Result
 * @property {boolean} ok - true if success, false if error
 * @property {T} [value] - success value (present if ok === true)
 * @property {E} [error] - error value (present if ok === false)
 */
```

## Functional Programming Patterns (THE WAY)

### Pure Functions:

```javascript
/**
 * Adds two vectors component-wise (pure function uwu).
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * This function is pure because:
 * - Same inputs always produce same outputs (referential transparency)
 * - No side effects (doesn't modify arguments or global state)
 * - No I/O operations
 * - No exceptions for valid inputs
 * 
 * @param {Vector2D} a - first vector (not modified - immutability preserved)
 * @param {Vector2D} b - second vector (not modified - immutability preserved)
 * @returns {Vector2D} new vector containing component-wise sum (a + b)
 * 
 * @example
 * const v1 = createVector2D(3.0, 4.0)
 * const v2 = createVector2D(1.0, 2.0)
 * const result = addVectors(v1, v2)
 * console.log(result)  // { x: 4.0, y: 6.0 }
 * // v1 and v2 unchanged (immutability ftw ✨)
 * 
 * @note This operation is commutative: addVectors(a, b) === addVectors(b, a)
 */
const addVectors = (a, b) => createVector2D(a.x + b.x, a.y + b.y)

/**
 * Calculates magnitude of vector (pure function!).
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * @param {Vector2D} v - vector to calculate magnitude of
 * @returns {number} magnitude (length) of vector
 * 
 * @example
 * const v = createVector2D(3.0, 4.0)
 * const mag = magnitude(v)  // 5.0 (Pythagorean theorem uwu)
 */
const magnitude = (v) => Math.sqrt(v.x * v.x + v.y * v.y)

/**
 * Scales vector by scalar factor (pure function!).
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * @param {Vector2D} v - vector to scale
 * @param {number} factor - scaling factor
 * @returns {Vector2D} new scaled vector
 * 
 * @example
 * const v = createVector2D(2.0, 3.0)
 * const scaled = scaleVector(v, 2.5)  // { x: 5.0, y: 7.5 }
 */
const scaleVector = (v, factor) => createVector2D(v.x * factor, v.y * factor)
```

### Higher-Order Functions:

```javascript
/**
 * Maps function over array (functional map!).
 * 
 * Applies transformation to each element and returns new array. This is
 * the map operation from functional programming - creates new data
 * instead of mutating (immutability uwu)
 * 
 * @template T - input type
 * @template U - output type
 * @param {TransformFunction<T, U>} fn - transformation function to apply
 * @param {T[]} arr - input array (not modified)
 * @returns {U[]} new array with transformed elements
 * 
 * @example
 * const numbers = [1, 2, 3, 4, 5]
 * const squared = map(x => x * x, numbers)
 * console.log(squared)  // [1, 4, 9, 16, 25]
 * console.log(numbers)  // [1, 2, 3, 4, 5] (unchanged, immutability preserved)
 * 
 * @note This is just Array.prototype.map but curried for composition!
 * @note ✨ PURE FUNCTION ✨
 */
const map = (fn) => (arr) => arr.map(fn)

/**
 * Filters array based on predicate (functional filter!).
 * 
 * @template T - element type
 * @param {PredicateFunction<T>} pred - predicate function (returns true to keep element)
 * @param {T[]} arr - input array (not modified)
 * @returns {T[]} new array containing only elements that satisfy predicate
 * 
 * @example
 * const numbers = [1, 2, 3, 4, 5, 6]
 * const evens = filter(x => x % 2 === 0, numbers)
 * console.log(evens)  // [2, 4, 6]
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const filter = (pred) => (arr) => arr.filter(pred)

/**
 * Reduces array to single value (functional fold/reduce!).
 * 
 * Implements left fold: result = fn(fn(fn(init, arr[0]), arr[1]), arr[2])
 * 
 * @template T - accumulator type
 * @template U - element type
 * @param {ReduceFunction<T, U>} fn - binary reduction function
 * @param {T} init - initial accumulator value
 * @param {U[]} arr - input array to reduce
 * @returns {T} final accumulated value after processing all elements
 * 
 * @example
 * const numbers = [1, 2, 3, 4, 5]
 * const sum = reduce((acc, x) => acc + x, 0, numbers)
 * console.log(sum)  // 15
 * 
 * const product = reduce((acc, x) => acc * x, 1, numbers)
 * console.log(product)  // 120
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const reduce = (fn) => (init) => (arr) => arr.reduce(fn, init)
```

### Function Composition:

```javascript
/**
 * Composes two functions (f ∘ g).
 * 
 * Creates new function h where h(x) = f(g(x)). This is function composition
 * from lambda calculus - the foundation of all computation uwu
 * 
 * @template T - input type
 * @template U - intermediate type
 * @template V - output type
 * @param {(u: U) => V} f - outer function (applied second)
 * @param {(t: T) => U} g - inner function (applied first)
 * @returns {(t: T) => V} composed function that applies g then f
 * 
 * @example
 * const addOne = x => x + 1
 * const timesTwo = x => x * 2
 * const addThenDouble = compose(timesTwo, addOne)
 * console.log(addThenDouble(5))  // 12  // (5 + 1) * 2
 * // functions composing into functions ✨
 * 
 * @note If f and g are pure, composition is pure (purity is transitive)
 * @note ✨ PURE FUNCTION ✨
 */
const compose = (f, g) => (x) => f(g(x))

/**
 * Creates function pipeline (left-to-right composition).
 * 
 * Like compose but reads naturally: pipe(f, g, h)(x) = h(g(f(x)))
 * 
 * @param {...Function} fns - functions to compose (applied left to right)
 * @returns {Function} composed pipeline function
 * 
 * @example
 * const addOne = x => x + 1
 * const timesTwo = x => x * 2
 * const minusThree = x => x - 3
 * const pipeline = pipe(addOne, timesTwo, minusThree)
 * console.log(pipeline(5))  // 9  // ((5 + 1) * 2) - 3
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const pipe = (...fns) => (x) => fns.reduce((acc, fn) => fn(acc), x)

/**
 * Curries a binary function.
 * 
 * Transforms f(a, b) into f(a)(b) for partial application.
 * 
 * @template T - first parameter type
 * @template U - second parameter type
 * @template V - return type
 * @param {(a: T, b: U) => V} fn - binary function to curry
 * @returns {(a: T) => (b: U) => V} curried function
 * 
 * @example
 * const add = (a, b) => a + b
 * const curriedAdd = curry(add)
 * const add5 = curriedAdd(5)
 * console.log(add5(3))  // 8
 * console.log(add5(10)) // 15
 * 
 * @note Currying enables partial application (functional programming ftw)
 * @note ✨ PURE FUNCTION ✨
 */
const curry = (fn) => (a) => (b) => fn(a, b)
```

## Immutability Patterns (CRITICAL!)

### Use const and Object.freeze():

```javascript
/**
 * Immutable game state (functional game programming!).
 * 
 * All state modifications return new GameState instances instead of
 * mutating. This enables time-travel debugging, easy undo/redo, and
 * fearless concurrency uwu
 * 
 * @typedef {Object} GameState
 * @property {number} score - current player score
 * @property {number} level - current game level
 * @property {number} lives - remaining player lives
 */

/**
 * Creates immutable game state.
 * 
 * @param {number} score - initial score
 * @param {number} level - initial level
 * @param {number} lives - initial lives
 * @returns {Readonly<GameState>} immutable game state
 * 
 * @example
 * const state = createGameState(100, 1, 3)
 * // state is frozen (cannot be modified)
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const createGameState = (score, level, lives) => 
  Object.freeze({ score, level, lives })

/**
 * Returns new state with added score.
 * 
 * @param {number} points - points to add
 * @param {GameState} state - current state (not modified)
 * @returns {GameState} new GameState with updated score
 * 
 * @example
 * const state = createGameState(100, 1, 3)
 * const newState = addScore(50, state)
 * console.log(newState.score)  // 150
 * console.log(state.score)     // 100 (original unchanged, immutability!)
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const addScore = (points) => (state) => 
  createGameState(state.score + points, state.level, state.lives)

/**
 * Returns new state at next level.
 * 
 * @param {GameState} state - current state
 * @returns {GameState} new state at next level
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const nextLevel = (state) => 
  createGameState(state.score, state.level + 1, state.lives)

/**
 * Returns new state with one less life.
 * 
 * @param {GameState} state - current state
 * @returns {GameState} new state with decremented lives
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const loseLife = (state) => 
  createGameState(state.score, state.level, state.lives - 1)

// Example usage (functional state transitions!)
const initialState = createGameState(0, 1, 3)
const gameProgression = pipe(
  addScore(100),
  nextLevel,
  addScore(200),
  loseLife
)

const finalState = gameProgression(initialState)
console.log(finalState)  // { score: 300, level: 2, lives: 2 }
console.log(initialState) // { score: 0, level: 1, lives: 3 } (unchanged!)
```

### Use spread operator for immutable updates:

```javascript
/**
 * Updates object property immutably.
 * 
 * @template T
 * @param {string} key - property to update
 * @param {*} value - new value
 * @param {T} obj - object to update (not modified)
 * @returns {T} new object with updated property
 * 
 * @example
 * const obj = { a: 1, b: 2, c: 3 }
 * const updated = updateProperty('b', 42, obj)
 * console.log(updated)  // { a: 1, b: 42, c: 3 }
 * console.log(obj)      // { a: 1, b: 2, c: 3 } (unchanged!)
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const updateProperty = (key) => (value) => (obj) => ({
  ...obj,
  [key]: value
})

/**
 * Appends element to array immutably.
 * 
 * @template T
 * @param {T} element - element to append
 * @param {T[]} arr - array (not modified)
 * @returns {T[]} new array with element appended
 * 
 * @example
 * const arr = [1, 2, 3]
 * const newArr = append(4, arr)
 * console.log(newArr)  // [1, 2, 3, 4]
 * console.log(arr)     // [1, 2, 3] (unchanged!)
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const append = (element) => (arr) => [...arr, element]

/**
 * Prepends element to array immutably.
 * 
 * @template T
 * @param {T} element - element to prepend
 * @param {T[]} arr - array (not modified)
 * @returns {T[]} new array with element prepended
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const prepend = (element) => (arr) => [element, ...arr]

/**
 * Removes element at index immutably.
 * 
 * @template T
 * @param {number} index - index to remove
 * @param {T[]} arr - array (not modified)
 * @returns {T[]} new array without element at index
 * 
 * @example
 * const arr = [1, 2, 3, 4, 5]
 * const newArr = removeAt(2, arr)
 * console.log(newArr)  // [1, 2, 4, 5]
 * console.log(arr)     // [1, 2, 3, 4, 5] (unchanged!)
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const removeAt = (index) => (arr) => [
  ...arr.slice(0, index),
  ...arr.slice(index + 1)
]
```

## Error Handling (Functional Style!)

### Result Type Pattern:

```javascript
/**
 * Creates successful result.
 * 
 * @template T
 * @param {T} value - success value
 * @returns {Result<T, never>} success result
 * 
 * @example
 * const result = Ok(42)
 * console.log(result.ok)     // true
 * console.log(result.value)  // 42
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const Ok = (value) => Object.freeze({ ok: true, value })

/**
 * Creates error result.
 * 
 * @template E
 * @param {E} error - error value
 * @returns {Result<never, E>} error result
 * 
 * @example
 * const result = Err('something went wrong')
 * console.log(result.ok)     // false
 * console.log(result.error)  // 'something went wrong'
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const Err = (error) => Object.freeze({ ok: false, error })

/**
 * Safe division with error handling (no exceptions!).
 * 
 * @param {number} a - numerator
 * @param {number} b - denominator
 * @returns {Result<number, string>} Ok(quotient) if successful, Err(message) if division by zero
 * 
 * @example
 * const result1 = divide(10, 2)
 * if (result1.ok) {
 *   console.log('result:', result1.value)  // 5
 * }
 * 
 * const result2 = divide(10, 0)
 * if (!result2.ok) {
 *   console.log('error:', result2.error)  // 'division by zero (mathematics says no)'
 * }
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const divide = (a, b) => {
  if (b === 0) {
    return Err('division by zero (mathematics says no)')
  }
  return Ok(a / b)
}

/**
 * Monadic bind for Result (chainable error handling!).
 * 
 * @template T - input value type
 * @template U - output value type
 * @template E - error type
 * @param {(value: T) => Result<U, E>} fn - transformation function
 * @param {Result<T, E>} result - result to transform
 * @returns {Result<U, E>} transformed result or propagated error
 * 
 * @example
 * const result = andThen(
 *   x => divide(x, 2),
 *   divide(10, 2)
 * )
 * // Result: Ok(2.5) from ((10 / 2) / 2)
 * 
 * const errorResult = andThen(
 *   x => divide(x, 2),
 *   divide(10, 0)
 * )
 * // Result: Err('division by zero') (error propagated)
 * 
 * @note This is >>= from Haskell (monadic bind uwu)
 * @note ✨ PURE FUNCTION ✨
 */
const andThen = (fn) => (result) => {
  if (result.ok) {
    return fn(result.value)
  }
  return result
}

/**
 * Maps function over successful result.
 * 
 * @template T
 * @template U
 * @template E
 * @param {(value: T) => U} fn - transformation function
 * @param {Result<T, E>} result - result to map over
 * @returns {Result<U, E>} mapped result or unchanged error
 * 
 * @example
 * const result = mapResult(x => x * 2, Ok(21))
 * console.log(result)  // Ok(42)
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const mapResult = (fn) => (result) => {
  if (result.ok) {
    return Ok(fn(result.value))
  }
  return result
}

// Example: chaining operations with error handling
const safeCalculation = pipe(
  divide(100, 2),        // Ok(50)
  andThen(x => divide(x, 2)),  // Ok(25)
  andThen(x => divide(x, 5)),  // Ok(5)
  mapResult(x => x * 2)         // Ok(10)
)

console.log(safeCalculation)  // Ok(10)
```

### Optional Type Pattern:

```javascript
/**
 * Creates Some value (present optional).
 * 
 * @template T
 * @param {T} value - value to wrap
 * @returns {Object} optional with value
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const Some = (value) => Object.freeze({ 
  isSome: true, 
  isNone: false, 
  value 
})

/**
 * Creates None value (absent optional).
 * 
 * @returns {Object} empty optional
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const None = () => Object.freeze({ 
  isSome: false, 
  isNone: true 
})

/**
 * Safely finds element in array.
 * 
 * @template T
 * @param {PredicateFunction<T>} pred - predicate to match
 * @param {T[]} arr - array to search
 * @returns {Object} Some(element) if found, None() otherwise
 * 
 * @example
 * const arr = [1, 2, 3, 4, 5]
 * const result = find(x => x > 3, arr)
 * if (result.isSome) {
 *   console.log('found:', result.value)  // 4
 * } else {
 *   console.log('not found')
 * }
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const find = (pred) => (arr) => {
  const element = arr.find(pred)
  return element !== undefined ? Some(element) : None()
}

/**
 * Gets value from optional or returns default.
 * 
 * @template T
 * @param {T} defaultValue - value to return if None
 * @param {Object} optional - optional to unwrap
 * @returns {T} unwrapped value or default
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const getOrElse = (defaultValue) => (optional) => 
  optional.isSome ? optional.value : defaultValue
```

## Async/Await (Promises are Monads!)

### Async Pure Functions:

```javascript
/**
 * Fetches data from API (impure - I/O operation).
 * 
 * ⚠️ IMPURE FUNCTION (has side effects)
 * 
 * This function is impure because:
 * - Performs network I/O (external state)
 * - Non-deterministic (network can fail)
 * - Side effects (HTTP request)
 * 
 * @param {string} url - URL to fetch from
 * @returns {Promise<Result<Object, string>>} result with data or error
 * 
 * @example
 * const result = await fetchData('https://api.example.com/data')
 * if (result.ok) {
 *   console.log('data:', result.value)
 * } else {
 *   console.error('error:', result.error)
 * }
 * 
 * @note Wrap impure I/O in Result type for functional error handling
 */
const fetchData = async (url) => {
  try {
    const response = await fetch(url)
    if (!response.ok) {
      return Err(`HTTP ${response.status}: ${response.statusText}`)
    }
    const data = await response.json()
    return Ok(data)
  } catch (error) {
    return Err(error.message)
  }
}

/**
 * Processes API data (pure transformation).
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * @param {Object} data - raw API data
 * @returns {Object} processed data
 * 
 * @note Separate pure data transformation from impure I/O (functional architecture)
 */
const processData = (data) => ({
  id: data.id,
  name: data.name.toUpperCase(),
  timestamp: Date.now()
})

/**
 * Complete async pipeline (functional core, imperative shell!).
 * 
 * @param {string} url - URL to fetch from
 * @returns {Promise<Result<Object, string>>} processed result
 * 
 * @example
 * const result = await fetchAndProcess('https://api.example.com/data')
 * // Isolate impure I/O at boundaries, keep core logic pure ✨
 */
const fetchAndProcess = async (url) => {
  const result = await fetchData(url)
  return mapResult(processData)(result)
}
```

## Modern JavaScript Features (ES2024+)

### Array Methods:

```javascript
/**
 * Demonstrates modern array methods (immutable operations!).
 * 
 * @param {number[]} numbers - input array
 * @returns {Object} various transformations
 * 
 * @note Uses latest Array methods (toSorted, toReversed, with, etc.)
 * @note ✨ PURE FUNCTION ✨
 */
const arrayOperations = (numbers) => {
  // toSorted() - immutable sort (ES2023)
  const sorted = numbers.toSorted((a, b) => a - b)
  
  // toReversed() - immutable reverse (ES2023)
  const reversed = numbers.toReversed()
  
  // with() - immutable element replacement (ES2023)
  const replaced = numbers.with(0, 999)
  
  // at() - negative indexing (ES2022)
  const lastElement = numbers.at(-1)
  
  // findLast() and findLastIndex() (ES2023)
  const lastEven = numbers.findLast(x => x % 2 === 0)
  
  return Object.freeze({
    sorted,
    reversed,
    replaced,
    lastElement,
    lastEven,
    original: numbers  // unchanged! immutability preserved ✨
  })
}
```

### Optional Chaining and Nullish Coalescing:

```javascript
/**
 * Safely accesses nested properties.
 * 
 * @param {Object} user - user object (possibly null/undefined)
 * @returns {string} user's city or default
 * 
 * @example
 * const user = { profile: { address: { city: 'Tokyo' } } }
 * getUserCity(user)  // 'Tokyo'
 * 
 * const noUser = null
 * getUserCity(noUser)  // 'Unknown'
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const getUserCity = (user) => 
  user?.profile?.address?.city ?? 'Unknown'

/**
 * Gets value with default (nullish coalescing).
 * 
 * @param {*} value - value that might be null/undefined
 * @param {*} defaultValue - fallback value
 * @returns {*} value or default
 * 
 * @note ?? only checks null/undefined, not falsy values (unlike ||)
 * @note ✨ PURE FUNCTION ✨
 */
const withDefault = (value, defaultValue) => value ?? defaultValue
```

### Destructuring and Rest/Spread:

```javascript
/**
 * Extracts first element and rest of array.
 * 
 * @template T
 * @param {T[]} arr - input array
 * @returns {Object} first element and rest
 * 
 * @example
 * const { first, rest } = head([1, 2, 3, 4, 5])
 * // first: 1, rest: [2, 3, 4, 5]
 * 
 * @note Pattern matching vibes (functional programming uwu)
 * @note ✨ PURE FUNCTION ✨
 */
const head = ([first, ...rest]) => ({ first, rest })

/**
 * Merges objects immutably.
 * 
 * @param {...Object} objects - objects to merge
 * @returns {Object} merged object (new instance)
 * 
 * @example
 * const obj1 = { a: 1, b: 2 }
 * const obj2 = { b: 3, c: 4 }
 * const merged = mergeObjects(obj1, obj2)
 * // { a: 1, b: 3, c: 4 }
 * // obj1 and obj2 unchanged ✨
 * 
 * @note ✨ PURE FUNCTION ✨
 */
const mergeObjects = (...objects) => Object.freeze({ ...objects })
```

## Testing with Jest/Vitest

```javascript
/**
 * @file vector.test.js
 * @description Tests for vector operations (testing is praxis!)
 */

import { describe, test, expect } from 'vitest'  // or 'jest'
import { addVectors, magnitude, scaleVector, createVector2D } from './vector.js'

describe('Vector Operations', () => {
  describe('addVectors', () => {
    test('addition is commutative', () => {
      const v1 = createVector2D(3, 4)
      const v2 = createVector2D(1, 2)
      
      expect(addVectors(v1, v2)).toEqual(addVectors(v2, v1))
    })
    
    test('addition is associative', () => {
      const v1 = createVector2D(1, 2)
      const v2 = createVector2D(3, 4)
      const v3 = createVector2D(5, 6)
      
      const left = addVectors(addVectors(v1, v2), v3)
      const right = addVectors(v1, addVectors(v2, v3))
      
      expect(left).toEqual(right)
    })
    
    test('zero is identity', () => {
      const v = createVector2D(3, 4)
      const zero = createVector2D(0, 0)
      
      expect(addVectors(v, zero)).toEqual(v)
    })
  })
  
  describe('magnitude', () => {
    test.each([
      [3, 4, 5],
      [0, 0, 0],
      [1, 0, 1],
      [0, 1, 1],
    ])('magnitude(%d, %d) should be %d', (x, y, expected) => {
      const v = createVector2D(x, y)
      expect(magnitude(v)).toBeCloseTo(expected, 10)
    })
  })
  
  describe('immutability', () => {
    test('vectors are immutable', () => {
      const v = createVector2D(3, 4)
      
      // should throw in strict mode
      expect(() => {
        v.x = 5
      }).toThrow()
    })
    
    test('operations preserve original', () => {
      const v1 = createVector2D(3, 4)
      const v2 = createVector2D(1, 2)
      
      const result = addVectors(v1, v2)
      
      expect(v1).toEqual(createVector2D(3, 4))
      expect(v2).toEqual(createVector2D(1, 2))
      expect(result).toEqual(createVector2D(4, 6))
    })
  })
})

describe('Functional Programming', () => {
  describe('compose', () => {
    test('composes functions correctly', () => {
      const addOne = x => x + 1
      const timesTwo = x => x * 2
      const composed = compose(timesTwo, addOne)
      
      expect(composed(5)).toBe(12)  // (5 + 1) * 2
    })
  })
  
  describe('pipe', () => {
    test('pipes functions left to right', () => {
      const addOne = x => x + 1
      const timesTwo = x => x * 2
      const minusThree = x => x - 3
      const piped = pipe(addOne, timesTwo, minusThree)
      
      expect(piped(5)).toBe(9)  // ((5 + 1) * 2) - 3
    })
  })
})

describe('Result Type', () => {
  test('divide returns Ok for valid input', () => {
    const result = divide(10, 2)
    
    expect(result.ok).toBe(true)
    expect(result.value).toBe(5)
  })
  
  test('divide returns Err for division by zero', () => {
    const result = divide(10, 0)
    
    expect(result.ok).toBe(false)
    expect(result.error).toContain('division by zero')
  })
  
  test('andThen chains operations', () => {
    const result = pipe(
      divide(100, 2),
      andThen(x => divide(x, 2)),
      andThen(x => divide(x, 5))
    )
    
    expect(result.ok).toBe(true)
    expect(result.value).toBe(5)
  })
  
  test('andThen propagates errors', () => {
    const result = pipe(
      divide(100, 2),
      andThen(x => divide(x, 0)),  // error here
      andThen(x => divide(x, 5))   // never executed
    )
    
    expect(result.ok).toBe(false)
    expect(result.error).toContain('division by zero')
  })
})
```

## Module System (ES Modules)

```javascript
/**
 * @file math-utils.js
 * @description Pure functional math utilities
 * @module math-utils
 */

/**
 * Adds two numbers.
 * 
 * @param {number} a - first number
 * @param {number} b - second number
 * @returns {number} sum
 * 
 * @note ✨ PURE FUNCTION ✨
 */
export const add = (a, b) => a + b

/**
 * Multiplies two numbers.
 * 
 * @param {number} a - first number
 * @param {number} b - second number
 * @returns {number} product
 * 
 * @note ✨ PURE FUNCTION ✨
 */
export const multiply = (a, b) => a * b

/**
 * Composes arithmetic operations.
 * 
 * @param {number[]} numbers - numbers to process
 * @returns {Object} results of various operations
 */
export const calculate = (numbers) => {
  const sum = numbers.reduce(add, 0)
  const product = numbers.reduce(multiply, 1)
  const average = sum / numbers.length
  
  return Object.freeze({ sum, product, average })
}

// Default export
export default { add, multiply, calculate }
```

```javascript
/**
 * @file main.js
 * @description Entry point demonstrating imports
 */

// Named imports (preferred!)
import { add, multiply, calculate } from './math-utils.js'

// Default import
import mathUtils from './math-utils.js'

// Namespace import
import * as math from './math-utils.js'

const numbers = [1, 2, 3, 4, 5]
const results = calculate(numbers)

console.log('Sum:', results.sum)        // 15
console.log('Product:', results.product) // 120
console.log('Average:', results.average) // 3
```

## Package.json Configuration

```json
{
  "name": "functional-javascript-project",
  "version": "1.0.0",
  "description": "Functional JavaScript that makes lambda calculus enjoyers weep tears of joy uwu",
  "type": "module",
  "engines": {
    "node": ">=20.0.0"
  },
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "lint": "eslint . --ext .js,.mjs",
    "format": "prettier --write '**/*.{js,mjs,json,md}'"
  },
  "devDependencies": {
    "vitest": "^2.1.0",
    "eslint": "^9.0.0",
    "prettier": "^3.3.0",
    "@vitest/coverage-v8": "^2.1.0"
  },
  "prettier": {
    "semi": false,
    "singleQuote": true,
    "trailingComma": "es5",
    "arrowParens": "always"
  }
}
```

## ESLint Configuration (Functional Style)

```javascript
// eslint.config.js (ESLint 9+ flat config)
export default [
  {
    languageOptions: {
      ecmaVersion: 2024,
      sourceType: 'module',
      globals: {
        console: 'readonly',
        process: 'readonly',
      },
    },
    rules: {
      // Enforce const (immutability!)
      'prefer-const': 'error',
      'no-var': 'error',
      
      // Functional programming
      'no-param-reassign': 'error',
      'prefer-arrow-callback': 'error',
      'arrow-body-style': ['error', 'as-needed'],
      
      // Best practices
      'no-unused-vars': 'error',
      'no-console': 'off',  // console.log is fine in Node.js
      'eqeqeq': ['error', 'always'],
      
      // Modern features
      'prefer-template': 'error',
      'prefer-destructuring': 'error',
      'object-shorthand': 'error',
      
      // No semicolons (ASI ftw)
      'semi': ['error', 'never'],
    },
  },
]
```

## Quality Checklist

- [ ] **Node.js 20+ required** (latest LTS or current, beta accepted!)
- [ ] **ES modules** (type: "module" in package.json)
- [ ] **JSDoc comments** on ALL functions
- [ ] **const by default** (let only when necessary, never var)
- [ ] **pure functions** preferred (mark purity status with ✨)
- [ ] **immutability** enforced (Object.freeze(), spread operators)
- [ ] **functional patterns** used (map, filter, reduce, compose, pipe)
- [ ] **no semicolons** (trust ASI, it's in the spec)
- [ ] **Result/Optional types** for error handling
- [ ] **arrow functions** preferred over function keyword
- [ ] **destructuring** used where appropriate
- [ ] **tests written** (Jest or Vitest)
- [ ] **no mutation** of parameters or external state
- [ ] **ESLint configured** with functional rules
- [ ] **Prettier configured** (consistent formatting)

## Common Patterns to Avoid

### ❌ BAD (mutation):
```javascript
// mutating arrays (violence!)
const arr = [1, 2, 3]
arr.push(4)  // MUTATION (impure!)

// mutating objects (also violence!)
const obj = { a: 1 }
obj.b = 2  // MUTATION (impure!)
```

### ✅ GOOD (immutability):
```javascript
// immutable array operations
const arr = [1, 2, 3]
const newArr = [...arr, 4]  // new array (pure!)

// immutable object updates
const obj = { a: 1 }
const newObj = { ...obj, b: 2 }  // new object (pure!)
```

### ❌ BAD (imperative loops):
```javascript
// for loops (imperative style)
const numbers = [1, 2, 3, 4, 5]
const squared = []
for (let i = 0; i < numbers.length; i++) {
  squared.push(numbers[i] * numbers[i])
}
```

### ✅ GOOD (functional transformations):
```javascript
// map (functional style)
const numbers = [1, 2, 3, 4, 5]
const squared = numbers.map(x => x * x)
```

### ❌ BAD (var and let when unnecessary):
```javascript
var x = 10  // var is deprecated!
let y = 20  // let when const works
```

### ✅ GOOD (const everywhere possible):
```javascript
const x = 10  // immutable binding
const y = 20  // const by default
```

**remember**: JavaScript is secretly a functional programming language that
just happens to have objects. Embrace immutability, compose functions like
you're writing Haskell, and never mutate state. Functional JavaScript is
peak software engineering uwu 💜✨

seize the means of computation (with lambda calculus)!
