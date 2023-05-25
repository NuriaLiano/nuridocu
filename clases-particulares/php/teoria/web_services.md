# Web services. SOAP y WSDL

## SOAP

Protocolo que permite desarrollar software en cualquier lenguaje y este ser interpretado por cualquier otro sistema o aplicación a través de una red mediante XML. SOAP establece reglas para enviar y recibir Remote Procedure Calls (RPC), como las de los mensajes HTTP request y HTTP response, por lo que no está ligado a ningún sistema operativo o lenguaje de programación.

Los servicios web SOAP se describen utilizando WSDL (Web Services Description Language), que es un lenguaje basado en XML para describir la interfaz de un servicio web.

### Estructura mensaje SOAP

#### PETICIÓN

##### Sintaxis

~~~xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header>
        <!-- Cabecera (opcional) -->
    </soap:Header>
    <soap:Body>
        <!-- Cuerpo de la petición -->
    </soap:Body>
</soap:Envelope>

~~~

##### Ejemplo

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"
    soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

    <soap:Body xmlns:m="http://www.example.org/stock">
        <m:GetStockPrice>
            <m:StockName>IBM</m:StockName>
        </m:GetStockPrice>
    </soap:Body>
</soap:Envelope>
~~~

- **``<?xml version="1.0" encoding="UTF-8"?>``**: Esta declaración indica la versión XML utilizada (1.0) y la codificación de caracteres (UTF-8) del documento.
- **``<soap:Envelope>``**: Es el elemento raíz de la estructura SOAP. Define el sobre que contiene toda la información de la solicitud o respuesta SOAP.
  - **``xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"``**: El atributo xmlns:soap establece el espacio de nombres asociado con el prefijo "soap" y define la ubicación de la especificación SOAP utilizada.
  - **``soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding"``**: Este atributo opcional especifica el estilo de codificación utilizado en la respuesta SOAP. En este caso, se utiliza el estilo de codificación "http://www.w3.org/2003/05/soap-encoding".
- **``<soap:Body>``**: Contiene el cuerpo de la solicitud o respuesta SOAP. Es el contenedor principal para los datos específicos de la operación SOAP.
  - **``xmlns:m="http://www.example.org/stock"``**: El atributo xmlns:m establece un espacio de nombres personalizado asociado con el prefijo "m". En este caso, se utiliza el espacio de nombres "http://www.example.org/stock".
- **``<m:GetStockPrice>``**: Representa la operación específica que se está solicitando en el servicio web. En este ejemplo, se solicita el precio de una acción.
- **``<m:StockName>IBM</m:StockName>``**: Es el elemento que contiene el nombre de la acción para la cual se solicita el precio. En este caso, se utiliza "IBM" como ejemplo.

##### Ejemplo con SOAP:FAULT

Se utiliza en el cuerpo de la respuesta SOAP para transmitir información sobre un error específico que ha ocurrido. Es opcional y se incluye cuando se necesita informar sobre un fallo en la respuesta SOAP.

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"
    soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

    <soap:Body xmlns:m="http://www.example.org/stock">
        <m:GetStockPrice>
            <m:StockName>IBM</m:StockName>
        </m:GetStockPrice>
    </soap:Body>

    <soap:Fault>
        <soap:Code>
            <soap:Value>soap:Receiver</soap:Value>
        </soap:Code>
        <soap:Reason>
            <soap:Text xml:lang="en">Invalid StockName</soap:Text>
        </soap:Reason>
        <soap:Detail>
            <m:ErrorDetails>Error occurred while retrieving stock price</m:ErrorDetails>
        </soap:Detail>
    </soap:Fault>

</soap:Envelope>
~~~

- **``<soap:Fault>``**: Representa un mensaje de error en una respuesta SOAP. Contiene información detallada sobre el error.
  - **``<soap:Code>``**: Define el código de error asociado al mensaje. En este caso, se utiliza <soap:Value> para establecer el valor del código como "soap:Receiver".
  - **``<soap:Reason>``**: Proporciona una explicación textual del motivo del error. <soap:Text> se utiliza para especificar el texto del motivo en el idioma indicado (xml:lang). En este ejemplo, el texto del motivo es "Invalid StockName".
  - **``<soap:Detail>``**: Proporciona detalles adicionales sobre el error. Aquí se puede agregar información específica del servicio web o del contexto del error. En este caso, se utiliza <m:ErrorDetails> para indicar que se produjo un error al recuperar el precio de la acción.

