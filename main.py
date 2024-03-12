import random
import matplotlib.pyplot as plt
import numpy as np


class VoiceDataGenerator:
    """
    A class to generate synthetic voice data.

    Attributes:
        duration (int): The duration of the voice data in 1/10 seconds.
        gender (str): The gender of the voice data ('M' for male, 'F' for female).
        noise (int): The level of noise to be added to the voice data.
        tune_pitch (int): Adjustment to the mean pitch.
        tune_pitch_sd (int): Adjustment to the pitch standard deviation.
        _pitch_mean (int): Mean pitch value.
        _pitch_sd (int): Pitch standard deviation value.
        __data (numpy.ndarray): Array to store the generated voice data.
    """

    PITCH_MEANS = {"M": 110, "F": 190}  # Mean pitch values for male and female
    PITCH_STANDARD_DEVIATION = {
        "M": 50,
        "F": 80,
    }  # Pitch standard deviation for male and female

    def __init__(
        self, duration=300, gender="M", noise=40, tune_pitch=0, tune_pitch_sd=0
    ) -> None:
        """
        Initializes the VoiceDataGenerator object.

        Args:
            duration (int): The duration of the voice data in 1/10 seconds.
            gender (str): The gender of the voice data ('M' for male, all else will be treated as female).
            noise (int): The level of noise to be added to the voice data.
            tune_pitch (int): Adjustment to the mean pitch for relatively higher or lower individuals.
            tune_pitch_sd (int): Adjustment to the pitch standard deviation.
        """
        self.duration = duration
        self.gender = gender if gender in ("M", "F") else "F"
        self.tune_pitch = tune_pitch
        self.tune_pitch_sd = tune_pitch_sd
        self._pitch_mean = (
            VoiceDataGenerator.PITCH_MEANS.get(self.gender) + self.tune_pitch
        )
        self._pitch_sd = (
            VoiceDataGenerator.PITCH_STANDARD_DEVIATION.get(self.gender)
            + self.tune_pitch_sd
        )
        self.noise = noise
        self.__data = self.generate_data()

    @property
    def data(self):
        """Getter method for the voice data."""
        return self.__data

    def generate_data(self):
        """Generates synthetic voice data."""
        x = np.arange(0, self.duration)
        y = self._talk_flow(self.duration)
        return np.column_stack((x, y))

    def _skip_invert(self, ls):
        """Inverts every second value of the input list."""
        ls = np.array(ls)
        ls[::2] *= -1
        return ls

    def _talk_flow(self, duration):
        """
        Simulates the flow of talking.
        Args:
            duration (int): The duration of the voice data.
        Returns:
            list: List of frequencies.
        """
        frequencies = []
        talking = self._normal() > 0.5
        while duration > 0:
            elapse = round(self._normal() * 90 + 10 if talking else self._normal() * 60)
            elapse = duration if elapse > duration else elapse
            frequencies.extend(
                self._sentence(elapse) if talking else self._silence(elapse)
            )
            duration -= elapse
            talking = not talking
        return frequencies

    def _sentence(self, duration):
        """
        Simulates a sentence being spoken.
        Args:
            duration (int): The duration of the sentence.
        Returns:
            list: List of frequencies.
        """
        frequencies = []
        while duration > 0:
            elapse = round((self._normal() + 0.5) * 1.5)
            if elapse > duration:
                elapse = duration
            frequencies.extend(self._word(elapse))
            duration -= elapse
        return frequencies

    def _word(self, duration):
        """
        Simulates a word being spoken.
        Args:
            duration (int): The duration of the word.
        Returns:
            list: List of frequencies.
        """
        return [self._gauss(self._pitch_mean, self._pitch_sd) for _ in range(duration)]

    def _silence(self, duration):
        """
        Simulates a period of silence.
        Args:
            duration (int): The duration of the silence.
        Returns:
            list: List of frequencies.
        """
        return [round(self._normal() * self.noise) for _ in range(duration)]

    def _gauss(self, main, sd):
        """
        Generates a random value from a Gaussian distribution.
        Args:
            main (int): Mean value.
            sd (int): Standard deviation.
        Returns:
            float: Random value from the Gaussian distribution.
        """
        return random.gauss(main, sd)

    def _normal(self):
        """Generates a random value from a uniform distribution."""
        return random.random()

    def plot(self, reflection=True):
        """
        Plots the voice data.
        Args:
            reflection (bool): Whether to reflect the voice data around the x-axis. Default is True.
        Returns:
            None
        """
        x = self.data[:, 0]
        y = self.data[:, 1]
        plt.figure(figsize=(15, 4))
        plt.title("Voice Frequency")
        plt.xlabel("Time (1/10 seconds)")
        plt.ylabel("Pitch (HZ)")
        plt.text(
            0.025,
            0.95,
            f"Gender: {self.gender}\nPitch Mean: {self._pitch_mean}\nPitch SD: {self._pitch_sd}",
            transform=plt.gca().transAxes,
            ha="left",
            va="top",
        )
        if reflection:
            y = self._skip_invert(y)
            plt.ylim(-self._pitch_mean * 4, self._pitch_mean * 4)
        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    # set parameters you want, or leave default
    voice_generator = VoiceDataGenerator(gender="ddd")
    print(voice_generator.data)  # print the data.
    voice_generator.plot(False)  # plot the data, reflection is shown in default
