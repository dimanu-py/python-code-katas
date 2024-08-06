# :atm: ATM Machine Kata :atm:

## Resources

These instructions where extracted from Codurance website. The link to the original instructions can be found in the link bellow.

[![Web](https://img.shields.io/badge/Codurance-Website-14a1f0?style=for-the-badge&logo=web&logoColor=white&labelColor=101010)](https://www.codurance.com/katas/atm-machine)

## Description

> [!NOTE]
> Graphical examples are only for illustrative purposes and do not represent the actual data structure or the need to implement it.

<details><summary>Iteration 1</summary>

### Business Rules

We want to build an ATM and the first thing we need to do, is to create the software that will break down which bills and coins to
give you when you are trying to make a withdrawal.

The content of the ATM is:

| Value | Type |
|-------|------|
| 500   | bill |
| 200   | bill |
| 100   | bill |
| 50    | bill |
| 20    | bill |
| 10    | bill |
| 5     | bill |
| 2     | coin |
| 1     | coin |

### Example

Input: user wants to withdraw 434$
Output: 2 bills of 200$, 1 bill of 20$, 1 bill of 10$, 2 coins of 2$

</details>

<details><summary>Iteration 2</summary>

### Business Rules

The ATM has the following distribution of money:
- When the ATM has no more money should return an error that shows "The ATM has not enough money, please go to the nearest ATM."
- If the ATM has no more bills or coins should try to use other quantities to allow the user to withdraw the amount requested.

The content of the ATM is:

| Value | Type | quantity of units |
|-------|------|-------------------|
| 500   | bill | 2                 |
| 200   | bill | 3                 |
| 100   | bill | 5                 |
| 50    | bill | 12                |
| 20    | bill | 20                |
| 10    | bill | 50                |
| 5     | bill | 100               |
| 2     | coin | 250               |
| 1     | coin | 500               |

### Example

Input 1: user wants to withdraw 1725$
Output: 2 bills of 500$, 3 bills of 200$, 1 bill of 100$, 1 bill of 20$, 1 bill of 5$

Input 2: user wants to withdraw 1825$
Output: 4 bills of 100$, 12 bills of 50$, 19 bill of 20$, 44 bill of 10$, 1 bill of 5$

</details>

## Objective

The main objective is to practice TDD and the SOLID principles.

## Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/python-code-katas)