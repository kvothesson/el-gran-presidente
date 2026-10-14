# Decreto 001 — El frío se cobra
### Programa técnico · El Gran Presidente T4E1

> El Gran Presidente es un personaje de ficción. Esta propuesta es real, está abierta a debate y se puede copiar, mejorar o refutar. Firma: Kvothesson.

## En una línea

**El que saca petróleo de la Argentina paga regalías. El que usa nuestro frío, viento y energía para pensar, también, pero en cómputo.** Es una regla vieja aplicada a un recurso nuevo: no prohíbe, no expropia y no espanta.

## Qué existe y qué se propone

| Pieza | Estado |
|---|---|
| Regalías por explotar recursos (12% en hidrocarburos, Ley 17.319) | Existe desde 1967: es el modelo |
| RIGI (Ley 27.742) | Existe |
| Súper RIGI para IA y data centers | En el Congreso (verificar estado) |
| Stargate Argentina (500 MW) | Anunciado en oct 2025, sin contratos firmes públicos |
| Acceso a la información pública (Ley 27.275) | Existe: el art. 4 se puede pedir hoy |
| Exigir energía propia y métricas verdes a data centers | Antecedentes en Irlanda y Singapur |
| Cómputo público para ciencia y startups | Antecedente en las AI Factories de la UE (EuroHPC) |
| Cuota de cómputo, metas de empleo, cláusula de cumplimiento | **Propuesta de este decreto** |

## 1. Problema

Argentina tiene ventajas reales para alojar data centers de IA: clima frío, viento, espacio y potencial renovable en la Patagonia. Los incentivos ya existen (RIGI, y el Súper RIGI en discusión para inversiones de IA desde USD 1.000 M). El anuncio más grande es Stargate Argentina: 500 MW y USD 20.000–25.000 M (oct 2025), aunque a mediados de 2026 no hay contratos firmes públicos.

El riesgo es repetir el patrón histórico de un enclave: mucho consumo de energía y agua, beneficios fiscales largos, poco empleo calificado y ningún cómputo disponible para el sistema científico y productivo local. Hoy el país tiene ~73 MW instalados (Brasil, ~2.100 MW), así que las reglas que se fijen ahora definen el sector por décadas.

## 2. Principio

Ni puerta cerrada ni puerta regalada: **beneficios a cambio de encadenamiento verificable**. Las condiciones tienen que ser lo bastante livianas para no espantar la inversión y lo bastante medibles para que se puedan auditar.

## 3. Medidas

| Art. | Medida | Propuesta concreta (a calibrar) | Cómo se verifica |
|---|---|---|---|
| 1 | **Regalía en cómputo** | Reservar entre el 2% y el 5% de la capacidad de GPU, a precio de costo, para los argentinos: acceso ciudadano (ver Decreto 002), universidades, CONICET y startups, con asignación por convocatoria abierta | Horas-GPU cedidas y usadas, por institución, en un reporte trimestral |
| 2 | **Energía adicional** | La demanda del data center se cubre con generación renovable nueva (PPA propio), no con capacidad existente de la red. Los excedentes se inyectan al sistema | Certificados de origen y CAMMESA. MW nuevos instalados contra MW consumidos |
| 3 | **Talento local** | Meta escalonada de empleo técnico argentino (p. ej., 60% al año 3 y 80% al año 6), más un programa de formación con universidades de la provincia anfitriona | Nómina anonimizada por rol y origen, y convenios firmados |
| 4 | **Transparencia total** | Publicación anual en datos abiertos de energía, agua, empleo, cómputo cedido, beneficios fiscales recibidos y uso del suelo | Dataset público y verificable, auditado por un organismo de control |
| 5 | **Cláusula de cumplimiento** | El beneficio fiscal se suspende de forma proporcional si se incumplen los arts. 1–4 durante dos períodos seguidos. No es una expropiación: es una condición del beneficio | Previsto en el acto de adhesión al régimen |

## 4. ¿Cuánto es el 5%? (orden de magnitud)

Supuestos gruesos, para discutir y no para citar como dato:

