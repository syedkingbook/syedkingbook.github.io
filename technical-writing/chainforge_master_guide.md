---
layout: default
title: "ChainForge Docs as Code Implementation"
---


# ChainForge Docs as Code Implementation

**Comprehensive Master Reference** | **Version:** 2.0.0 | **Scope:** Full Pipeline & Python SDK Architecture

---

## Table of Contents

[Executive Summary and Core Philosophy](#1-executive-summary--core-philosophy)

[Phase 1: Environment Bootstrapping and Git Initialization](#2-phase-1-environment-bootstrapping--git-initialization)

[Phase 2: MkDocs Material and Navigation Architecture](#3-phase-2-mkdocs-material--navigation-architecture)

[Phase 3: Python SDK Modularization and Design Patterns](#4-phase-3-python-sdk-modularization--design-patterns)

[Phase 4: Dynamic API Reference Integration (mkdocstrings)](#5-phase-4-dynamic-api-reference-integration-mkdocstrings)

[Phase 5: Verification, Execution and Live-Reload Feedback Loop](#6-phase-5-verification-execution--live-reload-feedback-loop)

---

## Executive Summary and Core Philosophy

Modern developer infrastructure demands absolute synchronization between codebases and documentation. Traditional static workflows (such as exporting static PDFs or manual wiki updates) suffer from chronic version drift. This article provides steps to implement Docs as Code for a Blockchain product ChainForge. The ChainForge Docs as Code pipeline bridges this gap by merging core SDK implementation with automated documentation generation using MkDocs, Material themes, and `mkdocstrings`.

---

## Phase 1: Environment Bootstrapping and Git Initialization

Before authoring documentation, ensure your local development workstation has Python 3.9+ and Git installed. If Git is missing in Windows, deploy it via `winget`:

```powershell
winget install --id Git.Git -e --source winget
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```

Next, instantiate your local workspace directory and isolate dependencies inside a virtual environment:

```powershell
mkdir chainforge-docs
cd chainforge-docs
python -m venv venv
.\venv\Scripts\Activate.ps1
git init
```

---

## Phase 2: MkDocs Material and Navigation Architecture

To configure the developer portal layout, features, and syntax highlighters, create your `mkdocs.yml` configuration file in the project root:

```yaml
site_name: ChainForge Developer Portal
site_description: Documentation for ChainForge Smart Contract Blockchain
theme:
  name: material
  palette:
    primary: indigo
    accent: light blue
  features:
    - navigation.tabs
    - content.code.copy
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [.]
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.def_list_handler
nav:
  - Home: index.md
  - Architecture: architecture.md
  - API Reference: api-reference.md
  - SDK Quickstart: sdk-quickstart.md
  - Master Guide: master-guide.md
```

---

## Phase 3: Python SDK Modularization and Design Patterns

To turn raw scripts into a professional installable package (`chainforge-sdk`), structure your codebase into a dedicated folder with a declarative `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61.0.0"]
build-backend = "setuptools.build_meta"

[project]
name = "chainforge-sdk"
version = "1.0.0"
description = "Official sample Python SDK for ChainForge Developer Platform"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.25.0",
]
```

Organize internal client modules inside `chainforge_sdk/client.py` with robust docstrings so that `mkdocstrings` can parse them automatically:

```python
class DotDict(dict):
    """Allows dot notation access to dictionary keys (e.g., bal.balanceFormatted)."""
    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        raise AttributeError(f"'DotDict' object has no attribute '{attr}'")
```

---

## Phase 4: Dynamic API Reference Integration (mkdocstrings)

Instead of maintaining manual API documentation in static PDFs, create `docs/api-reference.md` and inject the live client module directly:

```markdown
# API Reference

Below is the programmatically injected API reference parsed live from the Python SDK codebase.

::: chainforge_sdk.client
    options:
      show_root_heading: true
      show_source: true
```

---

## Phase 5: Verification, Execution and Live-Reload Feedback Loop

Perform an editable installation of your SDK package so that local code modifications reflect immediately:

```powershell
pip install -e .
pip install mkdocs-material mkdocstrings mkdocstrings-python
```

Execute your balance verification script and launch the MkDocs development server:

```powershell
$env:CHAINFORGE_API_KEY="cfk_test_123456789"
python check_balance.py
python -m mkdocs serve
```

Navigate to `http://127.0.0.1:8000` in your browser. Any edit made to your Markdown files or Python docstrings will instantly trigger a live reload, completing the closed-loop Docs-as-Code architecture.

## Project link:
Refer to the following Github link for Docs as Code project demonstration:
https://github.com/syedkingbook/ChainForge-Docs-as-Code-Python-SDK-Framework