# :pager: Ohce Kata :pager:
        
## Resources

These instructions where extracted from Kata Log website. The link to the original instructions can be found in the link bellow.

[![Web](https://img.shields.io/badge/Kata-Log-14a1f0?style=for-the-badge&logo=web&logoColor=white&labelColor=101010)](https://kata-log.rocks/ohce-kata)

## Description

Ohce is a console application that echoes the reverse of what you input through the console.

Even though it seems a silly application, ohce knows a thing or two.

1. When you start ohce, it greets you differently depending on the current time, but only in Spanish:
    - Between 20 and 6 hours, ohce will greet you saying: ¡Buenas noches < your name >!
    - Between 6 and 12 hours, ohce will greet you saying: ¡Buenos días < your name >!
    - Between 12 and 20 hours, ohce will greet you saying: ¡Buenas tardes < your name >!
2. When you introduce a palindrome, ohce likes it and after reverse-echoing it, it adds ¡Bonita palabra!
3. Ohce knows when to stop, you just have to write Stop! and it'll answer Adios < your name > and end.

<details><summary>Example</summary>

```bash
$ ohce Pedro
> ¡Buenos días Pedro!
$ hola
> aloh
$ oto
> oto
> ¡Bonita palabra!
$ stop
> pots
$ Stop!
> Adios Pedro
```
</details>

## Objective

This kata is going to be developed applying an Outside-In TDD approach.

## Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/python-code-katas)