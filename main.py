from src import MacMenuStatus, Config, WidgetBuilder


def main():
    config = Config()
    widgets = WidgetBuilder(config).build()
    app = MacMenuStatus(config, widgets)
    app.run()


if __name__ == "__main__":
    main()
