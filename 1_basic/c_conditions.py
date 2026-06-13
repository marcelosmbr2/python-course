# If-elif-else

age = int(input("Digite sua idade: "))

if age < 18:
    print("Você é menor de idade.")
elif age < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")

# Switch-case (match-case)

day = input("Digite um dia da semana: ").lower()

match day:
    case "segunda-feira":
        print("Hoje é segunda-feira.")
    case "terça-feira":
        print("Hoje é terça-feira.")
    case "quarta-feira":
        print("Hoje é quarta-feira.")
    case "quinta-feira":
        print("Hoje é quinta-feira.")
    case "sexta-feira":
        print("Hoje é sexta-feira.")
    case "sábado":
        print("Hoje é sábado.")
    case "domingo":
        print("Hoje é domingo.")
    case _:
        print("Dia da semana inválido.")
