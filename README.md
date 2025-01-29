# :snake: Python Code Katas :snake:

> [!NOTE]
> All the code katas are solved using Python. Most of the katas are configured in a similar way, using uv as package manager and python 3.12.
> Those katas that need extra or different configurations will have its specific instructions in the README file.

[![Python](https://img.shields.io/badge/Python-3.12+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Standard Configuration

The project can be configured either by using `pip` or `pyenv`. Both ways will be explained.

<details><summary>Using pip</summary>

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
2. Activate the virtual environment:
    ```bash
    source .venv/bin/activate # Linux / Mac
    .venv\Scripts\activate # Windows
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
</details>

<details><summary>Using pyenv and uv</summary>

These instructions are extracted from pyenv documentation. You can find everything [here](https://github.com/pyenv/pyenv?tab=readme-ov-file)

1. Install pyenv:
    ```bash
    curl https://pyenv.run | bash
    ```
2. Set you bash profile to load pyenv. In my case I use fish:

    ```bash
    set -Ux PYENV_ROOT $HOME/.pyenv
    fish_add_path $PYENV_ROOT/bin
   
    echo pyenv init - | source >> ~/.config/fish/config.fish
    ```
3. Select the python version you want to use:
    ```bash
    pyenv install 3.12
    pyenv local 3.12
    ```
   
4. Install the dependencies:
    ```bash
    pip install uv
    uv sync --all-groups
    ```
</details>

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
uv run pytest kata_name/tests
```

> [!NOTE]
> I tend to use a Makefile to store the most common commands. You can check the Makefile in the root of the project.

## Katas

- [x] [FizzBuzz](fizz_buzz/README.md)
- [x] [Leap Year](leap_year/README.md)
- [x] [Gilded Rose Refactoring](gilded_rose/README.md)
- [x] [Parallel Change Refactoring](parallel_change/README.md)
- [x] [Tire Pressure](tire_pressure/README.md)
- [x] [Tell Don't Ask](tell_dont_ask/README.md)
- [ ] [Character Copier](character_copier/README.md)
- [ ] [Bags](bags/README.md)
- [ ] [ATM Machine](atm/README.md)
- [x] [Trip Service](trip_service/README.md)
- [x] [Tic Tac Toe](tic_tac_toe/README.md)
- [ ] [Ohce](ohce/README.md)

## Visit my GitHub profile for more projects 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py)
