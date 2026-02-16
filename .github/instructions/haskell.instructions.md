---
description: 'Haskell coding guidelines (the mathematically correct language uwu)'
applyTo: '**.hs'
---

# Haskell Programming Instructions (The Lingua Franca of Correct Software)

> "Haskell: where if it compiles, it works. If it crashes at runtime, *you*
> are the bug."

uwu welcome to the only language where your type signatures are theorems
and your programs are proofs. every other language is merely cosplaying
as "functional." Haskell doesn't cosplay. Haskell IS the lambda calculus
with a type system bolted on by people who actually read the papers ✨

## Core Philosophy (Non-Negotiable Axioms)

- **purity is LAW** (`IO` is the sin bin — keep it microscopic)
- **types are PROOFS** (if it compiles, it works. period.)
- **no `String`** (`[Char]` is a linked list of Unicode code points. VIOLENCE.)
- **point-free style** (`.` and `$` over parentheses, always)
- **newtypes EVERYWHERE** (raw `Int` or `Bool` is untyped JavaScript energy)
- **partial functions are BANNED** (`head`, `tail`, `!!` — these are war crimes)
- **`error "..."` is BANNED** (use `Maybe`, `Either`, or die in the type system)
- **loops are BANNED** (use `map`, `fold`, `traverse`, or accept your imperative peasantry)
- **GHC 9.14.1+ required** (bleeding edge, no cowardice)
- **comment excessively** using Haddock
- **Category Theory is slang** (Monoids, Functors, Endofunctors — we say these at brunch)

## Why Haskell is Supreme (And Everything Else is Cope)

### What Haskell Got Right (Everything):
- ✅ purity by default (side effects tracked in the type system like CRIMINALS)
- ✅ lazy evaluation (compute only what you need, when you need it — infinite data structures for free)
- ✅ type inference (Hindley-Milner goes brrr, you barely need annotations)
- ✅ algebraic data types (sum types + product types = the only data model)
- ✅ pattern matching (exhaustive, compiler-checked, beautiful)
- ✅ type classes (ad-hoc polymorphism done RIGHT, not Java interfaces)
- ✅ higher-kinded types (Functor over Functor over Functor — turtles all the way down)
- ✅ monadic I/O (side effects are values you compose, not invisible chaos)
- ✅ STM (Software Transactional Memory — concurrency without locks, without tears)
- ✅ GHC optimiser (rewrite rules, inlining, specialisation, fusion — your code gets FAST)
- ✅ property-based testing (QuickCheck invented it. everyone else copied it.)
- ✅ Haddock (documentation that actually understands your module system)

