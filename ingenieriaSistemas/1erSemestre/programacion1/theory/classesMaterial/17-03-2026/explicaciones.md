# Clase Práctico 1 — Martes 17/03/2026
## Programación 1 · Práctico · Prof. Sergio Cortinas (Oliver) y Andrés Mauricio Repeto Ferrero

---

## La Gran Pregunta

¿Para qué sirve aprender a programar si la inteligencia artificial ya programa por vos?

Esta pregunta no es retórica de adorno. Fue el hilo conductor de toda la primera clase práctica, aunque no se dijo explícitamente. Todo lo que se habló — las carreras de los profes, el miedo al reemplazo por IA, los consejos sobre el obligatorio — gira alrededor de esta misma tensión: ¿vale la pena aprender a fondo, o alcanza con saber pedirle a la IA?

La respuesta que dieron los profesores, con ejemplos propios, es rotunda: **vale la pena aprender a fondo, y los que no lo hacen son los que se quedan afuera**.

---

## Conexión con la Clase Anterior

Esta fue la primera clase práctica del semestre. Todavía no hubo contenido técnico. La clase anterior (teórico con Gonzalo) ya había introducido la carrera y el sistema de evaluación. Este práctico repitió parte de esa información para los que aún no la tenían clara, y la completó con el enfoque particular del equipo docente de los martes.

---

## Quiénes son los Profesores

Antes de hablar de programación, los profesores se presentaron con bastante detalle. Esto no es ruido — entender quiénes son te ayuda a entender por qué dicen lo que dicen.

---

### Sergio Cortinas (Oliver)

> "Lo que sobra es tiempo: estoy terminando la tesis, tengo el proyecto de la tesis que ya tiene clientes y financiamiento del BID, trabajo como proveedor de servicios para ACNUR, voy a entrar como PM en SoftBees, y tengo dos hijos."

**Traducción:** Lo dijo en modo irónico. No le sobra tiempo para nada. Lo usa para mostrar que viene de la práctica real, no del aula.

Oliver está terminando Ingeniería de Sistemas en ORT (defiende tesis la primera semana de abril de 2026). Su proyecto de tesis se llama **Señor Ked**: un sistema para hogares de ancianos que gestiona medicación, insumos e ingresos hospitalarios. Lo que lo hace interesante es que usa inteligencia artificial — en lugar de cargar datos a mano, el personal manda mensajes de voz (como WhatsApp) y el sistema los procesa. Es SaaS, tiene financiamiento del BID, ya tiene clientes reales y está incubado en el centro de crecimiento de ORT.

Además de eso, trabaja como proveedor de servicios para **ACNUR** (la comisión de la ONU para refugiados) en un proyecto con el Ministerio de Relaciones Exteriores, donde oficia de Project Manager. Tiene 20 años de experiencia en IT: empezó como programador en TATA Consultancy Services, pasó por gestión de proyectos, auditoría interna y testing de automatización. Los últimos 10 años se dedicó exclusivamente a gestión de proyectos.

> "El proyecto es el que tiene toda la culpa cuando la cosa está mal, y cuando las cosas van bien son del equipo."

**Traducción:** El PM es el responsable de todo lo que sale mal, pero cuando sale bien, el mérito es del equipo. Es la dinámica natural del rol.

> "Acá PM es todo. Acá el PM es PM, Scrum Master, Product Owner, a veces QA."

**Traducción:** En las empresas de acá (Uruguay), el PM no tiene un equipo de 5 PMs por debajo como en Google. Acá hacés de todo con pocos recursos.

---

### Andrés Mauricio Repeto Ferrero

> "Me conocen por el segundo nombre, Mauricio."

**Traducción:** Se presenta como Mauricio. Es más ordenado y directo que Oliver.

Mauricio se graduó de Ingeniería en ORT en 2011. Trabajó en Business Intelligence durante varios años y desde 2018 se pasó a inteligencia artificial. Tiene maestría, defendió su tesis alrededor de 2023. Vive en Medellín, Colombia hace dos años. Juega al fútbol y hace CrossFit.

