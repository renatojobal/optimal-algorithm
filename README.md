# API para aplicación del algoritmo óptimo de reemplazo de páginas

## Guía
### Prepara el entorno
1. Clona el repositorio
2. Ve a la carpeta raiz del proyecto y escribe lo siguiente para instalar Flask
`pip install -r requirements`ç
> Puedes crear un entorno virtual de python para esto
3. Ejecuta el servicio con:
`service.py`
Listo.
### Uso
La aplicación se estará ejecutando en: `http://127.0.0.1:5000/ `

Se debe enviar a ese url una petición http con los siguientes datos:
- Metódo: `POST`
- URL: `http://127.0.0.1:5000/`
- Body: `JSON(application/json)`
- Body params:
	- **"pages_list"** [*Requerido]* Es un string que representará la lista de páginas. Cáda elemento debe estar separado por un espacio " ".
	- **"frames_number"** [*Requerido*] Es el número de marcos de página
	- **"default_null"** [*Opcional*] Es el valor que por defecto se mostrará es los marcos vaciós.

Ejemplo de petición:
```
{
	"pages_list": "1 2 5 8 2",
	"frames_number": 3,
	"default_null": " "
}
```
Se obtendrá como respuesta un json. Cuyo único nodo `result_matrix` es una lista de listas. La respuesta a la petición anterior sería:
```
{
    "result_matrix": [
        [
            "1",
            "1",
            "1",
            "8",
            "8"
        ],
        [
            " ",
            "2",
            "2",
            "2",
            "2"
        ],
        [
            " ",
            " ",
            "5",
            "5",
            "5"
        ]
    ]
}
```




