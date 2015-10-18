# Subir archivos por cliente FTP

*Soporte
- Lectura de directorios.
- Comprime archivos .zip.
- Subir archivos por FTP
- Control de logs.

Ejemplo:
Subir un archivo al servidor
file_name = 'C:/test.zip'
upload = UploadFile(file_names=file_name).simple
