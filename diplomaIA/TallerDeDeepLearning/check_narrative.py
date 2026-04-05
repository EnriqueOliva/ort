import json

# Read the notebook
with open('c:/Users/Enrique/Documents/2doSemestre/TallerDeDeepLearning/workspace/obligatorio/lab/obligatorio.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Extract all markdown cells
md_cells = [(i, ''.join(c['source'])) for i, c in enumerate(nb['cells']) if c['cell_type'] == 'markdown']

# Find long cells (potential narrative)
long_cells = [(i, text) for i, text in md_cells if len(text) > 200]

print("="*80)
print("NARRATIVE AND EXPLANATION ANALYSIS")
print("="*80)
print(f"\nMarkdown cells with >200 chars: {len(long_cells)}/{len(md_cells)}")

print("\n" + "="*80)
print("LONGEST CELLS (potential detailed explanations):")
print("="*80)

sorted_cells = sorted(long_cells, key=lambda x: len(x[1]), reverse=True)[:5]
for i, text in sorted_cells:
    print(f"\n--- Cell {i} ({len(text)} chars) ---")
    # Print first 400 chars
    preview = text[:400].replace('\n', ' ')
    print(preview)
    print("...")

# Check for evolution/iteration language
print("\n" + "="*80)
print("EVOLUTION/ITERATION INDICATORS:")
print("="*80)
print("\nChecking for phrases indicating iterative development:")

evolution_phrases = [
    'primero', 'luego', 'despues', 'inicialmente', 'posteriormente',
    'primera version', 'segunda version', 'iteracion', 'mejora',
    'probamos', 'intentamos', 'experimento', 'resultado', 'observamos',
    'decidimos', 'cambiamos', 'modificamos'
]

all_text = '\n'.join([text for i, text in md_cells])
found_phrases = [phrase for phrase in evolution_phrases if phrase in all_text.lower()]

if found_phrases:
    print(f"Found {len(found_phrases)} evolution indicators:")
    for phrase in found_phrases:
        print(f"  - {phrase}")
else:
    print("[WARNING] No evolution/iteration language found!")
    print("The professor asked for a 'story' of how the approach evolved.")

# Check for problem-solution structure
print("\n" + "="*80)
print("PROBLEM-SOLUTION STRUCTURE:")
print("="*80)

problem_words = ['problema', 'issue', 'error', 'fallo', 'dificultad']
solution_words = ['solucion', 'soluciono', 'arreglo', 'fixeamos', 'resolvimos']

has_problems = any(word in all_text.lower() for word in problem_words)
has_solutions = any(word in all_text.lower() for word in solution_words)

print(f"Mentions problems: {'YES' if has_problems else 'NO'}")
print(f"Mentions solutions: {'YES' if has_solutions else 'NO'}")

if not (has_problems or has_solutions):
    print("\n[INFO] Notebook doesn't show problem-solving narrative.")
    print("Good notebooks show: tried X, got Y problem, solved with Z")

print("\n" + "="*80)