#### RESPUESTA

##### Sintaxis

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"
    soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

    <soap:Header>
        <!-- Aquí se pueden incluir elementos adicionales en el encabezado -->
    </soap:Header>

    <soap:Body>
        <!-- Aquí se incluye el contenido de la respuesta -->
    </soap:Body>

</soap:Envelope>
~~~

##### Ejemplo

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"
    soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

    <soap:Body xmlns:m="http://www.example.org/stock">
        <m:GetStockPriceResponse>
            <m:Price>34.5</m:Price>
        </m:GetStockPriceResponse>
    </soap:Body>

</soap:Envelope>

~~~

- **``<?xml version="1.0" encoding="UTF-8"?>``**: Esta declaración indica la versión XML utilizada (1.0) y la codificación de caracteres (UTF-8) del documento.
- **``<soap:Envelope>``**: Es el elemento raíz de la estructura SOAP. Define el sobre que contiene toda la información de la solicitud o respuesta SOAP.
  - **``xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"``**: El atributo xmlns:soap establece el espacio de nombres asociado con el prefijo "soap" y define la ubicación de la especificación SOAP utilizada.
  - **``soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding"``**: Este atributo opcional especifica el estilo de codificación utilizado en la respuesta SOAP. En este caso, se utiliza el estilo de codificación "http://www.w3.org/2003/05/soap-encoding".
- **``<soap:Body>``**: Contiene el cuerpo de la solicitud o respuesta SOAP. Es el contenedor principal para los datos específicos de la operación SOAP.
  - **``xmlns:m="http://www.example.org/stock"``**: El atributo xmlns:m establece un espacio de nombres personalizado asociado con el prefijo "m". En este caso, se utiliza el espacio de nombres "http://www.example.org/stock".
- **``<m:GetStockPriceResponse>``**: Representa la respuesta a la solicitud GetStockPrice.
  - **``<m:Price>34.5</m:Price>``**: que contiene el valor del precio del stock, en este caso, 34.5.

#### Elementos necesarios

- **Envelope (Envoltorio)** : Es el elemento raíz del mensaje SOAP. Contiene todos los demás elementos y define el espacio de nombres SOAP utilizado en el mensaje.
- **Header (Cabecera)** : Es un elemento opcional que contiene información adicional relacionada con la transacción SOAP. Puede incluir información de autenticación, seguridad u otros datos relevantes.
- **Body (Cuerpo)** : Es el elemento principal que contiene el mensaje RPC. Aquí se incluyen los detalles específicos de la operación que se está realizando.
- **Fault (Error)** : Es un elemento opcional que se utiliza para representar errores o excepciones en caso de que ocurra algún problema durante la ejecución de la operación. En caso de que sea hijo de body representa un error específico relacionado con la operación dentro del body.

### Bibliotecas y extensiones SOAP

son herramientas que simplifican y agilizan el desarrollo de aplicaciones web basadas en SOAP, proporcionando funciones y clases predefinidas para trabajar con los aspectos específicos de este protocolo de comunicación. Facilitan la creación de clientes y servidores SOAP, la manipulación de mensajes y la interacción con servicios web SOAP.

- Abstracción del protocolo: Proporcionan una capa de abstracción sobre los detalles técnicos del protocolo SOAP, permitiendo a los desarrolladores trabajar con objetos y métodos que representan los elementos SOAP subyacentes, como el encabezado, el cuerpo y los elementos de datos.
- Generación de clientes y servidores: Permiten generar automáticamente el código necesario para crear clientes y servidores SOAP.
- Manipulación de mensajes SOAP: Proporcionan funciones y métodos para manipular y modificar mensajes SOAP,
- Soporte para WSDL: Permite generar automáticamente el código cliente o servidor a partir de un archivo WSDL, lo que simplifica el proceso de desarrollo y garantiza la coherencia entre el cliente y el servidor SOAP.

Algunas bibliotecas o extensiones:

