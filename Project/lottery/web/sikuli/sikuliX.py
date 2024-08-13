from py4j.java_gateway import JavaGateway
import subprocess
import os

DIR_NAME = os.path.dirname(os.path.abspath(__file__))
jar_path = DIR_NAME + "/SikuliApi.jar"
print(jar_path)


def opengateway():
    try:
        subprocess.run('start "jvm" java -jar ' + jar_path, shell=True)
    except subprocess.CalledProcessError as e:
        print('GatewayError')
        raise e
    gateway = JavaGateway()
    app = gateway.entry_point
    print('Open Gateway')
    return gateway, app


class Sikuli:
    def __init__(self):
        self.gateway, self.app = opengateway()

    def closeGateway(self):
        self.gateway.shutdown()
        print('Shutdown Gateway')

    def click_(self, img_path, similarily=0.7, target_x=0, target_y=0):
        return self.app.screen().click(self.app.pattern(img_path).similar(similarily).targetOffset(target_x, target_y))

    def wait_(self, img_path, second, similarily=0.7):
        return self.app.screen().wait(self.app.pattern(img_path).similar(similarily), float(second))

    def find_(self, img_path, similarily=0.7):
        return self.app.screen().find(self.app.pattern(img_path).similar(similarily))

    def waitVanish_(self, img_path, second, similarily=0.7):
        return self.app.screen().waitVanish(self.app.pattern(img_path).similar(similarily), float(second))

    def exists_(self, img_path, second, similarily=0.7):
        return self.app.screen().exists(self.app.pattern(img_path).similar(similarily), float(second))
