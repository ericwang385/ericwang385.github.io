---
title: "Eric Chengyuan Wang"
date: 2025-01-08
lastmod: 2026-10-20
description: "Computer Science Ph.D. student at Stevens Institute of Technology. Research in programming languages, formal methods, compiler correctness, and systems verification."
draft: false
---

![Eric Chengyuan Wang](/images/Profile.jpg)

## Ph.D. Student in Computer Science

**Stevens Institute of Technology**\
**Advisor:** Michael Greenberg\
**Email:** [cwang7@stevens.edu](mailto:cwang7@stevens.edu)\
**Phone:** +1 551 344 5797\
**GitHub:** [ericwang385](https://github.com/ericwang385/)\
[**Download CV**](/cv/Resume.pdf)

---

[About](#about-me) · [Research](#research) · [Publications](#publications) · [Education](#education) · [Experience](#professional-experience) · [Skills](#technical-skills) · [Awards](#honors--awards)

## About Me

I am Eric Chengyuan Wang, a Ph.D. student in Computer Science at Stevens Institute of Technology. My advisor is Michael Greenberg. My research focuses on programming languages and formal methods, with particular interest in compiler correctness and the verification of systems software.

My current work includes POSIX shell compiler verification, incremental execution, and eBPF verification. I work on the incrementalization and eBPF projects with ATLAS Lab at Brown University. I expect to graduate in May 2028.

**Internship availability:** May–September 2027. I am interested in formal methods and compiler engineering roles.

### Research Interests

- Programming languages, type systems, and effect handlers.
- Compiler optimization and correctness.
- Language-based security, information-flow control, and system verification.

## Research

### POSIX Shell Compiler Verification

**October 2023–present · Hoboken, USA**

I am developing a Coq model of core POSIX shell features, including pipelines and background commands. The model includes process management and filesystem behavior. I am working to verify that shell programs parallelized by PaSh are equivalent to their sequential execution.

### Incrementalization System Verification

**ATLAS Lab, Brown University · June 2026–present · Providence, USA**

I am formalizing the execution semantics of a system that adds incremental execution to shell programs. I am working to establish an equivalence relation between incremental execution and standard shell execution under specified assumptions.

### eBPF Verification in Lean

**ATLAS Lab, Brown University · July 2026–present · Providence, USA**

I built a C-like DSL in Lean for writing eBPF programs. It supports eBPF helper functions and familiar C-style programming constructs. The project goal is to integrate this work with the Linux kernel to support the eBPF verifier.

### Safe Gradual Type Migration

**September 2022–June 2024 · Hoboken, USA**

I designed an inference-based algorithm to migrate untyped programs to gradually typed programs. I defined migration safety as introducing no new static errors. I proved this property for the proposed algorithm and existing migration approaches.

### Static Policy Enforcement for a Functional Programming Language

**Master's thesis · February–June 2022 · Gothenburg, Sweden**

I formalized purpose limitation, a policy in the General Data Protection Regulation (GDPR). I designed an information-flow control type system to check this policy statically and implemented it in Haskell. I formalized the type system in Agda and proved soundness and noninterference.

## Publications

### Accepted: CVPR 2020

**A Neural Rendering Framework for Free-Viewpoint Relighting**\
Zhang Chen, Anpei Chen, Guli Zhang, **Chengyuan Wang**, Yu Ji, Kiriakos N. Kutulakos, and Jingyi Yu.

[Paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chen_A_Neural_Rendering_Framework_for_Free-Viewpoint_Relighting_CVPR_2020_paper.pdf) · [arXiv](https://arxiv.org/abs/1911.11530) · [Code](https://github.com/LansburyCH/relightable-nr)

**MARS Lab · September 2019–February 2020 · Shanghai, China**

I built a relightable rendering model. I used a graph neural network (GNN) to extract 3D features from point clouds.

### Target Venues

- **POPL 2028:** [POSIX Shell Compiler Verification](#posix-shell-compiler-verification).
- **PLDI 2027:** [Safe Gradual Type Migration](#safe-gradual-type-migration) and [Incrementalization System Verification](#incrementalization-system-verification).

## Education

### Ph.D., Computer Science

**Stevens Institute of Technology · September 2022–present**\
Expected graduation: **May 2028**. Advisor: **Michael Greenberg**.

### M.Eng., Computer Science and Engineering

**Chalmers University of Technology · September 2020–June 2022**

### B.Eng., Computer Science and Engineering

**Shanghai University · August 2016–June 2020**

## Selected Projects

### Compiler for a Fragment of Java

**Individual project · March–June 2021 · Gothenburg, Sweden**

I implemented a lexer, parser, and LLVM intermediate representation (IR) code generator in Rust for a subset of Java. I also implemented LLVM optimization passes for the generated code.

## Professional Experience

### Backend as a Service Framework

**Synyi Tech · June–August 2021 · Shanghai, China**

I contributed to a Go framework for a medical information system. The framework automatically generates APIs for create, read, update, and delete (CRUD) operations. It combines policy-based authentication with a TypeScript DSL for frontend interaction.

### R&D Intern

**DGene Tech · March 2019–May 2020 · Shanghai, China**

I worked on a 3D face reconstruction project. I built and compressed a neural network and deployed it on an Android phone.

## Technical Skills

- **Programming languages:** Rust, C/C++, Haskell, Go, Python, TypeScript, and MATLAB.
- **Proof assistants:** Lean, Coq, and Agda.
- **Compiler tools:** LLVM.
- **Machine learning tools:** PyTorch.

## Honors & Awards

- **Second Class Prize**, ASC Student Supercomputer Challenge, 2019.
- **Silver medal**, TensorFlow Speech Recognition Challenge on Kaggle.

## Languages

- **Mandarin Chinese:** Native speaker.
- **English:** Fluent.

---

*Last updated: October 20, 2026.*
