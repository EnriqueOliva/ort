import json
import sys

notebook_path = r'C:\Users\Enrique\Documents\2doSemestre\InteligenciaArtificialGenerativa\workspace\obligatorio\main.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
print("\n=== FINDING ISSUES ===\n")

issues_found = []
cells_to_delete = []
cells_to_modify = []

for idx, cell in enumerate(nb['cells']):
    source = ''.join(cell['source'])

    if '## Experimento 4: Sensibilidad a Hiperparámetros' in source and cell['cell_type'] == 'markdown':
        if 'Objetivo' not in source:
            print(f"Cell {idx}: DUPLICATE 'Experimento 4: Sensibilidad' (WILL DELETE)")
            issues_found.append(f"Cell {idx}: Duplicate Experimento 4 markdown")
            cells_to_delete.append(idx)
        else:
            print(f"Cell {idx}: Experimento 5 (mislabeled as 4, WILL KEEP)")

    if 'EXPERIMENTO 4: Sensibilidad a Hiperparámetros' in source:
        print(f"Cell {idx}: Print statement with 'EXPERIMENTO 4' (WILL CHANGE TO 5)")
        issues_found.append(f"Cell {idx}: Print statement needs update")
        cells_to_modify.append((idx, 'print_statement'))

    if "plt.suptitle('Experimento 4: Sensibilidad a Hiperparámetros'" in source:
        print(f"Cell {idx}: Plot title with 'Experimento 4' (WILL CHANGE TO 5)")
        issues_found.append(f"Cell {idx}: Plot title needs update")
        cells_to_modify.append((idx, 'plot_title'))

print(f"\n=== APPLYING FIXES ===\n")

for idx in reversed(cells_to_delete):
    print(f"Deleting cell {idx}...")
    del nb['cells'][idx]

for idx, fix_type in cells_to_modify:
    adjusted_idx = idx
    for deleted_idx in cells_to_delete:
        if deleted_idx < idx:
            adjusted_idx -= 1

    source = ''.join(nb['cells'][adjusted_idx]['source'])

    if fix_type == 'print_statement':
        new_source = source.replace(
            'print("EXPERIMENTO 4: Sensibilidad a Hiperparámetros")',
            'print("EXPERIMENTO 5: Sensibilidad a Hiperparámetros")'
        )
        nb['cells'][adjusted_idx]['source'] = new_source.splitlines(True)
        print(f"Updated print statement in cell {adjusted_idx}")

    elif fix_type == 'plot_title':
        new_source = source.replace(
            "plt.suptitle('Experimento 4: Sensibilidad a Hiperparámetros',",
            "plt.suptitle('Experimento 5: Sensibilidad a Hiperparámetros',"
        )
        nb['cells'][adjusted_idx]['source'] = new_source.splitlines(True)
        print(f"Updated plot title in cell {adjusted_idx}")

print(f"\n=== VERIFICATION ===\n")
print("Scanning for remaining 'Experimento' headings:\n")

for idx, cell in enumerate(nb['cells']):
    source = ''.join(cell['source'])
    if '## Experimento' in source:
        title_line = [line for line in source.split('\n') if '## Experimento' in line][0]
        print(f"Cell {idx}: {title_line}")

print("\n=== SAVING ===\n")
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"✓ Notebook saved successfully!")
print(f"✓ Total cells after fixes: {len(nb['cells'])}")
print(f"\n=== SUMMARY ===")
print(f"Issues found: {len(issues_found)}")
print(f"Cells deleted: {len(cells_to_delete)}")
print(f"Cells modified: {len(cells_to_modify)}")
