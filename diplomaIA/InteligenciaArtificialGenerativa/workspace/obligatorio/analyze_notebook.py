import json
import sys

notebook_path = r'C:\Users\Enrique\Documents\2doSemestre\InteligenciaArtificialGenerativa\workspace\obligatorio\main.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}\n")
print("="*80)

empty_print_cells = []
experiment_5_index = None

for idx, cell in enumerate(nb['cells']):
    cell_type = cell['cell_type']

    if cell_type == 'markdown':
        source = ''.join(cell['source'])
        if '## Experimento 5' in source:
            experiment_5_index = idx
            print(f"\n[Cell {idx}] MARKDOWN - Experimento 5 FOUND")
            print(f"Content preview: {source[:100]}...")

    elif cell_type == 'code':
        source = ''.join(cell['source']).strip()

        if source == 'print("")' or source == "print('')":
            empty_print_cells.append({
                'index': idx,
                'content': source,
                'type': 'empty_print'
            })
            print(f"\n[Cell {idx}] CODE - EMPTY PRINT STATEMENT")
            print(f"Content: {repr(source)}")

        elif len(source) < 20 and source:
            print(f"\n[Cell {idx}] CODE - SHORT CONTENT")
            print(f"Content: {repr(source)}")

        elif not source:
            empty_print_cells.append({
                'index': idx,
                'content': '',
                'type': 'completely_empty'
            })
            print(f"\n[Cell {idx}] CODE - COMPLETELY EMPTY")

print("\n" + "="*80)
print(f"\nEXPERIMENTO 5 INDEX: {experiment_5_index}")

if experiment_5_index is not None:
    print(f"\nCell immediately after Experimento 5 (index {experiment_5_index + 1}):")
    next_cell = nb['cells'][experiment_5_index + 1]
    print(f"  Type: {next_cell['cell_type']}")
    content = ''.join(next_cell['source']).strip()
    print(f"  Content: {repr(content[:200])}")

print("\n" + "="*80)
print(f"\nSUMMARY OF PROBLEMATIC CELLS:")
print(f"Total empty/minimal cells found: {len(empty_print_cells)}\n")

for cell_info in empty_print_cells:
    print(f"Cell {cell_info['index']}: {cell_info['type']} - {repr(cell_info['content'])}")
