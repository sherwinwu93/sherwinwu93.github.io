#!/bin/bash
# 清除或创建 xx.txt
> xx.txt
for f in *.txt; do
    # 防止无匹配时保留 "*" 本身
    [ -e "$f" ] || continue
    base="${f%.txt}"
    printf "\t<h3><a href=\"%s.html\">%s</a></h3>\n" "$base" "$base"
done >> xx.txt
