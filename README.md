# Bingo maker

- Create bingo sheet by given text
- Send sheet via discord

### Installation

```
pip install -r requirements.txt
```

- Setup `.env` file
  - Follow `.env_sample` to create your `.env` file

### Start

- `Python main.py`

### Config

- in `lib/config`, you can setup different settings.

```
config = {
    "font_name": "font.otf",
    "font_size": 30,
    "font_color": "black",
    "border_size": (5, 5, 5, 5),
    "border_color": "black",
    "image_size": (190, 190),
    "image_color": (195, 195, 195),
}
```

- Put font file you like inside `asset`
- Modify `text_list.txt` in `asset` to make your own unique bingo sheet

### How to use

- Invite the bot with token given in your `.env` file to your guild
- In any channel, use command to draw bingo card
- `$doro` Will draw a bingo card for current user
- User will get the same card until you delete relate file in bingo_sheet folder

### Bingo sheet

![alt text](https://github.com/Hung-Liang/bingo_sheet_maker/blob/master/bingo_sheet/sample.png?raw=true)
