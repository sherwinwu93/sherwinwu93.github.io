#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import os

def split_into_clauses(text):
    """
    将文本按段落、句子、子句分割：
    1. 先按空行分割段落
    2. 每个段落内合并所有换行为空格
    3. 按句子结束标点 .?! 分割句子
    4. 每个句子内按 ,;: 拆分子句（保留分隔符）
    5. 第一个子句无缩进，其余缩进两个空格
    """
    # 按空行分割段落（支持多个空行）
    paragraphs = re.split(r'\n\s*\n', text.strip())
    result = []
    
    for para in paragraphs:
        if not para.strip():
            continue
        
        # 合并段落内的所有换行为空格，压缩多余空格
        para = ' '.join(para.split())
        
        # 按句子分割（保留结尾标点）
        sentences = []
        current = ''
        i = 0
        n = len(para)
        in_quote = False
        in_single_quote = False
        
        while i < n:
            ch = para[i]
            current += ch
            
            if ch == '"':
                in_quote = not in_quote
            elif ch == "'" and (i == 0 or para[i-1] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                in_single_quote = not in_single_quote
            
            if ch in '.?!' and not in_quote and not in_single_quote:
                # 检查是否是缩写（简单判断）
                if ch == '.' and i + 1 < n and para[i+1] == ' ':
                    words = current.split()
                    if words:
                        last_word = words[-1]
                        abbreviations = {'Mr', 'Mrs', 'Ms', 'Dr', 'Prof', 'Sr', 'Jr', 
                                       'etc', 'vs', 'e.g', 'i.e', 'inc', 'corp', 'co',
                                       'St', 'Ave', 'Blvd', 'Rd', 'Ste'}
                        if last_word in abbreviations or re.match(r'^\d+(st|nd|rd|th)$', last_word):
                            i += 1
                            continue
                
                if current.strip():
                    sentences.append(current.strip())
                    current = ''
            
            i += 1
        
        if current.strip():
            sentences.append(current.strip())
        
        # 处理每个句子，拆分子句
        for sent in sentences:
            # 按逗号、分号、冒号分割，但保留分隔符
            parts = re.split(r'(?<=[,;:])', sent)
            clauses = []
            for p in parts:
                p = p.strip()
                if p:
                    clauses.append(p)
            
            if len(clauses) <= 1:
                result.append(sent)
            else:
                result.append(clauses[0])
                for clause in clauses[1:]:
                    result.append('  ' + clause)
        
        # 段落结束添加空行
        result.append('')
    
    # 移除末尾多余空行
    while result and result[-1] == '':
        result.pop()
    
    return result

def format_for_org(text, title):
    """
    将文本转换为 Org-mode 格式
    """
    lines = split_into_clauses(text)
    
    org_content = []
    org_content.append('#+OPTIONS: \\n:t toc:nil num:nil html-postamble:nil')
    org_content.append('#+HTML_HEAD_EXTRA: <style>body {background: rgb(193, 230, 198) !important;}</style>')
    org_content.append(f'* {title}')
    org_content.append('#+begin_verse')
    org_content.extend(lines)
    org_content.append('#+end_verse')
    
    return '\n'.join(org_content)

def main():
    if len(sys.argv) != 2:
        print("用法: python handle-text.py <文件名.txt>")
        print("示例: python handle-text.py \"July 31th stoic joy.txt\"")
        sys.exit(1)
    
    input_file = sys.argv[1]
    base_name = os.path.splitext(input_file)[0]
    output_file = base_name + '.org'
    title = base_name
    
    if not os.path.exists(input_file):
        print(f"❌ 错误: 文件 '{input_file}' 不存在")
        sys.exit(1)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"❌ 读取文件错误: {e}")
        sys.exit(1)
    
    # 将所有弯引号替换为直引号
    text = text.replace('‘', "'").replace('’', "'").replace('“', "'").replace('”', "'").replace('"', "'")
    
    result = format_for_org(text, title)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"✅ 转换完成！")
        print(f"📥 输入: {input_file}")
        print(f"📤 输出: {output_file}")
        print(f"📝 标题: {title}")
        print(f"📊 行数: {len(result.splitlines())}")
        
        lines = result.splitlines()
        preview_lines = min(25, len(lines))
        print("\n" + "="*60)
        print(f"预览 (前{preview_lines}行):")
        print("="*60)
        for line in lines[:preview_lines]:
            print(line if line else '(空行)')
        if len(lines) > preview_lines:
            print(f"... (共{len(lines)}行)")
        print("="*60)
        
    except Exception as e:
        print(f"❌ 写入文件错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
