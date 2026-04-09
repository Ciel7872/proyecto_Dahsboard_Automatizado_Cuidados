# DocumentarTodo!

# Configurar integracion externa con Cepal api
# configurar con otros indicarores y analisis apis(averiguar en word)
# Zona: api_Cepal-----------------


# Configurar geo_infra : Script para traer mapas

# herramienta de vizulacion: streamlit
# Analizar la herramientas 
# Zona: data---------------


# Analizar las entrevistas de mexico en word.

---------------

### Para descargarse todo usen comando: 

docker-compose up --build
(esperen un ratito hasta que haya descargado todo)

### Para ejecutar dentro del contenedor usen
docker exec -it monitor-cepal python >ruta>
### Por ejemplo:
docker exec -it monitor-cepal python src/apis/api_cepal.py

### sino usen un venv y descargue con pip los requirements(asi descargan todo local y ya no usan el contenedor) para que se sientan mas comodos

### a partir de la rama de desarrollo creen su rama (no de la main ojo)
### Para actualizar sus repositorios locales
git fetch --all 
### Para crear una rama nueva desde desarrollo:
git checkout desarrollo
git checkout -b >su nombre o feature_api_...>


### comando streamlist
docker exec -it monitor-cepal python src/apis/api_cepal.py

En http://localhost:8501/ 