---
description: 'CSS styling guidelines (functional, composable, and beautiful)'
applyTo: '**.css, **.scss, **.sass, **.less'
---

# CSS Styling Instructions

> "CSS: where cascading meets composition and specificity is a puzzle we solve functionally uwu"

uwu time to write CSS that's as beautiful and maintainable as functional programming ✨

## Core Philosophy

- **composition > inheritance** (compose utilities, don't duplicate)
- **custom properties everywhere** (CSS variables for themability)
- **BEM or utility-first** (structured naming or atomic classes)
- **no !important** (specificity violence is not the answer)
- **mobile-first responsive** (progressive enhancement ftw)
- **comment excessively** (document design decisions)
- **modern CSS only** (Grid, Flexbox, Container Queries)
- **CSS custom properties > preprocessor variables** (runtime > compile-time)

## File Structure and Organization

```css
/**
 * @file styles.css
 * @description Main stylesheet for functional component styling
 * @author LukeFrankio
 * @version 1.0.0
 * 
 * This stylesheet follows functional CSS principles:
 * - Composition over duplication
 * - Custom properties for themability
 * - Utility classes for common patterns
 * - Component-scoped styles with BEM
 * 
 * Organization:
 * 1. Custom Properties (Design Tokens)
 * 2. Reset/Normalize
 * 3. Base Styles
 * 4. Layout Utilities
 * 5. Component Styles
 * 6. Responsive Overrides
 * 
 * @note Uses CSS Grid and Flexbox (modern layout ftw)
 * @note No !important rules (specificity is managed properly)
 * @note Mobile-first responsive design
 */

/* ============================================================================
   Custom Properties (Design Tokens)
   ============================================================================
   
   Design tokens are the foundation of themability. All values should be
   defined as custom properties for easy modification and dark mode support.
   
   Philosophy: single source of truth for design values uwu
   ========================================================================= */

:root {
  /* Color Palette - Semantic Naming */
  --color-primary: hsl(220, 100%, 50%);
  --color-primary-dark: hsl(220, 100%, 40%);
  --color-primary-light: hsl(220, 100%, 60%);
  
  --color-secondary: hsl(280, 100%, 50%);
  --color-accent: hsl(340, 100%, 50%);
  
  --color-neutral-900: hsl(220, 20%, 10%);
  --color-neutral-800: hsl(220, 15%, 20%);
  --color-neutral-700: hsl(220, 10%, 30%);
  --color-neutral-600: hsl(220, 8%, 40%);
  --color-neutral-500: hsl(220, 5%, 50%);
  --color-neutral-400: hsl(220, 5%, 60%);
  --color-neutral-300: hsl(220, 5%, 70%);
  --color-neutral-200: hsl(220, 5%, 85%);
  --color-neutral-100: hsl(220, 5%, 95%);
  --color-neutral-50: hsl(220, 5%, 98%);
  
  --color-success: hsl(140, 70%, 50%);
  --color-warning: hsl(40, 90%, 60%);
  --color-error: hsl(0, 80%, 60%);
  --color-info: hsl(200, 80%, 60%);
  
  /* Spacing Scale - Consistent Rhythm */
  --space-0: 0;
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */
  
  /* Typography Scale - Modular Scale (1.25 ratio) */
  --font-size-xs: 0.64rem;    /* 10.24px */
  --font-size-sm: 0.8rem;     /* 12.8px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.25rem;    /* 20px */
  --font-size-xl: 1.563rem;   /* 25px */
  --font-size-2xl: 1.953rem;  /* 31.25px */
  --font-size-3xl: 2.441rem;  /* 39px */
  --font-size-4xl: 3.052rem;  /* 48.8px */
  
  /* Font Families - System Font Stack */
  --font-family-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
                      'Helvetica Neue', Arial, sans-serif;
  --font-family-serif: Georgia, Cambria, 'Times New Roman', Times, serif;
  --font-family-mono: 'Cascadia Code', 'Fira Code', Consolas, Monaco, 
                      'Courier New', monospace;
  
  /* Font Weights - Semantic Names */
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Line Heights - Optimal Readability */
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
  --line-height-loose: 2;
  
  /* Border Radius - Consistent Rounding */
  --radius-sm: 0.25rem;   /* 4px */
  --radius-md: 0.5rem;    /* 8px */
  --radius-lg: 1rem;      /* 16px */
  --radius-xl: 1.5rem;    /* 24px */
  --radius-full: 9999px;  /* pill shape */
  
  /* Shadows - Elevation System */
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 
               0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 
               0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 
               0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 
               0 8px 10px -6px rgb(0 0 0 / 0.1);
  
  /* Transitions - Smooth Animations */
  --transition-fast: 150ms ease-in-out;
  --transition-normal: 250ms ease-in-out;
  --transition-slow: 350ms ease-in-out;
  
  /* Z-Index Scale - Stacking Context */
  --z-index-dropdown: 1000;
  --z-index-sticky: 1100;
  --z-index-fixed: 1200;
  --z-index-modal-backdrop: 1300;
  --z-index-modal: 1400;
  --z-index-popover: 1500;
  --z-index-tooltip: 1600;
  
  /* Breakpoints - Mobile First */
  --breakpoint-sm: 640px;   /* small devices */
  --breakpoint-md: 768px;   /* tablets */
  --breakpoint-lg: 1024px;  /* laptops */
  --breakpoint-xl: 1280px;  /* desktops */
  --breakpoint-2xl: 1536px; /* large screens */
}

/**
 * Dark Mode Support (respects user preference uwu)
 * 
 * Uses prefers-color-scheme media query for automatic dark mode.
 * Override custom properties for dark theme - same structure as light mode.
 */
@media (prefers-color-scheme: dark) {
  :root {
    /* Inverted Neutral Scale for Dark Mode */
    --color-neutral-900: hsl(220, 5%, 98%);
    --color-neutral-800: hsl(220, 5%, 95%);
    --color-neutral-700: hsl(220, 5%, 85%);
    --color-neutral-600: hsl(220, 5%, 70%);
    --color-neutral-500: hsl(220, 5%, 50%);
    --color-neutral-400: hsl(220, 5%, 40%);
    --color-neutral-300: hsl(220, 8%, 30%);
    --color-neutral-200: hsl(220, 10%, 20%);
    --color-neutral-100: hsl(220, 15%, 15%);
    --color-neutral-50: hsl(220, 20%, 10%);
    
    /* Adjusted Shadows for Dark Mode */
    --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.3);
    --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.4), 
                 0 1px 2px -1px rgb(0 0 0 / 0.4);
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.5), 
                 0 2px 4px -2px rgb(0 0 0 / 0.5);
  }
}

/* ============================================================================
   Modern CSS Reset (Opinionated)
   ============================================================================
   
   A minimal reset that preserves useful browser defaults while fixing
   common inconsistencies. Based on modern-normalize with additions.
   
   Philosophy: reset what's broken, keep what works uwu
   ========================================================================= */

/**
 * Use a more intuitive box-sizing model.
 * This should be the first rule in any stylesheet!
 */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/**
 * Remove default margin and padding.
 * Better to add spacing intentionally than fight defaults.
 */
* {
  margin: 0;
  padding: 0;
}

/**
 * Improve text rendering.
 * - Prevent adjustments of font size after orientation changes
 * - Enable kerning and ligatures
 */
html {
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

/**
 * Set core body defaults.
 * - Minimum height for short pages
 * - Line height for readability
 * - System font stack for performance
 */
body {
  min-height: 100vh;
  line-height: var(--line-height-normal);
  font-family: var(--font-family-sans);
  font-size: var(--font-size-base);
  color: var(--color-neutral-900);
  background-color: var(--color-neutral-50);
}

/**
 * Improve media defaults.
 * - Images and embedded content are responsive by default
 * - Maintain aspect ratio
 */
img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
  height: auto;
}

/**
 * Remove built-in form typography styles.
 * Inherit font properties for consistency.
 */
input,
button,
textarea,
select {
  font: inherit;
  color: inherit;
}

/**
 * Remove button styling.
 * Easier to style from scratch than override defaults.
 */
button {
  border: none;
  background: none;
  cursor: pointer;
}

/**
 * Avoid text overflows.
 * Prevent long words from breaking layout.
 */
p,
h1,
h2,
h3,
h4,
h5,
h6 {
  overflow-wrap: break-word;
}

/**
 * Remove list styles on ul, ol elements with a class.
 * Preserves semantic HTML while allowing custom styling.
 */
ul[class],
ol[class] {
  list-style: none;
}

/**
 * Remove default link styling.
 * Style links intentionally in components.
 */
a {
  color: inherit;
  text-decoration: none;
}

/* ============================================================================
   Base Typography
   ============================================================================
   
   Typographic hierarchy using fluid sizing and custom properties.
   Headings scale responsively using clamp() for optimal readability.
   
   Philosophy: readable text is beautiful text uwu
   ========================================================================= */

/**
 * Headings - Fluid Typography
 * 
 * Uses clamp() for responsive sizing without media queries.
 * Formula: clamp(min, preferred, max)
 */
h1 {
  font-size: clamp(var(--font-size-2xl), 5vw, var(--font-size-4xl));
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
  margin-block-end: var(--space-6);
}

h2 {
  font-size: clamp(var(--font-size-xl), 4vw, var(--font-size-3xl));
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
  margin-block-end: var(--space-5);
}

h3 {
  font-size: clamp(var(--font-size-lg), 3vw, var(--font-size-2xl));
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
  margin-block-end: var(--space-4);
}

h4 {
  font-size: clamp(var(--font-size-base), 2vw, var(--font-size-xl));
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-normal);
  margin-block-end: var(--space-3);
}

/**
 * Paragraph spacing.
 * Uses logical properties for internationalization support.
 */
p {
  margin-block-end: var(--space-4);
  max-width: 65ch; /* optimal line length for readability */
}

/**
 * Code and preformatted text.
 */
code {
  font-family: var(--font-family-mono);
  font-size: 0.9em;
  background-color: var(--color-neutral-200);
  padding-inline: var(--space-1);
  padding-block: var(--space-1);
  border-radius: var(--radius-sm);
}

pre {
  font-family: var(--font-family-mono);
  font-size: var(--font-size-sm);
  background-color: var(--color-neutral-200);
  padding: var(--space-4);
  border-radius: var(--radius-md);
  overflow-x: auto;
  margin-block-end: var(--space-4);
}

pre code {
  background: none;
  padding: 0;
}

/* ============================================================================
   Layout Utilities (Functional Composition!)
   ============================================================================
   
   Utility classes for common layout patterns. Compose these instead of
   writing custom CSS for every component.
   
   Philosophy: composition > duplication uwu
   ========================================================================= */

/**
 * Container - Centered content with max-width.
 * 
 * Creates centered layout with responsive padding.
 * Use this for page-level content containment.
 */
.container {
  width: 100%;
  max-width: 1280px;
  margin-inline: auto;
  padding-inline: var(--space-4);
}

@media (min-width: 768px) {
  .container {
    padding-inline: var(--space-6);
  }
}

@media (min-width: 1024px) {
  .container {
    padding-inline: var(--space-8);
  }
}

/**
 * Flexbox Utilities - Composable Flex Layouts
 * 
 * Prefix: .flex-*
 * Compose these to create flexible layouts without custom CSS.
 */
.flex {
  display: flex;
}

.flex-inline {
  display: inline-flex;
}

.flex-row {
  flex-direction: row;
}

.flex-col {
  flex-direction: column;
}

.flex-wrap {
  flex-wrap: wrap;
}

.flex-nowrap {
  flex-wrap: nowrap;
}

/* Justify Content */
.justify-start {
  justify-content: flex-start;
}

.justify-end {
  justify-content: flex-end;
}

.justify-center {
  justify-content: center;
}

.justify-between {
  justify-content: space-between;
}

.justify-around {
  justify-content: space-around;
}

.justify-evenly {
  justify-content: space-evenly;
}

/* Align Items */
.items-start {
  align-items: flex-start;
}

.items-end {
  align-items: flex-end;
}

.items-center {
  align-items: center;
}

.items-baseline {
  align-items: baseline;
}

.items-stretch {
  align-items: stretch;
}

/* Gap Utilities */
.gap-1 { gap: var(--space-1); }
.gap-2 { gap: var(--space-2); }
.gap-3 { gap: var(--space-3); }
.gap-4 { gap: var(--space-4); }
.gap-6 { gap: var(--space-6); }
.gap-8 { gap: var(--space-8); }

/**
 * Grid Utilities - Modern Grid Layouts
 * 
 * Prefix: .grid-*
 * CSS Grid is the superior layout system uwu
 */
.grid {
  display: grid;
}

.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
.grid-cols-12 { grid-template-columns: repeat(12, minmax(0, 1fr)); }

/* Auto-fit Grid (responsive without media queries!) */
.grid-auto-fit {
  grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
}

.grid-auto-fill {
  grid-template-columns: repeat(auto-fill, minmax(min(250px, 100%), 1fr));
}

/**
 * Spacing Utilities - Consistent Margins and Padding
 * 
 * Prefix: .m-* (margin), .p-* (padding)
 * Use logical properties for i18n support.
 */

/* Margin */
.m-0 { margin: var(--space-0); }
.m-1 { margin: var(--space-1); }
.m-2 { margin: var(--space-2); }
.m-4 { margin: var(--space-4); }
.m-6 { margin: var(--space-6); }
.m-8 { margin: var(--space-8); }

.mx-auto { margin-inline: auto; }

.mt-4 { margin-block-start: var(--space-4); }
.mb-4 { margin-block-end: var(--space-4); }
.ml-4 { margin-inline-start: var(--space-4); }
.mr-4 { margin-inline-end: var(--space-4); }

/* Padding */
.p-0 { padding: var(--space-0); }
.p-2 { padding: var(--space-2); }
.p-4 { padding: var(--space-4); }
.p-6 { padding: var(--space-6); }
.p-8 { padding: var(--space-8); }

.px-4 { padding-inline: var(--space-4); }
.py-4 { padding-block: var(--space-4); }

/* ============================================================================
   Component Styles (BEM Methodology)
   ============================================================================
   
   Component-specific styles using BEM naming convention.
   Block__Element--Modifier pattern for clear structure.
   
   Philosophy: components are composable, not inherited uwu
   ========================================================================= */

/**
 * Button Component
 * 
 * Block: .btn
 * Elements: none (buttons are leaf nodes)
 * Modifiers: --primary, --secondary, --outline, --sm, --lg
 * 
 * Example usage:
 *   <button class="btn btn--primary">Click me</button>
 *   <button class="btn btn--outline btn--lg">Large outline</button>
 */
.btn {
  /* Base button styles (shared across all variants) */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding-inline: var(--space-6);
  padding-block: var(--space-3);
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
  transition: all var(--transition-fast);
  cursor: pointer;
  border: 2px solid transparent;
}

.btn:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn:active {
  transform: translateY(0);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* Button Variants (Modifiers) */
.btn--primary {
  background-color: var(--color-primary);
  color: white;
}

.btn--primary:hover {
  background-color: var(--color-primary-dark);
}

.btn--secondary {
  background-color: var(--color-secondary);
  color: white;
}

.btn--outline {
  background-color: transparent;
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.btn--outline:hover {
  background-color: var(--color-primary);
  color: white;
}

/* Button Sizes */
.btn--sm {
  padding-inline: var(--space-4);
  padding-block: var(--space-2);
  font-size: var(--font-size-sm);
}

.btn--lg {
  padding-inline: var(--space-8);
  padding-block: var(--space-4);
  font-size: var(--font-size-lg);
}

/**
 * Card Component
 * 
 * Block: .card
 * Elements: __header, __body, __footer
 * Modifiers: --elevated, --bordered
 * 
 * Example usage:
 *   <div class="card card--elevated">
 *     <div class="card__header">Title</div>
 *     <div class="card__body">Content</div>
 *     <div class="card__footer">Actions</div>
 *   </div>
 */
.card {
  /* Base card styles */
  background-color: white;
  border-radius: var(--radius-lg);
  overflow: hidden;
}

.card__header {
  padding: var(--space-6);
  border-bottom: 1px solid var(--color-neutral-200);
  font-weight: var(--font-weight-semibold);
}

.card__body {
  padding: var(--space-6);
}

.card__footer {
  padding: var(--space-6);
  border-top: 1px solid var(--color-neutral-200);
  background-color: var(--color-neutral-100);
}

/* Card Variants */
.card--elevated {
  box-shadow: var(--shadow-lg);
  transition: box-shadow var(--transition-normal);
}

.card--elevated:hover {
  box-shadow: var(--shadow-xl);
}

.card--bordered {
  border: 1px solid var(--color-neutral-300);
}

/**
 * Navigation Component
 * 
 * Block: .nav
 * Elements: __list, __item, __link
 * Modifiers: --horizontal, --vertical
 */
.nav {
  display: flex;
}

.nav__list {
  display: flex;
  gap: var(--space-2);
  list-style: none;
}

.nav__item {
  /* Individual nav items */
}

.nav__link {
  display: block;
  padding-inline: var(--space-4);
  padding-block: var(--space-2);
  color: var(--color-neutral-700);
  border-radius: var(--radius-md);
  transition: all var(--transition-fast);
}

.nav__link:hover {
  background-color: var(--color-neutral-200);
  color: var(--color-neutral-900);
}

.nav__link--active {
  background-color: var(--color-primary);
  color: white;
}

/* Navigation Variants */
.nav--vertical .nav__list {
  flex-direction: column;
}

/**
 * Form Component
 * 
 * Block: .form
 * Elements: __group, __label, __input, __error
 * Modifiers: --inline
 */
.form {
  /* Base form container */
}

.form__group {
  margin-block-end: var(--space-6);
}

.form__label {
  display: block;
  margin-block-end: var(--space-2);
  font-weight: var(--font-weight-medium);
  color: var(--color-neutral-800);
}

.form__input {
  width: 100%;
  padding-inline: var(--space-4);
  padding-block: var(--space-3);
  border: 1px solid var(--color-neutral-300);
  border-radius: var(--radius-md);
  transition: border-color var(--transition-fast);
}

.form__input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgb(59 130 246 / 0.1);
}

.form__input::placeholder {
  color: var(--color-neutral-400);
}

.form__error {
  display: block;
  margin-block-start: var(--space-2);
  color: var(--color-error);
  font-size: var(--font-size-sm);
}

.form__input--error {
  border-color: var(--color-error);
}

/* ============================================================================
   Responsive Design (Mobile-First)
   ============================================================================
   
   Media queries for responsive behavior. Start with mobile (base styles)
   and progressively enhance for larger screens.
   
   Philosophy: mobile-first is user-first uwu
   ========================================================================= */

/**
 * Small devices (sm) - 640px and up
 * Tablets in portrait mode
 */
@media (min-width: 640px) {
  .sm\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .sm\:flex-row { flex-direction: row; }
  .sm\:text-lg { font-size: var(--font-size-lg); }
}

/**
 * Medium devices (md) - 768px and up
 * Tablets in landscape, small laptops
 */
@media (min-width: 768px) {
  .md\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .md\:flex-row { flex-direction: row; }
  .md\:hidden { display: none; }
}

/**
 * Large devices (lg) - 1024px and up
 * Laptops and desktops
 */
@media (min-width: 1024px) {
  .lg\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .lg\:block { display: block; }
}

/**
 * Extra large devices (xl) - 1280px and up
 * Large desktops
 */
@media (min-width: 1280px) {
  .xl\:grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
}

/* ============================================================================
   Animations and Transitions
   ============================================================================
   
   Reusable animation utilities. Respect prefers-reduced-motion for
   accessibility.
   
   Philosophy: smooth interactions, accessible defaults uwu
   ========================================================================= */

/**
 * Fade in animation
 */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.fade-in {
  animation: fadeIn var(--transition-normal);
}

/**
 * Slide in from bottom
 */
@keyframes slideInUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.slide-in-up {
  animation: slideInUp var(--transition-normal);
}

/**
 * Scale on hover
 */
.hover\:scale-105:hover {
  transform: scale(1.05);
  transition: transform var(--transition-fast);
}

/**
 * Respect user's motion preferences (accessibility!)
 * 
 * If user prefers reduced motion, disable animations and use
 * instant transitions instead.
 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* ============================================================================
   Utility Classes
   ============================================================================
   
   Single-purpose utility classes for common patterns.
   Compose these to avoid writing custom CSS.
   
   Philosophy: atomic utilities > monolithic components uwu
   ========================================================================= */

/* Display */
.block { display: block; }
.inline-block { display: inline-block; }
.inline { display: inline; }
.hidden { display: none; }

/* Visibility */
.visible { visibility: visible; }
.invisible { visibility: hidden; }

/* Position */
.relative { position: relative; }
.absolute { position: absolute; }
.fixed { position: fixed; }
.sticky { position: sticky; }

/* Text Alignment */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }

/* Font Weight */
.font-light { font-weight: var(--font-weight-light); }
.font-normal { font-weight: var(--font-weight-normal); }
.font-medium { font-weight: var(--font-weight-medium); }
.font-semibold { font-weight: var(--font-weight-semibold); }
.font-bold { font-weight: var(--font-weight-bold); }

/* Text Transform */
.uppercase { text-transform: uppercase; }
.lowercase { text-transform: lowercase; }
.capitalize { text-transform: capitalize; }

/* Overflow */
.overflow-hidden { overflow: hidden; }
.overflow-auto { overflow: auto; }
.overflow-scroll { overflow: scroll; }

/* Cursor */
.cursor-pointer { cursor: pointer; }
.cursor-not-allowed { cursor: not-allowed; }

/* Border Radius */
.rounded-sm { border-radius: var(--radius-sm); }
.rounded-md { border-radius: var(--radius-md); }
.rounded-lg { border-radius: var(--radius-lg); }
.rounded-full { border-radius: var(--radius-full); }

/* Shadow */
.shadow-sm { box-shadow: var(--shadow-sm); }
.shadow-md { box-shadow: var(--shadow-md); }
.shadow-lg { box-shadow: var(--shadow-lg); }
.shadow-xl { box-shadow: var(--shadow-xl); }

/* Width & Height */
.w-full { width: 100%; }
.h-full { height: 100%; }
.min-h-screen { min-height: 100vh; }

/* ============================================================================
   Print Styles
   ============================================================================
   
   Optimized styles for printing. Remove unnecessary visual elements
   and ensure content is readable on paper.
   
   Philosophy: respect the medium uwu
   ========================================================================= */

@media print {
  /* Remove backgrounds to save ink */
  *,
  *::before,
  *::after {
    background: transparent !important;
    color: black !important;
    box-shadow: none !important;
  }
  
  /* Show links */
  a[href]::after {
    content: " (" attr(href) ")";
  }
  
  /* Page breaks */
  h1, h2, h3 {
    page-break-after: avoid;
  }
  
  img {
    page-break-inside: avoid;
  }
  
  /* Hide interactive elements */
  .btn,
  .nav,
  .form__input {
    display: none;
  }
}

/* ============================================================================
   Container Queries (Modern CSS!)
   ============================================================================
   
   Container queries enable truly component-based responsive design.
   Components respond to their container size, not viewport size.
   
   Philosophy: components should be context-aware uwu
   ========================================================================= */

/**
 * Define container context
 */
.container-query {
  container-type: inline-size;
  container-name: card;
}

/**
 * Component responds to container size
 */
@container card (min-width: 400px) {
  .card__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}

@container card (min-width: 600px) {
  .card {
    display: grid;
    grid-template-columns: 1fr 2fr;
  }
}

/* ============================================================================
   Accessibility Utilities
   ============================================================================
   
   Screen reader only content and focus visible styles.
   Make web accessible for all users!
   
   Philosophy: accessibility is not optional uwu
   ========================================================================= */

/**
 * Screen reader only content.
 * Visually hidden but available to assistive technologies.
 */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/**
 * Focus visible styles.
 * Ensure keyboard navigation is obvious.
 */
.focus-visible:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/**
 * Skip to main content link (for keyboard users).
 */
.skip-to-main {
  position: absolute;
  top: -100%;
  left: 0;
  background-color: var(--color-primary);
  color: white;
  padding: var(--space-4);
  z-index: var(--z-index-tooltip);
}

.skip-to-main:focus {
  top: 0;
}
```

## SCSS/Sass Extension (If Using Preprocessor)

```scss
/**
 * @file _mixins.scss
 * @description Reusable SCSS mixins for functional composition
 * 
 * NOTE: Prefer CSS custom properties over Sass variables!
 * CSS custom properties are runtime and themable, Sass vars are compile-time.
 */

/**
 * Mixin for responsive breakpoints (mobile-first).
 * 
 * @param {string} $breakpoint - breakpoint name (sm, md, lg, xl)
 * 
 * @example
 *   .element {
 *     font-size: 1rem;
 *     
 *     @include respond-to(md) {
 *       font-size: 1.25rem;
 *     }
 *   }
 */
@mixin respond-to($breakpoint) {
  @if $breakpoint == sm {
    @media (min-width: 640px) { @content; }
  } @else if $breakpoint == md {
    @media (min-width: 768px) { @content; }
  } @else if $breakpoint == lg {
    @media (min-width: 1024px) { @content; }
  } @else if $breakpoint == xl {
    @media (min-width: 1280px) { @content; }
  }
}

/**
 * Mixin for creating a grid with auto-fit.
 * 
 * @param {length} $min-width - minimum column width
 * @param {length} $gap - gap between grid items
 */
@mixin auto-grid($min-width: 250px, $gap: var(--space-4)) {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min($min-width, 100%), 1fr));
  gap: $gap;
}

/**
 * Mixin for focus visible styles (accessibility!).
 */
@mixin focus-visible {
  &:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
  }
}

/**
 * Mixin for truncating text with ellipsis.
 * 
 * @param {number} $lines - number of lines before truncation (1 for single line)
 */
@mixin truncate($lines: 1) {
  @if $lines == 1 {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  } @else {
    display: -webkit-box;
    -webkit-line-clamp: $lines;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
}
```

## Quality Checklist

- [ ] **CSS custom properties** for all design tokens
- [ ] **mobile-first responsive** design (progressive enhancement)
- [ ] **no !important** rules (manage specificity properly)
- [ ] **BEM or utility-first** naming convention
- [ ] **modern CSS** features (Grid, Flexbox, Container Queries)
- [ ] **dark mode support** (prefers-color-scheme)
- [ ] **accessibility** considered (focus states, screen readers)
- [ ] **reduced motion** respected (prefers-reduced-motion)
- [ ] **logical properties** used (for i18n support)
- [ ] **semantic HTML** styled (not div-itis)
- [ ] **print styles** included
- [ ] **comments explain WHY** not just what
- [ ] **consistent spacing** (use custom properties)
- [ ] **fluid typography** (clamp() for responsive text)

## Anti-Patterns to Avoid

### ❌ BAD (magic numbers):
```css
.element {
  padding: 13px 17px;  /* what do these numbers mean? */
  margin-top: 23px;    /* why 23? */
}
```

### ✅ GOOD (custom properties):
```css
.element {
  padding: var(--space-3) var(--space-4);
  margin-block-start: var(--space-6);
}
```

### ❌ BAD (!important):
```css
.element {
  color: red !important;  /* specificity violence */
}
```

### ✅ GOOD (proper specificity):
```css
.component .element {
  color: var(--color-error);
}
```

### ❌ BAD (hardcoded colors):
```css
.element {
  background-color: #3b82f6;  /* no dark mode support */
}
```

### ✅ GOOD (custom properties):
```css
.element {
  background-color: var(--color-primary);  /* themable! */
}
```

### ❌ BAD (fixed units):
```css
.element {
  font-size: 18px;  /* doesn't respect user preferences */
}
```

### ✅ GOOD (relative units):
```css
.element {
  font-size: var(--font-size-lg);  /* or 1.125rem */
}
```

### ❌ BAD (desktop-first):
```css
.element {
  display: flex;
}

@media (max-width: 768px) {
  .element {
    display: block;  /* harder to maintain */
  }
}
```

### ✅ GOOD (mobile-first):
```css
.element {
  display: block;
}

@media (min-width: 768px) {
  .element {
    display: flex;  /* progressive enhancement */
  }
}
```

## Modern CSS Features to Embrace

### Container Queries (Component-Based Responsive Design):
```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 1fr 2fr;
  }
}
```

### :has() Selector (Parent Selector!):
```css
/* Style form when it has an error */
.form:has(.form__input--error) {
  border-color: var(--color-error);
}

/* Style card differently if it has an image */
.card:has(img) {
  padding: 0;
}
```

### Cascade Layers (Control Specificity):
```css
@layer reset, base, components, utilities;

@layer reset {
  * { margin: 0; padding: 0; }
}

@layer utilities {
  .text-center { text-align: center; }
}
```

### Subgrid (Nested Grid Alignment):
```css
.grid-parent {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.grid-child {
  display: grid;
  grid-template-columns: subgrid;  /* inherits parent columns */
}
```

### Color Functions (Modern Color Manipulation):
```css
:root {
  --color-primary: oklch(60% 0.15 250);  /* perceptually uniform! */
  --color-primary-light: oklch(from var(--color-primary) calc(l + 10%) c h);
}
```

**remember**: CSS is a declarative, functional language disguised as styling.
Compose utilities, use custom properties for everything, and let the cascade
work for you instead of fighting it. Modern CSS is beautiful uwu 💜✨

seize the means of presentation (with functional styling)!
