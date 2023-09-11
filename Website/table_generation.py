# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:49:00 2018
@author: kmuss
Modified on Fri Dec 07 23:18:00 2018
@author: scottveirs
"""
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def get_folder_path(folder: list) -> Path:
    return Path.cwd().joinpath(*folder)


sounds_path = get_folder_path(["Sounds", "catalog", "flac"])
flac_files = [f for f in sounds_path.iterdir() if f.is_file()]

htmlpath = get_folder_path(["Website"])
base_URL = "http://www.orcasound.net/data/product/SRKW/call-catalog/no-narration_flac+mp3+ogg+spectrograms"
title_text = "Sound spectrum table"

env = Environment(loader=FileSystemLoader(htmlpath))
template = env.get_template("spectrum_template.html")
data = []

for file in flac_files:
    file_name = file.stem
    heading = file_name.split("-")[1]

    data.append({
        'heading': heading,
        'mp3_url': "/".join([base_URL, "mp3", f"{file_name}.mp3"]),
        'ogg_url': "/".join([base_URL, "ogg", f"{file_name}.ogg"]),
        'spectrogram_url': "/".join([base_URL, "spectrogram-pngs", f"{file_name}.png"]),
        'raw_spectrogram_url': f"http://www.orcasound.net/data/raw/SRKW-Ford-Osborne-tapes/Ford89-SRKW-spectrograms/{heading}.png"
    })

final_html = template.render(**{
    'title': title_text,
    'data': data
})

with open(htmlpath.joinpath("spectrum_comparison.html"), "w") as fh:
    fh.write(final_html)


