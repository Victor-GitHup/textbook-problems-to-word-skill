---
name: textbook-problems-to-word
description: Extract specified numbered exercises from a PDF textbook as complete visual crops and assemble a print-ready Word homework sheet with answer space. Use when an assignment lists textbook pages and problem numbers; do not use for solving the problems.
---

# Textbook problems to Word

Create a Word document containing the requested title, one complete problem image per page, and blank space for handwritten answers. Preserve formulas, diagrams, subparts, and figure captions as images. Include assignment-specific instructions only when the user supplies them.

## First use

This skill needs a local Python 3 runtime with the packages in [requirements.txt](requirements.txt), plus Poppler's `pdftoppm` command. Run `python3 scripts/check_environment.py` from this skill directory. Install missing dependencies using the host's package manager and run the check again. If the user has not yet supplied a textbook and problem list, reply **exactly** `已安装完成，请上传习题来源文件以及作业对应题号` only after the check succeeds. If setup cannot be completed, state what is missing instead of claiming success. A chat without file access and code execution cannot run this workflow.

## Workflow

1. Read the assignment list and identify the exact textbook edition. Use the table of contents and printed page labels to map each cited page to a PDF page index; do not assume they are equal. Search the relevant pages for each problem number, then visually inspect each page.
2. For every problem, choose one crop rectangle containing its number, full wording, all subparts, the complete referenced figure, and its caption. Exclude neighboring problems. If a problem spans pages or disjoint page regions, capture the necessary pieces and combine them in reading order into one image. Keep the image legible at the intended print size.
3. Make a small JSON recipe with `pdf`, `title`, `output`, and `problems`. Each problem has `number`, `pdf_page` (one-based), and `crop` (`[left, top, right, bottom]` in PDF points). For a split problem, use `parts` instead: an ordered list of objects with `pdf_page` and `crop`; the script joins them vertically. Optionally add `note` for instructions supplied by the assignment. Inspect the crops before publishing. Run [make_homework.py](scripts/make_homework.py) with the available Python runtime.
4. Render the resulting `.docx` to page images with an available Word renderer (for example LibreOffice then `pdftoppm`, or the host's document tools). Inspect **every** page for the right number, complete diagrams and captions, readable scale, no neighboring exercises, and enough answer space. Correct crop coordinates and repeat as needed. Check the final page count and embedded image count against the assignment list. If rendering is unavailable, report that visual verification was not completed.

Treat page matching and crop bounds as visual decisions; text extraction can help locate candidates but cannot validate formulas or figures. For a different textbook layout, adjust the crop and page design rather than forcing a fixed template. Blackboard or other assignment-site integration is outside this local document workflow unless the user explicitly requests it and grants access.

## Example recipe

```json
{
  "pdf": "/absolute/path/textbook.pdf",
  "title": "Homework 3",
  "output": "/absolute/path/Homework 3.docx",
  "problems": [
    {"number": "3.20", "pdf_page": 117, "crop": [105, 98, 320, 265]}
  ]
}
```
