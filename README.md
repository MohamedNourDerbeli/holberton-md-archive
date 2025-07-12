# 📝 Project Markdown Exporter

This tool parses HTML files of project pages and converts them into clean, structured Markdown (`.md`) files. Ideal for backing up, reviewing, or sharing your technical project documentation offline or on platforms like GitHub.

---

## 📦 Features

- Extracts and formats:
  - ✅ Project Title
  - ✅ Main Project Image
  - ✅ Description
  - ✅ Resources (with links)
  - ✅ Learning Objectives
  - ✅ Requirements
- Supports both single file and full directory input
- Auto-sanitizes file names for compatibility
- Outputs Markdown files to a customizable folder

---

## 🛠 Usage

```bash
python3.11 parse_project.py <html_file_path_or_directory> [output_directory]
