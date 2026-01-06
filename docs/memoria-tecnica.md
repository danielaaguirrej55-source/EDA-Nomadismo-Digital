# Memoria técnica — [Nomadismo Digital]

| Autor | LinkedIn | GitHub |
|-------|----------|--------|
| **Daniela A. Aguirre** | [LinkedIn](https://www.linkedin.com/in/alicia-aguirre-5b5a57188/) | [GitHub](https://github.com/danielaaguirrej55-source) |
| **Juan F. Cía** | [LinkedIn](https://www.linkedin.com/in/juanfcia/) | [GitHub](https://github.com/juanfcia) |
| **Alejandro Balaguer** | - | - |

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

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2. Contexto y objetivos
El nomadismo digital ha crecido como alternativa laboral y de estilo de vida, pero la elección de destino suele depender de factores económicos (coste de vida, vivienda, precios esenciales) además de la calidad de vida. Este proyecto analiza, a nivel global, qué variables económicas y de coste de vida están asociadas con un mejor posicionamiento de los destinos para nómadas digitales.

**Objetivo general:** identificar patrones y diferencias entre destinos mejor y peor rankeados mediante un Análisis Exploratorio de Datos (EDA), evaluando el peso relativo de variables como vivienda, coste total, salarios y precios de bienes/servicios esenciales.

**Objetivos específicos:**
- Comparar costes entre grupos (top vs bottom del ranking).
- Evaluar el papel del coste de vivienda como factor diferenciador.
- Explorar coherencia entre salarios e índices de precios (poder adquisitivo).
- Detectar outliers atractivos (alta valoración con coste moderado).
- Identificar qué rubros de gasto impactan más en la viabilidad.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
  
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
## 4. Diseño y arquitectura:
El proyecto se estructura como un pipeline de análisis exploratorio:
4.1. **Carga de datos** desde el archivo fuente del dataset:
-  ```bash
# Clonar repositorio
git clone https://github.com/[usuario]/EDA-Nomadismo-Digital.git
cd EDA-Nomadismo-Digital

4.2. **Preparación**: limpieza, tratamiento de nulos, validaciones y variables derivadas:
   # Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

4.3. **EDA**: análisis descriptivo, segmentación por ranking y exploración de relaciones entre variables.
   
4.4. **Comunicación**: generación de visualizaciones y conclusiones (notebook + presentación).
**Estructura del repositorio (referencial):**
- `data/`: datasets originales utilizados:

| Dataset | Registros | Variables | Fuente |
|---------|-----------|-----------|--------|
| Cost of Living | 4.742 ciudades | 65 variables | [Numbeo/Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data) |
| Circleloop Index | 85 países | 10 variables | [Circleloop](https://www.circleloop.com/nomadindex/) |
| Movingto Index | 40 países | 10 variables | [Movingto](https://www.movingto.com/digital-nomad-index) |
- 
- `img/`: imágenes/gráficas exportadas para documentación/presentación. (pendiente)
- 
- `requirements.txt`: Entorno y dependencias:
El proyecto se desarrolló en Python y las dependencias del entorno están definidas en `requirements.txt`, lo que permite reproducir el análisis instalando las librerías necesarias. Aunque el archivo incluye dependencias transitivas, para el EDA se utilizaron principalmente librerías de análisis y visualización de datos (p. ej., pandas/numpy y matplotlib/seaborn, además de Jupyter para la ejecución de notebooks).


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 5. Implementación:
El EDA se desarrolló en notebooks de Jupyter dentro de la carpeta `notebooks/`. El flujo de trabajo incluye: carga de los datasets, limpieza, análisis descriptivo, comparaciones por grupos del ranking, variables agregadas, visualizaciones y detección de outliers.

**Archivos principales:**
- `notebooks/[NOMBRE].ipynb`: (Cuando ya tengamos notebook final: renombrar a algo neutro)
- ### Notebooks por fase
- **ETL / Preparación de datos:** notebooks encargados de limpiar, homogeneizar e integrar variables de coste de vida e índices.
- **Variables agregadas:** notebooks donde se crean variables derivadas y métricas para el análisis.
- **EDA univariante y bivariante:** notebooks con estadística descriptiva, comparaciones por grupos y relaciones entre variables.
- **Notebook principal:** consolidación de resultados, visualizaciones finales y conclusiones.
 > Nota: aunque algunos archivos mantienen nombres individuales, el contenido final integra el trabajo del equipo.
  
- `data/[NOMBRE]`: Datasets utilizados:
- El análisis se realizó sobre el dataset descrito en el punto 1 y 4, tras un proceso de limpieza y preparación (ETL) documentado en los notebooks correspondientes.
- 
- `img/`: gráficas exportadas usadas en la presentación y documentación (pendiente)
- 
- `docs/memoria-tecnica.md`: memoria técnica del proyecto (se añade al finalizar)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 6. Pruebas:
Al tratarse de un análisis exploratorio, las “pruebas” se enfocaron en validaciones de calidad del dato:
- Revisión de valores nulos y estrategia de tratamiento (eliminación/imputación según variable).
- Búsqueda de duplicados y verificación de claves.
- Validación de rangos razonables (por ejemplo, costes y salarios no negativos).
- Comprobación de coherencia de unidades/monedas cuando fue necesario, se hizo una estandarizacion de mondea a USD.
- Revisión de outliers para distinguir errores de registro vs. casos reales.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 7. Resultados:

Los resultados del EDA se presentan organizados según las preguntas iniciales del proyecto. Para ello, se compararon destinos por grupos de ranking (por ejemplo, destinos mejor posicionados frente a peor posicionados), se analizaron distribuciones y relaciones entre variables económicas y se revisaron casos atípicos (outliers).

### 7.1 ¿Son realmente más baratos los destinos mejor rankeados?
La comparación por grupos sugiere que existen diferencias en el coste de vida entre destinos mejor y peor posicionados, aunque dichas diferencias no son uniformes para todos los rubros. En particular, **[mencionar si el coste total baja o no en el top]**.  
**Evidencia:** [Figura/Tabla: comparación de coste total por grupos de ranking].

### 7.2 ¿El coste de vivienda es el principal factor diferenciador?
Entre las variables analizadas, el coste de vivienda destaca por **[mayor diferencia entre grupos / mayor correlación / mayor dispersión]**, lo que indica que este componente tiene un peso importante en la viabilidad económica del destino.  
**Evidencia:** [Figura: boxplot de alquiler por grupos] y/o [Tabla: ranking de variables por correlación].

### 7.3 ¿Existe coherencia entre salarios locales y precios esenciales?
Al contrastar variables de ingresos (si están disponibles) con precios de productos/servicios esenciales, se observa **[patrón: coherencia parcial / baja coherencia / relación esperada]**. Esto sugiere que el ranking no depende únicamente del nivel salarial, sino también de la estructura de costes y de la relación entre ingresos y gasto básico.  
**Evidencia:** [Figura: scatter salario vs coste] / [Figura: índices de poder adquisitivo].

### 7.4 ¿Hay “outliers” atractivos?
Se identificaron destinos que combinan buen posicionamiento con costes moderados (outliers atractivos), lo cual puede representar oportunidades para perfiles con presupuesto limitado. Estos casos aparecen asociados a **[región/condiciones]**.  
**Evidencia:** [Figura: scatter ranking vs coste con puntos destacados] + lista breve de ejemplos.

### 7.5 ¿Qué tipo de gasto pesa más en la viabilidad del nomadismo digital?
El análisis sugiere que los rubros con mayor impacto en la diferencia entre destinos son **[vivienda / coste total / otro]**, mientras que otros gastos muestran variación menor o menor capacidad explicativa.  
**Evidencia:** [Tabla/Figura: contribución o comparación de rubros].

### 7.6 Resumen de respuestas
1. **Más baratos en promedio:** [Sí/No/Depende] — [1 frase].
2. **Vivienda como factor principal:** [Sí/No] — [1 frase].
3. **Coherencia salarios-precios:** [Alta/Media/Baja] — [1 frase].
4. **Outliers atractivos:** [Sí] — [menciona 1–3 destinos].
5. **Gasto más determinante:** [vivienda/otro] — [1 frase].

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 8. Despliegue y uso

## 9. Gestión del proyecto

## 10. Conclusiones y trabajo futuro
