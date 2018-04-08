#!/bin/bash
set -ev
md2=`ls -l content/*/*.md 2>/dev/null | wc -l`
md1=`ls -l content/*.md 2>/dev/null | wc -l`
rst2=`ls -l content/*/*.rst 2>/dev/null | wc -l`
rst1=`ls -l content/*.rst 2>/dev/null | wc -l`

[ $md2 != 0 ] && hint content/*/*.md
[ $md1 != 0 ] && hint content/*.md
[ $rst1 != 0 ] && rst-lint content/*.rst
[ $rst2 != 0 ] && rst-lint content/*/*.rst
