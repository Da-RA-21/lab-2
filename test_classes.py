import pytest
from classes import *


class Test:
    def setup_method(self):
        # TypeError scenarios
            # channel errors
        self.t1 = Television(True, 'str', 0)
        self.t2 = Television(True, 1.1, 0)
        self.t3 = Television(True, True, 0)
            # volume errors
        self.t4 = Television(True, 0, 'str')
        self.t5 = Television(True, 0, 1.1)
        self.t6 = Television(True, 0, True)
            # power errors
        self.t7 = Television('True', 0, 0)
        self.t8 = Television(1, 1, 1)
        self.t9 = Television(1.1, 0, 0)

        # ValueError scenarios
        self.t10 = Television(True, 0, -1)
        self.t11 = Television(True, -1, 0)

        # Good Scenarios
        self.t12 = Television(True, 0, 0)
        self.t13 = Television(True, 1, 1)
        self.t14 = Television(True, 2, 2)
        self.t15 = Television(True, 3, 2)
        self.t16 = Television(False, 0, 0)

    def teardown_method(self):
        del self.t1
        del self.t2
        del self.t3
        del self.t4
        del self.t5
        del self.t6
        del self.t7
        del self.t8
        del self.t9
        del self.t10
        del self.t11
        del self.t12
        del self.t13
        del self.t14
        del self.t15
        del self.t16

    def test_power(self):
        with pytest.raises(TypeError):
            self.t7.power()
            self.t8.power()
            self.t9.power()
        assert self.t12.power() is False
        assert self.t16.power() is True

    def test_channel_up(self):
        with pytest.raises(TypeError):
            self.t1.channel_up()
            self.t2.channel_up()
            self.t3.channel_up()
            self.t7.channel_up()
            self.t8.channel_up()
            self.t9.channel_up()
        with pytest.raises(ValueError):
            self.t11.channel_up()

        assert self.t12.channel_up() == 1
        assert self.t13.channel_up() == 2
        assert self.t14.channel_up() == 3
        assert self.t15.channel_up() == 0
        assert self.t16.channel_up() == 0

    def test_channel_down(self):
        with pytest.raises(TypeError):
            self.t1.channel_down()
            self.t2.channel_down()
            self.t3.channel_down()
            self.t7.channel_down()
            self.t8.channel_down()
            self.t9.channel_down()
        with pytest.raises(ValueError):
            self.t11.channel_down()

        assert self.t12.channel_down() == 3
        assert self.t13.channel_down() == 0
        assert self.t14.channel_down() == 1
        assert self.t15.channel_down() == 2
        assert self.t16.channel_down() == 0

    def test_volume_up(self):
        with pytest.raises(TypeError):
            self.t4.volume_up()
            self.t5.volume_up()
            self.t6.volume_up()
            self.t7.volume_up()
            self.t8.volume_up()
            self.t9.volume_up()
        with pytest.raises(ValueError):
            self.t10.volume_up()

        assert self.t12.volume_up() == 1
        assert self.t13.volume_up() == 2
        assert self.t14.volume_up() == 2
        assert self.t16.volume_up() == 0

    def test_volume_down(self):
        with pytest.raises(TypeError):
            self.t4.volume_down()
            self.t5.volume_down()
            self.t6.volume_down()
            self.t7.volume_down()
            self.t8.volume_down()
            self.t9.volume_down()
        with pytest.raises(ValueError):
            self.t10.volume_down()

        assert self.t12.volume_down() == 0
        assert self.t13.volume_down() == 0
        assert self.t14.volume_down() == 1
        assert self.t16.volume_down() == 0

    def test_str(self):
        with pytest.raises(TypeError):
            print(self.t1)
            print(self.t2)
            print(self.t3)
            print(self.t4)
            print(self.t5)
            print(self.t6)
            print(self.t7)
            print(self.t8)
            print(self.t9)
        with pytest.raises(ValueError):
            print(self.t10)
            print(self.t11)

        assert self.t12.__str__() == f'TV status: Is on = True, Channel = 0, Volume = 0'
        assert self.t13.__str__() == f'TV status: Is on = True, Channel = 1, Volume = 1'
        assert self.t14.__str__() == f'TV status: Is on = True, Channel = 2, Volume = 2'
        assert self.t15.__str__() == f'TV status: Is on = True, Channel = 3, Volume = 2'
        assert self.t16.__str__() == f'TV status: Is on = False, Channel = 0, Volume = 0'