La combinación de los dos profes es complementaria: Oliver va al anécdota y la experiencia vivida, Mauricio va a la estructura y la claridad.

---

## Logística de la Materia

---

### Modalidad y Horarios

La materia es **híbrida (hyflex)**: podés ir presencial o conectarte por Zoom en simultáneo. No son dos modalidades separadas — es la misma clase al mismo tiempo.

- **Teórico con Gonzalo:** lunes 20:30–22:30 y miércoles 17:30–19:25, salón 309
- **Práctico (este espacio):** martes únicamente, 17:30–19:25, salón S221 + Zoom

> "Nosotros acá lo que vamos a hacer es ayudarlos a pensar, a tratar de resolver un problema, a ver por dónde empezar y a dónde quiero llegar."

**Traducción:** El práctico no es para repetir la teoría. Es para sentarse a resolver, con guía. La teoría ya la dio Gonzalo — acá se aplica.

La dinámica del semestre va a ser así: primero Gonzalo introduce el concepto en el teórico, después en el práctico se trabaja sobre ese concepto con ejercicios. Los mismos ejercicios que están en Aulas se cargan en **Miro** (una pizarra virtual colaborativa). Las soluciones también están disponibles en Aulas.

> "Siempre la solución está en el aula. El tema es saber cómo llegar a esa solución."

**Traducción:** Las respuestas están publicadas. El trabajo no es encontrar la respuesta — es entender cómo se llega a ella.

---

### Sistema de Evaluación (repaso)

> "Si no llegás al mínimo en el Obligatorio 2, perdés la materia. No es que te va mal — la perdés."

**Traducción:** Hay notas mínimas que funcionan como condición de continuidad. Si no llegás, no importa cuánto hayas sacado en el resto.

| Componente | Puntos | Condiciones Especiales |
|---|---|---|
| Parcial 1 | 15 pts | Sin material |
| Parcial 2 | 40 pts | Sin material, mínimo requerido |
| Obligatorio 1 | 10 pts | HTML/CSS |
| Obligatorio 2 | 35 pts | HTML/CSS + JavaScript, mínimo 18 pts, defensa obligatoria |

- **Aprobación:** 70 puntos o más
- **Exoneración:** 86 puntos o más
- **Pérdida de la materia:** menos de 70 puntos, o no llegar al mínimo del Obligatorio 2, o no presentarse a la defensa

> "No ir a la defensa es perder la materia. Sin importar cuánto tenés."

**Traducción:** La defensa del Obligatorio 2 no es opcional. Es una condición de aprobación independiente. Si no vas, no importa tu nota — perdiste.

La defensa dura aproximadamente 30 minutos. Los profes piden un cambio sencillo al código para verificar que lo hiciste vos y que lo entendés. Si no pueden asistir, hay que avisar con tiempo para reprogramar.

**Créditos con vencimiento:** Si aprobás parciales pero no aprobás el examen antes de la fecha límite del semestre, perdés los créditos acumulados. No se guardan para el año siguiente.

---

### Plataformas

Hay tres sistemas que van a usar todo el semestre:

- **Aulas:** materiales de la materia, teóricos, prácticos, parciales resueltos, horarios de laboratorio
- **Gestión:** entrega de trabajos y consulta de notas
- **Biblioteca:** recursos adicionales

> "Las tres plataformas tienen el mismo usuario y contraseña. Si cambiás la clave en una, cambia en las tres."

**Traducción:** Son sistemas independientes pero con credenciales compartidas. Cambiar la contraseña en una afecta las otras dos.

En Aulas también hay un **calendario de eventos del semestre** disponible para descargar — fechas de parciales, entregas y demás.

---

## La IA y el Futuro del Desarrollador

Este fue el bloque más rico de la clase. No fue una exposición formal — fue una conversación que arrancó de una pregunta y se extendió con aportes de los propios estudiantes.

---

### El experimento de Oliver con Copilot

> "En la empresa, que es partner de Microsoft, nos pidieron que desarrolláramos una aplicación usando únicamente Copilot, sin tocar código nosotros. Es muy difícil."

