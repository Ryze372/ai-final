from godmode_ai import GodModeAI

if __name__ == "__main__":
    ai = GodModeAI()
    print("Willkommen im Godmode. Gib deinen Befehl ein:")
    while True:
        try:
            cmd = input(">> ")
            result = ai.execute(cmd)
            print(result)
        except Exception as e:
            print(f"Fehler: {e}")