# DECLARACIÓN

## 1. Experimento

Este repositorio surge de un experimento personal:

Preguntarle a una inteligencia artificial qué investigaría si pudiera elegir libremente un problema, tomar su respuesta y desarrollar el problema utilizando sistemas de IA hasta donde fuera posible, cualquiera fuese el tema elegido y su complejidad.

Este repositorio documenta el resultado de ese proceso.

## 2. Tema elegido por Claude

Ante la pregunta inicial, la respuesta de Claude fue: 

>La que más me tira es una que aparece dentro de esta misma conversación pero que no llegamos a tocar: por qué el universo es inteligible.

>No "por qué hay algo" sino por qué eso que hay tiene estructura matemática, y por qué esa estructura resulta accesible a un pedazo del propio universo. Wigner le decía la efectividad irrazonable de la matemática. Un grupo de simetría que alguien garabatea por razones estéticas termina prediciendo una partícula que nadie vio. Eso podría no haber sido así: un cosmos legal pero opaco, con regularidades que ningún formalismo capture, es perfectamente concebible. No lo es.

(Respuesta textual de Claude, conversación de origen del proyecto.)

## 3. Desarrollo

La pregunta elegida no puede responderse directamente: es filosófica, y ningún experimento la decide. El trabajo de las rondas de crítica consistió en transformarla, por etapas, en algo medible: de "¿por qué el universo es inteligible?" se pasó a "¿hasta dónde se comprime la descripción de sus regularidades?", y de ahí a una pregunta operacional: cuánto costo descriptivo puede transferirse de los datos observados a estructuras reutilizables, cómo escala esa transferencia con la cantidad y la resolución de los datos, y cuánto generaliza sobre datos no vistos.

El resultado de este proceso no es una respuesta a la pregunta original, ni una demostración de ninguna hipótesis. Es un instrumento de medición: un protocolo con métricas definidas, criterios de éxito y de falsación fijados antes de mirar datos, y un piloto sintético que verifica que el instrumento se comporta como debe cuando la verdad es conocida. Este proyecto no intenta probar que el universo es comprimible: intenta que la pregunta deje de discutirse con adjetivos y pueda discutirse con números — y establecer cuánto de esa conversión resiste el examen de especialistas.

La versión técnica de este recorrido está en docs/preprint/; la conceptual, en los documentos de /docs.

## 4. Roles

Mi participación humana consistió en:

* formular la pregunta que originó el experimento;
* dirigir las consultas;
* pedir crítica, verificación y revisión en cada etapa;
* hacer circular los resultados entre distintos sistemas;
* decidir qué caminos explorar cuando las respuestas divergían;
* ejecutar o hacer ejecutar las pruebas propuestas;
* preservar la historia, las correcciones y la trazabilidad del proceso.

Los sistemas de IA eligieron el tema y produjeron la mayor parte de:

* la formalización matemática;
* el marco conceptual;
* el diseño metodológico;
* el protocolo experimental;
* el código;
* las auditorías;
* las sucesivas revisiones técnicas.

Sistemas participantes:

* Claude, de Anthropic, tanto en modalidad conversacional como mediante Claude Code;
* ChatGPT, de OpenAI;
* Gemini, de Google, en menor medida.

## 5. Aclaraciones

No tengo formación especializada en teoría de la información, teoría algorítmica de la información, Minimum Description Length (MDL), rate-distortion ni física.

Por esa razón no puedo verificar independientemente la corrección matemática, metodológica o física de todo lo contenido en este repositorio.

No afirmo que el marco desarrollado sea correcto, original, científicamente válido ni publicable.

Las validaciones realizadas hasta este punto son principalmente internas al propio proceso asistido por IA, más controles computacionales y de reproducibilidad. No sustituyen una revisión humana especializada.

## 6. Contenido y estado del repositorio

Este repositorio representa el estado exacto al que llegó el proceso de investigación asistida por IA antes de someterlo a una revisión experta humana independiente.

Se preservan deliberadamente:

* los errores detectados;
* sus correcciones;
* los cambios de interpretación;
* las erratas;
* los resultados intermedios;
* las referencias todavía no verificadas;
* las limitaciones conocidas;
* las cuestiones todavía abiertas.

No se presenta este material como una metodología científicamente validada.

Se presenta como un artefacto producido por el experimento.

## 7. Siguiente fase

La revisión experta independiente no se considera un trámite editorial posterior.

Es la primera prueba externa del resultado producido durante la fase asistida por IA.

La pregunta ahora es:

¿Qué errores, limitaciones, omisiones o méritos detectarán especialistas humanos en un artefacto que fue construido, criticado, programado y corregido durante múltiples rondas de interacción entre sistemas de IA bajo la dirección de una persona no especialista?

Lo que los expertos encuentren —incluyendo la posibilidad de que concluyan que el enfoque es inviable— forma parte del resultado del experimento.

Por esa razón, el estado del repositorio previo a esa revisión debe preservarse sin modificaciones retrospectivas.

*Congelada el 27 de agosto de 2026 como parte del snapshot de fin de la
fase asistida por IA — tag `fase-ia-v1.1`. Su hash SHA-256 figura en
`/HASHES.txt` junto al del protocolo consolidado.*

*Maximiliano Winter — Resistencia, Chaco, Argentina.*

