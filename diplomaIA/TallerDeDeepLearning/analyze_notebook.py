import json
import sys

# Read the notebook
with open('c:/Users/Enrique/Documents/2doSemestre/TallerDeDeepLearning/workspace/obligatorio/lab/obligatorio.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Extract all markdown cells
markdown_cells = [(i, ''.join(c['source'])) for i, c in enumerate(nb['cells']) if c['cell_type'] == 'markdown']

print(f"Total cells: {len(nb['cells'])}")
print(f"Markdown cells: {len(markdown_cells)}")
print("\n" + "="*80)

# Look for justification-related keywords
justification_keywords = [
    'justific', 'decisión', 'decision', 'por qué', 'porque',
    'razón', 'razon', 'motivo', 'elegimos', 'elección', 'eleccion',
    'criterio', 'selección', 'seleccion', 'decidimos'
]

print("\nSearching for justification keywords...")
found_justifications = []
for i, text in markdown_cells:
    text_lower = text.lower()
    for keyword in justification_keywords:
        if keyword in text_lower:
            found_justifications.append((i, text[:300]))
            break

if found_justifications:
    print(f"\nFound {len(found_justifications)} cells with justification-related content:")
    for i, text in found_justifications:
        print(f"\n--- Cell {i} ---")
        print(text)
else:
    print("\nNO justification-related keywords found in markdown cells!")

print("\n" + "="*80)
print("\nKey sections found:")

# Look for key sections
key_sections = {
    'Introduction': ['introducción', 'introduction'],
    'Hyperparameters': ['hiperparámetros', 'hyperparameters'],
    'Data Augmentation': ['augmentation', 'augmentación'],
    'Model Architecture': ['arquitectura', 'modelo', 'u-net', 'unet'],
    'Loss Function': ['loss', 'pérdida', 'dice', 'bce'],
    'Optimizer': ['optimizer', 'optimizador', 'adam'],
    'Training': ['entrenamiento', 'training', 'epochs'],
    'Evaluation': ['evaluación', 'evaluation', 'resultados']
}

for section_name, keywords in key_sections.items():
    found = False
    for i, text in markdown_cells:
        text_lower = text.lower()
        if any(kw in text_lower for kw in keywords):
            if not found:
                print(f"\n{section_name}:")
                found = True
            # Print first 200 chars of matching cells
            if len(text) < 200:
                print(f"  Cell {i}: {text.strip()}")
            else:
                print(f"  Cell {i}: {text[:200].strip()}...")
            if section_name in ['Introduction', 'Hyperparameters', 'Data Augmentation']:
                break  # Only show first match for these sections

print("\n" + "="*80)
print("\nChecking specific decisions mentioned in Introduction:")
intro_cell = [text for i, text in markdown_cells if 'introducción' in text.lower()]
if intro_cell:
    print(intro_cell[0])
