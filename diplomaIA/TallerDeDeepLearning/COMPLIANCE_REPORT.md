# U-Net Implementation Compliance Report
## Obligatorio - Taller de Deep Learning

---

## Executive Summary

This report analyzes the student's U-Net implementation notebook (`obligatorio.ipynb`) for compliance with the assignment requirements, with special focus on **documentation and justification of decisions** as emphasized by the professor.

**KEY FINDING:** The notebook demonstrates technical competence and includes a comprehensive introduction, but **significantly lacks explicit justifications** for the majority of design decisions made.

---

## 1. Documentation Requirements Analysis

### 1.1 Assignment Requirements
From `obligatorio.txt` (line 150):
> **"Cualquier decisión tiene que ser justificada en el notebook."**
> (Any decision must be justified in the notebook)

### 1.2 Professor's Emphasis
From class transcription (`8-22-10-2025.txt`, lines around 51-53):
> **"Cualquier decisión tiene que ser justificada en el notebook"**
> **"Van a hacer data augmentation, justifiquen."**
> **"Van a hacer crop, justifiquen."**
> **"Van a redimensionar las imágenes, tienen que justificar."**

The professor explicitly states that students must justify:
- Data augmentation choices
- Cropping/resizing decisions
- Any preprocessing decisions
- Architecture modifications
- Hyperparameter selections

---

## 2. Quantitative Analysis

### 2.1 Notebook Structure
- **Total cells:** 122
- **Markdown cells:** 65 (53.3%)
- **Code cells:** 57 (46.7%)

### 2.2 Justification Metrics
- **Cells with justification keywords:** 1 out of 65 (1.5%)
- **Keywords searched:** "porque", "por qué", "razón", "motivo", "debido a", "esto permite", "esto ayuda"
- **Code comments:** 0 (no comments in code cells)

### 2.3 Narrative Elements
- **Long explanatory cells (>200 chars):** 6 out of 65 (9.2%)
- **Evolution indicators found:** 5 ("primero", "luego", "mejora", "probamos", "resultado")
- **Problem-solution structure:** Partial (mentions problems but not solutions)

---

## 3. Decision Analysis

### 3.1 Decisions Mentioned (but not justified)

| Decision | Mentioned | Justified | Status |
|----------|-----------|-----------|--------|
| **Image size (384x384)** | ✓ | ✗ | ⚠️ MISSING |
| **InstanceNorm** | ✓ | ✗ | ⚠️ MISSING |
| **Dropout (0.1)** | ✓ | ✗ | ⚠️ MISSING |
| **Data augmentation** | ✓ | ✗ | ⚠️ MISSING |
| **BCEDiceLoss** | ✓ | ~ | ⚠️ PARTIAL |
| **Optimizer** | ✓ | ✗ | ⚠️ MISSING |
| **Learning rate (1e-4)** | ✓ | ✗ | ⚠️ MISSING |
| **Skip connections** | ✓ | ✗ | ⚠️ MISSING |
| **U-Net depth (4 levels)** | ✓ | ✗ | ⚠️ MISSING |
| **Batch size (8)** | ✓ | ✗ | ⚠️ MISSING |
| **Padding strategy** | ✗ | ✗ | ⚠️ NOT DISCUSSED |

### 3.2 Only Justified Decision

**Cell 54 - Dice Loss:**
> "Es buena para datasets desbalanceados porque normaliza por el tamaño del objeto"

This is the ONLY cell in the entire notebook that explicitly provides a "porque" (because) justification.

---

## 4. Introduction Analysis

### 4.1 Introduction Content (Cell 1)
The introduction provides a comprehensive summary:

```
Este notebook implementa la arquitectura U-Net desde cero en PyTorch para
segmentación binaria de personas, desarrollado como obligatorio del Taller
de Deep Learning. Basado en el paper de Ronneberger et al. (2015), el
modelo utiliza un encoder-decoder de 4 niveles con skip connections,
InstanceNorm para estabilidad en batches pequeños, y Dropout en el
bottleneck como regularización. Las imágenes originales de 800×800 se
procesan a 384×384 durante entrenamiento, con augmentación adaptada al
dataset (transformaciones geométricas y de color realistas). El
entrenamiento emplea BCEDiceLoss, scheduler de learning rate con
decaimiento coseno, y un sistema de checkpoints que preserva el mejor
modelo.
```

