# Memoria técnica — [Nomadismo Digital]

**Autores:**
Juan F. Cía
Daniela A. Aguirre Jiménez
Alejanddro Balager

**Fecha:**  
0?/01/2026

**Repositorio:**  
EDA-Nomadismo-Digital

## 1. Resumen ejecutivo:
### Pregunta de investigación
A nivel global, ¿qué características económicas y de coste de vida diferencian a los destinos mejor posicionados para el nomadismo digital frente a los menos atractivos?

### Objetivo general
Realizar un Análisis Exploratorio de Datos (EDA) para estudiar la relación entre el posicionamiento/ranking de destinos para nómadas digitales y variables económicas/de coste de vida (según disponibilidad en el dataset), con el fin de identificar qué factores explican mejor las diferencias entre destinos más y menos atractivos, y si estos factores influyen tambien al buscar calidad de vida.

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) a nivel global para identificar qué variables económicas y de coste de vida diferencian a los destinos mejor posicionados para el nomadismo digital frente a los menos atractivos. El análisis se basa en un dataset de destinos internacionales que incluye un ranking de atractivo y métricas relacionadas con coste de vivienda, precios de bienes/servicios esenciales y, cuando aplica, indicadores de ingresos o salario.

El trabajo consistió en la revisión y limpieza de los datasets [Numbeo/Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data) | [Circleloop](https://www.circleloop.com/nomadindex/) y [Movingto](https://www.movingto.com/digital-nomad-index) (tratamiento de valores faltantes, verificación de rangos y consistencia de unidades), la generación de estadísticos descriptivos y comparativas por grupos de ranking (por ejemplo: top vs bottom), y el estudio de relaciones entre variables mediante correlaciones y visualizaciones (distribuciones, boxplots, heatmaps de correlación y scatter y regplots multidimensionales.). Además, se exploraron posibles casos atípicos (“outliers”) que combinan coste moderado con alta valoración.

Los resultados muestran que **[hallazgo 1]**, y que **[hallazgo 2]**. En particular, **[variable clave]** aparece como el factor con mayor capacidad para separar destinos altamente atractivos de los menos atractivos, mientras que **[otra variable]** presenta **[relación/efecto]**. Finalmente, se identificaron destinos que destacan por **[outlier: alta calidad/coste moderado]**, lo que sugiere oportunidades para perfiles de nómadas digitales con restricciones de presupuesto.

En conclusión, el EDA indica que **[conclusión principal]** y proporciona una base cuantitativa para priorizar destinos según **[criterio: coste, vivienda, poder adquisitivo, etc.]**.



## 2. Contexto y objetivos
El nomadismo digital ha crecido como alternativa laboral y de estilo de vida, pero la elección de destino suele depender de factores económicos (coste de vida, vivienda, precios esenciales) además de la calidad de vida. Este proyecto analiza, a nivel global, qué variables económicas y de coste de vida están asociadas con un mejor posicionamiento de los destinos para nómadas digitales.

**Objetivo general:** identificar patrones y diferencias entre destinos mejor y peor rankeados mediante un Análisis Exploratorio de Datos (EDA), evaluando el peso relativo de variables como vivienda, coste total, salarios y precios de bienes/servicios esenciales.

**Objetivos específicos:**
- Comparar costes entre grupos (top vs bottom del ranking).
- Evaluar el papel del coste de vivienda como factor diferenciador.
- Explorar coherencia entre salarios e índices de precios (poder adquisitivo).
- Detectar outliers atractivos (alta valoración con coste moderado).
- Identificar qué rubros de gasto impactan más en la viabilidad.

  

## 3. Requisitos:
### Requisitos funcionales
- Importar y explorar los datasets (estructura, tipos de datos, duplicados).
- Limpiar datos (valores nulos, formatos, unidades si aplica).
- Generar estadísticos descriptivos y comparaciones por grupos.
- Crear visualizaciones para soportar conclusiones (distribuciones, boxplots, heatmaps de correlación y scatter y regplots multidimensionales.)
- Identificar outliers y documentar casos relevantes.

### Requisitos no funcionales
- Reproducibilidad: ejecución mediante notebook/script con dependencias definidas.
- Claridad: resultados explicados con tablas y gráficas interpretables.
- Trazabilidad: cambios y avances gestionados en GitHub.

  

## 4. Diseño y arquitectura:
El proyecto se estructura como un pipeline de análisis exploratorio:
1. **Carga de datos** desde el archivo fuente del dataset.
2. **Preparación**: limpieza, tratamiento de nulos, validaciones y variables derivadas.
3. **EDA**: análisis descriptivo, segmentación por ranking y exploración de relaciones entre variables.
4. **Comunicación**: generación de visualizaciones y conclusiones (notebook + presentación).

**Estructura del repositorio (referencial):**
- `data/`: dataset(s) utilizados:  [Numbeo/Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data) | [Circleloop](https://www.circleloop.com/nomadindex/) y [Movingto](https://www.movingto.com/digital-nomad-index)
- 
- `notebooks/`: notebooks con el EDA.
- 
- `img/`: imágenes/gráficas exportadas para documentación/presentación.
- 
- `docs/`: memoria técnica en Markdown.
- 
- `requirements.txt`: dependencias del entorno.

- 
## 5. Implementación

## 6. Pruebas

## 7. Resultados

## 8. Despliegue y uso

## 9. Gestión del proyecto

## 10. Conclusiones y trabajo futuro
