---
author: "@nurialiano"
license: "Creative Commons Attribution-NonCommercial 4.0 International"
---

# Modo Inspeccionar(F12)/Devtools en profundidad

> :warning: **ADVERTENCIA** los ejemplos de esta sección están basados en Chrome y Firefox pero está enfocado a los aspectos generales que incluyen la mayoría de los navegadores

En secciones anteriores hemos hablamos sobre el Modo Inspeccionar(F12) que implementan los navegadores (y al que probablemente hayas llegado de casualidad alguna vez), en esta sección vamos a darle forma y a investigar para que sirve cada herramienta y como podemos utilizalo en nuestra web.

## ¿Qué es el modo Inspeccionar(F12)/Devtools del navegador?

Lo primero que tenemos que aclarar es que el **Modo Inspeccionar tiene un nombre y es 'Devtools'**. Este nombre no es muy conocido fuera del entorno de la programación web ya que no está presente en nigún punto de la herramienta pero es ampliamente conocido dentro del mundo de la programación ya que es una herramienta muy utilzada. A partir de aquí nos referiremos al modo inspeccionar como Devtool para asentar este nombre y asociarlo a la herramienta.


Llegados hasta aqui vamos a sacar el elefante de la habitación y vamos a admitir que sí, todos hemos entrado en esa herramienta sin querer y hemos dicho '¿A que tecla dí?'

a. Definición y propósito
b. Ventajas y beneficios de utilizar el modo de inspección

## ¿Cómo abro las Devtools?

a. Métodos abreviados de teclado para abrir el modo de inspección
b. Acceso a través del menú del navegador

## Interfaz de las Devtools

a. Visión general de la interfaz
b. Paneles principales y sus funciones (Elementos, Estilos, Consola, Red, etc.)

## Inspeccionar elementos HTML

a. Seleccionar y resaltar elementos en la página
b. Navegar por la estructura del DOM
c. Modificar contenido y atributos de elementos en tiempo real

## Modificar CSS

a. Visualizar y editar reglas de estilo aplicadas a los elementos
b. Realizar cambios temporales para experimentar con el diseño
c. Crear nuevas reglas de estilo y aplicarlas a elementos específicos

## Ejecutar, depurar y analizar Javascript

a. Depurar errores y problemas en el código JavaScript
b. Establecer puntos de interrupción y realizar seguimiento de la ejecución del código
c. Explorar variables y objetos en el ámbito actual

## Analizar el rendimiento y la red

a. Evaluar el tiempo de carga de recursos (imágenes, scripts, etc.)
b. Identificar cuellos de botella y optimizar el rendimiento de la página
c. Simular diferentes condiciones de red para probar la respuesta del sitio

    Análisis del consumo de memoria: La pestaña de "Memory" muestra un desglose detallado del uso de memoria por parte de tu página web. Puedes ver información sobre el consumo de memoria en tiempo real, así como tomar capturas de memoria en momentos específicos.

    Registro de asignaciones y eliminaciones de memoria: La pestaña de "Memory" registra las asignaciones y eliminaciones de memoria a medida que ocurren. Esto te permite rastrear y entender qué partes de tu código están creando y liberando memoria.

    Análisis de instantáneas de memoria: Puedes capturar instantáneas de memoria en diferentes puntos de la ejecución de tu página web. Estas instantáneas proporcionan una visión detallada del estado de la memoria en ese momento, incluyendo información sobre objetos y estructuras de datos presentes en la memoria.

    Búsqueda y filtrado de datos: La pestaña de "Memory" te permite buscar y filtrar datos específicos para facilitar el análisis. Puedes buscar objetos por nombre, tipo o tamaño, lo que te ayuda a identificar posibles problemas de memoria, como fugas o excesos de consumo.

    Comparación de instantáneas de memoria: Puedes comparar dos instantáneas de memoria para identificar cambios en el consumo de memoria entre ellas. Esto puede ser útil para determinar si se están liberando correctamente los recursos después de ciertas acciones o eventos en tu página web.

