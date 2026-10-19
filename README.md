# Formal Languages Toolkit

A collection of Python implementations for core topics in formal languages and compiler construction: finite automata, token recognition, FIRST/FOLLOW sets, and shift-reduce parsing.

This repository consolidates four academic projects into a single, organized toolkit. Each module can be executed independently and includes sample inputs.

## Included modules

| Module | What it demonstrates | Entry point |
| --- | --- | --- |
| [NFA to DFA conversion](./automata-conversion/) | Epsilon closure and subset construction | `automata-conversion/main.py` |
| [Token recognition](./token-recognition/) | Finite-automaton recognition of selected C keywords and operators | `token-recognition/main.py` |
| [FIRST and FOLLOW](./first-follow/) | FIRST/FOLLOW calculation for simple context-free grammars | `first-follow/first_and_follow.py` |
| [Shift-reduce parser](./shift-reduce-parser/) | Stack-based shift and reduce operations using grammar files | `shift-reduce-parser/sr.py` |

## Requirements

- Python 3.8 or newer
- No third-party dependencies

## Quick start

Clone the repository:

```bash
git clone https://github.com/dev1206al/formal-languages-toolkit.git
cd formal-languages-toolkit
```

Run any module from the repository root:

```bash
python3 automata-conversion/main.py
python3 token-recognition/main.py
python3 first-follow/first_and_follow.py
python3 shift-reduce-parser/sr.py
```

The shift-reduce parser asks for a grammar file. For example:

```text
shift-reduce-parser/examples/gram1.txt
```

## Module details

### 1. NFA to DFA conversion

Implements the subset-construction algorithm, including epsilon closures, to transform a nondeterministic finite automaton into a deterministic one. The included examples print transition tables, initial states, final states, and sink-state transitions.

### 2. Token recognition

Builds a finite automaton that recognizes a small set of C-language tokens:

- Keywords: `if`, `int`, `else`, `while`
- Operators or expressions: `i`, `i++`

The sample runner evaluates valid and invalid strings and reports whether each one is accepted.

### 3. FIRST and FOLLOW sets

Loads a context-free grammar from a text file and calculates FIRST and FOLLOW sets for its non-terminal symbols. Ten sample grammars are available under [`first-follow/examples`](./first-follow/examples/).

By default, the program uses `grammar5.txt`. A different example can be selected in `first_and_follow.py`.

### 4. Shift-reduce parser

Demonstrates bottom-up parsing through a stack and two central operations:

- **Shift:** moves the next input token to the stack.
- **Reduce:** replaces a matching right-hand side with its production's left-hand side.

Six sample grammars are included under [`shift-reduce-parser/examples`](./shift-reduce-parser/examples/).

## Repository structure

```text
formal-languages-toolkit/
├── automata-conversion/
│   ├── logic.py
│   └── main.py
├── token-recognition/
│   ├── af.py
│   └── main.py
├── first-follow/
│   ├── examples/
│   ├── notes/
│   └── first_and_follow.py
├── shift-reduce-parser/
│   ├── examples/
│   └── sr.py
├── docs/images/
└── README.md
```

## Scope

These implementations are educational demonstrations of the underlying algorithms. They are intentionally compact and are not intended to replace production lexer or parser generators.

## Author

**Luis Enrique Alvarez Segura**  
Computer Engineering graduate, Universidad Autónoma Metropolitana (UAM)

- [GitHub](https://github.com/dev1206al)
- [LinkedIn](https://www.linkedin.com/in/luis-enrique-alvarez-segura/)

