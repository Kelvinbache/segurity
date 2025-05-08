# Security 

Create a more secure security system than the current ones, to prevent theft, scams or any crime that may occur on the web.

# Technical Flowchart
This diagram illustrates the data flow and system components.
owchart TD
---
A[Usuario] --> B{Aplicación Móvil/Web};
B --> C{API Gateway};
C --> D{Servicios de Autenticación};
C --> E{Servicios de Transacciones};
E --> F{Motor de Riesgo y IA};
F --> G[Base de Datos];
E --> G;
D --> G;