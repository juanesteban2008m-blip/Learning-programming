Algoritmo profesor_estudiantes
	// Declare or constantns 
	PI_VALUE<-3.1416 
	
    // Declare or variables enteros
definir lado, baseRect, alturaRect, baseTri, alturaTri Como Entero 
	//Declare or variables reales 
definir radio, areaCuadrado, areaRectangulo, areaTriangulo, areaCirculo, totalAreas Como Real
	
    // Request and calculate area of the square
    Escribir "Introduce el valor del lado del cuadrado: "
    Leer lado
    areaCuadrado <- lado * lado
    Escribir "El área del cuadrado es: ", areaCuadrado
	
    // Request and calculate area of the rectangle
    Escribir "Introduce el valor de la base del rectángulo: "
    Leer baseRect
    Escribir "Introduce el valor de la altura del rectángulo: "
    Leer alturaRect
    areaRectangulo <- baseRect * alturaRect
    Escribir "El área del rectángulo es: ", areaRectangulo
	
    // Request and calculate area of the triangle
    Escribir "Introduce el valor de la base del triángulo: "
    Leer baseTri
    Escribir "Introduce el valor de la altura del triángulo: "
    Leer alturaTri
    areaTriangulo <- (baseTri * alturaTri) / 2
    Escribir "El área del triángulo es: ", areaTriangulo
	
    // Request and calculate area of the circle
    Escribir "Introduce el valor del radio del círculo: "
    Leer radio
    areaCirculo <- PI * (radio * radio)
    Escribir "El área del círculo es: ", areaCirculo
	
    // Calculate the total areas
    totalAreas <- areaCuadrado + areaRectangulo + areaTriangulo + areaCirculo
    Escribir "El total de todas las áreas es: ", totalAreas

FinAlgoritmo
