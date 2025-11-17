# Tecnología en Chile
La tecnología de celdas de combustible PEM tiene una gran oportunidad de aplicación en Chile debido a una combinación única de recursos, infraestructura y compromisos estratégicos del país. Chile cuenta con una de las mayores capacidades mundiales de generación de hidrógeno verde a nivel mundial, gracias al potencial solar del desierto de Atacama y a los vientos de la zona Austral [1,2], lo que permite producir hidrogeno a bajo costo y con una huella de carbono mínima. En Chile ya existen proyectos piloto que operan con celdas PEM. Uno de ellos es impulsado por ENAP [3], mientras que otro, de alto interés internacional, corresponde a la planta instalada por HIF en Magallanes [4]. Además, la industria minera, una actividad estratégica nacional, requiere tecnologías energéticas limpias y de alta eficiencia que reduzcan emisiones locales, donde las celdas PEM pueden sustituir motores diésel en equipos. Finalmente, Chile mantiene compromisos internacionales de descarbonización al 2050, lo que impulsa la adopción de tecnologías de hidrógeno en aplicaciones industriales, portuarias y residenciales [5]. En conjunto, estos factores hacen que la implementación de celdas PEM sea técnicamente viable y estratégicamente coherente con la política energética del país.

# Evaluación del impacto social, ambiental y económico en Chile
La adopción de celdas de combustible PEM en Chile puede generar impactos significativos en lo social, ambiental y económico. Desde la perspectiva ambiental, la operación de las celdas PEM es completamente libre de emisiones locales, lo que contribuye a mejora la calidad del aire en zonas urbanas y en áreas industriales como en la parte minera, donde la sustitución de motores diésel reduciría material particulado y NOx [6]. Además, si el hidrógeno proviene de fuentes renovables, como ocurre con el proyecto de HIF en Magallanes [4], la huella de carbono del sistema cae prácticamente a cero, alineándose con los compromisos del país para la carbono neutralidad al 2050 [5]. En el ámbito social, la introducción de esta tecnología impulsa la creación de nuevos perfiles laborales en el ecosistema del hidrógeno verde, fortaleciendo capacidades locales en regiones como Antofagasta y Magallanes, donde universidades y centros de investigación ya están formando capital humano para esta industria emergente. Finalmente, desde el punto de vista económico, las celdas PEM habilitan el desarrollo de cadenas de valor asociadas al hidrógeno verde, un sector donde Chile posee ventajas competitivas naturales, como se vio en el apartado anterior. Esto abre oportunidades de inversión extranjera, como con HIF [4], como también nacional, con el proyecto de ENAP en Cabo Negro [7]. Además, el mercado del hidrógeno se espera que crezca a 317 billones de dólares para el 2030 [8].

# Proyección futura en Chile
Considerando lo analizado en los puntos anteriores, Chile enfrenta una oportunidad excepcional para desarrollar el mercado del hidrógeno gracias a sus ventajas competitivas naturales, que permiten reducir una de las principales barreras económicas de esta tecnología: el costo de producción. La existencia de proyectos nacionales e internacionales en ejecución demuestra que el interés por el hidrógeno y las celdas PEM es real y creciente. No obstante, al tratarse de una tecnología aún emergente, persisten desafíos asociados a la reducción de costos, el desarrollo de infraestructura y la generación de conocimiento local. Aun así, una mayor adopción de estas tecnologías podría acelerar el aprendizaje, abaratar procesos y consolidar un ecosistema más competitivo. En síntesis, la factibilidad futura es altamente positiva, siempre que Chile mantenga su ritmo de inversión, fortalecimiento regulatorio y desarrollo tecnológico en los próximos años.

# Implementación Código [9]

## Constantes y tablas de parámetros
En primer lugar se definieron las constantes del proceso, en donde se agregan los valores dados por el paper.
Por otro lado, los parámetros de las tablas fueron dados en gráficos en el paper, en donde cada punto fue sacado a través de WebPlotDigitizer [10], para luego agregarlos con respecto a su temperatura.

