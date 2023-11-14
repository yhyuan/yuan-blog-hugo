---
title: "Cargo Commands"
date: 2023-11-13T10:52:47-05:00
tags: ['rust']
draft: false
---

## Cargo Commands
* `cargo new`
* `cargo run`
* `cargo build`
* `cargo fmt` (`rustup component add rustfmt`)
    * .rustfmt.toml configuration
```toml
format_code_in_doc_comments = true
group_imports = "StdExternalCrate"
imports_granularity = "Module"
unstable_features = true
version = "Two"
wrap_comments = true
```
* `cargo clippy` (`rustup component add clippy`) Code lint (.clippy.toml)
* `cargo install sccache`  Reducing compile times with sccache
    * useage 
```
$ export RUSTC_WRAPPER=`which sccache` 
$ cargo build
```
* `cargo install cargo-update`: makes it easy to update your Cargo packages.
* `cargo install cargo-expand`: lets you expand macros to see the resulting code.
* `cargo install cargo-fuzz`: let’s you easily integrate with libFuzzer for fuzz testing.
* `cargo install cargo-watch`: automates re-running Cargo commands on code changes.
* `cargo install cargo-tree`: lets you visualize project dependency trees
* `cargo install -f cargo-outdated`: outdated dependencies
* `cargo install -f cargo-audit`: avoid vunnerability
