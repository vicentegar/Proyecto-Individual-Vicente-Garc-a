Tecnología de Celdas PEM en Chile
Tecnología en Chile

La tecnología de celdas de combustible PEM presenta una gran oportunidad de aplicación en Chile gracias a su combinación única de recursos naturales, infraestructura energética y compromisos estratégicos de descarbonización.

Chile posee una de las mayores capacidades de producción de hidrógeno verde del mundo, habilitada por el altísimo potencial solar del desierto de Atacama y los vientos intensos de la zona austral [1,2]. Esto permite generar hidrógeno a menor costo y con una huella de carbono considerablemente más baja.

En el país ya existen proyectos piloto que utilizan celdas PEM. Entre ellos destaca el desarrollado por ENAP [3] y la planta de HIF en Magallanes, iniciativa de gran interés internacional [4].

La minería, uno de los motores económicos de Chile, también impulsa esta adopción al requerir tecnologías limpias y eficientes que reduzcan emisiones locales. Las celdas PEM tienen el potencial de sustituir motores diésel en equipos industriales, especialmente en minería. Asimismo, los compromisos nacionales de carbono-neutralidad al 2050 refuerzan la implementación de tecnologías basadas en hidrógeno en aplicaciones industriales, portuarias y residenciales [5].

En conjunto, estos factores hacen que la implementación de celdas PEM sea técnicamente viable y estratégicamente coherente con la política energética del país.

Evaluación del impacto social, ambiental y económico en Chile

La adopción de celdas de combustible PEM puede generar impactos relevantes en distintos ámbitos:

Impacto ambiental

Las celdas PEM no producen emisiones locales, mejorando la calidad del aire en zonas urbanas o industriales.

En minería, sustituir motores diésel reduce material particulado y NOx [6].

Cuando funcionan con hidrógeno verde —como el producido en Magallanes— la huella de carbono es prácticamente cero [4].

Contribuyen a los compromisos de carbono-neutralidad para 2050 [5].

Impacto social

Se crean nuevos perfiles laborales en el ecosistema del hidrógeno verde.

Universidades y centros regionales (Antofagasta, Magallanes) ya están formando capital humano especializado.

Impulsa el desarrollo tecnológico local y nuevas capacidades en la industria energética.

Impacto económico

Las celdas PEM habilitan una cadena de valor completa asociada al hidrógeno verde.

Chile posee ventajas competitivas naturales para producir hidrógeno a bajo costo.

Aumenta el interés de inversión extranjera (HIF) y nacional (ENAP en Cabo Negro) [4,7].

El mercado global del hidrógeno se proyecta en 317 mil millones de dólares para 2030 [8].

Proyección futura en Chile

Chile enfrenta una oportunidad extraordinaria para consolidarse como líder mundial en hidrógeno verde. Sus ventajas competitivas naturales reducen una de las principales barreras de esta tecnología: el costo de producción del hidrógeno.

La existencia de múltiples proyectos nacionales e internacionales demuestra que el interés por las celdas PEM es real y creciente. Sin embargo, aún existen desafíos: reducción de costos, infraestructura, regulación y la acumulación de conocimiento técnico.

Pese a estos puntos, la perspectiva a futuro es altamente positiva. Si Chile mantiene el ritmo de inversión, regulación moderna y desarrollo tecnológico, podrá consolidar un ecosistema competitivo y sostenible basado en hidrógeno verde.

Implementación del Código [9]
Constantes y tablas de parámetros

Se definen:

Constantes del proceso, tomadas directamente del paper.

Tablas de parámetros extraídas desde gráficos del paper mediante WebPlotDigitizer [10], de acuerdo a cada temperatura.

Presiones parciales

En base a las condiciones experimentales del paper:

Hidrógeno (1 bar): alimentado puro → presión parcial igual a la total del ánodo.

Oxígeno (0,21 bar): aire atmosférico (21% O₂).

Vapor de agua (Psat): los gases se humidifican mediante burbujeo a la misma temperatura de operación → vapor a presión de saturación.

Voltaje de circuito abierto

Se emplea la ecuación de Nernst, que depende de la energía libre de Gibbs, variable con la temperatura.
Se utiliza la expresión del potencial dependiente de temperatura vista en clases (cálculo adjunto y documentado).

Sobrepotenciales

Se utilizan las expresiones del paper:

Activación: despeje de la ecuación de Butler–Volmer.

Óhmico: fórmula empírica propuesta por los autores (justificación adjunta).

Concentración: incluida por completitud, aun cuando sea despreciable en este rango de operación.

Generación de la curva

La curva de polarización se genera evaluando la ecuación completa del modelo para un rango de densidades de corriente:

Se obtienen los parámetros correspondientes a la temperatura elegida:
C1, C2, i0,c, in.

Se calcula el voltaje de circuito abierto con la ecuación de Nernst.

Para cada densidad de corriente se calculan los tres sobrepotenciales.

Estos se restan del voltaje abierto para obtener el voltaje total.

Se recorre todo el vector de corrientes para construir la curva V–i final.

Referencias

[1] Bernardelli, F. (2011, junio). Energía solar termodinámica en América Latina: los casos del Brasil, Chile y México (Doc. № LC/W.402). CEPAL. https://repositorio.cepal.org/handle/11362/3867

[2] Ministerio de Energía. (s. f.). Explorador Eólico. Gobierno de Chile. https://eolico.minenergia.cl/

[3] ENAP. (2024, 17 de octubre). Planta de hidrógeno verde de ENAP presenta un 72% de avance. https://www.enap.cl/sala-de-prensa/planta-de-hidrogeno-verde-de-enap-presenta-un-72-de-avance

[4] HIF Global. (s. f.). HIF Haru Oni. https://es.hifglobal.com/locations/hif-haru-oni

[5] Ministerio del Medio Ambiente. (s. f.). Estrategia Climática de Largo Plazo 2050. Gobierno de Chile. https://cambioclimatico.mma.gob.cl/estrategia-climatica-de-largo-plazo-2050/descripcion-del-instrumento/

[6] Silva Garrido, V. E. (2022). Diseño de un piloto de celdas de combustible de hidrógeno como fuente de energía para camiones CAEX (Tesis de pregrado). Universidad de Chile. https://repositorio.uchile.cl/handle/2250/188029

[7] ENAP. (2024, octubre 17). Planta de hidrógeno verde de ENAP presenta un 72% de avance. https://www.enap.cl/sala-de-prensa/planta-de-hidrogeno-verde-de-enap-presenta-un-72-de-avance

[8] Grand View Research. (s. f.). Hydrogen generation market. https://www.grandviewresearch.com/industry-analysis/hydrogen-generation-market

[9] Santarelli, M. G., Torchio, M. F., & Cochis, P. (2005). Parameters estimation of a PEM fuel cell polarization curve and analysis of their behavior with temperature. Journal of Power Sources, 145(2), 334–345.

[10] Rohatgi, A. (2025). WebPlotDigitizer. https://automeris.io/WebPlotDigitizer