## Administrar los datos almacenados

    Cookies: La pestaña de "Storage" muestra una lista de las cookies asociadas con la página web actual. Puedes ver detalles como el nombre de la cookie, su valor, el dominio asociado y la fecha de expiración. También puedes editar o eliminar cookies específicas.

    Almacenamiento local y de sesión: Esta pestaña te permite acceder a los datos almacenados localmente por la página web en el almacenamiento local (localStorage) y en el almacenamiento de sesión (sessionStorage). Puedes ver las claves y los valores asociados con estos almacenes, así como editar o eliminar los datos según sea necesario.

    Almacenamiento de bases de datos: Algunas aplicaciones web utilizan bases de datos en el lado del cliente para almacenar datos de forma estructurada. La pestaña de "Storage" te permite explorar y administrar estas bases de datos, ver sus tablas y registros, y realizar consultas.

    Almacenamiento de caché: Si la página web utiliza la API de almacenamiento en caché, la pestaña de "Storage" también muestra los datos almacenados en la caché del navegador. Puedes ver los recursos almacenados en caché y, si es necesario, eliminarlos para forzar la actualización de esos recursos.

    IndexDB: IndexDB es una API de almacenamiento de bases de datos basada en objetos que permite a las aplicaciones web almacenar grandes cantidades de datos en el navegador. La pestaña de "Storage" te permite acceder y administrar las bases de datos IndexDB utilizadas por la página web.

## Mejorar el rendimiento, la funcionalidad y la capacidad sin conexión de tu aplicación web.

## Evaluar y mejorar la accesibilidad

    Comprobaciones de accesibilidad automatizadas: La pestaña "Accessibility" te permite realizar comprobaciones automáticas de accesibilidad en tu página web. Estas comprobaciones verifican si tu página cumple con las pautas de accesibilidad, como las establecidas en el conjunto de normas WCAG (Web Content Accessibility Guidelines). Obtendrás informes detallados sobre los problemas de accesibilidad encontrados y sugerencias para corregirlos.

    Inspección de atributos y propiedades accesibles: La pestaña "Accessibility" muestra una lista de los elementos de tu página web y sus atributos y propiedades relacionados con la accesibilidad. Puedes examinar estos atributos y propiedades para asegurarte de que están correctamente configurados y proporcionan la información necesaria para los usuarios que dependen de la accesibilidad.

    Simulación de discapacidades: La pestaña "Accessibility" te permite simular diferentes discapacidades, como la ceguera, la baja visión, la discapacidad auditiva o la discapacidad motora. Al habilitar estas simulaciones, puedes experimentar cómo se percibe y se utiliza tu página web por parte de personas con diferentes discapacidades, lo que te ayuda a identificar posibles barreras de accesibilidad y realizar mejoras.

    Inspección de contraste y legibilidad: La pestaña "Accessibility" ofrece herramientas para evaluar el contraste de color entre los elementos de tu página web. Un contraste inadecuado puede dificultar la legibilidad y afectar a las personas con discapacidades visuales. Puedes verificar si los colores utilizados cumplen con los estándares de accesibilidad y hacer ajustes en caso necesario.

    Compatibilidad con lectores de pantalla: La pestaña "Accessibility" te permite evaluar cómo se lee tu página web con lectores de pantalla, que son herramientas utilizadas por personas con discapacidad visual para acceder al contenido de la web. Puedes reproducir la lectura del contenido y asegurarte de que la estructura, los elementos interactivos y la información se transmitan correctamente a través de un lector de pantalla.

## Emular vista en otros dispositivos

a. Emular dispositivos móviles y ajustar la vista de la página
b. Analizar el rendimiento y los problemas específicos de la versión móvil

## Recursos y herramientas adicionales

a. Extensiones y complementos útiles para el modo de inspección
b. Enlaces a documentación y tutoriales adicionales sobre el tema

## Consejos y buenas prácticas

a. Mejores prácticas para el uso eficiente del modo de inspección
b. Sugerencias para evitar problemas comunes y maximizar la productividad
