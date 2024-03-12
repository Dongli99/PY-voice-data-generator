# Voice Data Generator

Voice Data Generator is a Python tool for simulating voice data with customizable parameters such as pitch, duration, and noise. This tool is designed for various applications, including speech analysis, machine learning training data generation, and audio signal processing experimentation.

## Features

- Generate synthetic voice data with specified pitch, duration, and noise levels.
- Visualize generated voice frequency patterns using matplotlib.
- Easily customizable parameters for different voice characteristics and analysis needs.

## Usage

- Install the required dependencies:

```bash
   pip install numpy matplotlib
```

- Clone the repository:

```bash
   git clone https://github.com/Dongli99/PY-voice-data-generator.git
```

- Navigate to the project directory:

```bash
cd PY-voice-data-generator.git
```

- Navigate to the project directory:

```bash
cd PY-voice-data-generator.git
```

- Run the script:

```bash
python main.py
```

## Customize Settings

### Set VoiceDataGenerator

- `duration` (int, default=300): The duration of the voice data in 1/10 seconds.
- `gender` (str, default="M"): The gender of the voice data ('M' for male, all else will be treated as female).
- `noise` (int, default=40): The level of noise to be added to the voice data.
- `tune_pitch` (int, default=0): Adjustment to the mean pitch.
- `tune_pitch_sd` (int, default=0): Adjustment to the pitch standard deviation.

#### Example

```python
voice_generator = VoiceDataGenerator(duration=400, gender="F")
print(voice_generator.data)  # print the data.
voice_generator.plot()  # plot the data, reflection is shown in default
```

![example1](example1.png)

### Set Reflection on Plot

- reflection (bool, default=True): Whether to reflect the voice data around the x-axis.

#### Example

```python
voice_generator = VoiceDataGenerator()
print(voice_generator.data) 
voice_generator.plot(False)
```

![example2](example2.png)