### 4.2 Introduction Assessment
**What it does well:**
- ✓ Lists all major decisions made
- ✓ Provides technical overview
- ✓ Mentions paper source

**What it lacks:**
- ✗ No explanation of WHY 384x384 was chosen
- ✗ No justification for WHY InstanceNorm over BatchNorm
- ✗ No reasoning for WHY 4 levels of depth
- ✗ No explanation of WHY those specific augmentations
- ✗ No justification for WHY dropout value of 0.1
- ✗ No explanation of WHY learning rate 1e-4

The introduction **describes** decisions but does not **justify** them.

---

## 5. Critical Missing Justifications

### 5.1 Image Size (384x384)
**What's needed:**
- Why 384x384 and not 256x256 or 512x512?
- What were the computational constraints?
- Did you test other sizes?
- How does this relate to the professor's comment about training with 800x800 being impossible?

**What's provided:** Only mentioned in introduction and hyperparameters cell.

### 5.2 InstanceNorm vs BatchNorm
**What's needed:**
- Why InstanceNorm instead of the more common BatchNorm?
- Is it because of small batch sizes (batch=8)?
- What problems would BatchNorm cause?
- Did you test both?

**What's provided:** Introduction mentions "InstanceNorm para estabilidad en batches pequeños" but doesn't explain WHY small batches are unstable with BatchNorm or WHY InstanceNorm solves this.

### 5.3 Data Augmentation Strategy
**What's needed:**
- Why those specific augmentations (HorizontalFlip, ShiftScaleRotate, etc.)?
- Why NOT vertical flip?
- Why those particular distortion methods?
- Did you test different augmentation strategies?

**What's provided:** Cell 27 lists transformations but provides zero justification for choices.

### 5.4 BCEDiceLoss Combination
**What's needed:**
- Why combine BCE and Dice?
- What does each contribute?
- Did you try them separately?
- What were the results?

**What's provided:** Cell 54 only justifies why Dice is good for imbalanced datasets, but doesn't justify combining it with BCE.

### 5.5 Hyperparameters
**What's needed for each:**
- Learning rate 1e-4: Why this value?
- Batch size 8: Why not 4 or 16?
- Dropout 0.1: Why this rate?
- 600 epochs: How was this determined?

**What's provided:** Cell 10 just lists values with no justification.

### 5.6 Padding Strategy
**Critical issue:** The professor explicitly discussed padding decisions in class:
- Lines 102-113 of transcription discuss padding='same' vs no padding
- The original U-Net uses no padding (output is smaller than input)
- Using padding='same' avoids the need for cropping

**What's needed:**
- Did you use padding='same' or not?
- If yes, why deviate from the original paper?
- If no, how did you handle the size mismatch?

**What's provided:** No discussion of padding strategy at all.

---

## 6. Comparison with Requirements

### 6.1 From Assignment (obligatorio.txt)

**Section 1 - Dataset Analysis (5 points):**
- "Justificación de las decisiones tomadas en la preprocesamiento de datos"
- **Status:** ⚠️ Decisions mentioned but not justified

**Section 2 - Model Implementation (20 points):**
- "Construcción de la arquitectura U-Net siguiendo la estructura descrita en el paper"
- "Se aceptan mejoras... pero justificando su uso"
- **Status:** ⚠️ Architectural choices not justified

**Section 3 - Training (10 points):**
- "Configuración adecuada del ciclo de entrenamiento"
- "Elección de la función de pérdida y del optimizador"
- **Status:** ⚠️ Choices made but not justified

### 6.2 From Professor's Transcription

Line 51-53:
> "Cualquier decisión tiene que ser justificada en el notebook. Van a hacer data augmentation, justifiquen. Van a hacer crop, justifiquen. Van a redimensionar las imágenes, tienen que justificar."

Line 119-121:
> "Capaz que es algo tan fácil como no me entraba y por eso hago una normalización... cuando tengan una justificación o por lo menos tengan un problema, intenté hacer esto y me dio."

**The professor wants to see:**
- The thought process
- Why each decision was made
- What problems you encountered
- How you solved them
- What you tried that didn't work

---

## 7. What Good Justification Looks Like

### 7.1 Example: Image Size Decision
**Good justification would be:**

