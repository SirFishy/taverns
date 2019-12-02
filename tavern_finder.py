from service import tavern_service


def main():
    taverns = tavern_service.get_taverns()
    for tavern in taverns:
        print(tavern)


if __name__ == "__main__":
    main()
