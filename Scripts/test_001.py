import allure,pytest
class Test_001:
    @allure.step(title = "登录")
    def test_001(self):
        allure.attach("用户名","输入用户名")
        allure.attach("密码","输入密码")
        allure.attach("登录","点击登录")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.setp(title = "注册")
    def test_02(self):
        assert 1