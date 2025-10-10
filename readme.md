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

