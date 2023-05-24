Aquí tienes la solución al ejercicio que planteas:

    Creación del servicio web SOAP:

php

<?php
function calculaLetra($dni) {
    $cadena = 'TRWAGMYFPDXBNJZSQVHLCKE';
    $indice = $dni % 23;
    $letra = $cadena[$indice];
    return $letra;
}

$server = new SoapServer(null, array('uri' => 'http://localhost/soap-service'));
$server->addFunction('calculaLetra');
$server->handle();
?>

    Recepción de DNI y letra para comprobación:

php

<?php
function compruebaDNI($dni, $letra) {
    $letraCalculada = calculaLetra($dni);
    return $letra == $letraCalculada;
}

$server = new SoapServer(null, array('uri' => 'http://localhost/soap-service'));
$server->addFunction('compruebaDNI');
$server->handle();
?>

    Creación de la clase OperacionesConDNI:

php

<?php
class OperacionesConDNI {
    public function calculaLetra($dni) {
        $cadena = 'TRWAGMYFPDXBNJZSQVHLCKE';
        $indice = $dni % 23;
        $letra = $cadena[$indice];
        return $letra;
    }

    public function compruebaDNI($dni, $letra) {
        $letraCalculada = $this->calculaLetra($dni);
        return $letra == $letraCalculada;
    }
}

$server = new SoapServer(null, array('uri' => 'http://localhost/soap-service'));
$server->setClass('OperacionesConDNI');
$server->handle();
?>

    Creación del WSDL utilizando WSDLDocument:

php

<?php
require_once 'WSDLDocument.php';

$wsdl = new WSDLDocument('OperacionesConDNI', 'http://localhost/soap-service');
$wsdl->addMethod('calculaLetra', 'http://localhost/soap-service#calculaLetra', 'http://localhost/soap-service#calculaLetra');
$wsdl->addMethod('compruebaDNI', 'http://localhost/soap-service#compruebaDNI', 'http://localhost/soap-service#compruebaDNI');

header('Content-Type: text/xml');
echo $wsdl->saveXML();
?>

Recuerda que debes reemplazar 'http://localhost/soap-service' con la URL real donde estará alojado tu servicio web SOAP. Además, asegúrate de tener instaladas las dependencias requeridas, como la clase WSDLDocument si decides utilizarla.

Para consumir los servicios desde un cliente SOAP, puedes utilizar la clase SoapClient de PHP y las URL correspondientes a cada método del servicio.