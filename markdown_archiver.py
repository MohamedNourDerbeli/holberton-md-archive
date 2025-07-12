import requests
from bs4 import BeautifulSoup
import os
import sys
import re

def parse_project_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract Project Title (H1 tag)
    project_title_tag = soup.find('div', class_='project-header').find('h1') if soup.find('div', class_='project-header') else None
    project_title = project_title_tag.get_text(strip=True) if project_title_tag else 'No Project Title Found'
    # Sanitize title for filename
    sanitized_title = re.sub(r'[^a-zA-Z0-9_\-]', '', project_title.replace(' ', '_'))
    if not sanitized_title:
        sanitized_title = 'untitled_project'

    # Extract Project Image URL
    project_image_url = None
    main_image_div = soup.find('div', class_='panel-body text-justify')
    if main_image_div:
        img_tag = main_image_div.find('img')
        if img_tag and 'src' in img_tag.attrs:
            project_image_url = img_tag['src']

    # Extract Project Description (excluding image if present)
    project_description = ''
    description_panel_body = soup.find('div', class_='panel-body text-justify')
    if description_panel_body:
        if main_image_div and img_tag:
            img_tag.extract()
        paragraphs = description_panel_body.find_all('p')
        project_description = '\n\n'.join([p.get_text(strip=True) for p in paragraphs])

    # Extract Resources
    resources_section = soup.find('h2', string='Resources')
    resources_markdown = ''
    if resources_section:
        current_tag = resources_section.next_sibling
        while current_tag:
            if current_tag.name == 'h2':
                break
            if current_tag.name == 'h4':
                resources_markdown += f"#### {current_tag.get_text(strip=True)}\n\n"
            elif current_tag.name == 'ul':
                for li in current_tag.find_all('li'):
                    link = li.find('a')
                    if link and 'href' in link.attrs:
                        resources_markdown += f"* [{link.get_text(strip=True)}]({link['href']})\n"
                    else:
                        resources_markdown += f"* {li.get_text(strip=True)}\n"
                resources_markdown += "\n"
            current_tag = current_tag.next_sibling

    # Extract Learning Objectives
    learning_objectives_h2 = soup.find('h2', string='Learning Objectives')
    learning_objectives_markdown = ''
    if learning_objectives_h2:
        ul_tag = learning_objectives_h2.find_next_sibling('ul')
        if ul_tag:
            for li in ul_tag.find_all('li'):
                learning_objectives_markdown += f"* {li.get_text(strip=True)}\n"
            learning_objectives_markdown += "\n"

    # Extract Requirements
    requirements_h2 = soup.find('h2', string='Requirements')
    requirements_markdown = ''
    if requirements_h2:
        h3_tag = requirements_h2.find_next_sibling('h3')
        if h3_tag:
            requirements_markdown += f"### {h3_tag.get_text(strip=True)}\n\n"
            ul_tag = h3_tag.find_next_sibling('ul')
            if ul_tag:
                for li in ul_tag.find_all('li'):
                    requirements_markdown += f"* {li.get_text(strip=True)}\n"
                requirements_markdown += "\n"

    # Extract Tasks
    tasks_markdown = ''
    task_containers = soup.find_all('div', class_='panel panel-default task-card')
    for task_div in task_containers:
        # Skip the 'Tasks list' panel if it exists
        if task_div.find('h3', string='Tasks list'):
            continue

        task_title = task_div.find('h3', class_='panel-title')
        task_body = task_div.find('div', class_='panel-body')
        task_repo_info = task_div.find('div', class_='list-group-item')

        title = task_title.get_text(strip=True) if task_title else 'No Title'
        tasks_markdown += f"### {title}\n\n"

        if task_body:
            body_paragraphs = task_body.find_all('p', recursive=False)
            for p in body_paragraphs:
                tasks_markdown += f"{p.get_text(strip=True)}\n\n"

            body_lists = task_body.find_all('ul', recursive=False)
            for ul in body_lists:
                for li in ul.find_all('li'):
                    tasks_markdown += f"* {li.get_text(strip=True)}\n"
                tasks_markdown += "\n"

            code_example = task_body.find('pre')
            if code_example:
                tasks_markdown += f"```bash\n{code_example.get_text(strip=True)}\n```\n\n"

        if task_repo_info:
            tasks_markdown += f"**Repo Info:**\n"
            repo_ul = task_repo_info.find('ul')
            if repo_ul:
                for li in repo_ul.find_all('li'):
                    tasks_markdown += f"* {li.get_text(strip=True)}\n"
                tasks_markdown += "\n"

    # Construct the final Markdown output
    markdown_output = f"# Project: {project_title}\n\n"

    if project_image_url:
        markdown_output += f"![Project Image]({project_image_url})\n\n"

    markdown_output += f"## Description\n\n{project_description}\n\n"

    if resources_markdown:
        markdown_output += f"## Resources\n\n{resources_markdown}\n"

    if learning_objectives_markdown:
        markdown_output += f"## Learning Objectives\n\n{learning_objectives_markdown}\n"

    if requirements_markdown:
        markdown_output += f"## Requirements\n\n{requirements_markdown}\n"

    if tasks_markdown:
        markdown_output += f"## Tasks\n\n{tasks_markdown}\n"

    return markdown_output, sanitized_title


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3.11 parse_project.py <html_file_path_or_directory> [output_directory]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./parsed_projects"

    os.makedirs(output_dir, exist_ok=True)

    html_files = []
    if os.path.isfile(input_path):
        html_files.append(input_path)
    elif os.path.isdir(input_path):
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(('.html', '.htm')):
                    html_files.append(os.path.join(root, file))
    else:
        print(f"Error: Invalid input path: {input_path}")
        sys.exit(1)

    if not html_files:
        print(f"No HTML files found in {input_path}")
        sys.exit(0)

    for html_file_path in html_files:
        try:
            with open(html_file_path, 'r') as f:
                html_content = f.read()
        except FileNotFoundError:
            print(f"Error: File not found at {html_file_path}")
            continue

        markdown_output, sanitized_title = parse_project_html(html_content)

        output_filename = os.path.join(output_dir, f"{sanitized_title}.md")

        with open(output_filename, 'w') as f:
            f.write(markdown_output)

        print(f"Project information successfully extracted from {html_file_path} and saved to {output_filename}")

