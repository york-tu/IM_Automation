import os, sys, yaml
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)
# from Project.lottery.configs.setting import Setting
import common.utils.globalvar as gl

class BaseKey:
    # conf's path
    jira_conf_path = 'jira/config/jira_key.yml'

    def get_yaml_conf(self):
        yamlfile = open(os.path.join(root_path, self.jira_conf_path))
        ymlconf = yaml.safe_load(yamlfile)
        return ymlconf

    def get_jira_data(self):
        env = gl.get_value('ENV')
        brand = gl.get_value('BRAND')
        test_type = gl.get_value('TEST_TYPE')

        cycle_key = self.get_yaml_conf()['jira_conf'][env][brand][test_type]
        gl.set_value('CYCLE_KEY', cycle_key)


