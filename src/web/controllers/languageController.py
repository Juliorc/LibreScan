from gettext import translation


class LanguageController:

    def __init__(self, env):
        self.env = env

    def change_language(self, lang):
        translations = translation(domain='messages', localedir='./i18n/locale', languages=[lang])
        self.env.install_gettext_translations(translations)
        return self.env.get_template('home.jade').render()