| Variable | Supuesto |
|---|---|
| Potencia del data center | 500 MW (Stargate Argentina anunciado) |
| GPUs | ~300.000 clase H100 (1,2 a 1,4 kW por GPU con enfriamiento y red) |
| Rendimiento de inferencia | 300 (conservador) a 2.000 (optimista) tokens/s por GPU |
| **5% de regalía** | **~0,4 a ~2,6 billones de tokens por día** |
| Uso por persona | 30.000 tokens/día (un usuario típico consume entre 15.000 y 50.000) |

En personas, que se entiende mejor:

| | Millones de personas por día |
|---|---|
| Regalía 5%, escenario optimista | ~87 |
| Toda la población | 46 |
| Uso real esperado (1 de cada 3 argentinos por día) | ~15 |
| Regalía 5%, escenario conservador | ~13 |

**Conclusión:** aun en el escenario conservador, la regalía cubre casi todo el uso real esperado del país. En el optimista alcanza para toda la población. El costo por token a igual calidad cae unas 10 veces cada 12 a 18 meses, así que el margen crece solo. El escenario conservador cuenta solo tokens generados, los más caros, así que subestima la capacidad real.

## 5. Por qué no espanta la inversión

- **Los costos son acotados.** Ceder entre el 2% y el 5% de la capacidad a precio de costo pesa poco frente a beneficios fiscales de 30 años.
- **Las condiciones ya son estándar en otros países.** Varios condicionan permisos de data centers a la energía nueva y a reportar agua y energía. Las empresas ya lo miden para sus reportes ESG.
- **El talento local les baja costos.** A la empresa le conviene operar con ingenieros formados en la zona.
- **La previsibilidad vale más que el subsidio.** Reglas claras y estables, fijadas antes de la inversión, son justamente lo que los especialistas señalan como el déficit argentino.

## 6. Implementación

- **Vía más simple:** incorporar los arts. 1–5 como condiciones de adhesión en la reglamentación del régimen de incentivos para el sector data centers/IA, o como artículo específico en el Súper RIGI.
- **Vía provincial:** las provincias anfitrionas pueden exigir los arts. 2–4 en sus permisos ambientales y convenios.
- **Para empezar ya:** el art. 4 (transparencia) se puede pedir hoy vía acceso a la información pública (Ley 27.275) para cualquier proyecto adherido.

## 7. Preguntas abiertas

1. ¿Qué porcentaje de cómputo cedido es razonable antes de que afecte la decisión de inversión?
2. ¿Quién asigna el cómputo soberano sin que se politice? Una opción es un comité científico con convocatoria pública y resultados abiertos.
3. ¿Cómo se mide el agua en diseños con enfriamiento por aire, típicos de climas fríos?
4. ¿Las metas de empleo deben ser obligatorias o un bonus en el beneficio?

## 8. Fuentes

- [Stargate Argentina — DatacenterDynamics](https://www.datacenterdynamics.com/en/news/openai-plans-500mw-data-center-in-argentina/)
- [Gobierno argentino y OpenAI — Buenos Aires Herald](https://buenosairesherald.com/business/argentine-government-and-openai-announce-project-to-build-data-center-in-patagonia)
- [Sur Energy espera activar data centers en 2027 — Bloomberg Línea](https://www.bloomberglinea.com/latinoamerica/argentina/sur-energy-socia-de-open-ai-en-argentina-espera-activar-data-centers-patagonicos-en-2027/)
- [Súper RIGI y data centers — iProfesional](https://www.iprofesional.com/tecnologia/457187-como-argentina-se-puede-transformar-en-un-megacentro-de-datos-a-traves-del-super-rigi)
- [¿Nuevo campo digital u otra economía de enclave? — El Economista](https://eleconomista.com.ar/economia/argentina-frente-boom-data-centers-nuevo-campo-digital-u-otra-economia-enclave-n94044)
- [Argentina en la carrera de los data centers — El Observador](https://www.elobservador.com.uy/argentina/economia-y-negocios/argentina-frente-la-carrera-global-los-data-centers-ventajas-y-desafios-atraer-inversiones-ia-n6053040)

**Pendiente de verificar antes de publicar:** estado actual del Súper RIGI en el Congreso y si Stargate Argentina se presentó formalmente al RIGI.
