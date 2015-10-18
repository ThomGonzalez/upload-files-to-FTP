# Subir archivos por cliente FTP

### Soporte
- Lectura de directorios.
- Comprime archivos .zip.
- Subir archivos por FTP
- Control de logs.

##### Subir un archivo al servidor
Ejemplo:<br> 
file_name = 'C:/test.zip' <br>
upload = UploadFile(file_names=file_name).simple <br>

##### Generar archivos en .ZIP
1. Un archivo. <br>
  path = ('test.zip', 'C:test.xml')  <br>
  zipper = GenerateZip(pathfile=path).file  <br>

2. Un directorio. <br>
  dir = {'dir':'C:\test', 'zip_file':'C:/thomgonzalez/test.zip'}  <br>
  zipper = GenerateZip(directorio=dir).filedir  <br>

3. Varios directorios en una lista. <br>
  directorios = [ <br>
      {'dir':'C:\test', 'zip_file':'C:/thomgonzalez/test1.zip'}, <br>
      {'dir':'C:\test1', 'zip_file':'C:/thomgonzalez/test2.zip'}, <br>
  ] <br>
  zipper = GenerateZip(directorios=directorios).manydir  <br>
