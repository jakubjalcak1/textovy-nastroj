def pocet_slov(text):
    return len(text.split())

def skratit(text, n):
    if len(text) <= n:
        return text
    return f"{text[:n-1]}…"

def najcastejsie_slovo(text):
    if len(text.split()) == 0:
        raise ValueError("text neobsahuje ziadne slova")
    slova = text.lower().split()
    return max(slova, key=slova.count)


print(najcastejsie_slovo("Ahoj svet ahoj"))