class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        This method initializes all the changeable variables for the class
        :return: None
        """
        self.pow = False
        self.chan = 0
        self.vol = 0

    def power(self) -> None:
        """
        This method flips the power on and off depending on the current state
        :return: boolean for power status: true if on, false if off
        """
        if self.pow is True:
            self.pow = False
        else:
            self.pow = True

    def channel_up(self) -> None:
        """
        increments the channel by one and defaults to the min if at the max already
        :return: integer of the new channel number
        """

        if self.pow is True:
            if self.chan == self.MAX_CHANNEL:
                self.chan = self.MIN_CHANNEL
            else:
                self.chan += 1
        else:
            pass

    def channel_down(self) -> None:
        """
        decrements the channel by one and defaults to the max if at the min already
        :return: integer of the new channel
        """
        if self.pow is True:
            if self.chan == self.MIN_CHANNEL:
                self.chan = self.MAX_CHANNEL
            else:
                self.chan -= 1
        else:
            pass

    def volume_up(self) -> None:
        """
        increments the volume by one and defaults to the min if at max already
        :return: integer value of new volume
        """
        if self.pow is True:
            if self.vol == self.MAX_VOLUME:
                pass
            else:
                self.vol += 1
        else:
            pass

    def volume_down(self) -> None:
        """
        decrements the volume by one and defaults to the max if at the min already
        """
        if self.pow is True:
            if self.vol == self.MIN_VOLUME:
                pass
            else:
                self.vol -= 1
        else:
            pass

    def __str__(self) -> str:
        """
        prepares a string that includes info on current power status, channel number, and volume number
        :return: string containing information about the status of the television
        """
        return str(f'TV status: Is on = {self.pow}, Channel = {self.chan}, Volume = {self.vol}')