**Traducción:** Usar IA para programar sin entender de programación no es tan fácil como parece. Incluso para profesionales con años de experiencia, delegar todo a la IA sin poder leer ni corregir el código generado es un problema real.

> "Lo que funciona es que nosotros no escribimos el código, pero diseñamos toda la infraestructura de los sistemas, de los servidores, y todo el workflow."

**Traducción:** El rol del desarrollador se desplaza: menos tiempo escribiendo líneas de código, más tiempo diseñando cómo el sistema tiene que funcionar. Pero para diseñar bien una arquitectura, necesitás entender cómo funciona el código que la IA va a escribir.

> "Hace un mes y medio que estamos con el proyecto y se necesita todo del equipo."

**Traducción:** Incluso con IA, el trabajo en equipo, la coordinación y el conocimiento técnico siguen siendo necesarios. La IA no reemplaza al equipo — se suma como una herramienta más.

---

### El caso de los programadores COBOL

Un estudiante trajo un ejemplo que Oliver validó completamente:

> "Los programadores de COBOL que más le tenían miedo a la IA son los que hoy más la están usando, porque entienden el código."

**Traducción:** La IA es más útil para quien ya sabe programar. Los que saben leer el código generado pueden verificarlo, corregirlo y sacarle más provecho. Los que no saben son los que dependen ciegamente de lo que salga.

---

### El caso del estudiante que perdió fluidez codificando

Otro estudiante compartió algo personal y honesto:

> "Desde que incorporé la IA en mi trabajo, realmente noté como que luego al escribir código por mi cuenta, se me hace mucho más difícil."

**Traducción:** Si delegás todo a la IA y dejás de ejercitar la escritura de código, la habilidad se atrofia.

Este mismo estudiante observó que la IA a veces cae en loops recursivos al atacar un problema difícil, consumiendo tokens sin llegar a ningún lado. Es una limitación real de las herramientas actuales.

> "Si yo hubiese programado esto a mano, directamente, como lo he hecho siempre, hubiese tardado 8 horas. Pero al intentar y bloquearme con la IA, una y otra y otra vez, simplemente estoy frustrándome más y más."

**Traducción:** La IA a veces es más lenta que hacerlo solo. Especialmente cuando el problema es complejo o la IA no entiende el contexto completo.

---

### La analogía del deporte

> "Es como cuando practicás un deporte. Los futbolistas que pasan meses sin jugar, después son un desastre."

**Traducción:** La programación es una habilidad que necesita práctica continua. Podés haber sido muy bueno en algún momento, pero si dejás de usarla, se va. La IA puede ser el equivalente a dejar de entrenar.

---

### El mensaje de los profes sobre la IA

> "No va a suplantar a los desarrolladores. Mientras uno aprenda, sepa lo que está haciendo, laburo va a tener."

**Traducción:** La IA no elimina la profesión — la transforma. Los trabajos que desaparecen son los que no se adaptan. Los que se adaptan no solo sobreviven — suelen quedar mejor posicionados.

Oliver también mencionó que las empresas que anunciaron despidos masivos "por culpa de la IA" en realidad estaban cubriendo malas proyecciones de crecimiento:

> "Si reducen gente es porque estimaron mal crecimiento. Y hoy en día muchas se escudan atrás de la inteligencia artificial."

**Traducción:** La IA fue el chivo expiatorio conveniente para decisiones empresariales que no tienen nada que ver con la tecnología.

---

## Oportunidades de la Carrera

> "Hay salida en ciberseguridad, en AI, en gestión de software, en testing, en comunicaciones, en games."

**Traducción:** Ingeniería de Sistemas no es una sola carrera — es un tronco con muchas ramas. No todos van a terminar escribiendo código.

Oliver mencionó el **Centro de Innovación y Emprendimiento (CIE)** de ORT: tiene alrededor de 40 emprendimientos en pre-incubación y 20 graduados. La tesis puede ser un proyecto de emprendimiento propio, un proyecto de empresa o un proyecto de la facultad. Ejemplos reales: Viatic, Avanza, y **PiolApp/Kisanaro** — una aplicación usada por el cuerpo técnico del seleccionado de Uruguay (el Maestro Tabárez la usó para estadísticas de jugadores).

