from src import MacMenuStatus, Config


def main():
    config = Config()
    app = MacMenuStatus(config)
    app.run()


if __name__ == "__main__":
    main()
