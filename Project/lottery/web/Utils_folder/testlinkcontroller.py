import datetime
import testlink  # TestLink-API-Python-client (0.6.4)

class TestlinkController():
    url = "http://testlink.paradise-soft.com.tw/lib/api/xmlrpc/v1/xmlrpc.php"
    key = "8fb7f0607afadcf81370a77ce152b79f"
    tlc = testlink.TestlinkAPIClient(url, key)
    auto_create_limit = 3  # 限制各品牌每日自動建置版本上限


    # 獲取該品牌最新版本的名稱
    # testplanid = '108'  --TestPlanID
    # brand = 'LV'  --品牌
    def getlasttestplanbuildname(self, testplanid, brand):
        response = self.tlc.getBuildsForTestPlan(testplanid)
        lasttime = '0001-01-01 00:00:01'
        build_name = ''
        for i in range(0, len(response)):
            if brand.lower() in response[i]['name'].lower() and response[i]['creation_ts'] > lasttime:
                lasttime = response[i]['creation_ts']
                build_name = response[i]['name']

        if build_name != '':
            return build_name


    # 確認此版本是否存在
    # testplanid = '108'  ---TestPlanID
    # buildname = 'LV-20170807-test'
    def checkbuildname_in_testplan(self, testplanid, buildname):
        response = self.tlc.getBuildsForTestPlan(testplanid)
        for i in range(0, len(response)):
            if buildname.lower() in response[i]['name'].lower():
                return buildname

        raise Exception(buildname + ' not exist')

    # 於指定TestCase壓上測試結果
    # project = PS_web, PS_app, PS_admin
    # environments = uat, prod
    # brand = 'LV'
    # testcaseexternalid = 'PS_web-21'  --TestCaseID
    # status = 'p' or 'f' or 'b' --Pass / False / block
    # buildname = 'LV-20170807-test'  --版本名稱
    # ex: TestlinkController().settestcaseresult('PS_web', 'uat', 'LV', 'PS_web-21','p')
    def settestcaseresult(self, project, environments, brand, testcaseexternalid, status, buildname=None):
        testplanid = TestlinkController().gettestplanid(project, environments)

        if buildname is None:
            self.buildname = TestlinkController().getlasttestplanbuildname(testplanid, brand)
        elif buildname is not None and isinstance(buildname, str):
            self.buildname = TestlinkController().checkbuildname_in_testplan(testplanid, buildname)
        response = self.tlc.reportTCResult(testplanid=testplanid, testcaseexternalid=testcaseexternalid,
                                           buildname=self.buildname, platformid=0, status=status)
        print('Project: '+project+' ', 'Environments: '+environments+' ', 'brand: '+brand+' ',
              'TestCaseID: ' + testcaseexternalid + ' -', response[0]['message'])

    def set_allcase_pass(self, project, environments, brand, status, buildname=None):

        testplanid = TestlinkController().gettestplanid(project, environments)

        if buildname is None:
            self.buildname = TestlinkController().getlasttestplanbuildname(testplanid, brand)
        elif buildname is not None and isinstance(buildname, str):
            self.buildname = TestlinkController().checkbuildname_in_testplan(testplanid, buildname)

        response_01 = self.tlc.getTestCasesForTestPlan(testplanid)
        keylist = list(response_01.keys())
        for i in range(0, len(keylist)):
            response_02 = self.tlc.reportTCResult(testplanid=testplanid, testcaseid=keylist[i],
                                               buildname=self.buildname, platformid=0, status=status)
            print('Project: '+project+' ', 'Environments: '+environments+' ', 'brand: '+brand+' ',
                  'TestCaseID: ' + keylist[i] + ' -', response_02[0]['message'])


    # 自動建置TestPlan今日版本,未帶onebrand參數則以uat_brand/prod_brand為主
    # 若帶onebrand參數，則以該品牌為主
    # project = PS_web, PS_app, PS_admin
    # environments = uat, prod
    # brands = 'LV' 或是指定品牌
    # ex: TestlinkController().createnewbuilds('PS_web','uat')
    # ex: TestlinkController().createnewbuilds('PS_web','uat', ['LV', 'LS'])
    def createnewbuilds(self, project, environments, brands):
        if isinstance(brands, list):
            for i in range(0, len(brands)):
                if not isinstance(brands[i], str):
                    raise Exception('createNewBuilds()',
                                    'ERROR: parameter brands only can use string in list or string')
            brand = brands
        elif isinstance(brands, str):
            brand = [brands]
        else:
            raise Exception('createNewBuilds()', 'ERROR: parameter brands only can use string in list or string')
        if environments.lower() != 'uat' and environments.lower() != 'prod':
            raise Exception('createNewBuilds()', 'ERROR: parameter environments can only type uat or prod')

        dateforname = datetime.datetime.now().strftime('%Y/%m/%d')
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        testplanid = self.gettestplanid(project, environments)
        for i in range(0, len(brand)):
            buildname = brand[i] + '-' + dateforname
            buildtype = self.tlc.createBuild(testplanid=testplanid, buildname=buildname,
                                             buildnotes='builded by automaction in ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                             , active=1, open=1, releasedate=date)
            num = 0
            while 'already exists' in buildtype[0]['message']:
                num = num + 1
                buildname = brand[i] + '-' + dateforname + '-' + str(num)
                buildtype = self.tlc.createBuild(testplanid=testplanid, buildname=buildname,
                                                 buildnotes='builded by automaction in ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                                 , active=1, open=1, releasedate=date)
                if num == self.auto_create_limit:
                    break
            print(buildname + ' :', buildtype[0]['message'])

    # 獲取TestPlanID
    # project = PS_web, PS_app, PS_admin
    # environments = uat, prod
    # ex: TestlinkController().gettestplanid('PS_web', 'uat')
    # ex: TestlinkController().gettestplanid('PS_web', 'uat', 'LV')
    def gettestplanid(self, project, environments):
        response = self.tlc.getProjects()
        for i in range(0, len(response)):
            if project.lower() == response[i]['prefix'].lower():
                projectid = response[i]['id']
                response2 = self.tlc.getProjectTestPlans(projectid)
                for y in range(0, len(response2)):
                    if environments.lower() in response2[y]['name'].lower():
                        testplanid = response2[y]['id']
                        return testplanid
                raise Exception('gettestplanid()', 'ERROR: 無此Testplan名稱')
        raise Exception('gettestplanid()', 'ERROR: 無此Project名稱')