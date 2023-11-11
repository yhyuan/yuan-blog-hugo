---
title: "Create U256 in Rust"
date: 2023-11-11T14:26:51-05:00
tags: ['rust']
draft: false
---

## How to Create U256 in Rust without external crate

```rust
#[derive(Debug, Copy, Clone, PartialEq, Eq)]
struct U256 {
    data: [u64; 4],
}

impl U256 {
    // Create a new U256 from a u64 value
    fn new(value: u64) -> Self {
        U256 { data: [value, 0, 0, 0] }
    }

    // Implement addition for U256
    fn add(&self, other: &U256) -> U256 {
        let mut result = U256 { data: [0; 4] };
        let mut carry = 0;

        for i in 0..4 {
            let (sum, overflow) = self.data[i].overflowing_add(other.data[i]);
            let (with_carry, overflow2) = sum.overflowing_add(carry);
            result.data[i] = with_carry;
            carry = if overflow || overflow2 { 1 } else { 0 };
        }

        result
    }

    // Implement subtraction for U256
    fn sub(&self, other: &U256) -> U256 {
        let mut result = U256 { data: [0; 4] };
        let mut borrow = 0;

        for i in 0..4 {
            let (diff, underflow) = self.data[i].overflowing_sub(other.data[i]);
            let (with_borrow, underflow2) = diff.overflowing_sub(borrow);
            result.data[i] = with_borrow;
            borrow = if underflow || underflow2 { 1 } else { 0 };
        }

        result
    }

    // Implement shift-and-add multiplication for U256
    fn mul(&self, other: &U256) -> U256 {
        let mut result = U256 { data: [0; 4] };

        for i in 0..4 {
            for j in 0..4 {
                if let Some(overflow) = result.data[i].checked_add(self.data[j] * other.data[i - j]) {
                    result.data[i] = overflow;
                } else {
                    // Overflow handling, if needed
                    panic!("Multiplication overflow");
                }
            }
        }

        result
    }

    // Implement long division for U256
    fn div(&self, other: &U256) -> U256 {
        let mut result = U256 { data: [0; 4] };
        let mut remainder = *self;

        for i in (0..256).rev() {
            result = result << 1;
            if remainder >= *other {
                result.data[0] |= 1;
                remainder = remainder.sub(other);
            }
        }

        result
    }
}

fn main() {
    let num1 = U256::new(123456789);
    let num2 = U256::new(987654321);

    let sum = num1.add(&num2);
    let difference = num1.sub(&num2);
    let product = num1.mul(&num2);
    let quotient = num1.div(&num2);

    println!("Sum: {:?}", sum);
    println!("Difference: {:?}", difference);
    println!("Product: {:?}", product);
    println!("Quotient: {:?}", quotient);
}
```

## How to implement a Finite Field struct with a prime in rust? 
```rust
#[derive(Debug, Copy, Clone, PartialEq, Eq)]
struct FiniteFieldElement {
    value: u64,
    prime: u64,
}

impl FiniteFieldElement {
    // Create a new FiniteFieldElement
    fn new(value: u64, prime: u64) -> Self {
        let normalized_value = value % prime;
        FiniteFieldElement {
            value: normalized_value,
            prime,
        }
    }

    // Addition in the finite field
    fn add(&self, other: &FiniteFieldElement) -> FiniteFieldElement {
        let sum = (self.value + other.value) % self.prime;
        FiniteFieldElement::new(sum, self.prime)
    }

    // Subtraction in the finite field
    fn sub(&self, other: &FiniteFieldElement) -> FiniteFieldElement {
        let diff = (self.value + self.prime - other.value) % self.prime;
        FiniteFieldElement::new(diff, self.prime)
    }

    // Multiplication in the finite field
    fn mul(&self, other: &FiniteFieldElement) -> FiniteFieldElement {
        let product = (self.value * other.value) % self.prime;
        FiniteFieldElement::new(product, self.prime)
    }

    // Exponentiation in the finite field
    fn pow(&self, exponent: u64) -> FiniteFieldElement {
        let result = self.value.pow(exponent as u32) % self.prime;
        FiniteFieldElement::new(result, self.prime)
    }

    // Modular inverse in the finite field
    fn inverse(&self) -> Option<FiniteFieldElement> {
        let (gcd, x, _) = extended_gcd(self.value as i64, self.prime as i64);

        if gcd == 1 {
            let inverse = (x % self.prime as i64 + self.prime as i64) as u64;
            Some(FiniteFieldElement::new(inverse, self.prime))
        } else {
            None // No inverse exists if gcd is not 1
        }
    }
}

// Extended Euclidean Algorithm to find modular inverse
fn extended_gcd(a: i64, b: i64) -> (i64, i64, i64) {
    if b == 0 {
        (a, 1, 0)
    } else {
        let (d, x, y) = extended_gcd(b, a % b);
        (d, y, x - y * (a / b))
    }
}

fn main() {
    let prime = 23; // Choose a prime number for the finite field
    let element1 = FiniteFieldElement::new(5, prime);
    let element2 = FiniteFieldElement::new(10, prime);

    let sum = element1.add(&element2);
    let difference = element1.sub(&element2);
    let product = element1.mul(&element2);
    let power = element1.pow(3);
    let inverse = element1.inverse();

    println!("Sum: {:?}", sum);
    println!("Difference: {:?}", difference);
    println!("Product: {:?}", product);
    println!("Power: {:?}", power);
    println!("Inverse: {:?}", inverse);
}
```

