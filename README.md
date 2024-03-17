<h1 align="center">
  Relink Grinder
</h1>
<h2 align="center">
An AFK Script for <em>Granblue Fantasy: Relink</em>
</h2>

**NOTE**: This is only compatible with Windows

## What is this?

_Relink Grinder_ is an afk script for the video game, [Granblue Fantasy: Relink](https://store.steampowered.com/app/881020/Granblue_Fantasy_Relink/), a JRPG by Cygames. This game re-introduces many characters from the original game, [Granblue Fantasy](https://granbluefantasy.jp/en/), except for the fact that this is not a gacha. Every character can be customized to have different equipments and loadouts, most of which are obtained through boss drops. Every equipment requires materials to upgrade, and unfortunately, these upgrade materials are only obtainable through boss fights.

## Why use this?

Upgrading equipment is **expensive**, and it can take days to fully maximize your equipment. Since not everyone has time
to grind, AFK farming is one of the methods to get upgrade materials. However, Cygames has an anti-afk service in the
game that prompts the user, once they have completed 10 runs, whether they want to continue playing a quest. If no
response is provided, the user will be sent back to the lobby. Because of this, **true afk farming is only limited to 10
runs** and user intervention is required to skip the anti-afk prompt.

## Program features

- Quests
  - Continues quest after 10 runs, bypassing the user intervention requirement
  - Performs link attack whenever possible
  - Attempts to revive the player's character when they are below 0 HP
- Siero's Knickknack Shack
  - Automatic sigil transmutation with a way to restock knickknack vouchers
    - Restocking knickknack vouchers can be done via through **Trade Sigils** or **Trade Wrightstones**

## How To Use

There is no executable, so this is required:

### Requirements

1. [python](https://www.python.org/downloads/) 3.10 or better
2. [Make](https://www.gnu.org/software/make/)
3. [git](https://git-scm.com/downloads)

Open a terminal of your choice and clone this repository (a folder will be created automatically with the name of this repository)

```sh
git clone https://github.com/jwmarb/relink-grinder.git
```

Using the same terminal, navigate to it and run `make` to install dependencies:

```sh
cd relink-grinder && make
```

After this, you can run the following scripts below:

### Quest Farming

#### In-game Prerequisites

1. At least 3 CPU party members capable of doing a run
2. Max defence/HP build on your player character

Before running this script, make sure **Granblue Fantasy: Relink** is opened, and navigate to any quest of your choice (make sure your CPU team is capable of completing it)

When you have selected a quest and are transitioning into it, you can start the program like so:

```sh
make run main=main
```

When the quest completes, you should see something a timestamp followed by the # of runs completed, which can look like:

```
[00:01:24] Runs completed: 1
```

When this happens, you should see your cursor disappear and the **Granblue Fantasy: Relink** window be focused. This means that the afk script is now running.

To end the script, press `ESC` on your keyboard

### Transmuting Sigils

#### In-game Prerequisites

1. Knickknack Vouchers
2. Wrightstones or sigils that you are willing to trade for

Go to **Siero's Knickknack Shack**, and before you can run the script, you must set up your navigation pathing
so the scripts work properly.

First, navigate into **Knickknack Vouchers**, then you will see three tabs you can navigate into: `Trade Treasure`,
`Trade Sigils`, `Trade Wrightstones`

For now, trading treasures is not supported. Navigate into either `Trade Sigils` or `Trade Wrighstones`. Follow the
instructions below for the specific tab:

- `Trade Sigils`

  1. Navigate into `Sort & Filter/Trade All`
  2. Switch to `Trade All` tab
  3. Select categories that match the sigils you want to trade for (do not trade)
  4. Go back to **Siero's Knickknack Shack** main screen without manipulating the selected navigation paths. (If you
     exit **Siero's Knickknack Shack** accidentally, you must start over and repeat)

- `Trade Wrightstones`
  1. **NOTE**: If you want to trade every wrightstone you have, you can go straight to step iv. The steps below are
     simply for filtering out wrightstones you do not want to trade.
  2. Navigate into `Sort & Filter`
  3. Under the `Filter` tab, select categories for the wrightstones you want to trade for. (ex. If you want to trade
     every wrightstone except the ones with 3 stats in it, simply select `1` and `2` for **Number of Traits**)
  4. Once you have set your filters, go back to **Siero's Knickknack Shack** main screen without manipulating the
     selected navigation paths. (If you exit **Siero's Knickknack Shack** accidentally, you must start over and repeat)

While you're at the main screen of **Siero's Knickknack Shack**, navigate into **Transmute Sigils** then select the
desired transmutation level. Once you selected (aka highlighted) a transmutation level, you can start the script by
running the following (while in the root directory of this repository):

```sh
make run main=transmute_sigils
```

Then select whichever option, and the script will run. The script will automatically stop when you have no more to trade
for in that selected option.
