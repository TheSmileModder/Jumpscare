# Jumpscare

A program that randomly triggers a fullscreen Jumpscare on your PC with your chosen intervals.


## Installation
**1. Clone/download from releases**

**2. Install dependencies** 
```bash
pip install -r requirements.txt
```

## Adding Jumpscare
Each jumpscare **needs** it own folder inside the `jumpscares` folder. The folder **must** contain `1 image` and `1 audio` file.

```
jumpscares/
    ButterDog/
        image.png
        audio.mp3
    Template/
        image.jpg
        audio.wav
    .../
```

*Supported image formates right now are*: `.png` `.jpg` `.jpeg` `.bmp` `.gif`

*Supported audio formates right now are*: `.wav` `.mp3` `.ogg`

The porgram will automatically search valid folders and picks a random one each time.



## Config

Edit `config.json` to change the settings:

```
{
    "screen_width": 1920,
    "screen_height": 1080,
    "jumpscare_folder": "jumpscares",
    "min_wait_seconds": 60,
    "max_wait_seconds": 600,
    "stop_global_hotkey": "ctrl+shift+q"
}
```


| Settings | What it does |
| ---- | ---- |
| `screen_width`/`screen_height` | Resolution of your monitor |       
| `jumpscare_folder` | Path to the folder containing your Jumpscares | 
| `min_wait_seconds` | Minimum time between jumpscares |
| `max_wait_seconds` | Maximum time between jumpscares |
| `stop_global_hotkey` | Keyboard shortcut to stop the programm ***(doesnt work on linux)*** |

