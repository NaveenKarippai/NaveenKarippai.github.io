#!/bin/bash
set -ev
md2=`ls -l content/*/*.md 2>/dev/null | wc -l`
md1=`ls -l content/*.md 2>/dev/null | wc -l`
rst2=`ls -l content/*/*.rst 2>/dev/null | wc -l`
rst1=`ls -l content/*.rst 2>/dev/null | wc -l`

if [ $md2 -ne 0 ]; then
	 hint content/*/*.md
fi
if [ $rst1 -ne 0 ]; then
 	rst-lint content/*.rst
fi
if [ $rst2 -ne 0 ]; then
 	rst-lint content/*/*.rst
fi
if [ $md1 -ne 0 ]; then
	hint content/*.md
fi