```markdown
### Decisión: Tamaño de imagen 384x384

Probamos varios tamaños de imagen:
- 800x800 (original): No era viable, cada época tomaba >3 horas con batch size 1
- 256x256: Entrenaba rápido pero perdíamos demasiado detalle en bordes de personas
- 512x512: Buenos resultados pero aún muy lento (1.5h por época)
- 384x384: Balance óptimo - mantiene suficiente detalle para segmentación precisa
  mientras permite batch size de 8 y épocas de ~15 minutos

Elegimos 384x384 porque:
1. Es divisible por 2^4 (necesario para 4 niveles de max pooling)
2. Permite batch size razonable (8) que estabiliza el entrenamiento
3. Mantiene suficiente resolución para detectar personas pequeñas
4. Hace el entrenamiento viable (feedback en minutos, no horas)
```

### 7.2 Example: InstanceNorm vs BatchNorm
**Good justification would be:**

```markdown
### Decisión: InstanceNorm en lugar de BatchNorm

Inicialmente usamos BatchNorm (estándar en CNNs), pero tuvimos problemas:
- Con batch size pequeño (8), BatchNorm tenía estadísticas muy ruidosas
- La pérdida oscilaba mucho entre batches
- El modelo no convergía bien

Cambiamos a InstanceNorm porque:
1. No depende del batch - normaliza cada imagen independientemente
2. Más estable con batch sizes pequeños
3. Funciona bien en segmentación (ver: paper de Huang et al. 2017)

Resultado: Pérdida más estable, convergencia más suave, Dice mejoró de 0.72 a 0.79
```

---

## 8. Strengths of Current Implementation

Despite lacking justifications, the notebook has several strengths:

### 8.1 Technical Implementation
- ✓ Complete U-Net architecture implementation
- ✓ Proper encoder-decoder structure with skip connections
- ✓ Good use of modern techniques (Mixed Precision Training, W&B logging)
- ✓ Comprehensive data analysis section
- ✓ Test-Time Augmentation for inference
- ✓ Proper RLE encoding for Kaggle submission

### 8.2 Code Organization
- ✓ Clean modular structure
- ✓ Well-organized sections
- ✓ Proper use of markdown headers
- ✓ Visualization of results

### 8.3 Documentation Structure
- ✓ Clear introduction summarizing approach
- ✓ Descriptive markdown cells for each section
- ✓ Logical flow from analysis → implementation → training → evaluation

---

## 9. Recommendations for Improvement

### 9.1 High Priority (Compliance Issues)

1. **Add justification sections after each major decision**
   - After hyperparameters: Why each value?
   - After augmentation: Why those transformations?
   - After model architecture: Why those modifications?

2. **Create a "Design Decisions" section**
   - Document all major choices
   - Explain reasoning for each
   - Include what was tried and didn't work

3. **Add narrative of evolution**
   - Show iterative development process
   - Document problems encountered
   - Explain how you solved them

### 9.2 Specific Additions Needed

**Add these markdown cells:**

```markdown
## Decisiones de Diseño y Justificaciones

### 1. Tamaño de Imagen: 384x384
[Explanation of why, what was tried, trade-offs]

### 2. Normalización: InstanceNorm
[Explanation of why InstanceNorm over BatchNorm]

### 3. Data Augmentation
[Justification for each transformation]

### 4. Función de Pérdida: BCE + Dice
[Why combination, what each contributes]

### 5. Hiperparámetros
[Justification for LR, batch size, dropout, etc.]

### 6. Padding Strategy
[Whether using padding='same' and why]
```

### 9.3 Medium Priority

4. **Add code comments for non-obvious implementation choices**
5. **Document experiments that didn't work**
6. **Include comparison of different approaches tried**

---

## 10. Defense Preparation

The professor mentioned (line 124-125):
> "¿Qué tres decisiones más importantes tuviste que tomar en tu obligatorio?"

**Student should be prepared to answer:**

1. **Image size 384x384:**
   - Why this specific size?
   - What constraints led to this?
   - What other sizes were tested?

2. **InstanceNorm instead of BatchNorm:**
   - Why deviate from common practice?
   - What problem does it solve?
   - How does it relate to batch size?

3. **BCEDiceLoss combination:**
   - Why combine two losses?
   - What does each contribute?
   - How are they weighted?

