from facade import SmartHomeFacade

def main():
    casa = SmartHomeFacade()
    casa.activar_modo_verano()
    casa.activar_modo_invierno()

if __name__ == "__main__":
    main()
