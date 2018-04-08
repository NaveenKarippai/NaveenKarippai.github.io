#!/bin/bash
set -ev
[ -f content/*/*.md ] && hint content/*/*.md
[ -f content/*/*.rst ] && rst-lint content/*/*.rst
[ -f content/*.md ] && hint content/*.md
[ -f content/*.rst ] && rst-lint content/*.rst
