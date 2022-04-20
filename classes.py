class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self, power: bool, channel: int, volume: int):
        """
        This method initializes all the changeable variables for the class
        :param power: sets an initial boolean value for power status; true for on, false for off
        :param channel: sets an initial integer value for channel number
        :param volume: sets an initial integer value for volume number
        :return: None
        """

        self.pow = power
        self.chan = channel
        self.vol = volume

    def power(self) -> bool:
        """
        This method flips the power on and off depending on the current state
        :return: boolean for power status: true if on, false if off
        """
        if type(self.pow) != bool:
            raise TypeError

        if self.pow is True:
            self.pow = False
            return self.pow
        else:
            self.pow = True
            return self.pow

    def channel_up(self) -> int:
        """
        increments the channel by one and defaults to the min if at the max already
        :return: integer of the new channel number
        """
        if type(self.pow) != bool or type(self.chan) != int:
            raise TypeError
        if self.chan < self.MIN_CHANNEL or self.chan > self.MAX_CHANNEL:
            raise ValueError

        if self.pow is True:
            if self.chan == self.MAX_CHANNEL:
                self.chan = self.MIN_CHANNEL
                return self.chan
            else:
                self.chan += 1
                return self.chan
        else:
            return self.chan

    def channel_down(self) -> int:
        """
        decrements the channel by one and defaults to the max if at the min already
        :return: integer of the new channel
        """
        if type(self.pow) != bool or type(self.chan) != int:
            raise TypeError
        if self.chan < self.MIN_CHANNEL or self.chan > self.MAX_CHANNEL:
            raise ValueError

        if self.pow is True:
            if self.chan == self.MIN_CHANNEL:
                self.chan = self.MAX_CHANNEL
                return self.chan
            else:
                self.chan -= 1
                return self.chan
        else:
            return self.chan

    def volume_up(self) -> int:
        """
        increments the volume by one and defaults to the min if at max already
        :return: integer value of new volume
        """
        if type(self.pow) != bool or type(self.vol) != int:
            raise TypeError
        if self.vol < self.MIN_VOLUME or self.vol > self.MAX_VOLUME:
            raise ValueError

        if self.pow is True:
            if self.vol == self.MAX_VOLUME:
                return self.vol
            else:
                self.vol += 1
                return self.vol
        else:
            return self.vol

    def volume_down(self) -> int:
        """
        decrements the volume by one and defaults to the max if at the min already
        """
        if type(self.pow) != bool or type(self.vol) != int:
            raise TypeError
        if self.vol < self.MIN_VOLUME or self.vol > self.MAX_VOLUME:
            raise ValueError

        if self.pow is True:
            if self.vol == self.MIN_VOLUME:
                return self.vol
            else:
                self.vol -= 1
                return self.vol
        else:
            return self.vol

    def __str__(self) -> str:
        """
        prepares a string that includes info on current power status, channel number, and volume number
        :return: string containing information about the status of the television
        """
        if type(self.pow) != bool or type(self.chan) != int or type(self.vol) != int:
            raise TypeError
        if (self.chan < 0 or self.chan > 3) or (self.vol < 0 or self.vol > 2):
            raise ValueError
        return str(f'TV status: Is on = {self.pow}, Channel = {self.chan}, Volume = {self.vol}')
