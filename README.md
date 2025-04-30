# BOTcadillo

**BOTcadillo** es un chatbot gastronómico creado con [Rasa](https://rasa.com/) que te ayuda a planificar tus comidas, recomendarte recetas según tu dieta, sugerir platos con los ingredientes que tienes y generar planes semanales personalizados. Además, puede informarte sobre el valor nutricional de diferentes platos y generar listas de compras.

---

## Funcionalidades principales

- **Recomendación de platos** a partir de los ingredientes que tengas.
- **Sugerencia de recetas** según el tipo de dieta (vegana, keto, mediterránea...).
- **Lista de la compra automática** para cualquier plato.
- **Análisis nutricional** de platos comunes.
- **Meal prep semanal** según ingredientes y dieta.
- **Respuestas naturales** para saludar, despedir y mantener una conversación amigable.
- **Fallback amigable** para cuando el bot no entiende algo: "Lo siento... con eso no te puedo ayudar, pero ¿qué tal si planificamos tu menú semanal para compensar?"

---

## Tecnologías utilizadas

- [Rasa Open Source](https://rasa.com/) 3.1
- Python 3.10
- IA conversacional basada en NLU + reglas + acciones personalizadas


## Cómo ejecutar el bot

1. **Clona este repositorio**
```bash
git clone https://github.com/tuusuario/BOTcadillo.git
cd BOTcadillo
```

2. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

3. **Entrena el modelo**
```bash
rasa train
```

4. **Lanza el servidor de acciones** (en una terminal)
```bash
rasa run actions
```

5. **Lanza el bot en modo conversación** (en otra terminal)
```bash
rasa shell
```

---

## Ejemplos para probar

```
Tengo pan, tomate y queso
Recomiéndame una receta vegana
¿Que nutrientes tiene la paella?
Hazme una lista de compras para preparar pasta al pesto
Quiero un plan semanal si soy vegetariano
¿Quién es Rayo McQueen?
```


> "BOTcadillo: si tienes ingredientes, yo tengo respuestas."
