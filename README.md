OPTIMIZACIÓN DE RUTAS DE ENTREGA 
Este proyecto resuelve el Problema del Viajante (TSP) para encontrar rutas de entrega eficientes entre varias ciudades. El programa genera un grafo de ciudades con distancias aleatorias y permite calcular rutas usando dos algoritmos: Nearest Neighbor y Backtracking.
REQUISITOS:
- Python 3.8 o superior
- pip
Instalación de dependencias
Ejecuta el siguiente comando para instalar las bibliotecas necesarias:
pip install -r requirements.txt
Cómo ejecutar el programa
1. Abre una terminal.
2. Navega hasta la carpeta donde está el archivo main.py.
3. Ejecuta el programa con:
python main.py
4. Sigue el menú interactivo en consola:
=== OPTIMIZADOR DE RUTAS DE ENTREGA ===
¿Cuántas ciudades quieres? (<=8 para backtracking):
Después, verás un menú como este:
--- Menú ---
1. Mostrar red de ciudades
2. Resolver con Nearest Neighbor
3. Resolver con Backtracking
4. Salir
5. Ingresa el número correspondiente a la opción deseada.
6. Introduce la ciudad inicial cuando se solicite (ej. C0, C1...).
7. El programa mostrará la ruta y un gráfico de la red con la ruta destacada.
SUGERECIAS:
- Usa Backtracking solo si hay 8 o menos ciudades, ya que es muy lento con más.
- Puedes repetir el proceso sin cerrar el programa.
- Usa Ctrl+C si deseas forzar la salida en cualquier momento.
VISUALIZACIÓN:
El programa muestra automáticamente un gráfico con la red de ciudades y la ruta seleccionada usando matplotlib.
