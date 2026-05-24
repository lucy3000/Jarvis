import math

def Calc(query):
    # Bereinigung des Eingabeausdrucks
    Term = str(query).lower().strip()

    # Wörter durch mathematische Symbole ersetzen
    Term = Term.replace("multiply", "*")
    Term = Term.replace("times", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("add", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("subtract", "-")
    Term = Term.replace("divide", "/")
    Term = Term.replace("by", "/")
    Term = Term.replace("power of", "**")
    Term = Term.replace("square root of", "math.sqrt")  # Für Wurzeln

    # Überprüfung, ob der Ausdruck noch gültig ist
    if not Term or any(char.isalpha() for char in Term.replace("math.sqrt", "")):
        # Fehler zurückgeben, wenn ungültige Zeichen oder leere Eingabe
        return "Error: Invalid mathematical expression"

    try:
        # Eval für die Berechnung verwenden (mit Sicherheitsbeschränkungen)
        result = eval(Term, {"__builtins__": None}, {"math": math})
        return result
    except Exception as e:
        # Fehlerbehandlung bei ungültigen Ausdrücken
        return f"Error: {str(e)}"
