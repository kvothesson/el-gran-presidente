# Decreto 002 — La biblioteca infinita
### Programa técnico · El Gran Presidente T4E2

> El Gran Presidente es un personaje de ficción. Esta propuesta es real, está abierta a debate y se puede copiar, mejorar o refutar. Firma: Kvothesson.

## En una línea

**Sarmiento puso una biblioteca en cada pueblo; ahora va una inteligencia en cada bolsillo, pagada con la regalía del frío (Decreto 001) y no con impuestos.**

## Qué existe y qué se propone

| Pieza | Estado |
|---|---|
| Bibliotecas populares (Ley 419, 1870, impulsada por Sarmiento) | Existe: es el modelo de derecho de acceso |
| Gratuidad universitaria (1949) | Existe |
| Conectar Igualdad (2010): computadoras para escuelas públicas | Existió: antecedente de acceso a herramienta digital |
| Empresas de IA que dan acceso a sus asistentes a gobiernos, docentes o estudiantes mediante acuerdos | Existen antecedentes afuera |
| Modelos de IA abiertos con licencias que permiten uso público masivo | Existen: son la alternativa |
| Cómputo público gratuito para investigadores (Clementina XXI y centros universitarios, vía SNCAD) | Existe: base para un piloto |
| Regalía en cómputo | Propuesta del Decreto 001 |
| Derecho ciudadano a IA, niveles de acceso, cláusula de privacidad | **Propuesta de este decreto** |

## 1. Problema

La IA ya es una herramienta de productividad, educación y trabajo. Hoy se paga en dólares y por suscripción: un plan de uso intensivo cuesta USD 100–200 por mes. Eso crea una brecha nueva, la misma que en su momento hubo con los libros, la universidad y la computadora. El que puede pagar multiplica su capacidad. El que no, queda afuera.

## 2. Medidas

| Art. | Medida | Detalle |
|---|---|---|
| 1 | **Derecho de acceso universal** | Toda persona con DNI accede a un asistente de IA de uso diario, sin costo, con tope de uso justo alto (orden de 50.000 tokens/día). Para casi todos se siente ilimitado |
| 2 | **Financiamiento por regalía** | Se paga con el cómputo de la regalía del Decreto 001 (2–5% de cada data center con beneficios), no con presupuesto ni impuestos |
| 3 | **Modelo garantizado** | La forma más simple: la empresa que instala sus servidores acá paga la regalía dando acceso ciudadano a su propio asistente, sea cual sea. Si alguna no lo ofrece, su parte de cómputo corre modelos abiertos alojados en suelo argentino |
| 4 | **Privacidad por defecto** | Las conversaciones no se usan para vigilancia, publicidad ni entrenamiento sin consentimiento explícito. Los datos quedan en el país. El DNI solo valida el cupo y nunca se vincula al contenido. Hay auditoría independiente |
| 5 | **Nivel intensivo** | Cupos de uso intensivo (equivalente a planes "Max") por convocatoria abierta para estudiantes, docentes, científicos, devs y pymes, con criterios públicos |

## 3. La cuenta

| | Millones de personas por día (30.000 tokens cada una) |
|---|---|
| Regalía 5%, escenario optimista | ~87 |
| Toda la población | 46 |
| Uso real esperado (1 de cada 3 argentinos por día) | ~15 |
| Regalía 5%, escenario conservador | ~13 |

- **Uso real:** en el escenario conservador la regalía empata con la demanda esperada. En el optimista sobra para toda la población y para miles de cupos intensivos.
- **Precio de lista:** dar un plan Max 20x a cada argentino costaría ~USD 110.000 M por año. A costo de cómputo propio y por uso real, el número es órdenes de magnitud menor.
- **Tendencia:** el costo por token a calidad constante viene cayendo cerca de 10 veces por año. El tope de uso justo puede subir todos los años con la misma regalía. "Infinito" no existe, porque todo cómputo es energía, pero el techo se aleja solo.

*Supuestos detallados en el programa del Decreto 001, §4. Son estimaciones de orden de magnitud, no datos.*

## 4. Implementación por etapas

1. **Piloto inmediato, sin data center nuevo.** Correr un modelo abierto en infraestructura pública existente (Clementina XXI, centros universitarios del SNCAD) para docentes y estudiantes de una provincia. Mide demanda real y costo.
2. **Con la regalía:** escalar a todos los ciudadanos cuando entre en operación el primer data center adherido.
3. **Con acuerdos:** cada empresa que se instale ofrece su propio asistente a los ciudadanos como forma de pagar la regalía.

**Interfaz:** una app y una web simples, también por WhatsApp para llegar a todos, con identidad vía Mi Argentina solo para validar el cupo.

## 5. Preguntas abiertas

1. ¿Uso justo por persona o bolsa familiar compartible?
2. ¿Quién elige qué modelo corre? Una opción es un comité técnico con benchmarks públicos y actualización semestral.
3. ¿Cómo se garantiza la privacidad frente a futuros gobiernos? ¿Ley, no decreto? ¿Cifrado y retención cero por diseño?
4. ¿Se ofrece también a los argentinos en el exterior?
5. ¿Debe haber una API abierta para que devs locales construyan servicios sobre el cupo ciudadano?

## 6. Fuentes

- Programa del Decreto 001 (fuentes sobre Stargate Argentina, RIGI y Súper RIGI)
- Ley 419 de Bibliotecas Populares (1870)
- Decreto 29.337/1949, gratuidad universitaria
- Decreto 459/2010, Programa Conectar Igualdad

**Pendiente de verificar antes de publicar:** detalles actuales de los programas de labs con países y licencias de los modelos abiertos citados (algunas restringen ciertos usos).
