import json

# Read the notebook
with open('c:/Users/Enrique/Documents/2doSemestre/TallerDeDeepLearning/workspace/obligatorio/lab/obligatorio.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Extract all markdown cells
markdown_cells = [(i, ''.join(c['source'])) for i, c in enumerate(nb['cells']) if c['cell_type'] == 'markdown']
all_markdown_text = '\n\n'.join([text for i, text in markdown_cells])

print("="*80)
print("ANALYSIS OF JUSTIFICATIONS IN NOTEBOOK")
print("="*80)

# Check what's mentioned but not necessarily justified
decisions_to_check = {
    'Image size (384x384)': ['384', 'image size', 'img_size', 'tamaño'],
    'InstanceNorm': ['instancenorm', 'instance norm', 'batch norm'],
    'Dropout': ['dropout'],
    'Data augmentation': ['augmentation', 'augmentación'],
    'Loss function (BCEDiceLoss)': ['bce', 'dice', 'loss', 'pérdida'],
    'Optimizer': ['optimizer', 'optimizador', 'adam', 'sgd'],
    'Learning rate': ['learning rate', 'lr'],
    'Padding': ['padding', 'pad', 'same'],
    'Skip connections': ['skip', 'concatena'],
    'U-Net depth': ['depth', 'nivel', 'profundidad'],
    'Batch size': ['batch size', 'batch_size']
}

print("\nDECISIONS MENTIONED (but may lack justification):")
print("-"*80)
for decision, keywords in decisions_to_check.items():
    found = any(kw.lower() in all_markdown_text.lower() for kw in keywords)
    status = "✓ MENTIONED" if found else "✗ NOT FOUND"
    print(f"{status:15} | {decision}")

# Look for cells that explain "why"
print("\n" + "="*80)
print("CELLS WITH POTENTIAL JUSTIFICATIONS:")
print("="*80)

justification_indicators = [
    'porque', 'por qué', 'razón', 'motivo', 'ya que',
    'debido a', 'para', 'esto es importante', 'esto permite',
    'esto ayuda', 'esto mejora', 'esto garantiza'
]

justified_cells = []
for i, text in markdown_cells:
    text_lower = text.lower()
    found_indicators = [ind for ind in justification_indicators if ind in text_lower]
    if found_indicators:
        justified_cells.append((i, text, found_indicators))

if justified_cells:
    for i, text, indicators in justified_cells:
        print(f"\nCell {i} (indicators: {', '.join(indicators)}):")
        print(text[:400] if len(text) > 400 else text)
        print("-"*80)
else:
    print("\n!!! WARNING: NO CELLS FOUND WITH JUSTIFICATION INDICATORS !!!")

# Check the introduction
print("\n" + "="*80)
print("INTRODUCTION ANALYSIS:")
print("="*80)
intro_cells = [(i, text) for i, text in markdown_cells if 'introducción' in text.lower()]
if intro_cells:
    for i, text in intro_cells:
        print(f"\nCell {i}:")
        print(text)

        # Extract decisions mentioned in intro
        print("\n--- Decisions mentioned in introduction ---")
        if '384' in text:
            print("✓ Image size: 384x384 (mentioned)")
        if 'instancenorm' in text.lower():
            print("✓ InstanceNorm (mentioned)")
        if 'dropout' in text.lower():
            print("✓ Dropout (mentioned)")
        if '4 niveles' in text or '4 levels' in text or 'encoder-decoder' in text.lower():
            print("✓ Architecture depth (mentioned)")
        if 'bce' in text.lower() or 'dice' in text.lower():
            print("✓ Loss function (mentioned)")

# Summary
print("\n" + "="*80)
print("SUMMARY:")
print("="*80)
print(f"Total markdown cells: {len(markdown_cells)}")
print(f"Cells with justification indicators: {len(justified_cells)}")
print(f"\nJustification ratio: {len(justified_cells)}/{len(markdown_cells)} = {len(justified_cells)/len(markdown_cells)*100:.1f}%")

# Final assessment
print("\n" + "="*80)
print("COMPLIANCE ASSESSMENT:")
print("="*80)
print("\nRequirement: 'Cualquier decisión tiene que ser justificada en el notebook'")
print("Professor's emphasis: 'Van a hacer data augmentation, justifiquen. Van a hacer")
print("crop, justifiquen. Van a redimensionar las imágenes, tienen que justificar'")
print("\nFINDING: The notebook appears to MENTION decisions (in introduction and comments)")
print("but may LACK EXPLICIT JUSTIFICATIONS explaining WHY each decision was made.")
print("\nThe introduction provides a summary of decisions but doesn't explain the")
print("reasoning behind each choice. True justifications should explain:")
print("  - WHY 384x384 was chosen over other sizes")
print("  - WHY InstanceNorm instead of BatchNorm")
print("  - WHY that specific data augmentation strategy")
print("  - WHY BCEDiceLoss combination")
print("  - etc.")
