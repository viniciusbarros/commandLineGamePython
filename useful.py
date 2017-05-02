class ColourPrint:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_blue(text):
        print(ColourPrint.OKBLUE + text + ColourPrint.ENDC)

    @staticmethod
    def print_green(text):
        print(ColourPrint.OKGREEN + text + ColourPrint.ENDC)

    @staticmethod
    def print_yellow(text):
        print(ColourPrint.WARNING + text + ColourPrint.ENDC)

    @staticmethod
    def print_red(text):
        print(ColourPrint.FAIL + text + ColourPrint.ENDC)

    @staticmethod
    def print_bold(text):
        print(ColourPrint.BOLD + text + ColourPrint.ENDC)

    @staticmethod
    def print_underline(text):
        print(ColourPrint.UNDERLINE + text + ColourPrint.ENDC)

    @staticmethod
    def print_line(text):
        print(ColourPrint.get_bold("--------------------" + text + "--------------------"))

    @staticmethod
    def test_print():
        text = "Text Message"
        print("Blue")
        ColourPrint.print_blue(text)
        print("Green")
        ColourPrint.print_green(text)
        print("Warning")
        ColourPrint.print_yellow(text)
        print("Fail")
        ColourPrint.print_red(text)
        print("Bold")
        ColourPrint.print_bold(text)
        print("Underline")
        ColourPrint.print_underline(text)

    @staticmethod
    def get_blue(text):
        return ColourPrint.OKBLUE + text + ColourPrint.ENDC

    @staticmethod
    def get_green(text):
        return ColourPrint.OKGREEN + text + ColourPrint.ENDC

    @staticmethod
    def get_yellow(text):
        return ColourPrint.WARNING + text + ColourPrint.ENDC

    @staticmethod
    def get_red(text):
        return ColourPrint.FAIL + text + ColourPrint.ENDC

    @staticmethod
    def get_bold(text):
        return ColourPrint.BOLD + text + ColourPrint.ENDC

    @staticmethod
    def get_underline(text):
        return ColourPrint.UNDERLINE + text + ColourPrint.ENDC


class GenericMenu:
    @staticmethod
    def generic_menu(title, question, options, object):
        executed = False

        while not executed:
            ColourPrint.print_line(title)
            ColourPrint.print_blue(question)

            for menu, text in options.items():
                ColourPrint.print_yellow("- \"{0}\" to {1}".format(menu, text))

            chosen_option = raw_input(ColourPrint.get_blue("I want to: "))

            try:
                # self.() //How to check whether this exist or not
                func = getattr(object, chosen_option)
                func()
            except AttributeError:
                ColourPrint.print_red("Option \"{}\" is invalid".format(chosen_option))
            else:
                executed = True