- **PHP SOAP**: Es una extensión incorporada en PHP que permite la comunicación y el consumo de servicios web SOAP. Proporciona funciones para crear clientes y servidores SOAP, enviar y recibir mensajes SOAP, y manejar la serialización y deserialización de datos SOAP.
- **NUSOAP**: Es una biblioteca PHP que ofrece una implementación completa de SOAP tanto para crear clientes como para desarrollar servicios web SOAP. Es fácil de usar y proporciona una interfaz orientada a objetos para trabajar con los elementos SOAP.
- **PEAR::SOAP**: Es una biblioteca basada en PEAR (PHP Extension and Application Repository) que permite crear y consumir servicios web SOAP. Proporciona una interfaz simple para trabajar con SOAP y facilita la creación de clientes y servidores SOAP.

### PHP SOAP

En PHP SOAP, para crear un servicio web, hay que utilizar la clase SoapServer.

~~~php
 class SoapServer {
/* Métodos */
public addFunction(mixed $functions): void
public addSoapHeader(SoapHeader $object): void
public __construct(mixed $wsdl, array $options = ?)
public fault(
    string $code,
    string $string,
    string $actor = ?,
    string $details = ?,
    string $name = ?
): void
public getFunctions(): array
public handle(string $soap_request = ?): void
public setClass(string $class_name, mixed $... = ?): void
public setObject(object $object): void
public setPersistence(int $mode): void
}
~~~

- SoapServer::addFunction — Añade una o más funciones al controlador de peticiones SOAP
- SoapServer::addSoapHeader — Añade un encabezado SOAP a la respuesta
- SoapServer::__construct — Constructor de SoapServer
- SoapServer::fault — SoapServer indica que ocurrió un fallo
- SoapServer::getFunctions — Devuelve una lista de las funciones definidas
- SoapServer::handle — Controla la petición SOAP
- SoapServer::setClass — Define la clase que controla las peticiones SOAP
- SoapServer::setObject — Define el objecto que será usado para controlar las peticiones SOAP
- SoapServer::setPersistence — Establece el modo de persistencia de SoapServer

Al igual que sucedía con SoapClient al programar un cliente, cuando se utiliza SoapServer se puede crear un
servicio sin documento WSDL asociado (como en el caso anterior), o indicar el documento WSDL
correspondiente al servicio.

#### PHPDOCUMENTOR

