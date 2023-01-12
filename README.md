![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

<p align="center">
<img src="https://cdn-3.expansion.mx/17/86/462e2f2d430496524df469ca5350/oficinas-olist.jpeg"   
>
</p>

<h1 align="center">Proyecto Final</h1>
<h1 align="center">Sistema de Análisis de Sentimientos y Reviews</h1>
<h3 align="center"><a href="https://github.com/belensendot">Maria Belén Sendot</a><br>Data Analytics</h3>
<h3 align="center"><a href="https://github.com/damul90">Daniel Muñoz López</a><br>Data Scientist</h3>
<h3 align="center"><a href="https://github.com/">Natalia Soledad Trulla</a><br>Data Analytics</h3>
<h3 align="center"><a href="https://github.com/Lautaro-Cenni">Lautaro Alejandro Cenni</a><br>Data Scientist</h3>
<h3 align="center"><a href="https://github.com/Alvaro9721">Álvaro Enrique Beleño Contreras</a><br>Data Engineer</h3>

<hr>

## Introducción

Olist es una compañía que trabaja en el ámbito del e-commerce, cuyo objetivo principal es multiplicar las ventas de lo susuarios por medio de un modelo que permite crear sólidas conexiones entre los *PYMES* y los clientes.

## Objetivo General

Encontrar soluciones innovadoras que permitan a las PYMES vender sus productos a un mayor número de clientes, manteniendo su conexión con los mercados más grandes, y optimizando la experiencia del usuario desde la búsqueda del productoa partir de la plataforma, hasta la entrega de este.

## Objetivos específicos del análisis sobre E-Commerce (Olist)

- **Evaluar** la evolución de la venta de productos por trimestre y por estado entre los años 2016 y 2018, investigando si efectivamente se produjo un crecimiento o disminución en la venta según producto y las regiones.

- **Determinar** cuáles son las localidades mejor ubicadas geográficamente según los tipos de productos y el consumo, para gestionar de forma eficiente el flujo de mercadería desde los centros físicos de almacenamiento, ya sea incorporando nuevas sedes o sumando nuevos productos a los existentes. También determinar cuáles son los estados con poco servicio para posibilitar su llegada a sectores de la sociedad que aún no han tenido esa posibilidad.

- **Evaluar** la experiencia de nuestros clientes a través del índice de recomendación de marca. Esto nos va a permitir entender cuáles son las buenas prácticas que contribuyen a la fidelización de los clientes promotores y analizar la voz del cliente detractor para accionar en consecuencia. Para esto realizamos un análisis de sentimiento.

- **Crear** un modelo de Machine Learning que realice las predicciones en base a los productos más vendidos mes a mes, para cubrir las necesidades de los usuarios acorde a la demanda, estimar la cantidad óptima de reabastecimiento, e identificar aquellos que requieren stock permanente.

- **Identificar** patrones de conversión según la herramienta de marketing para mejorar estrategias de conversion de ventas.

## Alcance
El presente proyecto tiene como enfoque el mercado e-commerce brasileño, el cual está basado en datos históricos de los perfiles de las PyMEs y consumidores finales en los años 2016 - 2018. Su realización está argumentada bajo el principio de crecimiento de una empresa, donde los KPI están directamente relacionados a los objetivos trazados, esto con la finalidad de crear un sistema que sea versátil a los requerimientos del mercado y alcanzar un mejor posicionamiento para cada cliente (PyME). Para lograr este objetivo se dispone a crear un modelo de machine learning que sea capaz de sugerir compras y por tanto aumentar las ventas de un determinado cliente.

## KPIs

<table>
    <tr>
        <th> Objetivo</th>
        <th> KPI</th>
        <th>Métrica</th>
    </tr>
    <tr>
        <th>Evaluar la evolución de la venta de productos por trimestre y por estado entre los años 2016 y 2018, investigando si efectivamente se produjo un crecimiento o disminución en la venta según producto y las regiones.</th>
        <th>Variación porcentual de la venta de productos por trimestre y por estado entre los años 2016 y 2018.</th>
        <th>(Ventas_actual - Ventas_trimestre_pasado) / (Ventas_trimestre_pasado) * 100</th>
    </tr>
    <tr>
        <th>Descubrir cuáles son las buenas prácticas que contribuyen a la fidelización de los clientes promotores y analizar la voz del cliente detractor para accionar en consecuencia. </th>
        <th>Grado de fidelización de los clientes: Variación porcentual entre clientes promotores y detractores por mes y estado entre los años 2016 y 2018.</th>
        <th>(% clientes-promotores) / (% clientes-detractores)</th>
    </tr>
        <tr>
        <th>Identificar patrones de conversión según la herramienta de marketing para mejorar las estrategias de venta, ver lo que no fue bueno, mejorar campañas próximas, valorar los éxitos, minimizar los errores cometidos y discutir con el equipo de marketing las conclusiones obtenidas.</th>
        <th>Aumentar el porcentaje de la tasa de conversión en un 10% mensual de herramienta de marketing utilizada según ventas realizadas.</th>
        <th>Closed_deals/total_deals</th>
    </tr>
        <tr>
        <th>Identificar la región con mayor variación de ventas en los periodos 2016-2018, con la finalidad de aprovechar el potencial de cada ciudad.</th>
        <th>Variación del  pronóstico de ventas para poder interpretar  el comportamiento de la industria y poder estimar cómo funcionará el negocio en los próximos meses.</th>
        <th>(Volumen total de ventas/ objetivo de ingresos alcanzados en el periodo) * 100</th>
    </tr>
        <tr>
        <th>Identificar el porcentaje de cancelaciones y los motivos para actuar en consecuencia.</th>
        <th>Disminuir el porcentaje de cancelación en un 25% por mes</th>
        <th>(Total de cancelaciones/total de ventas) * 100</th>
    </tr>
</table>

## Cronograma

[Link](https://trello.com/b/yUevKdVg/cronograma)
