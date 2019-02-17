class Settings:
    def __init__(self):
        SettingsFile = open("Settings.txt", "r")

        r = str(SettingsFile.readline())
        g = str(SettingsFile.readline())
        b = str(SettingsFile.readline())

        self.blR = r.replace('\n', '')
        self.blG = g.replace('\n', '')
        self.blB = b.replace('\n', '')

    def saveSettings(self):
        SettingsFile = open("Settings.txt", "w")
        SettingsFile.write((str(self.blR) + '\n' + str(self.blG) + '\n' + str(self.blB)))
        SettingsFile.close()


globSettings = Settings()