> "Obviamente no tienen que esperar la tesis para desarrollar una idea."

**Traducción:** El CIE está disponible ahora. Si tenés una idea, podés ir a pedir asesoramiento sin esperar al final de la carrera.

---

## Consejos para el Obligatorio

> "No esperen ni al último día ni al último momento."

**Traducción:** Subir una entrega parcial antes de la fecha límite sirve como respaldo. Si algo falla el último día, ya tenés algo cargado. No hay excepciones por problemas técnicos de último momento.

> "Me ha pasado tener que sacar puntos por cosas muy idiotas. Venía bien hasta que le tuve que sacar puntos porque no revisó el checklist."

**Traducción:** Lean la letra del obligatorio con atención. Usen el checklist que viene adjunto. Muchos errores son evitables.

**Recomendación de GitHub:** Para los que trabajan en pareja, usar GitHub como repositorio de código compartido. Cada uno trabaja en lo suyo y sube al repo. También existe GitHub Desktop como opción más visual.

---

## Consejos de Estudio

> "Si en la primera semana no entendés algo y no lo preguntás, en la segunda semana vas a estar más perdido."

**Traducción:** La materia es acumulativa. Cada semana se construye sobre la anterior. Si dejás pasar una semana sin entender algo, el problema se multiplica.

Recursos disponibles:

- Horarios de laboratorio con asistentes (se publican en abril)
- Ayudantes de cátedra
- 3 profesores para consultas
- Grabaciones de clase
- Foros, Teams, email

> "La idea es que ustedes terminen aprendiendo a aprender."

**Traducción:** El objetivo no es solo aprobar Programación 1. Es desarrollar la capacidad de aprender cualquier cosa nueva por tu cuenta — eso es lo que vas a necesitar en la industria donde la tecnología cambia todo el tiempo.

---

## Próxima Clase Práctica

En la próxima sesión se va a arrancar con ejercicios de **pensamiento computacional**. Estos ejercicios son el puente entre "pensar como humano" y "pensar como computadora" — cómo descomponer un problema en pasos concretos y ordenados antes de escribir una sola línea de código.

Los ejercicios ya están disponibles en Aulas y se van a trabajar también en **Miro**.

---

## Definiciones para el Parcial

**Modalidad hyflex:** Formato de clase en el que los estudiantes pueden asistir presencialmente o de forma remota por Zoom en simultáneo, sin diferenciación entre modalidades.

**Obligatorio:** Trabajo práctico evaluado con nota mínima de aprobación. El Obligatorio 2 tiene además una defensa oral obligatoria donde el estudiante debe demostrar autoría del código.

**Defensa del Obligatorio:** Instancia presencial de aproximadamente 30 minutos donde el estudiante realiza una modificación al código bajo supervisión para verificar que lo hizo y lo entiende. No presentarse equivale a perder la materia.

**Créditos con vencimiento:** Los puntos acumulados en parciales no se guardan indefinidamente. Si el estudiante obtiene derecho a examen pero no aprueba antes de la fecha límite del semestre, pierde los créditos.

---

## Posibles Preguntas para el Parcial

**¿Qué pasa si no me presento a la defensa del Obligatorio 2?**
Se pierde la materia, sin importar la nota acumulada hasta ese momento.

**¿Cuál es el puntaje mínimo para exonerar?**
86 puntos. Para aprobar sin exonerar, 70 puntos.

**¿Qué mínimo debe tener el Obligatorio 2 para no perder la materia?**
18 puntos sobre 35.

**¿Para qué sirve aprender a programar si existe la inteligencia artificial?**
Porque la IA es más efectiva para quienes entienden el código que genera. Un programador que sabe leer, verificar y corregir código puede usar la IA como multiplicador. Quien no sabe programar depende ciegamente del output sin poder evaluar su calidad.

---

*Documento generado mediante análisis exhaustivo (3 pasadas) de la transcripción de la clase del 17/03/2026 — Programación 1, Práctico, Prof. Sergio Cortinas y Andrés Mauricio Repeto Ferrero. ORT Uruguay, Ingeniería en Sistemas, 1er semestre 2026.*