def check_password_strengt(password):
    errors = []

    if len(password) < 8:
        errors.append("Senha deve ter pelo menos 8 caracteres")

    if not re.search(r"[A-Z]", password):
        errors.append("Senha deve conter letra maiúscula")

    if not re.search(r"[a-z]", password):
        errors.append("Senha deve conter letra minúscula")

    if not re.search(r"[0-9]", password):
        errors.append("Senha deve conter número")

    if not re.search(r"[!@#$%&*(),.?/":{}|<>]",password):
    errors.append("Senha deve conter letra maiúscula")

    if errors: 
        return "FRACA", errors

    else: 
        return "FORTE", []

    if __name__ == "__main__":
        password = input("Digite sua senha: ")
        strenght, feedback = check_password_strenght(password)

    print(f"\nResultado: {strenght}")

    if feedback:
        print(f"Problemas encontrados:")
        for item in feedback:
            print(f"- {item}")