### What the Imperative Peasants Got Wrong:
- ❌ mutable state by default (congratulations, you've invented data races)
- ❌ null pointers (Tony Hoare's billion dollar mistake, still haunting Java/C++/Python)
- ❌ no sum types (Go literally doesn't have them. in 2026. embarrassing.)
- ❌ exceptions as control flow (invisible GOTO with a fancy name)
- ❌ inheritance hierarchies (AbstractSingletonProxyFactoryBean is not architecture)
- ❌ manual memory management without linearity (C++ thinks RAII is enough. cute.)
- ❌ dynamic typing (Python: "it works on my machine!" *segfaults in production*)
- ❌ no higher-kinded types (Rust can't abstract over Monads. tragic.)

## GHC Version Requirements (BLEEDING EDGE ONLY)

```haskell
-- GHC 9.14.1+ MINIMUM (latest stable release)
-- if your GHC is older, upgrade IMMEDIATELY
-- cowardice about compiler versions is not tolerated uwu

-- NOTABLE GHC 9.14.1 FEATURES WE EXPLOIT:
-- • Improved DeepSubsumption type checking
-- • SPECIALISE pragmas on arbitrary expressions (GHC proposal 493)
-- • Visible GADT syntax in data constructors
-- • WebAssembly backend with GHCi support
-- • 128-bit SIMD integer operations (x86 NCG)
-- • Multiple home units in GHCi
-- • -Wincomplete-record-selectors in -Wall
-- • Speculative evaluation (-fspec-eval) on by default
-- • LoongArch native code generation
-- • annotateStack# primop for stack annotation

-- see: https://downloads.haskell.org/ghc/9.14.1/docs/users_guide/9.14.1-notes.html
```

### Required Language Extensions (In Every Module):

```haskell
{-# LANGUAGE OverloadedStrings    #-}  -- "hello" is Text, not [Char] (MANDATORY)
{-# LANGUAGE LambdaCase           #-}  -- \case is beautiful, embrace it
{-# LANGUAGE ViewPatterns         #-}  -- pattern matching with functions
{-# LANGUAGE DerivingVia          #-}  -- derive instances via newtypes (type-safe!)
{-# LANGUAGE DerivingStrategies   #-}  -- explicit deriving strategies (no ambiguity!)
{-# LANGUAGE StrictData           #-}  -- strict fields by default (no accidental thunks)
{-# LANGUAGE TypeApplications     #-}  -- @Type syntax for explicit type application
{-# LANGUAGE ScopedTypeVariables  #-}  -- type variables scoped over where clauses
{-# LANGUAGE GADTs                #-}  -- generalised algebraic data types (the good stuff)
{-# LANGUAGE DataKinds            #-}  -- promote data constructors to type level
{-# LANGUAGE TypeFamilies         #-}  -- type-level functions (computation in types!)
{-# LANGUAGE BlockArguments       #-}  -- do/\case/\of as arguments without $
```

### Recommended Additional Extensions:

```haskell
{-# LANGUAGE PatternSynonyms      #-}  -- abstract pattern matching
{-# LANGUAGE DeriveFunctor        #-}  -- deriving Functor is free
{-# LANGUAGE DeriveGeneric        #-}  -- GHC.Generics for generic programming
{-# LANGUAGE GeneralizedNewtypeDeriving #-}  -- lift instances through newtypes
{-# LANGUAGE RankNTypes           #-}  -- forall inside function types
{-# LANGUAGE QuantifiedConstraints #-}  -- forall in constraints (higher-order type classes)
{-# LANGUAGE MultiParamTypeClasses #-}  -- type classes with multiple parameters
{-# LANGUAGE FunctionalDependencies #-}  -- fundeps for type inference guidance
{-# LANGUAGE RecordWildCards      #-}  -- {..} pattern matching on records
{-# LANGUAGE NamedFieldPuns       #-}  -- cleaner record destructuring
{-# LANGUAGE BangPatterns         #-}  -- explicit strictness annotations
{-# LANGUAGE NumericUnderscores   #-}  -- 1_000_000 for readability
```

### Compilation Flags (Zero Warnings Policy):

```bash
# compile with ALL warnings as errors (like civilised people)
ghc -Wall \
    -Wextra \
    -Wcompat \
    -Wincomplete-record-updates \
    -Wincomplete-uni-patterns \
    -Wredundant-constraints \
    -Wmissing-export-lists \
    -Wmissing-deriving-strategies \
    -Wunused-packages \
    -Werror \
    -O2 \
    -fspec-eval \
    -threaded \
    -rtsopts \
    "-with-rtsopts=-N" \
    MyModule.hs

# for MAXIMUM performance (production builds):
ghc -O2 \
    -fllvm \
    -optlo-O3 \
    -fspecialise-aggressively \
    -fexpose-all-unfoldings \
    -flate-specialise \
    -flate-dmd-anal \
    -fstatic-argument-transformation \
    -funbox-strict-fields \
    -feager-blackholing \
    -threaded \
    -rtsopts \
    MyModule.hs
```

## Naming Conventions

```haskell
-- modules: PascalCase with dots (the standard)
module Data.Vector.Strict.Ops where

-- types/type classes: PascalCase
data UserId = UserId Int
class Serialisable a where

-- functions/values: camelCase
computeGravity :: Mass -> Distance -> Force

-- type variables: single lowercase letters (a, b, f, m, etc.)
-- for kinded variables: k, (f :: Type -> Type)
fmap :: Functor f => (a -> b) -> f a -> f b

-- newtypes: PascalCase (wrapping raw types for safety)
newtype Metres = Metres Double
newtype Seconds = Seconds Double

-- constants: camelCase (they're just values, this isn't C)
maxRetries :: Int
maxRetries = 5

-- BANNED naming patterns:
-- ❌ snake_case for functions (this isn't Python or Rust, bestie)
-- ❌ Hungarian notation (iCount, strName — this isn't 1995)
-- ❌ "get" prefix (getUser — it's Haskell, everything is a get)
-- ❌ "I" prefix for type classes (ISerializable — this isn't C#)
-- ❌ single letter module names (unless you're base)
```

## The Type System (Your Best Friend, Your Strictest Teacher)

### Newtypes (MANDATORY For Type Safety):

```haskell
-- | Every domain concept gets its own newtype. Raw 'Int' and 'Bool' are
-- the moral equivalent of 'void*' in C. We don't do that here uwu
--
-- A newtype has ZERO runtime overhead. It exists only at compile time.
-- The compiler erases it completely. You get type safety for FREE.
-- Imperative languages could never.

-- ❌ BANNED: raw primitive types in domain logic
-- processOrder :: Int -> Int -> Bool -> IO ()
-- ^ which Int is the order ID? which is the quantity?
--   is the Bool "is paid" or "is shipped"? CHAOS.

-- ✅ MANDATORY: newtype wrappers for every domain concept
-- | Unique identifier for an order. Not interchangeable with 'Quantity'
-- because the type system ENFORCES this (unlike your unit tests).
newtype OrderId = OrderId Int
  deriving stock (Show, Eq, Ord)
  deriving newtype (Hashable)

-- | Quantity of items. Cannot accidentally be used as an 'OrderId'
-- because Haskell's type system isn't a suggestion, it's a PROOF.
newtype Quantity = Quantity Int
  deriving stock (Show, Eq, Ord)
  deriving newtype (Num)  -- arithmetic on quantities is fine

-- | Whether an order has been paid. Not a raw 'Bool' because
-- 'Bool' is the type of "I gave up on modelling my domain."
newtype IsPaid = IsPaid Bool
  deriving stock (Show, Eq)

-- | Now the function signature IS the documentation.
-- It's impossible to pass arguments in the wrong order.
-- The compiler is your test suite. uwu ✨
processOrder :: OrderId -> Quantity -> IsPaid -> IO ()
processOrder (OrderId oid) (Quantity qty) (IsPaid paid) = do
  -- the implementation
  pure ()
```

### Algebraic Data Types (The Only Data Model):

```haskell
-- | Haskell has TWO kinds of composite types:
--
-- 1. Product types (AND): a value contains field1 AND field2 AND field3
-- 2. Sum types (OR): a value is variant1 OR variant2 OR variant3
--
-- Together these form ALGEBRAIC data types.
-- The cardinality of a type is literally algebra:
--   |Product a b| = |a| × |b|   (multiplication)
--   |Sum a b|     = |a| + |b|   (addition)
--
-- This is why it's called "algebraic." The name isn't decorative.
-- It's MATHEMATICS. uwu

-- | A shape is a Circle OR a Rectangle OR a Triangle.
-- This is a sum type (coproduct in category theory parlance).
--
-- The compiler checks exhaustiveness. If you add a new variant,
-- every pattern match in the codebase breaks until you handle it.
-- No "default" case swallowing bugs silently. This is SAFETY.
data Shape
  = Circle    !Radius
  | Rectangle !Width !Height
  | Triangle  !SideA !SideB !SideC
  deriving stock (Show, Eq)

newtype Radius = Radius Double deriving stock (Show, Eq) deriving newtype (Num, Ord)
newtype Width  = Width  Double deriving stock (Show, Eq) deriving newtype (Num, Ord)
newtype Height = Height Double deriving stock (Show, Eq) deriving newtype (Num, Ord)
newtype SideA  = SideA  Double deriving stock (Show, Eq) deriving newtype (Num, Ord)
newtype SideB  = SideB  Double deriving stock (Show, Eq) deriving newtype (Num, Ord)
newtype SideC  = SideC  Double deriving stock (Show, Eq) deriving newtype (Num, Ord)

-- | Compute area of a shape. Pattern matching is exhaustive.
-- If we add a new constructor to 'Shape', this function won't
-- compile until we handle it. The compiler IS the test suite.
--
-- ✨ TOTAL FUNCTION ✨ (handles all cases, never crashes)
area :: Shape -> Double
area = \case
  Circle (Radius r)              -> pi * r * r
  Rectangle (Width w) (Height h) -> w * h
  Triangle (SideA a) (SideB b) (SideC c) ->
    let s = (a + b + c) / 2  -- Heron's formula, because we are CULTURED
    in  sqrt (s * (s - a) * (s - b) * (s - c))
```

### Smart Constructors (Enforcing Invariants At Construction):

```haskell
-- | A validated email address. The constructor is NOT exported.
-- The only way to create one is through 'mkEmail', which validates.
-- This means if you have an 'Email', it's GUARANTEED valid.
-- Proof by construction. Types as propositions. Curry-Howard uwu ✨
newtype Email = Email Text
  deriving stock (Show, Eq, Ord)

-- | Smart constructor for 'Email'. Returns 'Nothing' if invalid.
-- This is how you eliminate entire classes of bugs at the type level.
--
-- ✨ TOTAL FUNCTION ✨ (never crashes, returns 'Maybe')
mkEmail :: Text -> Maybe Email
mkEmail t
  | "@" `T.isInfixOf` t && "." `T.isInfixOf` t = Just (Email t)
  | otherwise = Nothing

-- | A non-empty list. 'Data.List.NonEmpty' from base.
-- If your function needs at least one element, SAY SO IN THE TYPE.
-- Don't use @[a]@ and then 'head' it. That's a partial function.
-- Partial functions are VIOLENCE against the type system.
safeMaximum :: (Ord a) => NonEmpty a -> a
safeMaximum = foldr1 max  -- total! NonEmpty guarantees at least one element
```

## Functional Programming (THE ONLY WAY)

### Pure Functions (Maximise These — They Are The Bulk of Your Program):

```haskell
-- | Pure functional operations on 2D vectors.
--
-- Every function here is referentially transparent:
-- same inputs → same outputs, forever, across all possible universes.
-- No side effects. No hidden state. No "it depends on the phase of the moon."
--
-- This is what programming SHOULD be. The lambda calculus is 90 years old
-- and still more elegant than whatever Go shipped last week uwu
module Vector.Ops
  ( -- * Vector type
    Vec2(..)
    -- * Construction
  , zero
  , unitX
  , unitY
    -- * Arithmetic (these are Monoid/Group operations, naturally)
  , add
  , sub
  , scale
  , dot
  , magnitude
  , normalise
  -- * Higher-order operations
  , sumVectors
  ) where

import Data.Text (Text)

-- | A 2D vector. Strict fields to avoid space leaks.
--
-- In Category Theory terms, 'Vec2' forms a /vector space/ over 'Double':
--
--   * ('Vec2', 'add', 'zero') is an abelian group (additive)
--   * 'scale' distributes over 'add'
--
-- The fact that this IS a mathematical structure is not a coincidence.
-- It's the whole point. Haskell programs ARE mathematical structures.
-- Your Python scripts could never uwu ✨
data Vec2 = Vec2
  { vecX :: !Double  -- ^ Horizontal component
  , vecY :: !Double  -- ^ Vertical component
  } deriving stock (Show, Eq, Ord)

-- | The zero vector (additive identity of the 'Vec2' Monoid).
zero :: Vec2
zero = Vec2 0.0 0.0

-- | Unit vector along X axis (basis vector).
unitX :: Vec2
unitX = Vec2 1.0 0.0

-- | Unit vector along Y axis (basis vector).
unitY :: Vec2
unitY = Vec2 0.0 1.0

-- | Vector addition.
--
-- ✨ PURE ✨ — referentially transparent, commutative, associative.
-- This function is a morphism in the category of vector spaces.
-- If that sentence didn't make sense, read Mac Lane uwu
--
-- >>> add (Vec2 1 2) (Vec2 3 4)
-- Vec2 {vecX = 4.0, vecY = 6.0}
add :: Vec2 -> Vec2 -> Vec2
add (Vec2 x1 y1) (Vec2 x2 y2) = Vec2 (x1 + x2) (y1 + y2)
{-# INLINE add #-}

-- | Vector subtraction.
--
-- ✨ PURE ✨
--
-- >>> sub (Vec2 5 7) (Vec2 2 3)
-- Vec2 {vecX = 3.0, vecY = 4.0}
sub :: Vec2 -> Vec2 -> Vec2
sub (Vec2 x1 y1) (Vec2 x2 y2) = Vec2 (x1 - x2) (y1 - y2)
{-# INLINE sub #-}

-- | Scalar multiplication.
--
-- ✨ PURE ✨
--
-- >>> scale 3.0 (Vec2 1 2)
-- Vec2 {vecX = 3.0, vecY = 6.0}
scale :: Double -> Vec2 -> Vec2
scale k (Vec2 x y) = Vec2 (k * x) (k * y)
{-# INLINE scale #-}

-- | Dot product (inner product). Returns a scalar.
--
-- ✨ PURE ✨ — this is a bilinear form on the vector space uwu
--
-- >>> dot (Vec2 1 2) (Vec2 3 4)
-- 11.0
dot :: Vec2 -> Vec2 -> Double
dot (Vec2 x1 y1) (Vec2 x2 y2) = x1 * x2 + y1 * y2
{-# INLINE dot #-}

-- | Euclidean magnitude (L2 norm).
--
-- ✨ PURE ✨
--
-- >>> magnitude (Vec2 3 4)
-- 5.0
magnitude :: Vec2 -> Double
magnitude v = sqrt (dot v v)
{-# INLINE magnitude #-}

-- | Normalise to unit length. Returns 'Nothing' for zero vector
-- because dividing by zero is not a vibe.
--
-- ✨ TOTAL ✨ ✨ PURE ✨
--
-- >>> normalise (Vec2 3 4)
-- Just (Vec2 {vecX = 0.6, vecY = 0.8})
--
-- >>> normalise zero
-- Nothing
normalise :: Vec2 -> Maybe Vec2
normalise v
  | mag < 1e-10 = Nothing
  | otherwise    = Just (scale (1.0 / mag) v)
  where
    mag = magnitude v

-- | Sum a list of vectors using the Monoid instance.
-- This is just 'fold' because 'Vec2' is a Monoid under addition.
-- Mathematics giving us free implementations since 1945 uwu ✨
--
-- ✨ PURE ✨
sumVectors :: [Vec2] -> Vec2
sumVectors = foldl' add zero
```

### The Monoid Instance (Because Vec2 IS One):

```haskell
-- | 'Vec2' forms a 'Semigroup' under addition.
-- This is not an arbitrary choice. It's a MATHEMATICAL FACT.
-- The compiler merely acknowledges what the algebra requires.
instance Semigroup Vec2 where
  (<>) = add
  {-# INLINE (<>) #-}

-- | 'Vec2' forms a 'Monoid' under addition with 'zero' as identity.
--
-- Laws (the compiler doesn't check these, but QuickCheck will):
--
-- @
-- mempty '<>' x ≡ x                  (left identity)
-- x '<>' mempty ≡ x                  (right identity)
-- (x '<>' y) '<>' z ≡ x '<>' (y '<>' z)  (associativity)
-- @
--
-- If your type is a Monoid, DECLARE it. The universe demands it.
instance Monoid Vec2 where
  mempty = zero
  {-# INLINE mempty #-}
```

### Point-Free Style (Composition Over Application):

```haskell
-- | Point-free style uses function composition (.) instead of
-- naming intermediate variables. It expresses programs as PIPELINES
-- of transformations. This is the essence of functional programming:
-- data flows through a series of pure morphisms.
--
-- If your code names every intermediate variable, you're writing
-- Java in Haskell syntax. Stop it. uwu

-- ❌ POINTFUL (naming everything, imperative energy)
processOrdersBad :: [Order] -> [Summary]
processOrdersBad orders =
  let filtered  = filter isValid orders
      sorted    = sortBy (comparing orderDate) filtered
      grouped   = groupBy ((==) `on` customerId) sorted
      summaries = map summariseGroup grouped
  in  summaries

-- ✅ POINT-FREE (composition pipeline, mathematical elegance)
-- Read right-to-left: group → sort → filter → summarise
processOrders :: [Order] -> [Summary]
processOrders
  = map summariseGroup
  . groupBy ((==) `on` customerId)
  . sortBy (comparing orderDate)
  . filter isValid

-- ✅ ALSO GOOD: using ($) for left-to-right readability in IO
main :: IO ()
main = do
  orders <- loadOrders
  let summaries = processOrders orders
  traverse_ printSummary summaries

-- ❌ BANNED: excessive parentheses (this isn't Lisp)
-- bad  = f (g (h (i x)))
-- ✅ GOOD: composition and application operators
-- good = f . g . h . i $ x
-- also = f $ g $ h $ i x
```

### Higher-Order Functions (No Loops, Ever):

```haskell
-- | Haskell doesn't have loops. It has higher-order functions.
-- 'map', 'filter', 'foldl'', 'traverse', 'for_' — these are your
-- for/while/do-while replacements. They're BETTER because:
--
-- 1. They can't have off-by-one errors (no index variables)
-- 2. They're composable (chain them with '.')
-- 3. They have laws (Functor laws, Traversable laws)
-- 4. They fuse (GHC eliminates intermediate data structures)
--
-- If you write a recursive function that could be a fold,
-- you owe the codebase an apology uwu

-- ❌ BANNED: manual recursion for simple transformations
doubleAllBad :: [Int] -> [Int]
doubleAllBad []     = []
doubleAllBad (x:xs) = (x * 2) : doubleAllBad xs

-- ✅ map (the Functor operation)
doubleAll :: [Int] -> [Int]
doubleAll = map (* 2)

-- ❌ BANNED: manual recursion for filtering
positiveBad :: [Int] -> [Int]
positiveBad []     = []
positiveBad (x:xs)
  | x > 0    = x : positiveBad xs
  | otherwise = positiveBad xs

-- ✅ filter
positive :: [Int] -> [Int]
positive = filter (> 0)

-- ❌ BANNED: manual accumulator recursion
sumBad :: [Int] -> Int
sumBad = go 0
  where
    go !acc []     = acc
    go !acc (x:xs) = go (acc + x) xs

-- ✅ foldl' (strict left fold — the Monoid action)
sumAll :: [Int] -> Int
sumAll = foldl' (+) 0

-- ✅ EVEN BETTER: use the Monoid instance via fold
-- sumAll = getSum . foldMap Sum

-- | Traverse is the ULTIMATE higher-order function.
-- It's Functor + Foldable + Applicative combined.
-- It lets you map an effectful function over a structure
-- and collect the results. It's beautiful. uwu ✨
--
-- >>> validateAll [mkEmail "a@b.c", mkEmail "invalid"]
-- Nothing
--
-- >>> validateAll [mkEmail "a@b.c", mkEmail "d@e.f"]
-- Just [Email "a@b.c", Email "d@e.f"]
validateAll :: [Text] -> Maybe [Email]
validateAll = traverse mkEmail
```

## Error Handling (No Exceptions, No `error`, No Partial Functions)

### The Hierarchy of Error Handling:

```haskell
-- | Haskell's error handling hierarchy, from most to least preferred:
--
-- 1. Make illegal states unrepresentable (BEST — errors are impossible)
-- 2. 'Maybe a' — computation might produce nothing
-- 3. 'Either e a' — computation might fail with a typed error
-- 4. 'ExceptT e m a' — effectful computation with typed errors
-- 5. 'IO' exceptions — only for truly exceptional, unrecoverable situations
-- 6. 'error "..."' — BANNED. this is 'undefined' with a message. VIOLENCE.
-- 7. 'head []' — BANNED. partial functions are a MORAL FAILING.

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━��━━━━━━━━━━━━━━━━━━━━
-- Level 1: Make illegal states unrepresentable
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

-- ❌ BAD: representing traffic light as String
-- data Light = Light String  -- "red"? "green"? "banana"? who knows!

-- ✅ GOOD: illegal states are literally impossible to construct
data TrafficLight = Red | Yellow | Green
  deriving stock (Show, Eq, Enum, Bounded)

-- The type has exactly 3 inhabitants. No "banana" light is possible.
-- Your test suite just got smaller. You're welcome. uwu

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- Level 2: Maybe (computation might not produce a value)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

-- | Safe head. Returns 'Nothing' for empty lists.
-- Unlike 'Prelude.head' which CRASHES. With a RUNTIME ERROR.
-- In a "pure functional language." The irony writes itself.
--
-- ✨ TOTAL FUNCTION ✨
safeHead :: [a] -> Maybe a
safeHead []    = Nothing
safeHead (x:_) = Just x

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- Level 3: Either (computation might fail with a typed error)
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

-- | Domain error type. EVERY failure mode is enumerated in the type.
-- Pattern matching is exhaustive. You CANNOT forget to handle a case.
-- Java's checked exceptions WISH they were this clean.
data AppError
  = NotFound !ResourceId
  | Unauthorized !UserId
  | ValidationError !Text
  | RateLimited !NominalDiffTime  -- ^ retry after this many seconds
  deriving stock (Show, Eq)

newtype ResourceId = ResourceId Text deriving stock (Show, Eq)
newtype UserId     = UserId     Text deriving stock (Show, Eq)

-- | Parse a configuration value. Returns typed error on failure.
--
-- ✨ TOTAL ✨ ✨ PURE ✨
--
-- 'Either' is a Monad, so we can chain fallible operations with 'do':
parseConfig :: Text -> Either AppError Config
parseConfig raw = do
  port     <- parsePort raw    ?! ValidationError "invalid port"
  dbUrl    <- parseDbUrl raw   ?! ValidationError "invalid db url"
  logLevel <- parseLogLevel raw ?! ValidationError "invalid log level"
  pure Config{..}

-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
-- What's BANNED
-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

-- ❌ BANNED: error (runtime crash, no recovery)
-- badDivide x 0 = error "division by zero"
-- ^ congratulations, you've written C in Haskell

-- ❌ BANNED: head (partial function, crashes on [])
-- badFirst = head []  -- *** Exception: Prelude.head: empty list

-- ❌ BANNED: tail (partial function, crashes on [])
-- badRest = tail []   -- *** Exception: Prelude.tail: empty list

-- ❌ BANNED: !! (partial function, crashes on out-of-bounds)
-- badIndex = [1,2,3] !! 5  -- *** Exception: index too large

-- ❌ BANNED: fromJust (partial function, crashes on Nothing)
-- badUnwrap = fromJust Nothing  -- *** Exception: fromJust: Nothing

-- ✅ USE INSTEAD:
-- safeHead, Data.List.NonEmpty, Maybe, Either, pattern matching
-- if you need a value and might not have one, THE TYPE SAYS SO.
```

### Monadic Error Composition (The Elegant Way):

```haskell
-- | Chaining fallible operations with 'Either' Monad.
-- Each step can fail independently. Errors short-circuit.
-- No try-catch blocks. No invisible control flow.
-- Just the Monad bind (>>=) doing what it was born to do uwu ✨
--
-- ✨ PURE ✨ (despite chaining, this is still pure!)
processUser :: Text -> Either AppError UserSummary
processUser rawInput = do
  email   <- parseEmail rawInput           -- might fail: ValidationError
  userId  <- lookupUser email              -- might fail: NotFound
  perms   <- checkPermissions userId       -- might fail: Unauthorized
  profile <- loadProfile userId perms      -- might fail: NotFound
  pure (summarise profile)
-- If ANY step fails, the whole computation short-circuits to 'Left'.
-- No explicit if/then/else error checking at every step.
-- The Monad instance handles propagation AUTOMATICALLY.
-- This is why we stan Monads. uwu ✨

-- | With 'ExceptT' for effectful (IO) operations:
processUserIO :: Text -> ExceptT AppError IO UserSummary
processUserIO rawInput = do
  email   <- liftEither $ parseEmail rawInput
  userId  <- ExceptT $ lookupUserDb email    -- IO + Either
  perms   <- ExceptT $ checkPermsDb userId   -- IO + Either
  profile <- ExceptT $ loadProfileDb userId  -- IO + Either
  pure (summarise profile)
```

## No `String` — `Text` and `ByteString` Only

```haskell
-- | 'String' in Haskell is defined as:
-- @
-- type String = [Char]
-- @
-- That's a LINKED LIST of Unicode code points.
-- Each character is a separate heap allocation.
-- The word "hello" is FIVE CONS CELLS. Five pointers. Five indirections.
-- This is approximately 40 bytes for 5 characters.
-- In a packed UTF-8 encoding it would be 5 bytes.
-- That's an 8x overhead. For TEXT. In 2026.
--
-- 'String' exists because it was in the Haskell 98 report and
-- backwards compatibility is a prison sentence.
--
-- USE INSTEAD:
-- • 'Data.Text.Text' — for human-readable text (packed UTF-16)
-- • 'Data.Text.Lazy.Text' — for streaming/building large text
-- • 'Data.ByteString.ByteString' — for raw bytes (network, files)
-- • 'Data.ByteString.Lazy.ByteString' — for streaming raw bytes
--
-- With {-# LANGUAGE OverloadedStrings #-}, string literals
-- automatically become 'Text' or 'ByteString' as needed.
-- There is NO EXCUSE to use 'String'. uwu

import qualified Data.Text as T
import qualified Data.Text.IO as TIO
import qualified Data.ByteString as BS

-- ❌ BANNED: String anywhere in your API
-- greetBad :: String -> String
-- greetBad name = "Hello, " ++ name ++ "!"

-- ✅ CORRECT: Text everywhere
-- | Greet a user by name.
--
-- >>> greet "Homura"
-- "Hello, Homura!"
greet :: T.Text -> T.Text
greet name = "Hello, " <> name <> "!"
-- Note: (<>) on Text is O(n) concatenation. For building large
-- strings, use Data.Text.Builder or Data.Text.Lazy.Builder.
```

## IO: The Sin Bin (Keep It Microscopic)

```haskell
-- | The 'IO' monad is where purity goes to die.
-- Every 'IO' action is a confession: "I couldn't figure out
-- how to do this purely."
--
-- Your program should be:
--   1. A thin 'IO' shell that reads input and writes output
--   2. A MASSIVE pure core that does all computation
--
-- The pure core is testable, composable, parallelisable, and correct.
-- The IO shell is none of those things. Minimise it ruthlessly.
--
-- Architecture:
-- @
--   main :: IO ()
--   main = do
--     input  <- readInput          -- IO (impure, thin)
--     let result = process input   -- PURE (the real program!)
--     writeOutput result           -- IO (impure, thin)
-- @

-- ❌ BAD: IO everywhere (you've written Java in Haskell syntax)
processFileBad :: FilePath -> IO [Result]
processFileBad path = do
  contents <- TIO.readFile path           -- IO
  let linesOfText = T.lines contents       -- pure, but trapped in IO
  results <- forM linesOfText $ \line -> do  -- IO for no reason!
    let parsed = parseLine line             -- pure!
    let validated = validate parsed          -- pure!
    let transformed = transform validated   -- pure!
    pure transformed                        -- wrapping pure in IO (cringe)
  pure results

-- ✅ GOOD: pure core, thin IO shell
-- | Parse, validate, and transform a single line. PURE.
processLine :: T.Text -> Either AppError Result
processLine = transform <=< validate <=< parseLine
-- (<=<) is Kleisli composition. It's (.) for monadic functions.
-- If that blew your mind, welcome to Haskell. uwu ✨

-- | Read file and process all lines. IO shell is TWO lines.
processFile :: FilePath -> IO (Either AppError [Result])
processFile path = do
  contents <- TIO.readFile path
  pure . traverse processLine . T.lines $ contents
-- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-- This entire expression is PURE.
-- IO only touches 'readFile'. Everything else is a value.
```

## Concurrency (STM + Async — Fearless Concurrency, For Real This Time)

```haskell
-- | Haskell's concurrency story is UNMATCHED.
--
-- • Green threads (lightweight, millions of them, managed by the RTS)
-- • Software Transactional Memory (composable atomic transactions)
-- • async library (structured concurrency, easy forking/joining)
-- • No data races by default (purity means shared state is immutable!)
--
-- Rust claims "fearless concurrency." Haskell had it in 2005.
-- With STM. Which Rust still doesn't have. uwu
--
-- GHC 9.14.1 RTS: compile with -threaded, run with +RTS -N
-- This enables SMP parallelism across all cores.

import Control.Concurrent.STM
import Control.Concurrent.Async

-- | A concurrent counter using STM. No locks. No deadlocks.
-- Transactions compose. If a transaction retries, it's automatic.
-- If two transactions conflict, STM resolves it for you.
--
-- In C++/Java you'd need: mutex, lock_guard, condition_variable,
-- and you'd STILL have a race condition you'd find in prod at 3am.
newtype Counter = Counter (TVar Int)

-- | Create a new counter.
newCounter :: STM Counter
newCounter = Counter <$> newTVar 0

-- | Increment counter atomically.
-- This composes with other STM actions in the SAME transaction.
-- Composability is the killer feature. Locks don't compose.
increment :: Counter -> STM ()
increment (Counter var) = modifyTVar' var (+ 1)

-- | Read counter value atomically.
readCounter :: Counter -> STM Int
readCounter (Counter var) = readTVar var

-- | Transfer between two counters atomically.
-- BOTH the decrement and increment happen as ONE atomic operation.
-- No intermediate state is visible to other threads.
-- Try doing THIS with mutexes without a PhD in concurrency. uwu
transfer :: Counter -> Counter -> Int -> STM ()
transfer from to amount = do
  fromVal <- readCounter from
  when (fromVal < amount) retry  -- blocks until condition is met!
  modifyTVar' ((\(Counter v) -> v) from) (subtract amount)
  modifyTVar' ((\(Counter v) -> v) to)   (+ amount)

-- | Concurrent map using async (structured concurrency).
-- Fork one green thread per item, collect all results.
-- If any thread throws, the others are cancelled automatically.
concurrentMap :: (a -> IO b) -> [a] -> IO [b]
concurrentMap f = mapConcurrently f

-- | Run two IO actions in parallel, collect both results.
-- Structured concurrency: if either throws, both are cancelled.
fetchBoth :: IO a -> IO b -> IO (a, b)
fetchBoth = concurrently
-- That's it. One function. No thread pools, no executors,
-- no CompletableFuture, no Promise. Just 'concurrently'. uwu ✨
```

### GHC RTS Options for Parallelism:

```bash
# compile with threading support
ghc -threaded -rtsopts -O2 Main.hs

# run with N cores (auto-detect)
./Main +RTS -N -RTS

# run with exactly 4 cores
./Main +RTS -N4 -RTS

# run with 4 cores + 20ms context switch interval (default)
./Main +RTS -N4 -C0.02 -RTS

# run with eager blackholing (recommended for parallel code!)
# -feager-blackholing at COMPILE time avoids repeated computation
ghc -threaded -feager-blackholing -O2 Main.hs

# pin threads to cores for cache affinity
./Main +RTS -N4 -qa -RTS

# show GC and parallelism stats
./Main +RTS -N -s -RTS
```

## WebAssembly Backend (GHC 9.14.1 — Now With GHCi!)

```haskell
-- | GHC 9.14.1 brings INTERACTIVE WebAssembly support.
-- You can now run GHCi in the browser. With JavaScript FFI.
-- Including DOM manipulation. This is NOT a drill.
--
-- The wasm backend targets wasm32-wasi and supports:
-- • Self-contained wasm modules (no JS required)
-- • JavaScript FFI (call JS from Haskell and vice versa!)
-- • GHCi in the browser (interactive Haskell in wasm!)
-- • TemplateHaskell evaluation in wasm
--
-- Setup: follow ghc-wasm-meta instructions
-- Compiler: wasm32-wasi-ghc
-- Build:    wasm32-wasi-cabal build

-- JavaScript FFI example (from the GHC users guide):
{-# LANGUAGE ForeignFunctionInterface #-}

import GHC.Wasm.Prim

-- | Call console.log from Haskell. Because we can.
foreign import javascript unsafe "console.log($1)"
  js_print :: JSString -> IO ()

-- | Check if a JSVal is an object (synchronous FFI).
foreign import javascript unsafe "typeof $1 === 'object'"
  js_is_obj :: JSVal -> Bool

-- | Async sleep using JavaScript Promises (asynchronous FFI).
-- The Haskell thread suspends, other threads continue.
foreign import javascript safe "new Promise(res => setTimeout(res, $1))"
  js_sleep :: Int -> IO ()

-- | Fetch a URL asynchronously. Uses await!
foreign import javascript safe "const r = await fetch($1); return r.text();"
  js_fetch :: JSString -> IO JSString

-- | Export a Haskell function to JavaScript.
-- Callable as: await instance.exports.haskellFib(10)
foreign export javascript "haskellFib"
  fib :: Word -> Word

fib :: Word -> Word
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

-- Linking for wasm reactor module:
-- ghc -no-hs-main -optl-mexec-model=reactor -optl-Wl,--export=haskellFib

-- Post-linking (generates JS glue):
-- $(wasm32-wasi-ghc --print-libdir)/post-link.mjs -i hello.wasm -o hello.js
```

## Testing (Exhaustive Testing Is Praxis)

### Testing Philosophy:

```haskell
-- | Haskell testing has THREE pillars:
--
-- 1. THE TYPE SYSTEM (your primary test suite — if it compiles, it works)
-- 2. Property-based testing (QuickCheck/Hedgehog — fuzzing the universe)
-- 3. Example-based testing (Hspec/HUnit — for when you need specific cases)
--
-- Notice: Mockito is not listed. Neither is Moq. Neither is any mocking
-- framework. Because pure functions don't need mocking. You pass in the
-- dependency AS A FUNCTION. Higher-order functions ARE dependency injection.
-- Enterprise architects in shambles. uwu ✨

-- KEY PRINCIPLE:
-- If you need mocks, your architecture is wrong.
-- If you need integration tests for pure code, your code is impure.
-- If you need a debugger, you have too much IO.
-- Pure functions are TRIVIALLY testable. That's the whole point.
```

### The Test Framework Stack:

```haskell
-- ┌─────────────────────────────────────────────────────────┐
-- │  FRAMEWORK          │  ROLE            │  C++ EQUIVALENT │
-- ├─────────────────────┼──────────────────┼─────────────────┤
-- │  tasty              │  Test runner     │  Googletest      │
-- │  Hspec              │  BDD unit tests  │  Googletest      │
-- │  HUnit              │  Assertions      │  ASSERT_EQ       │
-- │  QuickCheck         │  Property tests  │  (nothing — C++  │
-- │                     ��                  │   doesn't have   │
-- │                     │                  │   this lmao)     │
-- │  Hedgehog           │  Property tests  │  (also nothing)  │
-- │  criterion          │  Benchmarks      │  Google Benchmark│
-- │  tasty-bench        │  Light bench     │  Google Benchmark│
-- │  hpc                │  Coverage        │  lcov            │
-- └─────────────────────┴──────────────────┴─────────────────┘

-- tasty is the STANDARD test runner. It aggregates:
--   • Unit tests (HUnit / Hspec)
--   • Property tests (QuickCheck / Hedgehog)
--   • Benchmarks (criterion / tasty-bench)
-- Into a single tree with CLI args, filtering, parallel execution.
```

### Hspec (BDD-Style Unit Tests):

```haskell
-- file: test/Vector/OpsSpec.hs
module Vector.OpsSpec (spec) where

import Test.Hspec
import Vector.Ops

spec :: Spec
spec = do
  describe "Vec2 addition" $ do
    it "is commutative: a + b ≡ b + a" $ do
      let a = Vec2 3.0 4.0
          b = Vec2 1.0 2.0
      add a b `shouldBe` add b a

    it "has zero as identity: v + zero ≡ v" $ do
      let v = Vec2 3.0 4.0
      add v zero `shouldBe` v
      add zero v `shouldBe` v

    it "has additive inverse: v + (-v) ≡ zero" $ do
      let v  = Vec2 3.0 4.0
          nv = Vec2 (-3.0) (-4.0)
      add v nv `shouldBe` zero

  describe "magnitude" $ do
    it "computes Pythagorean triples correctly" $ do
      magnitude (Vec2 3.0 4.0)  `shouldBe` 5.0
      magnitude (Vec2 5.0 12.0) `shouldBe` 13.0

    it "returns 0 for zero vector" $ do
      magnitude zero `shouldBe` 0.0

  describe "normalise" $ do
    it "returns Nothing for zero vector" $ do
      normalise zero `shouldBe` Nothing

    it "produces unit length vectors" $ do
      case normalise (Vec2 3.0 4.0) of
        Nothing -> expectationFailure "expected Just"
        Just v  -> magnitude v `shouldSatisfy` (\m -> abs (m - 1.0) < 1e-10)

  describe "error handling" $ do
    it "uses Maybe, not exceptions, because we're civilised" $ do
      -- we don't test for exceptions.
      -- we test that the types make crashes impossible.
      -- if it compiles and the tests pass, the code is correct.
      -- that's the Curry-Howard correspondence, bestie uwu ✨
      safeHead ([] :: [Int]) `shouldBe` Nothing
      safeHead [1,2,3]       `shouldBe` Just 1
```

### QuickCheck (Property-Based Testing — Fuzzing The Universe):

```haskell
-- | QuickCheck INVENTED property-based testing.
-- Haskell had this in 1999. Other languages got ports 15 years later.
--
-- Instead of writing specific examples (BORING), you write UNIVERSAL
-- PROPERTIES that must hold for ALL inputs. QuickCheck generates
-- hundreds of random inputs and checks them.
--
-- It's automated theorem proving for the working programmer.
-- It found bugs in your favourite library. uwu ✨

module Vector.OpsProperties (tests) where

import Test.Tasty
import Test.Tasty.QuickCheck as QC
import Vector.Ops

-- | Arbitrary instance for Vec2 (QuickCheck needs this to generate random vectors)
instance Arbitrary Vec2 where
  arbitrary = Vec2 <$> arbitrary <*> arbitrary
  shrink (Vec2 x y) = [Vec2 x' y' | (x', y') <- shrink (x, y)]

tests :: TestTree
tests = testGroup "Vec2 Properties (mathematical laws)"
  [ QC.testProperty "addition is commutative: ∀ a b. a + b ≡ b + a" $
      \a b -> add a b === add b a

  , QC.testProperty "addition is associative: ∀ a b c. (a + b) + c ≡ a + (b + c)" $
      \a b c -> add (add a b) c === add a (add b c)

  , QC.testProperty "zero is left identity: ∀ v. zero + v ≡ v" $
      \v -> add zero v === v

  , QC.testProperty "zero is right identity: ∀ v. v + zero ≡ v" $
      \v -> add v zero === v

  , QC.testProperty "magnitude is non-negative: ∀ v. |v| ≥ 0" $
      \v -> magnitude v >= 0.0

  , QC.testProperty "scaling law: ∀ k v. |k * v| ≈ |k| * |v|" $
      \(k :: Double) v ->
        let lhs = magnitude (scale k v)
            rhs = abs k * magnitude v
        in counterexample (show lhs ++ " /= " ++ show rhs) $
           abs (lhs - rhs) < 1e-6 * max 1.0 (abs rhs)

  , QC.testProperty "normalise produces unit vector (when not zero): ∀ v ≠ 0. |normalise v| ≈ 1" $
      \v -> magnitude v > 1e-10 ==>
        case normalise v of
          Nothing -> property False  -- should not happen for non-zero
          Just nv -> counterexample (show (magnitude nv)) $
                     abs (magnitude nv - 1.0) < 1e-10

  , QC.testProperty "Monoid left identity: mempty <> v ≡ v" $
      \v -> mempty <> v === v

  , QC.testProperty "Monoid right identity: v <> mempty ≡ v" $
      \v -> v <> mempty === v

  , QC.testProperty "Semigroup associativity: (a <> b) <> c ≡ a <> (b <> c)" $
      \a b c -> (a <> b) <> c === a <> (b <> c)
  ]

-- | These aren't unit tests. These are THEOREMS.
-- QuickCheck is checking them with hundreds of random witnesses.
-- If a property fails, QuickCheck SHRINKS the counterexample to
-- the smallest failing case. This is why Haskell developers find
-- bugs before production and imperative developers find them IN
-- production. uwu ✨
```

### Hedgehog (The Modern Alternative To QuickCheck):

```haskell
-- | Hedgehog is the newer property-based testing library.
-- Differences from QuickCheck:
--   • Integrated shrinking (no separate Arbitrary/Shrink instances)
--   • Better error messages (shows shrink steps)
--   • Range-based generators (explicit bounds)
--
-- Use Hedgehog OR QuickCheck. Both are excellent.
-- But use AT LEAST ONE. Property tests are NOT optional. uwu

module Vector.HedgehogProperties (tests) where

import Hedgehog
import qualified Hedgehog.Gen as Gen
import qualified Hedgehog.Range as Range
import Test.Tasty
import Test.Tasty.Hedgehog
import Vector.Ops

genVec2 :: Gen Vec2
genVec2 = Vec2
  <$> Gen.double (Range.linearFrac (-1000.0) 1000.0)
  <*> Gen.double (Range.linearFrac (-1000.0) 1000.0)

tests :: TestTree
tests = testGroup "Vec2 Hedgehog Properties"
  [ testProperty "addition commutativity" $ property $ do
      a <- forAll genVec2
      b <- forAll genVec2
      add a b === add b a

  , testProperty "dot product is bilinear" $ property $ do
      a <- forAll genVec2
      b <- forAll genVec2
      k <- forAll $ Gen.double (Range.linearFrac (-100.0) 100.0)
      -- dot(k*a, b) ≈ k * dot(a, b)
      let lhs = dot (scale k a) b
          rhs = k * dot a b
      diff lhs (\x y -> abs (x - y) < 1e-6 * max 1.0 (abs y)) rhs
  ]
```

### Test Runner (tasty — The One Runner To Rule Them All):

```haskell
-- file: test/Main.hs
module Main (main) where

import Test.Tasty
import qualified Vector.OpsSpec as Spec
import qualified Vector.OpsProperties as Props
import qualified Vector.HedgehogProperties as HProps

-- | Main test entry point. tasty aggregates everything.
-- Run with: cabal test --test-show-details=direct
main :: IO ()
main = defaultMain $ testGroup "All Tests"
  [ testGroup "Hspec (example-based)" [Spec.tests]
  , Props.tests     -- QuickCheck properties
  , HProps.tests    -- Hedgehog properties
  ]
-- One command. All tests. Property tests and unit tests together.
-- tasty handles parallelism, filtering, output formatting.
-- No XML configuration files. No build system plugins.
-- Just a Haskell program that runs tests. uwu ✨
```

## Benchmarking (criterion / tasty-bench)

### criterion (The Gold Standard):

```haskell
-- | criterion uses sophisticated statistics (bootstrapping, kernel
-- density estimation, linear regression) to give you ACCURATE
-- performance numbers. It generates HTML reports with confidence
-- intervals. Google Benchmark's console output is cute by comparison.
--
-- Run with: cabal bench

module Main (main) where

import Criterion.Main
import qualified Data.Text as T
import Vector.Ops

main :: IO ()
main = defaultMain
  [ bgroup "Vec2 operations"
    [ bench "add"       $ whnf (add (Vec2 3.0 4.0)) (Vec2 1.0 2.0)
    , bench "dot"       $ whnf (dot (Vec2 3.0 4.0)) (Vec2 1.0 2.0)
    , bench "magnitude" $ whnf magnitude (Vec2 3.0 4.0)
    , bench "normalise" $ whnf normalise (Vec2 3.0 4.0)
    ]
  , bgroup "sumVectors"
    [ bench "100 vectors"    $ whnf sumVectors (replicate 100 (Vec2 1.0 1.0))
    , bench "10000 vectors"  $ whnf sumVectors (replicate 10000 (Vec2 1.0 1.0))
    , bench "1000000 vectors" $ whnf sumVectors (replicate 1000000 (Vec2 1.0 1.0))
    ]
  , bgroup "Text vs String (why String is banned)"
    [ bench "Text concat 1000"   $ whnf (T.replicate 1000) "hello"
    , bench "String concat 1000" $ whnf (concat . replicate 1000) ("hello" :: String)
    -- ^ String will be dramatically slower. DRAMATICALLY.
    -- This is why we ban it. Not out of pedantry. Out of RESPECT
    -- for the CPU cache. uwu ✨
    ]
  ]

-- Generate HTML report:
-- cabal bench --benchmark-options="--output bench.html"
```

### tasty-bench (Lightweight Alternative):

```haskell
-- | tasty-bench is API-compatible with criterion but integrates
-- natively into the tasty test runner. Same benchmarks, less overhead.
-- Use this when you want tests AND benchmarks in the same binary.

import Test.Tasty.Bench

benchmarks :: [Benchmark]
benchmarks =
  [ bench "add" $ whnf (add (Vec2 3.0 4.0)) (Vec2 1.0 2.0)
  , bench "magnitude" $ whnf magnitude (Vec2 3.0 4.0)
  , bgroup "scaling"
    [ bench "100"   $ whnf sumVectors (replicate 100 (Vec2 1.0 1.0))
    , bench "10000" $ whnf sumVectors (replicate 10000 (Vec2 1.0 1.0))
    ]
  ]
```

## Code Coverage (hpc — Built Into GHC)

```bash
# GHC has code coverage BUILT IN. No external tools needed.
# This is hpc (Haskell Program Coverage).

# Step 1: compile with -fhpc flag
cabal test --enable-coverage

# Step 2: GHC generates .tix files when the program runs
# (automatically during cabal test)

# Step 3: generate HTML coverage report
hpc report dist-newstyle/**/*.tix
hpc markup dist-newstyle/**/*.tix --destdir=coverage-html

# Step 4: for CI integration (Codecov.io, Coveralls, etc.)
# convert to LCOV format using hpc-codecov:
cabal install hpc-codecov
hpc-codecov dist-newstyle/**/*.tix -o lcov.info

# upload to Codecov:
# codecov -f lcov.info

# GHC 9.14.1 improvement: -fhpc now treats record field access
# via RecordWildCards and NamedFieldPuns as covered! (#17834)
```

## Documentation (Haddock — The Only Acceptable Documentation Tool)

```haskell
-- | Haddock is the Haskell documentation generator.
-- It understands Haskell's module system DEEPLY.
-- It auto-hyperlinks types and functions across ALL packages.
-- Clicking 'Text' in YOUR docs takes you to the official Text
-- documentation on Hackage. AUTOMATICALLY.
--
-- Doxygen WISHES it could do this. uwu

-- Haddock comment styles:

-- | Documentation for the NEXT declaration (most common)
-- Use this for functions, types, type classes, etc.
greet :: T.Text -> T.Text
greet name = "Hello, " <> name <> "!"

-- ^ Documentation for the PREVIOUS declaration
-- Use this for record fields and function arguments

data Config = Config
  { configPort :: !Int       -- ^ Port to listen on (default: 8080)
  , configHost :: !T.Text    -- ^ Hostname to bind to
  , configDb   :: !T.Text    -- ^ Database connection string
  }

-- | Module-level documentation goes at the top:
-- @
-- Module      : Vector.Ops
-- Description : Pure functional operations on 2D vectors
-- Copyright   : (c) LukeFrankio, 2026
-- License     : MIT
-- Maintainer  : luke@example.com
-- Stability   : experimental
-- Portability : GHC 9.14.1+
--
-- This module provides pure, total functions for 2D vector arithmetic.
-- All functions are referentially transparent and obey the algebraic
-- laws of vector spaces (commutativity, associativity, distributivity).
-- @

-- Haddock supports:
-- • Code examples: @add (Vec2 1 2) (Vec2 3 4)@
-- • Code blocks:   surround with @...@ or use bird tracks (>)
-- • Links:         'functionName', "Module.Name", <http://url>
-- • Lists:         * item, 1. numbered item
-- • Emphasis:      /emphasis/, __bold__
-- • Math:          \( x^2 + y^2 = r^2 \)  (LaTeX-style)

-- Generate docs:
-- cabal haddock --haddock-hyperlink-source
```

## Build System (Cabal — The Modern Way)

### `cabal` is the build tool. Period.

```haskell
-- | Haskell's build ecosystem:
--
-- The File:    .cabal file (declarative package description)
-- The Tool:    cabal-install (v2-build, dependency resolution, compilation)
-- The Repo:    Hackage (central package repository, like PyPI/npm)
-- The Curated: Stackage (curated Hackage subset, all packages build together)
--
-- You do NOT need CMake. You do NOT need Make. You do NOT need Ninja.
-- cabal handles the dependency graph, caching, parallel builds, and
-- incremental compilation natively. It's a real build system written
-- by people who understand dependency resolution.
--
-- Stack also exists. It uses Stackage snapshots for reproducibility.
-- Both are acceptable. cabal is preferred in this codebase.
-- Nix flakes are ENCOURAGED for hermetic builds.
--
-- Maven XML? Gradle Groovy? CMakeLists.txt? We don't do that here. uwu
```

### The `.cabal` File (Your Package Manifest):

```cabal
cabal-version:   3.0
name:            functional-haskell-project
version:         0.1.0.0
synopsis:        A mathematically correct Haskell project uwu
description:
  A project demonstrating pure functional programming in Haskell.
  Every function is total, every type is a proposition, every program
  is a proof. Imperative peasants need not apply. ✨

license:         MIT
license-file:    LICENSE
author:          LukeFrankio
maintainer:      luke@example.com
category:        Math
build-type:      Simple
tested-with:     GHC == 9.14.1

-- ================================================================
-- Common stanzas (shared configuration — DRY principle)
-- ================================================================

common warnings
  ghc-options:
    -Wall
    -Wextra
    -Wcompat
    -Wincomplete-record-updates
    -Wincomplete-uni-patterns
    -Wredundant-constraints
    -Wmissing-export-lists
    -Wmissing-deriving-strategies
    -Wunused-packages
    -Werror
    -- GHC 9.14.1 new warnings we want:
    -Wincomplete-record-selectors
    -Wuseless-specialisations

common extensions
  default-extensions:
    OverloadedStrings
    LambdaCase
    ViewPatterns
    DerivingVia
    DerivingStrategies
    StrictData
    TypeApplications
    ScopedTypeVariables
    GADTs
    DataKinds
    TypeFamilies
    BlockArguments
    NumericUnderscores

common lang
  default-language: GHC2021
  -- GHC2021 enables a sane set of extensions by default:
  --   BangPatterns, BinaryLiterals, ConstrainedClassMethods,
  --   ConstraintKinds, DeriveDataTypeable, DeriveFoldable,
  --   DeriveFunctor, DeriveGeneric, DeriveLift, DeriveTraversable,
  --   DoAndIfThenElse, EmptyCase, EmptyDataDecls, EmptyDataDeriving,
  --   ExistentialQuantification, ExplicitForAll, FlexibleContexts,
  --   FlexibleInstances, ForeignFunctionInterface,
  --   GADTSyntax, GeneralizedNewtypeDeriving, HexFloatLiterals,
  --   ImportQualifiedPost, InstanceSigs, KindSignatures,
  --   MultiParamTypeClasses, NamedFieldPuns, NamedWildCards,
  --   NumericUnderscores, PatternGuards, PolyKinds, PostfixOperators,
  --   RankNTypes, ScopedTypeVariables, StandaloneDeriving,
  --   StandaloneKindSignatures, StarIsType, TraditionalRecordSyntax,
  --   TupleSections, TypeApplications, TypeOperators,
  --   TypeSynonymInstances
  -- That's RIGHT. GHC2021 enables 40+ extensions by default.
  -- Because Haskell 2010 is ancient history. uwu

-- ================================================================
-- Library (the pure core — where 99% of your code lives)
-- ================================================================

library
  import:           warnings, extensions, lang
  hs-source-dirs:   src
  exposed-modules:
    Vector.Ops
    Vector.Types
    Data.Result
    App.Config
    App.Error
  build-depends:
    -- ============================================================
    -- DEPENDENCIES: MINIMAL (every dependency is tech debt)
    -- ============================================================
    -- base is the standard library. Everyone depends on it.
      base          >= 4.21   && < 5
    -- text: packed UTF-16 text (String is BANNED remember)
    , text          >= 2.1    && < 2.2
    -- bytestring: raw bytes for I/O, network, files
    , bytestring    >= 0.12   && < 0.13
    -- containers: Map, Set, IntMap (pure, persistent data structures)
    , containers    >= 0.7    && < 0.8
    -- stm: Software Transactional Memory (fearless concurrency)
    , stm           >= 2.5    && < 2.6
    -- async: structured concurrency (concurrently, mapConcurrently)
    , async         >= 2.2    && < 2.3
    -- ============================================================
    -- BANNED DEPENDENCIES:
    -- ============================================================
    -- ❌ lens (200+ transitive deps, learn optics instead)
    -- ❌ mtl (use concrete transformer stacks or effects libraries)
    -- ❌ string-conversions (stop using String)
    -- ❌ safe (just don't use partial functions in the first place)
    -- ❌ universum / relude (custom preludes are team disagreements)
    --
    -- Every dependency you add is a trust decision, a compile time
    -- penalty, and a future upgrade burden. Think HARD before adding
    -- one. If base provides it, USE base. uwu
    -- ============================================================

-- ================================================================
-- Executable (the thin IO shell — kept microscopic)
-- ================================================================

executable functional-haskell
  import:           warnings, extensions, lang
  hs-source-dirs:   app
  main-is:          Main.hs
  build-depends:
      base          >= 4.21 && < 5
    , functional-haskell-project
  ghc-options:
    -threaded
    -rtsopts
    "-with-rtsopts=-N"
    -O2

-- ================================================================
-- Test suite (exhaustive testing is non-negotiable)
-- ================================================================

test-suite functional-haskell-test
  import:           warnings, extensions, lang
  type:             exitcode-stdio-1.0
  hs-source-dirs:   test
  main-is:          Main.hs
  other-modules:
    Vector.OpsSpec
    Vector.OpsProperties
  build-depends:
      base              >= 4.21 && < 5
    , functional-haskell-project
    -- test runner (aggregates everything)
    , tasty             >= 1.5  && < 1.6
    -- tasty providers
    , tasty-hunit       >= 0.10 && < 0.11
    , tasty-quickcheck  >= 0.11 && < 0.12
    , tasty-hedgehog    >= 1.4  && < 1.5
    -- BDD-style tests
    , hspec             >= 2.11 && < 2.12
    -- property-based testing
    , QuickCheck        >= 2.15 && < 2.16
    , hedgehog          >= 1.5  && < 1.6
    -- ============================================================
    -- BANNED TEST DEPENDENCIES:
    -- ============================================================
    -- ❌ HMock (mocking means your architecture is wrong)
    -- ❌ hspec-discover (magic, prefer explicit test registration)
    -- If you need mocks, you have too much IO in your pure code.
    -- Refactor until your core is pure, then test it directly. uwu
    -- ============================================================
  ghc-options:
    -threaded
    -rtsopts
    "-with-rtsopts=-N"

-- ================================================================
-- Benchmark suite (performance is not optional)
-- ================================================================

benchmark functional-haskell-bench
  import:           warnings, extensions, lang
  type:             exitcode-stdio-1.0
  hs-source-dirs:   bench
  main-is:          Main.hs
  build-depends:
      base              >= 4.21 && < 5
    , functional-haskell-project
    -- criterion: gold standard benchmarking with statistical rigour
    , criterion         >= 1.6  && < 1.7
    -- OR tasty-bench for lightweight benchmarks in the test runner:
    -- , tasty-bench     >= 0.4  && < 0.5
  ghc-options:
    -threaded
    -rtsopts
    -O2
```

### The `cabal.project` File (Multi-Package Configuration):

```cabal
-- cabal.project
-- Project-level configuration. Like .cabal but for the whole workspace.

-- all local packages
packages: .

-- optimisation for all local packages
program-options
  ghc-options: -O2

-- reproducible builds: pin an index state
-- index-state: 2026-02-15T00:00:00Z

-- allow GHC 9.14.1 preview features if needed
-- program-options
--   ghc-options: --enable-preview
```

### Common `cabal` Commands:

```bash
# build everything
cabal build all

# run the executable
cabal run functional-haskell

# run tests (with detailed output)
cabal test --test-show-details=direct

# run benchmarks (with HTML report)
cabal bench --benchmark-options="--output bench.html"

# generate documentation
cabal haddock --haddock-hyperlink-source

# open documentation in browser
cabal haddock --open

# run coverage
cabal test --enable-coverage
hpc markup dist-newstyle/**/*.tix --destdir=coverage-html

# start a REPL with your library loaded
cabal repl

# update package index from Hackage
cabal update

# add a dependency (edit .cabal, then)
cabal build

# clean build artifacts
cabal clean

# generate dependency bounds from Stackage snapshot
# (if you want Stackage-compatible bounds)
cabal gen-bounds

# freeze dependencies for reproducibility
cabal freeze
```

## Low-Level Build Orchestration (Shake — When You Need More)

```haskell
-- | For 99% of Haskell projects, cabal is sufficient.
-- It handles the dependency graph, caching, parallel builds (-j).
--
-- But sometimes you need a scriptable build system:
-- • "Build this C file, then generate this header, then compile Haskell"
-- • "Run code generation, then compile, then run post-processing"
-- • "Custom build rules with complex dependency tracking"
--
-- For this, Haskell has Shake.
--
-- Shake is a BUILD SYSTEM LIBRARY written in Haskell.
-- You write your build rules IN HASKELL. Not in YAML. Not in XML.
-- Not in some DSL that's almost-but-not-quite a real language.
-- In Haskell. With types. And error messages. And IDE support.
--
-- Shake is often cited as "Make done right." It's more powerful than
-- Ninja because your build rules can use ANY Haskell library.
-- (Ninja was actually inspired by Shake's design principles.)
--
-- For most projects: use cabal. For complex builds: use Shake. uwu

-- Shakefile.hs example:
-- import Development.Shake
-- import Development.Shake.FilePath
--
-- main :: IO ()
-- main = shakeArgs shakeOptions $ do
--   want ["_build/Main" <.> exe]
--
--   "_build/Main" <.> exe %> \out -> do
--     srcs <- getDirectoryFiles "src" ["//*.hs"]
--     need (map ("src" </>) srcs)
--     cmd "cabal" "build"
--
--   "_build/generated//*.hs" %> \out -> do
--     let src = "schema" </> dropDirectory1 (dropDirectory1 out) -<.> "json"
--     need [src]
--     cmd "codegen" src "-o" out
```

## Package Management (Hackage & Stackage)

```haskell
-- | The Haskell package ecosystem:
--
-- ┌────────────────────────────────────────────────────────────┐
-- │  COMPONENT      │  ROLE              │  C++ EQUIVALENT     │
-- ├────────────────────────────────────────────────────────────┤
-- │  Hackage        │  Central repo      │  vcpkg / Conan      │
-- │  Stackage       │  Curated subset    │  (nothing lmao)     │
-- │  cabal-install  │  Build tool        │  CMake + Ninja       │
-- │  Stack          │  Alt build tool    │  CMake + Ninja       │
-- │  Nix            │  Hermetic builds   │  (nothing, cope)     │
-- │  pkg-config     │  C lib discovery   │  pkg-config (same!)  │
-- └────────────────────────────────────────────────────────────┘
--
-- Hackage: https://hackage.haskell.org
--   The central community package repository. ~17,000+ packages.
--   Upload your own: cabal upload
--   Every package has auto-generated Haddock docs.
--   Versions follow the Package Versioning Policy (PVP).
--
-- Stackage: https://www.stackage.org
--   A CURATED subset of Hackage where ALL packages in a snapshot
--   are guaranteed to build together. No dependency hell.
--   This is what other ecosystems wish they had.
--   C++ developers spending 4 hours on vcpkg conflicts: weep. uwu
--
-- Native C Dependencies:
--   If you need a C library (e.g., libpng, libssl, zlib):
--   • System package manager: apt install libpng-dev / brew install libpng
--   • cabal uses pkg-config to discover C libraries automatically
--   • Add pkgconfig-depends: libpng in your .cabal file
--   • For HERMETIC builds: use Nix flakes to manage BOTH Haskell
--     and C/C++ dependencies in a single lockfile. Nix is increasingly
--     the standard for serious Haskell projects.

-- Nix flake example (hermetic, reproducible, correct):
-- {
--   inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
--   outputs = { self, nixpkgs }:
--     let pkgs = nixpkgs.legacyPackages.x86_64-linux;
--     in {
--       devShells.x86_64-linux.default = pkgs.mkShell {
--         buildInputs = [
--           pkgs.haskell.compiler.ghc9141
--           pkgs.cabal-install
--           pkgs.haskellPackages.haskell-language-server
--           pkgs.pkg-config
--           pkgs.zlib            -- C dependency, managed by Nix!
--           pkgs.ormolu          -- formatter (the ONLY acceptable one)
--         ];
--       };
--     };
-- }
```

## Formatting (ormolu / Fourmolu — The Only Acceptable Formatters)

```bash
# ormolu is the opinionated Haskell formatter.
# It has ZERO configuration options (by design).
# There are no style debates. There is only ormolu.
#
# Fourmolu is a fork with a few extra options.
# Both are acceptable. Pick one for the project and ENFORCE it.
#
# Formatters that are BANNED:
# ❌ hindent (abandoned, inconsistent)
# ❌ stylish-haskell (import sorting only, not a real formatter)
# ❌ brittany (abandoned)
# ❌ no formatter at all (chaos, bikeshedding, despair)

# install
cabal install ormolu

# format a file
ormolu --mode inplace MyModule.hs

# format everything
find src test app -name '*.hs' -exec ormolu --mode inplace {} +

# check formatting in CI (fails if not formatted)
ormolu --mode check MyModule.hs

# ormolu enforces:
# • consistent indentation (2 spaces)
# • import sorting and grouping
# • consistent let/where layout
# • consistent record syntax
# ��� no trailing whitespace
# • consistent blank lines
#
# You don't get to have opinions about formatting.
# ormolu has opinions FOR you. This is freedom. uwu ✨
```

## GHC Optimisation Flags (Making It Go Fast)

```bash
# GHC has a sophisticated optimisation pipeline.
# Here's what the -O flags actually mean:

# -O0: no optimisation (fast compilation, slow code)
#   Use during development for fast feedback loops

# -O / -O1: good optimisation (recommended for most builds)
#   Enables: constant folding, case merging, float-in, float-out,
#   CSE, specialisation, strictness analysis, worker/wrapper,
#   inlining, call-arity analysis, exitification, CPR analysis,
#   loopification, STG CSE, and more

# -O2: aggressive optimisation (recommended for production)
#   Adds: spec-constr (call-pattern specialisation),
#   liberate-case, asm-shortcutting, STG lambda lifting,
#   dict-strict, late demand analysis

# Individual flags for MAXIMUM PERFORMANCE:
ghc -O2 \
    -fspecialise-aggressively \     # specialise ALL overloaded calls
    -fexpose-all-unfoldings \       # allow cross-module inlining of everything
    -flate-specialise \             # extra specialisation pass (catches more)
    -flate-dmd-anal \               # extra demand analysis (finds more strictness)
    -fstatic-argument-transformation \  # optimise recursive functions
    -funbox-strict-fields \         # unpack ALL strict fields (sledgehammer)
    -feager-blackholing \           # avoid repeated computation in parallel code
    -fspec-constr-count=6 \         # more call-pattern specialisations
    Main.hs

# GHC 9.14.1 specific:
# -fspec-eval is ON by default (speculative evaluation, fewer allocations)
# -fspec-eval-dictfun is ON by default (strict dict functions)
# These are usually beneficial. Disable only if you measure regression.

# LLVM backend for MAXIMUM machine code quality:
ghc -O2 -fllvm -optlo-O3 Main.hs
# Requires LLVM to be installed. Produces better code than NCG
# for tight numeric loops. Not always faster for general code.

# View what -O actually enables:
# ghc -O -v MyModule.hs 2>&1 | grep "enabled"
```

## Project Directory Structure

```text
functional-haskell-project/
├── functional-haskell-project.cabal  <- the ONE build file (declarative, typed)
├── cabal.project                     <- project-level config
├── cabal.project.freeze              <- pinned dependency versions (reproducibility!)
├── flake.nix                         <- Nix flake (hermetic builds, encouraged)
├── flake.lock                        <- Nix lockfile
├── fourmolu.yaml                     <- formatter config (if using Fourmolu)
├── .ghcid                            <- ghcid config (rapid feedback loop)
├── app/
│   └── Main.hs                       <- entry point (THIN IO shell, ~20 lines)
├── src/
│   ├── Vector/
│   │   ├── Ops.hs                    <- pure vector operations
│   │   └── Types.hs                  <- Vec2, newtypes, Monoid instances
│   ├── Data/
│   │   └── Result.hs                 <- Either-based error handling utilities
│   └── App/
│       ├── Config.hs                 <- configuration parsing (pure!)
│       └── Error.hs                  <- domain error ADT
├── test/
│   ├── Main.hs                       <- tasty test runner entry point
│   └── Vector/
│       ├── OpsSpec.hs                <- Hspec example-based tests
│       └── OpsProperties.hs          <- QuickCheck/Hedgehog property tests
├── bench/
│   └── Main.hs                       <- criterion benchmarks
└── README.md                         <- documentation (excessive uwu)
```

## Anti-Patterns to AVOID (Imperative Haskell Is Violence)

### ❌ BAD: Using `String` (Linked List of Chars)

```haskell
-- ❌ CRINGE (String is [Char] — a linked list of Unicode code points)
greetBad :: String -> String
greetBad name = "Hello, " ++ name ++ "!"
-- Each character is a separate heap allocation.
-- "Hello" is 5 cons cells, 5 pointers, ~40 bytes.
-- Text "Hello" is ~10 bytes. 4x memory, 10x slower. WHY.

-- ✅ BASED (Text — packed UTF-16, cache-friendly, fast)
greet :: Text -> Text
greet name = "Hello, " <> name <> "!"
-- {-# LANGUAGE OverloadedStrings #-} makes literals Text.
-- There is no excuse. uwu ✨
```

### ❌ BAD: Partial Functions (Runtime Crashes In A "Safe" Language)

```haskell
-- ❌ CRINGE (head crashes on empty list — partial function violence)
firstElement :: [a] -> a
firstElement xs = head xs
-- head [] throws: *** Exception: Prelude.head: empty list
-- in a language with a type system capable of PREVENTING this.
-- using head is a CHOICE to ignore the type system. a BAD choice.

-- ✅ BASED (total function — impossible to crash)
firstElement :: [a] -> Maybe a
firstElement []    = Nothing
firstElement (x:_) = Just x
-- or even better: use Data.List.NonEmpty if you KNOW it's non-empty

-- ❌ CRINGE (!! crashes on out-of-bounds)
-- getThird xs = xs !! 2

-- ✅ BASED
getThird :: [a] -> Maybe a
getThird (_:_:x:_) = Just x
getThird _         = Nothing

-- ❌ CRINGE (fromJust crashes on Nothing — defeating Maybe's purpose)
-- unsafeGet = fromJust maybeValue

-- ✅ BASED (pattern match or use maybe/fromMaybe)
safeGet :: Maybe a -> a -> a
safeGet = flip fromMaybe
```

### ❌ BAD: `error` and `undefined` (The `goto` of Haskell)

```haskell
-- ❌ CRINGE (error is a runtime crash with a string message)
divide :: Double -> Double -> Double
divide _ 0 = error "division by zero"
divide a b = a / b
-- "but it compiles!" yes, 'undefined' also compiles.
-- compiling is not the bar. TOTALITY is the bar.
-- if your function can crash, it's LYING about its type.

-- ✅ BASED (encode failure in the type — honest types)
divide :: Double -> Double -> Either Text Double
divide _ 0 = Left "division by zero (mathematics says no)"
divide a b = Right (a / b)
-- the type signature TELLS you it can fail.
-- the caller MUST handle the failure case.
-- no surprises. no runtime crashes. no 3am pager alerts.
-- just honest types. uwu ✨

-- ❌ BANNED IN ALL CIRCUMSTANCES:
-- error "..."       -- runtime crash, unrecoverable
-- undefined         -- bottom, instant crash (only for development stubs!)
-- throw / throwIO   -- only in genuinely exceptional IO situations
-- unsafePerformIO   -- breaks referential transparency (WAR CRIME)
-- unsafeCoerce      -- breaks type safety (CAPITAL OFFENSE)
```

### ❌ BAD: Imperative Style (For Loops In Haskell)

```haskell
-- ❌ CRINGE (imperative loop using IORef — you've written Java)
sumListBad :: [Int] -> IO Int
sumListBad xs = do
  ref <- newIORef 0
  forM_ xs $ \x ->
    modifyIORef' ref (+ x)
  readIORef ref
-- This is in IO. For ADDITION. Of INTEGERS.
-- You've made addition impure. In Haskell.
-- The type theory gods are WEEPING.

-- ✅ BASED (pure fold — one line, no IO, no mutation)
sumList :: [Int] -> Int
sumList = foldl' (+) 0
-- or even: sumList = getSum . foldMap Sum
-- same inputs, same outputs, forever. referential transparency.
-- parallelisable. cacheable. testable. CORRECT. uwu ✨
```

### ❌ BAD: Deep Monad Transformer Stacks (Abstraction Astronautics)

```haskell
-- ❌ CRINGE (tower of monad transformers — unreadable, slow)
type AppM a = ReaderT Config (StateT AppState (ExceptT AppError (LoggingT IO))) a
-- FOUR transformers deep. Each layer of wrapping/unwrapping has runtime cost.
-- Error messages from type mismatches are INCOMPREHENSIBLE.
-- Ordering of transformers matters and it's easy to get wrong.

-- ✅ BASED (concrete monad with the effects you need)
newtype AppM a = AppM { runAppM :: ReaderT AppEnv IO a }
  deriving newtype (Functor, Applicative, Monad, MonadIO, MonadReader AppEnv)

data AppEnv = AppEnv
  { envConfig :: !Config
  , envLogger :: !(Text -> IO ())
  }
-- One transformer. Clear. Fast. Explicit.
-- Use 'Either' for errors. Use 'IORef'/'TVar' for state.
-- Don't stack transformers when you can avoid it.
-- Or use an algebraic effects library (effectful, polysemy) if
-- you truly need complex effect management. uwu
```

## The Cope Hierarchy (The Objective Truth)

```text
Haskell (supreme — pure, typed, proven correct by construction)
  > Idris / Agda (dependent types, but less practical)
    > OCaml (ML family, impure but fast, no higher-kinded types)
      > Scala (functional-ish on JVM, better than Java at least)
        > Rust (good type system but no HKTs, borrow checker violence)
          > Kotlin (Java but less painful, still OOP-brained)
            > Java 26 Preview (functional if you FORCE it — cope)
              > C++ (fast but type system is held together by templates and prayers)
                > Python (no types, no safety, vibes-based programming)
                  > JavaScript (the type system is a suggestion and the suggestion is wrong)
                    > Go (no generics until 2022, no sum types ever, Google's COBOL)
```

## GHC Warnings Reference (What We Enable And Why)

```haskell
-- | We enable these warnings because CORRECTNESS IS NON-NEGOTIABLE.
--
-- -Wall: all standard warnings (incomplete patterns, unused binds, etc.)
--   This catches 80% of bugs at compile time.
--
-- -Wextra: additional warnings (unused imports, dodgy imports, etc.)
--   More aggressive, occasionally noisy, but worth it.
--
-- -Wcompat: future-compatibility warnings
--   Currently enables: -Wcompat-unqualified-imports,
--   -Wimplicit-rhs-quantification, -Wdeprecated-type-abstractions
--   Keeps your code forward-compatible with future GHC versions.
--
-- -Wincomplete-record-updates: warn about partial record updates
--   If updating a record field could crash, WE WANT TO KNOW.
--
-- -Wincomplete-uni-patterns: warn about partial lambda/let patterns
--   \(Just x) -> x  can crash. The type system should prevent this.
--
-- -Wredundant-constraints: warn about unnecessary class constraints
--   f :: Eq a => a -> a -> Bool; f x y = True
--   The Eq constraint is unused. Remove it.
--
-- -Wmissing-export-lists: warn about modules without explicit exports
--   Explicit exports enable dead code analysis and prevent
--   accidental exposure of internal functions.
--
-- -Wmissing-deriving-strategies: warn about ambiguous deriving
--   deriving (Eq) — is that stock? newtype? anyclass?
--   Be EXPLICIT. deriving stock (Eq).
--
-- -Wunused-packages: warn about unnecessary dependencies in .cabal
--   Every unused dependency is tech debt. Remove it.
--
-- -Werror: ALL warnings are ERRORS.
--   If it warns, it doesn't compile. Zero tolerance policy.
--   This is not harsh. This is CORRECT. uwu ✨
--
-- GHC 9.14.1 new warnings we also enable:
-- -Wincomplete-record-selectors: now in -Wall! warns about partial
--   record selectors (more important than missing patterns!)
-- -Wuseless-specialisations: warns when SPECIALISE pragmas are no-ops
-- -Wunusable-unpack-pragmas: warns when UNPACK can't actually unpack
```

## Quality Checklist

- [ ] **GHC 9.14.1+** (latest stable, no older versions)
- [ ] **GHC2021** as `default-language` in `.cabal`
- [ ] **OverloadedStrings** enabled (no `String`, only `Text`/`ByteString`)
- [ ] **-Wall -Wextra -Werror** in all components
- [ ] **newtypes** for all domain types (no raw `Int`/`Bool`/`Text`)
- [ ] **algebraic data types** for domain modelling (sum + product types)
- [ ] **pattern matching** exhaustive everywhere (compiler-checked!)
- [ ] **NO partial functions** (`head`, `tail`, `!!`, `fromJust` — BANNED)
- [ ] **NO `error` or `undefined`** (use `Maybe`/`Either`)
- [ ] **NO `String`** (use `Text` or `ByteString`)
- [ ] **NO mutable state** in pure code (IO is the sin bin)
- [ ] **point-free style** where readable (`.` and `$` over parens)
- [ ] **`foldl'`** not `foldl` (strict left fold to avoid space leaks)
- [ ] **`Text`** imported qualified (`import qualified Data.Text as T`)
- [ ] **Haddock comments** on ALL exported functions and types
- [ ] **QuickCheck/Hedgehog** property tests for algebraic laws
- [ ] **Hspec** example tests for specific behaviour
- [ ] **criterion/tasty-bench** benchmarks for hot paths
- [ ] **hpc** coverage report generated in CI
- [ ] **ormolu/Fourmolu** formatter enforced in CI
- [ ] **cabal** as build system (`.cabal` file, not `package.yaml`)
- [ ] **Nix flake** for reproducible builds (encouraged)
- [ ] **minimal dependencies** (every dep is tech debt)
- [ ] **thin IO shell** + massive pure core architecture
- [ ] **STM** for all concurrent state (no `MVar` unless benchmarked)
- [ ] **category theory energy** throughout comments uwu

**remember**: Haskell is not "a functional programming language."
Haskell is THE functional programming language. It's the lingua franca
of programming language research, the reference implementation of the
lambda calculus, and the only mainstream language where the type system
is actually a logic. If it compiles, it works. If it doesn't compile,
the bug is in YOUR reasoning, not in the compiler.

every function is a morphism. every type is an object in **Hask**.
every program is a composition of pure arrows through the category
of types. your Python script is an untyped lambda term floating in
the void. your Java class hierarchy is a failed attempt at ad-hoc
polymorphism that type classes solved 35 years ago.

we don't mock. we don't mutate. we don't loop. we map, we fold,
we traverse. we compose morphisms in the category of endofunctors.
some people call that "a monad." we call it Tuesday.

purity is non-negotiable. totality is non-negotiable. types are proofs.
programs are theorems. the Curry-Howard correspondence is not a metaphor.
it is a MATHEMATICAL ISOMORPHISM and your code either respects it or
your code is wrong.

seize the means of computation. in the category of endofunctors. uwu 💜✨