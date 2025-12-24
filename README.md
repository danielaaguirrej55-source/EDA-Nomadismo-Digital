![Proyecto EDA: Nomadismo digital y coste de vida](./src/img/EDA-nomadismo-digital.jpg)

## 🌍 Nómadas digitales: análisis sobre el coste de vida

*Este proyecto se encuentra actualmente en fase de pensamiento.*

### 🏦 Autores del proyecto

**Daniela Aguirre**: 
1. [LinkedIn](https://www.linkedin.com/in/alicia-aguirre-5b5a57188/) 
2. [GitHub] 

**Alejandro Balaguer**: 
1. [LinkedIn] 
2. [GitHub] 

**Juan F. Cía**: 
1. [LinkedIn](https://www.linkedin.com/in/juanfcia/)
2. [GitHub](https://github.com/juanfcia)

### 📌 Descripción del proyecto

Este repositorio contiene un Análisis Exploratorio de Datos (EDA) exhaustivo sobre el conjunto de datos **Global Cost of Living**, con un enfoque específico en el fenómeno del **Nomadismo Digital**. 

El objetivo es identificar ciudades y países que ofrecen el mejor equilibrio entre calidad de vida y asequibilidad para profesionales remotos. En un mundo donde la oficina es cualquier lugar con Wi-Fi, entender las métricas de gasto mensual (vivienda, alimentación, transporte) es crucial para la toma de decisiones estratégicas de movilidad.

### 📊 Sobre los datasets

· Los datos utilizados con fuente primaria provienen del dataset Cost of Living, en [Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data), que recopila información detallada sobre los precios de consumo en miles de ciudades de todo el mundo.

El dataset incluye:

- Precios relacionados con la vivienda: precio del alquiler y servicios básicos.
- Coste de servicios básicos como alimentación y cesta de la compra.
- Coste de vida relacionados con el ocio: coste en restauración.
- Coste de la vida en utilities como calefacción, electricidad, agua, servicio de basuras...
- Gastos en transporte público y movilidad.

Inicialmente puede ser un único reporsitorio de datos aunque valoramos ampliarlos con más fuentes y crear un repositorio más amplio que ayude a resolver las preguntas clave de negocio.

Entre ellos valoraremos los siguientes:

Inicialmente puede ser un único reporsitorio de datos aunque valoramos ampliarlos con más fuentes y crear un repositorio más amplio que ayude a resolver las preguntas clave de negocio. Entre ellos valoramos este de .

· [Movingto](https://www.movingto.com/digital-nomad-index) recopila informacion sobre Top Countries for Digital Nomads 2025, a los cuales solo detallan un ranking de 40 países.

El dataset incluye:

- Internet Speed.
- Costo de vida.
- Puntuación de seguridad.
- "Visa Ease" es básicamente una puntuación de qué tan fácil es para un nómada digital quedarse legalmente en el país.
- Calidad de vida.
- Impuestos.

· [Circleloop](https://www.circleloop.com/nomadindex/?utm_source). Este dataset da un “ranking” rápido con algunas variables interesantes también. 

El conjunto de datos incluye:

- Broadband Cost: coste del plan de internet fijo (suele ser precio mensual promedio; en la tabla aparece con moneda £/€ según el sitio).
- Monthly Rent: renta mensual típica (normalmente un promedio/estimación de alquiler)
- Remote Jobs Searches, (generalmente un indicador de interés/demanda)

### 🚀 Preguntas clave a responder

A través de este EDA, buscamos resolver interrogantes como:

1. **¿Cuáles son los "hubs" más económicos?** Comparativa entre ciudades consolidadas para nómadas frente a capitales tradicionales.

2. **El "Índice Capuccino":** Análisis del coste del café y comida fuera de casa como indicador de accesibilidad social.

3. **Poder adquisitivo:** ¿Cómo varía la capacidad de ahorro según la moneda local y el coste del alquiler?

4. **Segmentación por regiones:** Identificación de las zonas geográficas con mayor inflación de precios en servicios esenciales.

### 🌐 Estructura del repositorio: Breve explicación de la organización

El repositorio cuenta con los siguientes archivos en su nivel principal:

1. **README.md** - Descripción del proyecto en formato markdown
2. **main.ipynb** - Versión final y limpia de vuestro notebook con el EDA completo
3. **Memoria.pdf** - Documento técnico con el análisis completo
4. **Presentacion.pdf** - Diapositivas utilizadas en el vídeo
5. **Carpeta src/** - Contiene todos los archivos auxiliares del proyecto

La carpeta src/ contiene a su vez:

1. **src/data/** - Todos los archivos de datos utilizados en el análisis
2. **src/img/** - Imágenes necesarias o generadas para el proyecto
3. **src/notebooks/** - Notebooks de desarrollo y pruebas
4. **src/utils/** - Código auxiliar reutilizable

### 🛠️ Tecnologías utilizadas

- **Python 3.12+**
- **Pandas & NumPy:** Manipulación y limpieza de datos.
- **Matplotlib & Seaborn:** Visualización de patrones y tendencias.

---

### 🎲 Descripción de las variables del dataset

Variables dataset Cost of Livin (./src/data/cost-of-living.csv) / [Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data)

| Columna      | Descripción                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| city         | Nombre de la ciudad                                                                                                |
| country      | Nombre del país                                                                                                    |
| x1           | Comida en restaurante económico (USD)                                                                              |
| x2           | Comida para 2 personas en restaurante de gama media, tres platos (USD)                                             |
| x3           | Menú McMeal en McDonald’s (o menú equivalente) (USD)                                                               |
| x4           | Cerveza nacional (0,5 litros de barril, en restaurante) (USD)                                                      |
| x5           | Cerveza importada (botella de 0,33 litros, en restaurante) (USD)                                                   |
| x6           | Cappuccino (normal, en restaurante) (USD)                                                                          |
| x7           | Coca-Cola / Pepsi (botella de 0,33 litros, en restaurante) (USD)                                                   |
| x8           | Agua (botella de 0,33 litros, en restaurante) (USD)                                                                |
| x9           | Leche (normal), 1 litro (USD)                                                                                      |
| x10          | Barra de pan blanco fresco (500 g) (USD)                                                                           |
| x11          | Arroz blanco (1 kg) (USD)                                                                                          |
| x12          | Huevos (docena) (USD)                                                                                              |
| x13          | Queso local (1 kg) (USD)                                                                                           |
| x14          | Pechugas de pollo (1 kg) (USD)                                                                                     |
| x15          | Carne de ternera (1 kg) o carne roja equivalente (USD)                                                             |
| x16          | Manzanas (1 kg) (USD)                                                                                              |
| x17          | Plátanos (1 kg) (USD)                                                                                              |
| x18          | Naranjas (1 kg) (USD)                                                                                              |
| x19          | Tomates (1 kg) (USD)                                                                                               |
| x20          | Patatas (1 kg) (USD)                                                                                               |
| x21          | Cebollas (1 kg) (USD)                                                                                              |
| x22          | Lechuga (1 unidad) (USD)                                                                                           |
| x23          | Agua (botella de 1,5 litros, en supermercado) (USD)                                                                |
| x24          | Botella de vino de gama media (en supermercado) (USD)                                                              |
| x25          | Cerveza nacional (botella de 0,5 litros, en supermercado) (USD)                                                    |
| x26          | Cerveza importada (botella de 0,33 litros, en supermercado) (USD)                                                  |
| x27          | Paquete de 20 cigarrillos (Marlboro) (USD)                                                                         |
| x28          | Billete de transporte público (solo ida) (USD)                                                                     |
| x29          | Abono mensual de transporte (precio normal) (USD)                                                                  |
| x30          | Bajada de bandera del taxi (tarifa normal) (USD)                                                                   |
| x31          | Taxi por kilómetro (tarifa normal) (USD)                                                                           |
| x32          | Taxi, 1 hora de espera (tarifa normal) (USD)                                                                       |
| x33          | Gasolina (1 litro) (USD)                                                                                           |
| x34          | Volkswagen Golf 1.4 90 KW Trendline (o coche nuevo equivalente) (USD)                                              |
| x35          | Toyota Corolla Sedán 1.6l 97kW Comfort (o coche nuevo equivalente) (USD)                                           |
| x36          | Gastos básicos (electricidad, calefacción, refrigeración, agua, basura) para apartamento de 85 m² (USD)            |
| x37          | 1 minuto de tarifa móvil prepago local (sin descuentos ni planes) (USD)                                            |
| x38          | Internet (60 Mbps o más, datos ilimitados, cable/ADSL) (USD)                                                       |
| x39          | Gimnasio, cuota mensual para 1 adulto (USD)                                                                        |
| x40          | Alquiler de pista de tenis (1 hora en fin de semana) (USD)                                                         |
| x41          | Cine, estreno internacional, 1 entrada (USD)                                                                       |
| x42          | Guardería o preescolar privado, jornada completa, mensual por 1 niño (USD)                                         |
| x43          | Colegio internacional de primaria, coste anual por 1 niño (USD)                                                    |
| x44          | 1 par de vaqueros (Levis 501 o similar) (USD)                                                                      |
| x45          | Vestido de verano en tienda de cadena (Zara, H&M o similar) (USD)                                                  |
| x46          | 1 par de zapatillas Nike para correr (gama media) (USD)                                                            |
| x47          | 1 par de zapatos de piel de vestir para hombre (USD)                                                               |
| x48          | Apartamento (1 dormitorio) en el centro de la ciudad (USD)                                                         |
| x49          | Apartamento (1 dormitorio) fuera del centro (USD)                                                                  |
| x50          | Apartamento (3 dormitorios) en el centro de la ciudad (USD)                                                        |
| x51          | Apartamento (3 dormitorios) fuera del centro (USD)                                                                 |
| x52          | Precio por metro cuadrado para comprar apartamento en el centro (USD)                                              |
| x53          | Precio por metro cuadrado para comprar apartamento fuera del centro (USD)                                          |
| x54          | Salario mensual neto medio (después de impuestos) (USD)                                                            |
| x55          | Tipo de interés hipotecario anual (%), fijo a 20 años                                                              |
| data_quality | 0 si Numbeo considera que se necesitan más colaboradores para mejorar la calidad de los datos; 1 en caso contrario |

Muestra de variables y resultados del dataset (.src/data/digital-nomad-index-2024.csv) en [Movingto](https://www.movingto.com/digital-nomad-index). 

| Rank | Country | Overall Score | Internet Speed | Cost of Living | Safety | Visa Ease | Quality of Life | Taxes | Tax-free Period |
| ------------ | 
1 | Portugal | 92 | 90 | 85 | 95 | 95 | 95 | NHR | 20% | 10 years |
2 | Estonia | 91 | 95 | 75 | 90 | 98 | 92 | 0-20% | 183days/year |
3 | Georgia | 90 | 85 | 88 | 82 | 100 | 80 | 1% | 183days/year |
4 | Spain | 89 | 88 | 80 | 92 | 92 | 94 | 24% | 183 days/year |
5 | Thailand | 88 | 85 | 95 | 80 | 90 | 88 | 0-35% | 183 days/year |

### 🎯 Principales conclusiones: resumen de hallazgos clave