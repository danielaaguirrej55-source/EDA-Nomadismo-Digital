![Proyecto EDA: Nomadismo digital y coste de vida](./src/img/EDA-nomadismo-digital.jpg)

## Nomadismo digital: análisis sobre el coste de vida

### Autores del proyecto

**Daniela Aguirre**: 
1. [LinkedIn](https://www.linkedin.com/in/alicia-aguirre-5b5a57188/) 
2. [GitHub] 

**Alejandro Balaguer**: 
1. [LinkedIn] 
2. [GitHub] 

**Juan F. Cía**: 
1. [LinkedIn](https://www.linkedin.com/in/juanfcia/)
2. [GitHub](https://github.com/juanfcia)

### Descripción del proyecto

Análisis exploratorio de datos sobre 4.742 ciudades y 85 países para identificar los mejores destinos para nómadas digitales, evaluando el equilibrio entre coste de vida, infraestructura digital y calidad de vida.

**Se validaron 9 hipótesis** sobre los factores determinantes del atractivo de un destino. El análisis integra 3 datasets complementarios: precios de consumo (Numbeo/Kaggle), índice de nomadismo digital de Circleloop y ránking de Movingto.

La **conectividad a internet** y el **bienestar social** son las variables más relevantes dentro de la puntuación nómadas de los destinos, incluso por encima del coste de vida. Y además los destinos mejor rankeados son más caros, no más baratos.

### **Resumen de correlaciones y confirmaciones de hipótesis planteadas en el EDA**

❌ **Hipótesis 1**: Existe una relación positiva entre coste y ránking, por lo que un menor gasto mensual no lleva a elegir destino
✅ **Hipótesis 2**: A mayor poder adquisitivo mejora la nota dada al país por parte de los nómadas
✅ **Hipótesis 3**: A mayor velocidad de acceso a internet, mejor el puesto en el ránking nómada
❌ **Hipótesis 4**: El coste en vivienda no es relevante. Comer fuera o el gasto en la cesta prevalecen
✅ **Hipótesis 5**: Mejor relación calidad precio de productos y servicios correla positivamente
✅ **Hipótesis 6**: Sí, los nómadas digitales se fijan en el índice de felicidad de los países
✅ **Hipótesis 7**: El TOP3 de países con menos coste y mejor puntuación son: Rumanía, Hungría y Lituania, tres en Europa
❌ **Hipótesis 8**: La seguridad en el país de destino no es un elemento clave para el ránking
✅ **Hipótesis 9**: La facilidad para conseguir la visa, en cambio, sí lo es

### Sobre los datasets

1. Resumen de datasets originales

| Dataset | Registros | Variables | Fuente |
|---------|-----------|-----------|--------|
| Cost of Living | 4.742 ciudades | 65 variables | [Numbeo/Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data) |
| Circleloop Index | 85 países | 10 variables | [Circleloop](https://www.circleloop.com/nomadindex/) |
| Movingto Index | 40 países | 10 variables | [Movingto](https://www.movingto.com/digital-nomad-index) |

2. Creación de 6 variables agregadas que dieran sentido al enorme volumen de variables de Costo of Living 

- `monthly_nomad_cost`: coste mensual total estimado para nómada
- `local_purchasing_power`: poder adquisitivo local
- `housing_salary_ratio`: % salario destinado a vivienda
- `nomad_housing_cost`: coste medio del alquiler de un piso de 1 habitación
- `basic_basket_index`: cesta básica de la compra en supermercados
- `daily_meal_cost`: coste diario de comidas fuera de casa

### Metodología

1. Fases del EDA

| Fase | Tipo | Técnicas |
|------|------|----------|
| 1 | Univariante | Barplot, Piechart, histogramas, boxplots, estadísticos descriptivos |
| 2 | Bivariante | Scatterplots y regplots |

1. Visualizaciones para el análisis

El análisis incluye distribuciones, boxplots, heatmaps de correlación y scatter y regplots multidimensionales.

### Cómo ejecutar el proyecto

```bash
# Clonar repositorio
git clone https://github.com/[usuario]/EDA-Nomadismo-Digital.git
cd EDA-Nomadismo-Digital

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar notebook principal
jupyter notebook main.ipynb
```

### Estructura del repositorio del proyecto

```
EDA-Nomadismo-Digital/
├── main.ipynb              # Notebook final del EDA (9 secciones)
├── README.md               # Este documento
├── requirements.txt        # Dependencias Python
└── src/
    ├── data/               # Datasets (datasets en raw y limpios)
    ├── img/                # Imágenes y visualizaciones
    ├── notebooks/          # Notebooks de desarrollo y ETL
    └── utils/              # Código python reutilizable
```

### Tecnologías utilizadas

| Componente | Tecnología |
|------------|------------|
| Lenguaje | Python 3.12+ |
| Librerías | Pandas, NumPy |
| Visualización | Matplotlib, Seaborn |
| Entorno | Jupyter Notebooks |


## Autores del proyecto

| Autor | LinkedIn | GitHub |
|-------|----------|--------|
| **Daniela Aguirre** | [LinkedIn](https://www.linkedin.com/in/alicia-aguirre-5b5a57188/) | - |
| **Alejandro Balaguer** | - | - |
| **Juan F. Cía** | [LinkedIn](https://www.linkedin.com/in/juanfcia/) | [GitHub](https://github.com/juanfcia) |


## Referencias

- [Global Cost of Living Dataset - Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data)
- [Movingto Digital Nomad Index 2025](https://www.movingto.com/digital-nomad-index)
- [Circleloop Nomad Index](https://www.circleloop.com/nomadindex/)
