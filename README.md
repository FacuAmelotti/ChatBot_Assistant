# ChatBot_Assistant
- En este proyecto se buscó desarrollar una herramienta (o prototipo) útil, que sea programable, y que permita ahorrar tiempo automatizando algún proceso y facilitar o disminuir la cantidad de tareas.
- La herramienta a construir fue un ChatBot, en este caso utiliza un motor de procesamiento de lenguaje natural llamado RiveScript para generar respuestas. 
- El software brinda al usuario una interfaz gráfica puede ingresar un mensaje y el chatbot responde automáticamente a través de la misma interfaz gráfica mediante una consola.

    ![Imagen 1](./imgs/chatbot_1.png)
    ![Imagen 2](./imgs/chatbot_2.png)
    ![Imagen 3](./imgs/chatbot_3.png)

---

### ¿Cómo automatizar el proceso?
1.	Definir la tarea que necesita ser automatizada: Desarrollar un Chat automático que pueda responder preguntas a usuarios de manera coherente. Mediante el uso de palabras claves en las preguntas y textos del usuario, el ChatBot vera que respuesta le parece la más adecuada.

2.	Dividir la tarea en pasos más pequeños: 
    1.	Obtener la entrada del usuario: Pedir al usuario que ingrese un mensaje a través de una interfaz gráfica.
    2.	Reprocesamiento de texto: Esta etapa implica la eliminación de caracteres no deseados, como signos de puntuación y caracteres especiales, y la conversión de todo el texto a minúsculas o mayúsculas.
    3.	Procesamiento del lenguaje natural: Este paso implica analizar el mensaje del usuario para determinar su intención y extraer información relevante. Esto puede hacerse mediante técnicas de procesamiento de lenguaje natural.
    4.	Selección de la respuesta: Este paso implica seleccionar la respuesta adecuada para el mensaje del usuario en función de su intención y la información extraída. 
    5.	Generación de respuesta: Generar una respuesta coherente y adecuada para el mensaje del usuario. 
    6.	Entrega de la respuesta: Entregar la respuesta generada al usuario a través de la consola.

3.	Elegir las bibliotecas de Python adecuadas: Este código es un script de Python que utiliza las bibliotecas rivescript (utilizado para motor de procesamiento de lenguaje natural), tkinter (utilizada para crear la interfaz gráfica de usuario) y PIL (utilizada para las imagenes).

4.	Programar la secuencia de comandos de Python: Archivo “/script.py”
El archivo chatBot.exe, es el script compilado. Listo para usar!

5.	Prueba secuencia de comandos.

6.	Monitorear el proceso automatizado: El funcionamiento del script, los procesos que lo conforman y la interfaz gráfica de usuario se han testeado varias veces y en cada una de las pruebas funciono correctamente. 