## I need to use u256 in this Finite Field structure. 
```rust
#[derive(Debug, Copy, Clone, PartialEq, Eq)]
struct FiniteFieldElement {
    value: U256,
    prime: U256,
}

impl FiniteFieldElement {
    // Create a new FiniteFieldElement
    fn new(value: U256, prime: U256) -> Self {
        let normalized_value = &value % &prime;
        FiniteFieldElement {
            value: normalized_value,
            prime,
        }
    }

    // Addition in the finite field
    fn add(&self, other: &FiniteFieldElement) -> FiniteFieldElement {
        let sum = &self.value + &other.value;
        let result = sum % &self.prime;
        FiniteFieldElement::new(result, self.prime.clone())
    }

    // Subtraction in the finite field
    fn sub(&self, other: &FiniteFieldElement) -> FiniteFieldElement {
        let diff = &self.value + &self.prime - &other.value;
        let result = diff % &self.prime;
        FiniteFieldElement::new(result, self.prime.clone())
    }

    // Multiplication in the finite field
    fn mul(&self, other: &FiniteFieldElement) -> FiniteFieldElement {
        let product = &self.value * &other.value;
        let result = product % &self.prime;
        FiniteFieldElement::new(result, self.prime.clone())
    }

    // Exponentiation in the finite field
    fn pow(&self, exponent: U256) -> FiniteFieldElement {
        let result = self.value.pow(exponent) % &self.prime;
        FiniteFieldElement::new(result, self.prime.clone())
    }

    // Modular inverse in the finite field
    fn inverse(&self) -> Option<FiniteFieldElement> {
        let gcd_result = extended_gcd(&self.value, &self.prime);

        if gcd_result.gcd == U256::one() {
            let inverse = (gcd_result.x % &self.prime + &self.prime) % &self.prime;
            Some(FiniteFieldElement::new(inverse, self.prime.clone()))
        } else {
            None // No inverse exists if gcd is not 1
        }
    }
}

// Extended Euclidean Algorithm to find modular inverse
fn extended_gcd(a: &U256, b: &U256) -> ExtendedGCDResult {
    if b.is_zero() {
        ExtendedGCDResult {
            gcd: a.clone(),
            x: U256::one(),
            y: U256::zero(),
        }
    } else {
        let gcd_result = extended_gcd(b, &(a % b));
        let x = gcd_result.y.clone();
        let y = gcd_result.x - (&gcd_result.y * (a / b));
        ExtendedGCDResult {
            gcd: gcd_result.gcd,
            x,
            y,
        }
    }
}

// Struct to hold the result of the extended GCD algorithm
#[derive(Debug, Clone)]
struct ExtendedGCDResult {
    gcd: U256,
    x: U256,
    y: U256,
}

fn main() {
    let prime = U256::from(23); // Choose a prime number for the finite field
    let element1 = FiniteFieldElement::new(U256::from(5), prime.clone());
    let element2 = FiniteFieldElement::new(U256::from(10), prime.clone());

    let sum = element1.add(&element2);
    let difference = element1.sub(&element2);
    let product = element1.mul(&element2);
    let power = element1.pow(U256::from(3));
    let inverse = element1.inverse();

    println!("Sum: {:?}", sum);
    println!("Difference: {:?}", difference);
    println!("Product: {:?}", product);
    println!("Power: {:?}", power);
    println!("Inverse: {:?}", inverse);
}

```

Cargo.toml
```toml
[dependencies]
num-bigint = "0.5"
num-traits = "0.2"
```