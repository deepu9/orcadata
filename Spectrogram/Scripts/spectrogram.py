import soundfile as sf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path


def get_folder_path(folder: list) -> Path:
    return Path.cwd().joinpath(*folder)

plot_path = get_folder_path(["Spectrogram", "Plots"])
sounds_path = get_folder_path(["Sounds", "catalog", "flac"])
flac_files = [f for f in sounds_path.iterdir() if f.is_file()]


for file in flac_files:
    data, samplerate = sf.read(file)
    filename = file.stem # Returns name of the file without file type.
    filenumber = filename.split(sep="-")[1]
    
    fig, ax = plt.subplots(1, 1)
    ax.specgram(data, Fs=samplerate, NFFT=1024)
    
    # Rescale y axis labels from Hz to KHz
    ticks_y = ticker.FuncFormatter(lambda x: f"{(x/1000):g}")
    ax.yaxis.set_major_formatter(ticks_y)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Frequency (kHz)")
    ax.set_title(f"Call {filenumber}")
    
    plt.savefig(plot_path.joinpath(f"{filename}.png"))