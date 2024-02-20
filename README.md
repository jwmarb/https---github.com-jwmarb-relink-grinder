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

Upgrading equipment is **expensive**, and it can take days to fully maximize your equipment. Since not everyone has time to grind, AFK farming is one of the methods to get upgrade materials. However, Cygames has an anti-afk service in the game that prompts the user, once they have completed 10 runs, whether they want to continue playing a quest. If no response is provided, the user will be sent back to the lobby. Because of this, **afk farming is only limited to 10 runs.**

_Relink Grinder_ allows the user to afk for more than 10 runs by automatically detecting the anti-AFK prompt and continuing the quest without user input required.

Additionally, _Relink Grinder_ automatically attempts to revive the player if they are down to prevent the quest from failing, thus reducing the likelihood of a run failing.

## How To Use

### In-game Prerequisites

1. At least 3 CPU party members capable of doing a run
2. Max defence/HP build on your player character

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

Before running the program, make sure **Granblue Fantasy: Relink** is opened, and navigate to any quest of your choice (make sure your CPU team is capable of completing it)

You will have to complete the quest first. Once you have completed the quest, you should be in the quest results screen. Enable `Repeat Quest`, then activate the afk script in the same terminal:

```sh
make run main=main
```

You should see something like:

```
[00:00:00] Runs completed: 1
```

When this happens, you should see your cursor disappear and the **Granblue Fantasy: Relink** window be focused. This means that the afk script is now running.

To end the script, press `ESC` on your keyboard
