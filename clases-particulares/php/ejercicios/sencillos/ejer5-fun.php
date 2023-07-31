<?php
// Función para calcular el costo de reparación de un vehículo
function calcularCostoReparacion($tipoVehiculo, $horasTrabajo, $precioHora, $calcularDescuento) {
    // Cálculo del costo base
    $costoBase = $horasTrabajo * $precioHora;

    // Aplicar descuento si es necesario
    if ($calcularDescuento) {
        $descuento = 0.0;

        // Función anónima para calcular el descuento basado en el tipo de vehículo
        $calcularDescuento = function($tipoVehiculo) use (&$descuento) {
            switch ($tipoVehiculo) {
                case 'automóvil':
                    $descuento = $descuento + 0.1; // 10% de descuento para automóviles
                    break;
                case 'camioneta':
                    $descuento = $descuento + 0.2; // 20% de descuento para camionetas
                    break;
                case 'motocicleta':
                    $descuento = $descuento + 0.15; // 15% de descuento para motocicletas
                    break;
            }
        };

        // Llamada a la función anónima para calcular el descuento
        $calcularDescuento($tipoVehiculo);

        // Aplicar descuento al costo base
        $costoBase = $costoBase - ($costoBase * $descuento);
    }

    return $costoBase;
}

// Datos de prueba
$tipoVehiculo = 'automóvil';
$horasTrabajo = 5;
$precioHora = 50;

// Llamada a la función para calcular el costo de reparación
$costoReparacion = calcularCostoReparacion($tipoVehiculo, $horasTrabajo, $precioHora, true);

echo "El costo de reparación para un $tipoVehiculo es de $costoReparacion dólares.";
?>