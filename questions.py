import random


categorias = {
  "paises": [
  "Argentina",
  "Peru",
  "Polonia",
  "Australia",
  "Japon",
  "Brasil",
  "Canada",
  "Marruecos",
],
  "animales": [
  "perro",
  "elefante",
  "conejo",
  "ballena",
  "loro",
  "comadreja",
  "colibri",
  "cocodrilo",
],
  "tecnologia": [
"python",
"programa",
"variable",
"funcion",
"bucle",
"cadena",
"entero",
"lista",
]
}

claves = list(categorias.keys())
score = 0
seguir = True
print("¡Bienvenido al Ahorcado!")

print("Categorias")
for i in range(1,len(claves) + 1):
  print(f"{i}-{claves[i-1]}")

cat = int(input("Ingrese una categoria: "))

while cat < 1 or cat > len(claves):
  print(f"{cat} no corresponde a una categoria")
  print()
  cat = int(input("Ingrese una categoria: "))

cat = claves[cat - 1] 
words = random.sample(categorias[cat], len(categorias[cat]))

print()
while len(words) > 0 and seguir:
  word = words.pop()
  attempts = 6
  guessed = []
  while attempts > 0:
  # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
      if letter in guessed:
        progress += letter + " "
      else:
        progress += "_ "
    print(progress)
  # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
      print("¡Ganaste!")
      score += 6
      print(f"Puntaje total {score}")
      break

    print(f"categoria: {cat}")
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if not letter.isalpha() or len(letter) > 1:
      print("Entrada no válida")
    elif letter in guessed:
      print("Ya usaste esa letra.")
    elif letter in word:
      guessed.append(letter)
      print("¡Bien! Esa letra está en la palabra.")
    else:
      guessed.append(letter)
      attempts -= 1
      score -= 1
      print("Esa letra no está en la palabra.")
    print()
  else:
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje total: 0")
  print("¿Seguir Jugando?")
  op = int(input("1 - SI\n2 - NO \n"))
  seguir = op == 1
print(f"Puntaje total: {score}")