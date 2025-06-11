# Jupyter to Markdown Setup Instructions

## GitHub Actions Workflow

Create `.github/workflows/mermaid.yml`:

```bash
mkdir -p .github/workflows

cat > .github/workflows/mermaid.yml << 'EOF'
name: Convert Notebooks
on:
  push:
    paths: ['**.ipynb']
jobs:
  convert:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      
      - name: Install jupyter
        run: pip install jupyter
      
      - name: Convert notebooks to markdown
        run: |
          find . -name "*.ipynb" -exec jupyter nbconvert --to markdown {} \;
      
      - name: Commit files
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "Convert notebooks to markdown" || echo "No changes to commit"
          git push
EOF
```

## Git Configuration

```bash
# Disable rebase on pull
git config pull.rebase false

# Create sync alias with auto-merge
git config --global alias.sync '!git pull --no-edit && git push'
```

## TOC Generator Script

Create `scripts/generate_toc.py`:

```bash
mkdir -p scripts

cat > scripts/generate_toc.py << 'EOF'
import json
import sys
import os
import glob

def generate_toc(notebook_path, update_in_place=False):
    with open(notebook_path, 'r') as f:
        nb = json.load(f)
    
    headers = []
    toc_cell_index = None
    
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            content = ''.join(cell['source'])
            
            # Check for TOC marker
            if '<!-- TOC -->' in content:
                toc_cell_index = i
            
            # Extract headers
            for line in content.split('\n'):
                if line.startswith('#'):
                    level = len(line.split(' ')[0])
                    title = line.strip('#').strip()
                    anchor = title.lower().replace(' ', '-').replace(':', '')
                    headers.append((level, title, anchor))
    
    # Generate TOC
    toc_lines = ["<!-- TOC -->", "# Table of Contents", ""]
    for level, title, anchor in headers:
        if level > 1:  # Skip main title
            indent = '  ' * (level - 2)
            toc_lines.append(f"{indent}- [{title}](#{anchor})")
    toc_lines.extend(["", "<!-- /TOC -->"])
    
    if update_in_place and toc_cell_index is not None:
        # Convert to notebook cell format (list of lines with \n)
        nb['cells'][toc_cell_index]['source'] = [line + '\n' for line in toc_lines]
        with open(notebook_path, 'w') as f:
            json.dump(nb, f, indent=1)
        return True
    return False

if __name__ == '__main__':
    update = '--update' in sys.argv
    
    # Check if --all flag is used
    if '--all' in sys.argv:
        notebooks = glob.glob('notebooks/*.ipynb')
        updated = 0
        for nb in notebooks:
            if generate_toc(nb, update):
                print(f"Updated TOC in {nb}")
                updated += 1
        print(f"\nProcessed {len(notebooks)} notebooks, updated {updated}")
    else:
        notebook = [arg for arg in sys.argv[1:] if not arg.startswith('--')][0]
        if generate_toc(notebook, update):
            print(f"Updated TOC in {notebook}")
        else:
            toc = generate_toc(notebook, False)
EOF
```

## Create TOC Alias

```bash
echo -e "\n# 📚 TOC Generator Alias - Added $(date +%Y-%m-%d)\nalias toc='python scripts/generate_toc.py --all --update'" >> ~/.zshrc
```

## Usage

1. Add `<!-- TOC -->` in a markdown cell where you want the table of contents
2. Run `toc` to generate TOC for all notebooks
3. Use `git sync` to push and pull changes

## Directory Structure

```
project/
├── .github/
│   └── workflows/
│       └── mermaid.yml
├── notebooks/
│   └── *.ipynb
└── scripts/
    └── generate_toc.py
```