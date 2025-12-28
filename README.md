![Proyecto EDA: Nomadismo digital y coste de vida](./src/img/EDA-nomadismo-digital.jpg)

## 🌍 Nomadismo digital: análisis sobre el coste de vida

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

El objetivo es identificar ciudades y países que ofrecen el mejor equilibrio entre calidad de vida y asequibilidad para profesionales remotos. En un mundo donde la oficina es cualquier lugar con Wi-Fi, entender las métricas de gasto mensual (vivienda, alimentación, transporte y servicios) es crucial para la toma de decisiones estratégicas de movilidad.

### 📊 Sobre los datasets

Los datos utilizados con fuente primaria provienen del dataset Cost of Living, en [Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data), que recopila información detallada sobre los precios de consumo en miles de ciudades de todo el mundo.

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

· [Circleloop](https://www.circleloop.com/nomadindex/). Este dataset da un “ranking” rápido con algunas variables interesantes también.

El conjunto de datos incluye:

- Broadband Cost: coste del plan de internet fijo (suele ser precio mensual promedio; en la tabla aparece con moneda £/€ según el sitio).
- Monthly Rent: renta mensual típica (normalmente un promedio/estimación de alquiler)
- Remote Jobs Searches, (generalmente un indicador de interés/demanda)

### 🚀 Preguntas clave a responder

A través de este EDA, buscamos resolver interrogantes como:

1. **¿Cuáles son los "hubs" más económicos?** Comparativa entre ciudades consolidadas para nómadas frente a capitales tradicionales.

2. **El "Índice Capuccino":** Análisis del coste del café y comida fuera de casa como indicador de accesibilidad social.

3. **Poder adquisitivo:** ¿Cómo varía la capacidad de ahorro según la moneda local y el coste de vida?

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

### 🎲 Descripción de las variables de los datasets

Variables dataset Cost of Living (./src/data/cost-of-living.csv) / [Kaggle](https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data)

El conjunto de datos original Cost of Living utiliza códigos de variables genéricos (x1–x55). Para mejorar la legibilidad, se utiliza un archivo CSV independiente (cost-of-living-vars-map.csv) para mapear las variables originales con nombres descriptivos y tipo de coste. Este mapa de variables se carga y aplica dentro de los cuadernos de análisis (por el momento, ETL_cost_living_juanfcia_draft), lo que garantiza una trazabilidad con los datos originales y además facilita el análisis posterior.

| Columna      | Nombre de variable                  | Descripción de variable                                                                                            | Tipo de coste                      |
| ------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| city         | city_name                           | Nombre de la ciudad                                                                                                |                                    |
| country      | country_name                        | Nombre del país                                                                                                    |                                    |
| x1           | meal_inexpensive_restaurant         | Comida en restaurante económico (USD)                                                                              | Restaurantes y bebidas             |
| x2           | meal_midrange_restaurant_2p         | Comida para 2 personas en restaurante de gama media, tres platos (USD)                                             | Restaurantes y bebidas             |
| x3           | mcmeal_fastfood	                 | Menú McMeal en McDonald’s (o menú equivalente) (USD)                                                               | Restaurantes y bebidas             |
| x4           | beer_domestic_restaurant_0_5l       | Cerveza nacional (0,5 litros de barril, en restaurante) (USD)                                                      | Restaurantes y bebidas             |
| x5           | beer_imported_restaurant_0_33l      | Cerveza importada (botella de 0,33 litros, en restaurante) (USD)                                                   | Restaurantes y bebidas             |
| x6           | cappuccino_restaurant	             | Cappuccino (normal, en restaurante) (USD)                                                                          | Restaurantes y bebidas             |
| x7           | soda_restaurant_0_33l	             | Coca-Cola / Pepsi (botella de 0,33 litros, en restaurante) (USD)                                                   | Restaurantes y bebidas             |
| x8           | water_restaurant_0_33l              | Agua (botella de 0,33 litros, en restaurante) (USD)                                                                | Restaurantes y bebidas             |
| x9           | milk_1l	                         | Leche (normal), 1 litro (USD)                                                                                      | Supermercado – alimentación básica |
| x10          | bread_white_500g	                 | Barra de pan blanco fresco (500 g) (USD)                                                                           | Supermercado – alimentación básica |
| x11          | rice_white_1kg	                     | Arroz blanco (1 kg) (USD)                                                                                          | Supermercado – alimentación básica |
| x12          | eggs_12                             | Huevos (docena) (USD)                                                                                              | Supermercado – alimentación básica |
| x13          | cheese_local_1kg                    | Queso local (1 kg) (USD)                                                                                           | Supermercado – alimentación básica |
| x14          | chicken_fillet_1kg	                 | Pechugas de pollo (1 kg) (USD)                                                                                     | Supermercado – alimentación básica |
| x15          | beef_1kg                            | Carne de ternera (1 kg) o carne roja equivalente (USD)                                                             | Supermercado – alimentación básica |
| x16          | apples_1kg	                         | Manzanas (1 kg) (USD)                                                                                              | Supermercado – alimentación básica |
| x17          | bananas_1kg                         | Plátanos (1 kg) (USD)                                                                                              | Supermercado – alimentación básica |
| x18          | oranges_1kg                         | Naranjas (1 kg) (USD)                                                                                              | Supermercado – alimentación básica |
| x19          | tomatoes_1kg                        | Tomates (1 kg) (USD)                                                                                               | Supermercado – alimentación básica |
| x20          | potatoes_1kg                        | Patatas (1 kg) (USD)                                                                                               | Supermercado – alimentación básica |
| x21          | onions_1kg                 	     | Cebollas (1 kg) (USD)                                                                                              | Supermercado – alimentación básica |
| x22          | lettuce_1unit                       | Lechuga (1 unidad) (USD)                                                                                           | Supermercado – alimentación básica |
| x23          | water_1_5l_supermarket              | Agua (botella de 1,5 litros, en supermercado) (USD)                                                                | Supermercado – bebidas y otros     |
| x24          | wine_midrange_supermarket           | Botella de vino de gama media (en supermercado) (USD)                                                              | Supermercado – bebidas y otros     |
| x25          | beer_domestic_supermarket_0_5l      | Cerveza nacional (botella de 0,5 litros, en supermercado) (USD)                                                    | Supermercado – bebidas y otros     |
| x26          | beer_imported_supermarket_0_33l     | Cerveza importada (botella de 0,33 litros, en supermercado) (USD)                                                  | Supermercado – bebidas y otros     |
| x27          | cigarettes_pack_marlboro            | Paquete de 20 cigarrillos (Marlboro) (USD)                                                                         | Supermercado – bebidas y otros     |
| x28          | public_transport_ticket_one_way     | Billete de transporte público (solo ida) (USD)                                                                     | Transporte                         |
| x29          | public_transport_monthly_pass       | Abono mensual de transporte (precio normal) (USD)                                                                  | Transporte                         |
| x30          | taxi_start_fare                     | Bajada de bandera del taxi (tarifa normal) (USD)                                                                   | Transporte                         |
| x31          | taxi_per_km                         | Taxi por kilómetro (tarifa normal) (USD)                                                                           | Transporte                         |
| x32          | taxi_waiting_1h                     | Taxi, 1 hora de espera (tarifa normal) (USD)                                                                       | Transporte                         |
| x33          | gasoline_1l                         | Gasolina (1 litro) (USD)                                                                                           | Transporte                         |
| x34          | car_vw_golf_new                     | Volkswagen Golf 1.4 90 KW Trendline (o coche nuevo equivalente) (USD)                                              | Vehículos (compra)                 |
| x35          | car_toyota_corolla_new              | Toyota Corolla Sedán 1.6l 97kW Comfort (o coche nuevo equivalente) (USD)                                           | Vehículos (compra)                 |
| x36          | utilities_85sqm                     | Gastos básicos (electricidad, calefacción, refrigeración, agua, basura) para apartamento de 85 m² (USD)            | Vivienda y suministros             |
| x37          | mobile_prepaid_1min                 | 1 minuto de tarifa móvil prepago local (sin descuentos ni planes) (USD)                                            | Vivienda y suministros             |
| x38          | internet_60mbps_unlimited           | Internet (60 Mbps o más, datos ilimitados, cable/ADSL) (USD)                                                       | Vivienda y suministros             |
| x39          | gym_monthly_membership	             | Gimnasio, cuota mensual para 1 adulto (USD)                                                                        | Ocio y estilo de vida              |
| x40          | tennis_court_1h_weekend             | Alquiler de pista de tenis (1 hora en fin de semana) (USD)                                                         | Ocio y estilo de vida              |
| x41          | cinema_ticket                       | Cine, estreno internacional, 1 entrada (USD)                                                                       | Ocio y estilo de vida              |
| x42          | private_preschool_monthly           | Guardería o preescolar privado, jornada completa, mensual por 1 niño (USD)                                         | Educación y cuidado infantil       |
| x43          | international_primary_school_yearly | Colegio internacional de primaria, coste anual por 1 niño (USD)                                                    | Educación y cuidado infanti        |
| x44          | jeans_levis_501                     | 1 par de vaqueros (Levis 501 o similar) (USD)                                                                      | Ropa y calzado                     |
| x45          | summer_dress_chain_store            | Vestido de verano en tienda de cadena (Zara, H&M o similar) (USD)                                                  | Ropa y calzado                     |
| x46          | nike_running_shoes                  | 1 par de zapatillas Nike para correr (gama media) (USD)                                                            | Ropa y calzado                     |   
| x47          | leather_business_shoes              | 1 par de zapatos de piel de vestir para hombre (USD)                                                               | Ropa y calzado                     |  
| x48          | rent_1br_city_center                | Apartamento (1 dormitorio) en el centro de la ciudad (USD)                                                         | Vivienda – alquiler y compra       |
| x49          | rent_1br_outside_center             | Apartamento (1 dormitorio) fuera del centro (USD)                                                                  | Vivienda – alquiler y compra       |
| x50          | rent_3br_city_center                | Apartamento (3 dormitorios) en el centro de la ciudad (USD)                                                        | Vivienda – alquiler y compra       |
| x51          | rent_3br_outside_center             | Apartamento (3 dormitorios) fuera del centro (USD)                                                                 | Vivienda – alquiler y compra       |
| x52          | price_sqm_city_center               | Precio por metro cuadrado para comprar apartamento en el centro (USD)                                              | Vivienda – alquiler y compra       |
| x53          | price_sqm_outside_center            | Precio por metro cuadrado para comprar apartamento fuera del centro (USD)                                          | Vivienda – alquiler y compra       |
| x54          | avg_net_salary                      | Salario mensual neto medio (después de impuestos) (USD)                                                            | Economía y financiación            |
| x55          | mortgage_interest_rate_20y          | Tipo de interés hipotecario anual (%), fijo a 20 años                                                              | Economía y financiación            |
| data_quality | data_quality_flag                   | 0 si Numbeo considera que se necesitan más colaboradores para mejorar la calidad de los datos; 1 en caso contrario | Calidad de los datos               |

Muestra de variables y resultados del dataset (.src/data/digital-nomad-index-2024.csv) en [Movingto](https://www.movingto.com/digital-nomad-index). 

| Rank           | Country        | Overall  | Internet Speed | Cost of Living | Safety   | Visa Ease  | Quality of Life | Taxes    | Tax-free Period |    
| -------------- | -------------- | -------- | -------------- | -------------  | -------- | ---------- | --------------- | -------- | --------------- |
| 1              | Portugal       | 92       | 90             | 85             | 95       | 95         | 95              | NHR 20%  | 10 years        |
| 2              | Estonia        | 91       | 95             | 75             | 90       | 98         | 92              | 0-20%    | 183 days/year   |
| 3              | Georgia        | 90       | 85             | 88             | 82       | 100        | 80              | 1%       | 183 days/year   |
| 4              | Spain          | 89       | 88             | 80             | 92       | 92         | 94              | 24%      | 183 days/year   |
| 5              | Thailand       | 88       | 85             | 95             | 80       | 90         | 88              | 0-35%    | 183 days/year   |
| 6              | México         | 87       | 82             | 90             | 75       | 94         | 86              | 1.92-35% | 183 days/year   |
| 7              | Czech Republic | 86       | 87             | 78             | 88       | 85         | 90              | 15%      | 183 days/year   |
| 8              | Malaysia       | 85       | 80             | 92             | 85       | 90         | 85              | 0-30%    | 182 days/year   |
| 9              | Croatia        | 84       | 76             | 88             | 88       | 89         |                 | 24%      | 1 year          |  
| 10             | Costa Rica     | 83       | 79             | 85             | 80       | 90         | 88              | 0-25%    | 183 days/year   |


Muestra de variables y resultados del dataset (.src/data/digital-nomad-index-2024.csv) en [Circleloop](https://www.circleloop.com/nomadindex/). 

| #              | Country        | Broadband Speed | Mobile Speed | Broadband Cost | Monthly Rent | Working Holidays Visa | Happiness Index | Migrant Population % | Remote Jobs Searches | Digital Nomad |   
| -------------- | -------------- | --------------- | ------------ | -------------- | ------------ | --------------------- | --------------- | -------------------- | -------------------- | ------------- |
| 1              | Canada         | 149.35          | 84.54        | £28.24         | £827         | True                  | 7.23            | 21.3                 | 83900                | 74.35         |
| 2              | UK             | 76.49           | 41.72        | £28.93         | £808         | True                  | 7.17            | 14.1                 | 68400                | 63.43         |
| 3              | Romania        | 188.55          | 41.48        | £6.6           | £283         | True                  | 6.12            | 2.4                  | 10980                | 62.28         |
| 4              | Sweden         | 158.73          | 56.64        | £32.08         | £771         | True                  | 7.35            | 20                   | 3490                 | 61.54         |
| 5              | Denmark        | 179.81          | 66.68        | £39.07         | £923         | True                  | 7.65            | 12.5                 | 1080                 | 61.49         |
| 6              | France         | 177.93          | 50.45        | £22.53         | £660         | True                  | 6.66            | 12.8                 | 5360                 | 60.80         |
| 7              | Netherlands    | 125.82          | 88.13        | £34.37         | £1056        | True                  | 7.45            | 13.4                 | 3440                 | 60.27         |
| 8              | Australia      | 58.52           | 88.35        | £39.16         | £997         | True                  | 7.22            | 30                   | 17600                | 60.16         |
| 9              | Switzerland    | 186.40          | 73.85        | £58.40         | £1345        | True                  | 7.56            | 29.9                 | 3840                 | 60.15         |
| 10             | Germani        | 120.13          | 49.67        | £23.28         | £718         | True                  | 7.08            | 15.7                 | 12720                | 60            |

### 🎯 Principales conclusiones: resumen de hallazgos clave