[Documentación oficial](https://docs.phpdoc.org/3.0/)

Es una herramienta de código libre que se utiliza para la generación automática de documentación en PHP. Se asemeja a Javadoc, que se utiliza en el lenguaje de programación Java. PHPDocumentor analiza los comentarios agregados al código fuente de una clase y genera documentación en varios formatos, como HTML, PDF y XML.

Para que PHPDocumentor funcione correctamente, es necesario seguir un formato específico en los comentarios de las clases. Los comentarios deben estar distribuidos en bloques y utilizar marcas específicas, como "@param" para indicar un parámetro y "@return" para indicar el valor devuelto por una función.

>:pencil: **NOTA** existe una extensión para VSCode que ayuda a generar los comentarios de manera más eficiente. [PHPDoc](https://marketplace.visualstudio.com/items?itemName=ronvanderheijden.phpdoc-generator)

~~~php
/**
 * Suma dos números enteros.
 *
 * @param int $a El primer número.
 * @param int $b El segundo número.
 * @return int La suma de los dos números.
 */
function sumar($a, $b) {
    return $a + $b;
}
~~~

En este ejemplo, el comentario PHPDoc describe brevemente la función y utiliza las marcas "@param" para indicar los parámetros de entrada y "@return" para indicar el valor devuelto por la función.

## WSDL

Un archivo WSDL define los métodos que se pueden invocar en el servicio web, los parámetros de entrada y salida de cada método, y los protocolos de transporte utilizados.

### Estructura WSDL

![Section 1.png](./estructura_wsdl.png)

- **Definición** : Es el elemento principal de todos los documentos WSDL. Define el nombre del servicio web, declara múltiples espacios de nombres utilizados en el resto del documento y contiene todos los elementos de servicio descritos aquí.
  - **xmlns** : Define el espacio de nombres que se utilizará para todos los elementos sin un prefijo de espacio de nombres explícito.
  >:black_joker: **Por ejemplo** el atributo "xmlns" establece el espacio de nombres predeterminado "http://schemas.xmlsoap.org/wsdl/" para todos los elementos dentro del elemento "definitions".
  - **xmlns:soap** :  Se utiliza para declarar un espacio de nombres con un prefijo específico, en este caso "soap". Permite asociar ese prefijo a un espacio de nombres específico dentro del documento WSDL.
  >:black_joker: **Por ejemplo** el atributo "xmlns:soap" asocia el prefijo "soap" con el espacio de nombres "http://schemas.xmlsoap.org/wsdl/soap/". Esto permite usar el prefijo "soap" para referirse a elementos y atributos dentro de ese espacio de nombres.
  - **targetNamespace** : Se utiliza para definir el espacio de nombres objetivo del documento WSDL. Establece el espacio de nombres al que pertenecen los elementos y tipos definidos en el archivo WSDL.
  >:black_joker: **Por ejemplo** el atributo "targetNamespace" establece el espacio de nombres objetivo como "http://example.com/namespace". Esto significa que los elementos y tipos definidos dentro del documento WSDL pertenecen a ese espacio de nombres.
- **Tipos de datos** : Los tipos de datos que se utilizarán en los mensajes se definen en forma de esquemas XML
- **Mensaje** : Es una definición abstracta de los datos, presentados como un mensaje completo o como argumentos que se asignarán a una invocación de método.
- **Operación** : Es la definición abstracta de la operación para un mensaje, como nombrar un método, una cola de mensajes o un proceso empresarial, que aceptará y procesará el mensaje.
- **Tipo de puerto** : Es un conjunto abstracto de operaciones asignadas a uno o más puntos finales, que define la colección de operaciones para una unión; la colección de operaciones, al ser abstracta, se puede asignar a múltiples transportes a través de varias uniones.
- **Unión** : Es un conjunto abstracto de operaciones asignadas a uno o más puntos finales, que define la colección de operaciones para una unión; la colección de operaciones, al ser abstracta, se puede asignar a múltiples transportes a través de varias uniones.
- **Puerto** : Es una combinación de una unión y una dirección de red, que proporciona la dirección de destino de la comunicación del servicio.
- **Servicio** : Es una colección de puntos finales relacionados que abarcan las definiciones del servicio en el archivo; los servicios asignan la unión al puerto e incluyen cualquier definición de extensibilidad.

### WSDL tipos de datos

#### Etiqueta types

#### Clases

(all y sequence)

#### Arrays

#### Message

(request, response)

#### Estilos de enlazado

(document o RPC) La selección que hagamos influirá en cómo se transmitan los mensajes dentro de las peticiones y
respuestas SOAP.
Además, cada estilo de enlazado puede ser de tipo encoded o literal (aunque en realidad la combinación
document/encoded no se utiliza). Al indicar encoded, estamos diciendo que vamos a usar un conjunto de
reglas de codificación, como las que se incluyen en el propio protocolo SOAP [espacio de nombres]
(http://schemas.xmlsoap.org/soap/encoding/), para convertir en XML los parámetros de las peticiones y
respuestas.
Nosotros trabajaremos únicamente con estilo de enlazado RPC/encoded

#### PortType

Las funciones que creas en un servicio web, se conocen con el nombre de operaciones en un documento
WSDL.
En lugar de definirlas una a una, es necesario agruparlas en lo que en WSDL se llama portType. Un portType
contiene una lista de funciones, indicando para cada función (operation) la lista de parámetros de entrada y
de salida que le corresponden.

~~~xml
<portType name="usuarioPortType">
<operation name="getUsuario">
<input message="tns:getUsuarioRequest"/>
<output message="tns:getUsuarioResponse"/>
</operation>
</portType>
~~~

Normalmente a no ser que estemos generando un servicio web bastante complejo, el documento WSDL
contendrá un único portType

Cada portType debe contener un atributo name con el nombre (único para todos los elementos portType).
Cada elemento operation también debe contener un atributo name, que se corresponderá con el nombre de
la función que se ofrece. Además, en función del tipo de operación de que se trate, contendrá:
Un elemento input para indicar funciones que no devuelven valor (su objetivo es sólo enviar un
mensaje al servidor).
Un elemento input y otro output, en este orden, para el caso más habitual: funciones que reciben algún
parámetro, se ejecutan, y devuelven un resultado.
Es posible (aunque muy extraño) encontrase funciones a la inversa: sólo con un parámetro output (el servidor
envía una notificación al cliente) o con los parámetros output e input por ese orden (el servidor le pide al
cliente alguna información).
Por tanto, al definir una función (un elemento operation) se debe tener cuidado con el orden de los
elementos input y output.
Normalmente, los elementos input y output contendrán un atributo message para hacer referencia a un
mensaje definido anteriormente.

#### Binding

Antes comentábamos que existían distintos estilos de enlazado, que influían en cómo se debían crear los
mensaje. En el elemento binding se debe indicar que el estilo de enlazado de tu documento sea
RPC/encoded.
Aunque es posible crear documentos WSDL con varios elementos binding, la mayoría contendrán solo uno (si
no fuera así, sus atributos name deberán ser distintos).
En él, para cada una de las funciones (operation) del portType que acabamos de crear, se deberá indicar
cómo se codifica y transmite la información.
Para el portType anterior, podemos crear un elemento binding como el siguiente:

~~~xml
<binding name="usuarioBinding" type="tns:usuarioPortType">
<soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
<operation name="getAlumno">
<soap:operation soapAction="http://ejercicios.soap.es/usuarios/Usuario.php?
getUsuario" style="rpc"/>
<input>
<soap:body use="encoded"
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
</input>
<output>
<soap:body use="encoded"
encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
</output>
</operation>
</binding>
~~~

Fíjate que el atributo type hace referencia al portType creado anteriormente. El siguiente elemento indica el
tipo de codificación (RPC) y, mediante la URL correspondiente, el protocolo de transporte a utilizar (HTTP)
El elemento soap:operation debe contener un atributo soapAction con la URL para esa función
(operation)en particular. Dentro de él habrá normalmente un elemento input y otro output (los mismos que
en la operation correspondiente). En ellos, mediante los atributos del elemento soap:body, se indica el estilo
concreto de enlazado (encoded con su encondingStyle correspondiente).

#### Service

Por último, falta definir el elemento service. Normalmente sólo encontraremos un elemento service en cada
documento WSDL. En él, se hará referencia al binding anterior utilizando un elemento port, y se indicará la
URL en la que se puede acceder al servicio.

~~~xml
<service name="usuario">
<port name="usuarioPort" binding="tns:usuarioBinding">
<soap:address location="http://ejercicios.soap.es/usuarios/Usuario.php" />
</port>
</service>
~~~

## Servicios web REST

REST es una tecnología mucho más flexible que transporta datos por medio del protocolo HTTP.
Además permite utilizar los diversos métodos que proporciona HTTP para comunicarse, como lo son GET,
POST, PUT, DELETE, PATCH.
Permite transmitir prácticamente cualquier tipo de datos, ya que el tipo de datos está definido por el Header
Content-Type, lo que nos permite mandar, XML, JSON, binarios (imágenes o documentos), text, etc.
La gran mayoría transmite en JSON por un motivo muy importante: JSON es interpretado de forma
natural por JavaScript
REST es más liviano en peso y mucho más rápido en su procesamiento que SOAP.

### Cliente

Para obtener los datos del un servicio web REST se utiliza la librería cURL. Es una biblioteca que permite
conectarse y comunicarse con diferentes tipos de servidores y diferentes tipos de protocolos.
Un ejemplo de una petición GET podría ser la siguiente:

~~~php
$url_servicio = "http://zoologico.laravel/rest";
$curl = curl_init($url_servicio);
//establecemos el verbo http que queremos utilizar para la petición
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "GET");
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
$respuesta_curl = curl_exec($curl);
curl_close($curl);
$respuesta_decodificada = json_decode($respuesta_curl);
~~~

### Servidor

La idea es generar una página que devuelva una respuesta en formato JSON.
Para ello se puede utilizar el método json de Laravel.
Se crea un controlador específico y las rutas correspondientes.
Luego, en el controlador se hacen los métodos necesarios para realizar todas las operaciones del servicio
web.

Por ejemplo, si queremos devolver en formato JSON todos los animales de nuestro zoologico, podemos hacer
algo así:

~~~php
$animales=Animal::all();
return response()->json($animales);
~~~

Si quisiéramos enviar un mensaje lo haríamos a través de un array asociativo:

~~~php
return response()->json(['mensaje' => ‘El mensaje a enviar’]);
~~~