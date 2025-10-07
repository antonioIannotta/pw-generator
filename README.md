# 🔐 pw-generator-cli

A simple, customizable **command-line password generator** built with [Typer](https://typer.tiangolo.com/).

---

## ✨ Features

- Generate secure random passwords directly from your terminal
- Choose custom password lengths
- Two commands: a default generator and a "complex" generator variant
- Lightweight and dependency-free (besides Typer)

---

## 📦 Installation

You can install the package locally (during development) with:

```bash
git clone https://github.com/<your-username>/pw-generator-cli.git
cd pw-generator-cli
pip install -e .
```
Or, once published to PyPI:

```bash
pip install pw-generator-cli
```

## 🚀 Usage
After installation, a command named pwgen will be available globally.

### 🧱 Basic Commands
Generate a standard password
```bash
pwgen generate
Output:
Generating passwords...
aP$3B!r9Qd
```
Generate a password with a specific length
```bash
pwgen generate --length 16
Output:
Generating passwords...
T1@bXh9!mP$2sFqC
```
Generate a complex password (same logic, alternate command)
```bash
pwgen genc --length 20
Output:
Generating passwords...
fP#3xK7nT@wD!9qG%rA1
```
## 🧠 How It Works
The password generator combines:

- Uppercase & lowercase letters (A–Z, a–z)

- Numbers (0–9)

- Symbols (from string.punctuation)

- Passwords are generated using Python’s built-in random module.

Default password length is 10 characters.

## ⚙️ Development
To run directly (without installing):

```bash
python -m pwgen.cli generate --length 12
```

To build a distributable package:
```bash
python -m build
```

## 🧾 License
This project is licensed under the MIT License — see the LICENSE file for details.

- 👤 Author
Antonio Iannotta
- 📧 antonio.iannotta.ai26@gmail.com






