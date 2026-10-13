# Nicole Robles NC= 0120

import cv2
from pathlib import Path

# 1. Buscar la imagen automáticamente en el proyecto
directorio_actual = Path(__file__).resolve().parent
imagen_encontrada = list(directorio_actual.rglob("img-jeep-0120.jpg"))

if not imagen_encontrada:
    # Intenta buscar un nivel arriba por si acaso
    imagen_encontrada = list(directorio_actual.parent.rglob("img-jeep-0120.jpg"))

if not imagen_encontrada:
    raise FileNotFoundError("No se encontró 'img-jeep-0120.jpg' en ninguna carpeta.")

ruta_original = imagen_encontrada[0]

# Definir carpeta de resultados
carpeta_resultados = directorio_actual / "resultados-img-0120"
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0120 = cv2.imread(str(ruta_original))

if img0120 is None:
    raise FileNotFoundError(f"No se pudo cargar la imagen: {ruta_original}")

# 3. Rotar la imagen 90 grados en sentido horario
img90_0120 = cv2.rotate(
    img0120, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0120.shape[:2]
centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0120 = cv2.warpAffine(
    img0120,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600x500
img600x500_0120 = cv2.resize(
    img0120, (600, 500)
)

# 6. Dibujar rectángulo rojo
img_rojo_0120 = img0120.copy()
x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0120,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar imágenes
cv2.imshow("jeep original 0120", img0120)
cv2.imshow("jeep 90 0120", img90_0120)
cv2.imshow("jeep 45 0120", img45_0120)
cv2.imshow("jeep 600x500 0120", img600x500_0120)
cv2.imshow("jeep rojo 0120", img_rojo_0120)

# 8. Guardar imágenes
cv2.imwrite(
    str(carpeta_resultados / "img-jeep1-0120.jpg"),
    img90_0120
)

cv2.imwrite(
    str(carpeta_resultados / "img-jeep2-0120.jpg"),
    img45_0120
)

cv2.imwrite(
    str(carpeta_resultados / "img-jeep3-0120.jpg"),
    img600x500_0120
)

cv2.imwrite(
    str(carpeta_resultados / "img-jeep4-0120.jpg"),
    img_rojo_0120
)

# 9. Finalizar
print("Examen realizado por Nicole Robles NC=0120")
print("Imágenes procesadas y guardadas.")

cv2.waitKey(0)
cv2.destroyAllWindows()