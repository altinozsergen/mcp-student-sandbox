# Mystery Module: Quadratic Equation Solver

## Overview

This module provides a function to solve quadratic equations using the **quadratic formula**. It takes the coefficients of a quadratic equation and returns the real solutions, or `None` if no real solutions exist.

---

## What It Does

The `mystery_module` implements the mathematical quadratic formula to find the roots (solutions) of equations in the form:

$$ax^2 + bx + c = 0$$

where `a`, `b`, and `c` are coefficients.

**Function**: `fn_x(a, b, c)`
- **Input**: Three coefficients (a, b, c)
- **Output**: A tuple of two solutions, or `None` if no real solutions exist

---

## How It Works

### The Quadratic Formula

The mathematical formula used is:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Step-by-Step Breakdown

1. **Calculate the discriminant** (`d`):
   ```
   d = b² - 4ac
   ```
   The discriminant determines the nature of solutions:
   - If `d > 0`: Two distinct real solutions
   - If `d = 0`: One repeated real solution
   - If `d < 0`: No real solutions (complex roots)

2. **Check if real solutions exist**:
   - If `d < 0`: Return `None` (no real solutions)
   - If `d ≥ 0`: Calculate both roots

3. **Calculate both roots**:
   - Solution 1: $\frac{-b + \sqrt{d}}{2a}$
   - Solution 2: $\frac{-b - \sqrt{d}}{2a}$

4. **Return as a tuple**: `(root1, root2)`

### Code Walkthrough

```python
import math

def fn_x(a, b, c):
    # Step 1: Calculate discriminant
    d = b**2 - 4*a*c
    
    # Step 2: Check if solutions exist
    if d < 0:
        return None  # No real solutions
    
    # Step 3-4: Calculate and return both solutions
    return ((-b + math.sqrt(d))/(2*a),    # First root
            (-b - math.sqrt(d))/(2*a))    # Second root
```

---

## Example Usage

### Example 1: Two Distinct Real Solutions

Solve: $x^2 - 5x + 6 = 0$

Coefficients: `a=1, b=-5, c=6`

```python
from mystery_module import fn_x

result = fn_x(1, -5, 6)
print(result)
# Output: (3.0, 2.0)
```

**Verification**:
- When x = 3: 3² - 5(3) + 6 = 9 - 15 + 6 = 0 ✓
- When x = 2: 2² - 5(2) + 6 = 4 - 10 + 6 = 0 ✓

---

### Example 2: One Repeated Root (Discriminant = 0)

Solve: $x^2 - 4x + 4 = 0$

Coefficients: `a=1, b=-4, c=4`

```python
result = fn_x(1, -4, 4)
print(result)
# Output: (2.0, 2.0)
```

**Explanation**: Both roots are the same because the discriminant equals 0.

---

### Example 3: No Real Solutions (Negative Discriminant)

Solve: $x^2 + 1 = 0$

Coefficients: `a=1, b=0, c=1`

```python
result = fn_x(1, 0, 1)
print(result)
# Output: None
```

**Explanation**: The discriminant is negative (d = 0 - 4 = -4 < 0), so there are no real solutions. The actual solutions would be complex: `±i`

---

### Example 4: Negative Coefficient

Solve: $-2x^2 + 8x - 8 = 0$

Coefficients: `a=-2, b=8, c=-8`

```python
result = fn_x(-2, 8, -8)
print(result)
# Output: (2.0, 2.0)
```

---

### Example 5: Fractional Solutions

Solve: $2x^2 - 7x + 3 = 0$

Coefficients: `a=2, b=-7, c=3`

```python
result = fn_x(2, -7, 3)
print(result)
# Output: (3.0, 0.5)
```

**Verification**:
- When x = 3: 2(3)² - 7(3) + 3 = 18 - 21 + 3 = 0 ✓
- When x = 0.5: 2(0.5)² - 7(0.5) + 3 = 0.5 - 3.5 + 3 = 0 ✓

---

## Mathematical Background

### Discriminant Analysis

The discriminant ($\Delta = b^2 - 4ac$) tells us about the nature of roots:

| Discriminant | Nature of Roots | Solutions |
|---|---|---|
| $\Delta > 0$ | Two distinct real roots | Real and different |
| $\Delta = 0$ | One repeated real root | Real and equal |
| $\Delta < 0$ | No real roots | Complex/Imaginary |

### When to Use

This function is useful for:
- Solving physics problems (projectile motion, free fall)
- Finding circuit parameters (electrical engineering)
- Optimization problems (parabolic curves)
- Finding intercepts in geometry
- Engineering calculations

---

## Important Notes

### ⚠️ Special Cases

1. **When `a = 0`**: The equation is NOT quadratic
   - Result: `ZeroDivisionError` (attempting to divide by 0)
   - The equation becomes linear: $bx + c = 0$

2. **Numerical Precision**:
   - The function returns floating-point numbers
   - Floating-point arithmetic may have small rounding errors
   - For exact rational roots, consider using `Decimal` or `fractions` modules

3. **Complex Roots** (Not handled):
   - When `d < 0`, only `None` is returned
   - To handle complex numbers, use `cmath` module instead:
   ```python
   import cmath
   # Returns complex roots when d < 0
   sqrt_d = cmath.sqrt(d)
   ```

---

## Advanced Examples

### Creating a More Robust Version

```python
import math
from typing import Optional, Tuple

def solve_quadratic(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    Enhanced version with error handling and type hints.
    
    Args:
        a, b, c: Coefficients of ax² + bx + c = 0
        
    Returns:
        Tuple of two solutions, or None if no real solutions
        
    Raises:
        ValueError: If coefficient 'a' is zero (not a quadratic equation)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero (not a quadratic equation)")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return None
    
    sqrt_d = math.sqrt(discriminant)
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    
    return (x1, x2)
```

### Handling Complex Roots

```python
import cmath
from typing import Tuple, Union

def solve_quadratic_complex(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """Solve quadratic equation, returning complex roots if necessary."""
    discriminant = b**2 - 4*a*c
    sqrt_d = cmath.sqrt(discriminant)
    
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    
    return (x1, x2)

# Example with complex roots
result = solve_quadratic_complex(1, 0, 1)
# Output: (1j, -1j) representing ±i
```

---

## Testing Examples

Here are test cases to verify the function works correctly:

```python
# Test 1: Two distinct roots
assert fn_x(1, -5, 6) == (3.0, 2.0)

# Test 2: Repeated root
assert fn_x(1, -4, 4) == (2.0, 2.0)

# Test 3: No real solutions
assert fn_x(1, 0, 1) is None

# Test 4: Negative coefficient
assert fn_x(-1, 0, 1) == (1.0, -1.0)

# Test 5: Fractional solutions
result = fn_x(2, -7, 3)
assert abs(result[0] - 3.0) < 1e-10
assert abs(result[1] - 0.5) < 1e-10
```

---

## Summary

The `mystery_module` provides a clean, efficient implementation of the quadratic formula:

- **Purpose**: Solves quadratic equations (ax² + bx + c = 0)
- **Input**: Three coefficients (a, b, c)
- **Output**: Tuple of two solutions or None
- **Limitations**: Only handles real solutions, no error handling for a=0
- **Use Cases**: Physics, engineering, mathematics, optimization

This is a fundamental mathematical tool with wide applications across STEM fields.

---

## See Also

- [Quadratic Formula - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_formula)
- [Python Math Module](https://docs.python.org/3/library/math.html)
- [Solving Quadratic Equations](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:quad-formula/a/quadratic-formula-explained)
