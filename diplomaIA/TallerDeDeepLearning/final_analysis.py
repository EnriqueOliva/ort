import json
import sys

# Read the notebook
with open('c:/Users/Enrique/Documents/2doSemestre/TallerDeDeepLearning/workspace/obligatorio/lab/obligatorio.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Extract all markdown cells
markdown_cells = [(i, ''.join(c['source'])) for i, c in enumerate(nb['cells']) if c['cell_type'] == 'markdown']
all_markdown_text = '\n\n'.join([text for i, text in markdown_cells])

print("="*80)
print("JUSTIFICATION COMPLIANCE ANALYSIS")
print("="*80)

# Check what's mentioned
decisions_to_check = {
    'Image size 384x384': ['384', 'image size', 'img_size'],
    'InstanceNorm': ['instancenorm', 'instance norm'],
    'Dropout': ['dropout'],
    'Data augmentation': ['augmentation', 'augmentacion'],
    'Loss BCEDiceLoss': ['bce', 'dice', 'loss'],
    'Optimizer': ['optimizer', 'optimizador', 'adam'],
    'Learning rate': ['learning rate', 'lr'],
    'Padding': ['padding', 'pad', 'same'],
    'Skip connections': ['skip', 'concatena'],
    'UNet depth': ['depth', 'nivel', 'profundidad', '4 niveles'],
    'Batch size': ['batch size', 'batch_size']
}

print("\nDECISIONS MENTIONED:")
print("-"*80)
for decision, keywords in decisions_to_check.items():
    found = any(kw.lower() in all_markdown_text.lower() for kw in keywords)
    status = "[YES]" if found else "[NO]"
    print(f"{status:6} {decision}")

# Look for justification indicators
print("\n" + "="*80)
print("JUSTIFICATION ANALYSIS:")
print("="*80)

justification_words = [
    'porque', 'por que', 'razon', 'motivo', 'ya que',
    'debido a', 'esto permite', 'esto ayuda', 'esto mejora'
]

justified_cells = []
for i, text in markdown_cells:
    text_lower = text.lower()
    found_words = [w for w in justification_words if w in text_lower]
    if found_words:
        justified_cells.append((i, text[:300], found_words))

print(f"\nCells with justification keywords: {len(justified_cells)}/{len(markdown_cells)}")

if justified_cells:
    print("\nCells found:")
    for i, text, words in justified_cells:
        print(f"\n--- Cell {i} ---")
        print(f"Keywords: {', '.join(words)}")
        print(text.replace('\n', ' ')[:200])
else:
    print("\n[!!!] NO CELLS WITH EXPLICIT JUSTIFICATION KEYWORDS FOUND")

# Check specific sections
print("\n" + "="*80)
print("SPECIFIC SECTIONS CHECK:")
print("="*80)

# Find hyperparameters section
hyper_cells = [(i, text) for i, text in markdown_cells if 'hiperpar' in text.lower()]
print(f"\nHyperparameters section: {'FOUND' if hyper_cells else 'NOT FOUND'}")

# Find data augmentation section
aug_cells = [(i, text) for i, text in markdown_cells if 'augment' in text.lower() and len(text) > 50]
print(f"Data augmentation section: {'FOUND' if aug_cells else 'NOT FOUND'}")
if aug_cells:
    for i, text in aug_cells[:1]:
        print(f"\n  Cell {i} content:")
        print(f"  {text[:250].replace(chr(10), ' ')}")
        # Check if it has justification
        has_just = any(w in text.lower() for w in justification_words)
        print(f"  Has justification: {'YES' if has_just else 'NO'}")

# Find model architecture section
model_cells = [(i, text) for i, text in markdown_cells if ('arquitectura' in text.lower() or 'implementation' in text.lower() or 'implementacion' in text.lower()) and len(text) > 30]
print(f"\nModel architecture section: {'FOUND' if model_cells else 'NOT FOUND'}")

# Check introduction
intro_cells = [(i, text) for i, text in markdown_cells if 'introduccion' in text.lower()]
print(f"Introduction section: {'FOUND' if intro_cells else 'NOT FOUND'}")
if intro_cells:
    i, text = intro_cells[0]
    print(f"\n  Cell {i} mentions:")
    mentions = []
    if '384' in text: mentions.append("384x384 size")
    if 'instancenorm' in text.lower(): mentions.append("InstanceNorm")
    if 'dropout' in text.lower(): mentions.append("Dropout")
    if 'bce' in text.lower(): mentions.append("BCE loss")
    if 'augment' in text.lower(): mentions.append("Augmentation")
    if mentions:
        for m in mentions:
            print(f"    - {m}")

    # Check if intro has justifications
    has_just = any(w in text.lower() for w in justification_words)
    print(f"  Contains justifications: {'YES' if has_just else 'NO'}")

# Final verdict
print("\n" + "="*80)
print("FINAL ASSESSMENT:")
print("="*80)
print("\nREQUIREMENT from obligatorio.txt:")
print("  'Cualquier decision tiene que ser justificada en el notebook'")
print("\nPROFESSOR'S EMPHASIS from transcription:")
print("  'Van a hacer data augmentation, justifiquen.'")
print("  'Van a hacer crop, justifiquen.'")
print("  'Van a redimensionar las imagenes, tienen que justificar'")
print("\nFINDING:")
print(f"  - Total markdown cells: {len(markdown_cells)}")
print(f"  - Cells with justification keywords: {len(justified_cells)}")
print(f"  - Justification ratio: {len(justified_cells)/len(markdown_cells)*100:.1f}%")

if len(justified_cells) < 5:
    print("\n[WARNING] Very few cells contain explicit justifications!")
    print("The notebook mentions decisions but lacks clear explanations of WHY")
    print("each decision was made. Each major decision should have:")
    print("  - Why 384x384 was chosen (computational constraints? performance?)")
    print("  - Why InstanceNorm over BatchNorm (small batch sizes?)")
    print("  - Why specific augmentations were selected")
    print("  - Why BCEDiceLoss combination")
    print("  - Why specific hyperparameter values")
else:
    print("\n[OK] Notebook contains justifications throughout")

print("\n" + "="*80)