4. **Architecture depth (4 levels):**
   - Why 4 and not 3 or 5?
   - How does this relate to image size?
   - What's the bottleneck size?

5. **Data augmentation strategy:**
   - Why those specific transformations?
   - Why not others (e.g., vertical flip)?
   - How does this improve generalization?

---

## 11. Compliance Rating

### Overall Compliance: ⚠️ PARTIAL COMPLIANCE

| Criterion | Score | Notes |
|-----------|-------|-------|
| **Technical Implementation** | ✓✓✓✓ 4/4 | Excellent implementation |
| **Documentation Completeness** | ✓✓✓ 3/4 | Good structure, missing depth |
| **Justification of Decisions** | ✗✗ 0.5/4 | **CRITICAL ISSUE** |
| **Narrative/Evolution** | ✓ 1/4 | Some indicators, lacks story |

### Issues by Severity:

**CRITICAL (Must Fix):**
- ⛔ Lack of explicit justifications for design decisions (1/65 cells = 1.5%)
- ⛔ No explanation of why 384x384 was chosen
- ⛔ No justification for InstanceNorm choice
- ⛔ No reasoning for data augmentation strategy
- ⛔ Missing padding strategy discussion

**IMPORTANT (Should Fix):**
- ⚠️ No problem-solution narrative
- ⚠️ No documentation of failed experiments
- ⚠️ Limited evolution/iteration language
- ⚠️ Hyperparameters listed without justification

**MINOR (Nice to Have):**
- ℹ️ No code comments
- ℹ️ Could include more comparative analysis
- ℹ️ Could show experimental results table

---

## 12. Final Verdict

### 12.1 Technical Quality
The implementation is **technically sound and complete**. The student demonstrates:
- Understanding of U-Net architecture
- Proficiency with PyTorch
- Knowledge of modern training techniques
- Proper evaluation methodology

### 12.2 Documentation Quality
The documentation **structure is good** but **lacks critical content**:
- Clear organization ✓
- Descriptive headers ✓
- Good introduction ✓
- **Missing justifications** ✗✗✗

### 12.3 Requirement Compliance

**Assignment requirement:**
> "Cualquier decisión tiene que ser justificada en el notebook"

**Current status:** **NOT COMPLIANT**
- Only 1 out of ~15 major decisions is justified
- Decisions are mentioned but not explained
- No reasoning provided for choices
- No narrative of development process

### 12.4 Risk Assessment

**For Defense:**
- **Risk Level:** HIGH
- **Reason:** If asked "why did you choose X?", student must be able to explain beyond what's in notebook
- **Mitigation:** Add justification sections immediately, prepare clear answers

**For Grading:**
- Points will likely be deducted from Section 1 (Dataset Analysis - justification of decisions)
- May affect Section 2 (Model Implementation - justifying improvements)
- May affect Section 3 (Training - configuration justification)

---

## 13. Action Items

### Immediate (Before Submission):
1. ✓ Add "Decisiones de Diseño" section with justifications for:
   - Image size
   - InstanceNorm
   - Data augmentation
   - Loss function
   - Hyperparameters
   - Padding strategy

2. ✓ For each justification, answer:
   - **Why** this choice?
   - **What** alternatives were considered?
   - **What** problems does it solve?
   - **How** does it improve results?

3. ✓ Add narrative elements showing evolution:
   - What was tried first
   - What problems occurred
   - How they were solved

### Before Defense:
4. ✓ Prepare to explain top 3-5 decisions verbally
5. ✓ Know the reasoning behind every hyperparameter
6. ✓ Be ready to discuss alternative approaches

---

## Conclusion

The student has created a technically impressive U-Net implementation with good documentation structure. However, the notebook **significantly fails to meet the explicit requirement** that "cualquier decisión tiene que ser justificada."

With only 1 out of 65 markdown cells containing justification language, and multiple critical decisions (image size, normalization, augmentation, loss function, hyperparameters) lacking any explanation of "why," the notebook does not comply with the assignment's documentation requirements as emphasized by both the assignment text and the professor in class.

**Recommendation:** Add explicit justification sections immediately before submission to avoid point deductions and ensure preparedness for defense.

---

*Report generated: 2025-12-02*
*Notebook analyzed: obligatorio.ipynb*
*Total cells analyzed: 122 (65 markdown, 57 code)*
