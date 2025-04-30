from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecomendarPlato(Action):

    def name(self) -> Text:
        return "action_recomendar_plato"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ingredientes = tracker.get_slot("ingrediente") or []
        dieta = tracker.get_slot("dieta")

        ingredientes = [i.lower() for i in ingredientes]

        if not ingredientes:
            dispatcher.utter_message(text="¿Qué ingredientes tienes disponibles?")
            return []

        if dieta:
            dieta = dieta.lower()

        if "tomate" in ingredientes and "queso" in ingredientes and "pan" in ingredientes:
            if dieta == "vegana":
                recomendacion = "Puedes hacer un bocadillo de tomate con hummus y rúcula."
            else:
                recomendacion = "Puedes preparar un bocadillo clásico con queso y tomate."
        elif "queso" in ingredientes and "pan" in ingredientes:
            recomendacion = "Puedes preparar un montadito."
        elif "tomate" in ingredientes and "pan" in ingredientes:
            recomendacion = "Puedes preparar una tostada con tomate."
        elif "tomate" in ingredientes and "queso" in ingredientes:
            recomendacion = "Puedes preparar una ensalada caprese (o vegana con tofu si sigues esa dieta)."
        else:
            recomendacion = "No tengo suficientes datos, ¿podrías decirme qué dieta sigues y qué ingredientes tienes?"

        dispatcher.utter_message(text=recomendacion)
        return []
class ActionListaCompras(Action):
    def name(self) -> Text:
        return "action_lista_compras"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        plato = tracker.get_slot("platos")

        ingredientes_por_plato = {
            "paella": ["arroz", "pollo", "mariscos", "pimiento", "azafrán", "aceite de oliva"],
            "pasta al pesto": ["pasta", "albahaca", "piñones", "ajo", "queso parmesano", "aceite de oliva"],
            "ensalada césar": ["lechuga", "pollo", "queso", "crutones", "salsa césar"],
            "potaje de lentejas": ["lentejas", "zanahoria", "cebolla", "pimiento", "ajo", "aceite de oliva"],
        }

        if plato and plato.lower() in ingredientes_por_plato:
            lista = ingredientes_por_plato[plato.lower()]
            respuesta = f"Para preparar {plato}, necesitas: {', '.join(lista)}."
        else:
            respuesta = "¿Qué plato quieres cocinar? Puedo darte la lista de compras para platos como paella, pasta al pesto, ensalada césar o potaje de lentejas."

        dispatcher.utter_message(text=respuesta)
        return []

class ActionRecomendarReceta(Action):
    def name(self) -> str:
        return "action_recomendar_receta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:

        dieta = next(tracker.get_latest_entity_values("dieta"), None)

        recetas = {
            "vegana": "Un curry de garbanzos con leche de coco y espinacas.",
            "vegetariana": "Una lasaña de berenjena con ricotta.",
            "cetogénica": "Salmón al horno con aguacate y ensalada verde.",
            "mediterránea": "Ensalada griega con queso feta y aceitunas.",
            "sin gluten": "Tortilla de patatas sin harina acompañada de ensalada."
        }

        if dieta and dieta.lower() in recetas:
            recomendacion = recetas[dieta.lower()]
        else:
            recomendacion = "¿Qué tipo de dieta sigues? Puedo recomendar recetas veganas, vegetarianas, cetogénicas, mediterráneas o sin gluten."

        dispatcher.utter_message(text=recomendacion)
        return []

class ActionInfoNutricional(Action):

    def name(self) -> Text:
        return "action_info_nutricional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        plato = tracker.get_slot("platos")

        nutricion_por_plato = {
            "paella": "La paella aporta carbohidratos por el arroz, proteínas por el marisco y grasas saludables por el aceite de oliva.",
            "pasta al pesto": "La pasta al pesto aporta energía (carbohidratos), grasas saludables del aceite de oliva y piñones, y algo de proteína del queso.",
            "ensalada césar": "Aporta proteína del pollo, calcio del queso y fibra de la lechuga. La salsa puede contener grasas.",
            "potaje de lentejas": "Rico en proteínas vegetales, fibra y hierro. Ideal para dietas equilibradas."
        }

        if plato and plato.lower() in nutricion_por_plato:
            mensaje = nutricion_por_plato[plato.lower()]
        else:
            mensaje = "¿Qué plato quieres analizar? Puedo darte la información nutricional de platos como paella, pasta al pesto, ensalada césar o potaje de lentejas."

        dispatcher.utter_message(text=mensaje)
        return []


class ActionMealPrepSemanal(Action):

    def name(self) -> Text:
        return "action_meal_prep_semanal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dieta = tracker.get_slot("dieta")
        ingrediente = tracker.get_slot("ingrediente")

        if not dieta:
            dispatcher.utter_message(text="¿Qué tipo de dieta sigues para poder prepararte un plan semanal?")
            return []

        dieta = dieta.lower()

        plan = f"Plan semanal para dieta {dieta}:\n"
        plan += "- Lunes: Bowl de quinoa con {0}\n".format(ingrediente[0] if ingrediente else "verduras")
        plan += "- Martes: Salteado de tofu con arroz integral\n"
        plan += "- Miércoles: Crema de lentejas y ensalada fresca\n"
        plan += "- Jueves: Curry de {0} con leche de coco\n".format(ingrediente[0] if ingrediente else "garbanzos")
        plan += "- Viernes: Ensalada de pasta integral con pesto vegano\n"
        plan += "- Sábado: Pizza saludable con base de coliflor\n"
        plan += "- Domingo: Batido energético con avena y fruta"

        dispatcher.utter_message(text=plan)
        return []