## Presiones Parciales
Se utilizan las presiones parciales de las condiciones experimentales que da el paper. La celda opera a presión atmosférica, alimentada con hidrógeno puro en el ánodo y aire en el cátodo. Por lo tanto:
- Hidrógeno (1 bar): Se suministra puro, por lo que la presión parcial corresponde a la presión total del gas en el ánodo.
- Oxígeno (0,21 bar): Se considera aire atmosférico, cuya fracción molar de oxígeno es aproximadamente 21%
- Agua (Psat): El hidrógeno y aire se humidifican mediante burbujeo a la misma temperatura de operación, por lo que el vapor de agua alcanza su presión de saturación a dicha temperatura.

## Voltaje de Circuito Abierto
Se emplea la ecuación de Nerst, la cual depende de la energía libre de Gibbs, una magnitud que varía con la temperatura. Con el fin de incorporar correctamente este efecto térmico en el modelo, utilice la expresión del potencial dependiente de la temperatura vista en clases. Los desarrollos y cálculos para obtener esta relación están adjuntos.

## Sobrepotenciales
Se definieron los distintos sobrepotenciales utilizando las expresiones entregadas en el paper. Para el sobrepotencial de activación se define la fórmula dada en el paper, que representa el despeje del sobrepotencial de la ecuación de BV. En el caso del sobrepotencial óhmico, se empleó la formulación empírica propuesta por los autores, cuya justificación detallada se encuentra en el documento adjunto.
Asimismo, se incluyó la expresión del sobrepotencial de concentración, aun cuando su contribución práctica sea despreciable dentro del rango de operación considerado. Esto permite que cualquier usuario del código pueda modificar este término si su propios parámetros experimentales así lo requieren.

## Generación de la curva
La curva de polarización se genera evaluando la ecuación completa del modelo para un rango de densidades de corriente. El código obtiene los parámetros correspondientes a la temperatura seleccionada (C1, C2, i0,c, in) y calcula el voltaje de circuito abierto usando la ecuación de Nerst. Luego, para cada valor de corriente, se computan los tres sobrepotenciales principales y se restan del voltaje de circuito abierto. Al recorrer todo el vector de densidades de corriente, se construye la curva V-i completa que se representa gráficamente.

# Referencias
[1] Bernardelli, F. (2011, junio). Energía solar termodinámica en América Latina: los casos del Brasil, Chile y México (Doc. № LC/W.402). Comisión Económica para América Latina y el Caribe. https://repositorio.cepal.org/handle/11362/3867  
[2] Ministerio de Energía. (s. f.). Explorador Eólico. Gobierno de Chile. https://eolico.minenergia.cl/  
[3] ENAP. (2024, 17 de octubre). Planta de hidrógeno verde de ENAP presenta un 72% de avance. https://www.enap.cl/sala-de-prensa/planta-de-hidrogeno-verde-de-enap-presenta-un-72-de-avance  
[4] HIF Global. (s. f.). HIF Haru Oni. https://es.hifglobal.com/locations/hif-haru-oni  
[5] Ministerio del Medio Ambiente. (s. f.). Estrategia Climática de Largo Plazo 2050. Gobierno de Chile. https://cambioclimatico.mma.gob.cl/estrategia-climatica-de-largo-plazo-2050/descripcion-del-instrumento/  
[6] Silva Garrido, V. E. (2022). Diseño de un piloto de celdas de combustible de hidrógeno como fuente de energía para camiones CAEX (Tesis de pregrado). Universidad de Chile. https://repositorio.uchile.cl/handle/2250/188029  
[7] ENAP. (2024, octubre 17). Planta de hidrógeno verde de ENAP presenta un 72% de avance. https://www.enap.cl/sala-de-prensa/planta-de-hidrogeno-verde-de-enap-presenta-un-72-de-avance  
[8] Grand View Research. (s. f.). Hydrogen generation market. https://www.grandviewresearch.com/industry-analysis/hydrogen-generation-market  
[9] Santarelli, M. G., Torchio, M. F., & Cochis, P. (2005). Parameters estimation of a PEM fuel cell polarization curve and analysis of their behavior with temperature.  
[10] Rohatgi, Ankit, “Webplotdigitizer: Extract data from plots, images, and maps” (2025), Consultado el 2 de noviembre de 2025

