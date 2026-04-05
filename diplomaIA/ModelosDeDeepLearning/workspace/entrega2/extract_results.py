import json

with open('Notebook_Double_Descent.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Extract outputs from cells
for i, cell in enumerate(nb['cells']):
    if cell.get('cell_type') == 'code':
        outputs = cell.get('outputs', [])
        for out in outputs:
            if out.get('output_type') == 'stream':
                text = ''.join(out.get('text', []))
                if 'Summary:' in text or 'SUMMARY OF RESULTS' in text:
                    print(f"\n{'='*70}")
                    print(f"CELL {i} OUTPUT:")
                    print('='*70)
                    print(text)
