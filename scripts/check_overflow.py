#!/usr/bin/env python3
"""
ตรวจสอบ overflow ใน Marp slides
"""
import re
from pathlib import Path

def count_content_lines(content):
    """นับบรรทัดเนื้อหา (ไม่รวม markdown syntax)"""
    lines = content.split('\n')
    content_lines = []
    in_code_block = False
    
    for line in lines:
        # ตรวจสอบ code block
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            content_lines.append(line)
            continue
        
        # นับบรรทัดใน code block
        if in_code_block:
            content_lines.append(line)
            continue
        
        # ข้ามบรรทัดว่าง
        if not line.strip():
            continue
        
        # ข้าม markdown div tags
        if line.strip().startswith('<div') or line.strip().startswith('</div'):
            continue
        
        # ข้าม markdown separators
        if line.strip() == '---':
            continue
        
        # นับบรรทัดเนื้อหา
        content_lines.append(line)
    
    return len(content_lines)

def split_slide_by_sections(content):
    """แบ่ง slide ออกเป็นส่วนๆ"""
    sections = []
    current_section = []
    
    lines = content.split('\n')
    for line in lines:
        # ตรวจสอบหัวข้อใหม่
        if line.strip().startswith('# ') and not line.strip().startswith('## '):
            if current_section:
                sections.append('\n'.join(current_section))
            current_section = [line]
        else:
            current_section.append(line)
    
    if current_section:
        sections.append('\n'.join(current_section))
    
    return sections

def check_overflow(filepath):
    """ตรวจสอบ overflow ในไฟล์"""
    content = Path(filepath).read_text(encoding='utf-8')
    
    # แบ่ง slides
    slides = content.split('\n---\n')
    
    print(f"ตรวจสอบไฟล์: {filepath}")
    print(f"จำนวน slides ทั้งหมด: {len(slides)}")
    print("=" * 80)
    
    overflow_slides = []
    
    for i, slide in enumerate(slides, 1):
        # ข้าม YAML frontmatter (chunk แรกที่ marp: true)
        if i == 1 and 'marp: true' in slide:
            continue
        
        # นับบรรทัดเนื้อหา
        line_count = count_content_lines(slide)
        
        # ตรวจสอบว่ามี code block ไหม
        code_blocks = len(re.findall(r'```', slide))
        
        # ตรวจสอบว่ามี tables ไหม
        tables = len(re.findall(r'\|.*\|.*\|', slide))
        
        # ตรวจสอบว่ามี columns ไหม
        has_columns = '<div class="columns">' in slide
        
        # Threshold สำหรับ overflow
        # - ปกติ: < 25 บรรทัด
        # - มี code blocks: < 35 บรรทัด
        # - มี tables: < 30 บรรทัด
        # - มี columns: < 40 บรรทัด
        
        threshold = 25
        if code_blocks > 0:
            threshold = 35
        if tables > 0:
            threshold = 30
        if has_columns:
            threshold = 40
        
        # ตรวจสอบ overflow
        if line_count > threshold:
            # ดึงหัวข้อ
            title_match = re.search(r'^#\s+(.+)$', slide, re.MULTILINE)
            title = title_match.group(1) if title_match else f"Slide {i}"
            
            overflow_slides.append({
                'number': i,
                'title': title,
                'line_count': line_count,
                'threshold': threshold,
                'code_blocks': code_blocks,
                'tables': tables,
                'has_columns': has_columns
            })
    
    # แสดงผล
    if overflow_slides:
        print(f"\n⚠️  พบ {len(overflow_slides)} slides ที่อาจ overflow:\n")
        for slide in overflow_slides:
            print(f"Slide {slide['number']}: {slide['title']}")
            print(f"  - บรรทัด: {slide['line_count']} (threshold: {slide['threshold']})")
            print(f"  - Code blocks: {slide['code_blocks']}")
            print(f"  - Tables: {slide['tables']}")
            print(f"  - Has columns: {slide['has_columns']}")
            print()
    else:
        print("\n✅ ไม่พบ overflow")
    
    return overflow_slides

if __name__ == '__main__':
    filepath = '/home/seiya/projects/ai-powered-internal-developer-framework/slides/meeting-presentation.md'
    overflow_slides = check_overflow(filepath)
