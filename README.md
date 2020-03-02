# song-info
Displays artist and name of the song being played currently.

Uses [Last.fm](https://www.last.fm/) and its [API](https://www.last.fm/api/) for getting information on song currently played on your device.

Output can be shown for example in a status bar on your desktop such as [Polybar](https://polybar.github.io/):

[!polybar example](../master/polybar_song_info.png)

## Dependencies
Python 3

## Last.fm
You need to have 
1) an [account](https://www.last.fm/join) for Last.fm, 
2) an [API-key](https://www.last.fm/api/), 
3) your music playing application set to enable scrobbling to Last.fm.

Set your API-key and username to `data/data.json` file and execute the `song-info.py` file.

## Polybar
For showing output on Polybar, add following module to your Polybar config file:
```
[module/song_info]
type = custom/script
exec = "python $HOME/.scripts/song_info.py"
tail = true
format = <label>
format-prefix = " "
format-prefix-foreground = ${colors.foreground}
label = %output:0:50%
```
And add "song_info" to "modules" part of the polybar you want the output to be shown on, e.g:

`modules-center = song_info`

