---- Clase 1 -----
-		¿Qué elementos clave se identifican en la estructura de un archivo de workflow de GitHub Actions?
R= El nombre , el evento que reacciona (ej: push sobre branches especificas, pull requiest …) lista de acciones (Jobs)
-	¿Qué eventos disparan estos workflows por defecto?
push:
    branches: [ "main" ]
  pull_request:
    "# The branches below must be a subset of the branches above"
    branches: [ "main" ]
-	¿Qué tareas o "jobs" suelen incluir los workflows de CI por defecto? 
Checkout ( de este repo me trae todo el código), Descargar dependencias ( pip install) build
Nota: Las ejecuciones de GitHub Actions en repositorios públicos y privados consumen minutos de la cuenta de GitHub. A los objetivos de la práctica alcanza con el Free Tier.

---clase 3----
- ¿Qué diferencias se observan entre los eventos que disparan el pipeline de CI y el de CD?
En el caso de CI, los eventos son push y pull-request sobre la branch main. En el caso de CD, es creacion de una tag que empieza con la letra "v".

- ¿Qué ventajas ofrece la automatización de la creación de releases?
Varias ventajas: queda una copia congelada del codigo que formó parte del release en el tag correspondiente, que queda registrado cuando se creo se creo ese tag, y se le da un numero de version al release.
 
¿Cómo se podría extender este pipeline de CD para desplegar la aplicación en un entorno de producción?
Se puede agregar un paso al pipeline de CD que haga un build, corra los tests, si todos pasan, crear un paquete y finalmente hacer deploy del paquete en produccion.

¿Cuál es la función del GITHUB_TOKEN?
Sirve para autenticar el acceso a la API de Github.

¿Cómo sería una forma segura de pasar configuraciones y contraseñas al pipeline?
Guardarlas como variables de entorno (env) o secrets.



