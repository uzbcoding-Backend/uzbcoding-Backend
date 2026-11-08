<div align="center">

<img src="./assets/matrix-hero.svg" alt="Animated Matrix code rain around neon UZBCODING BACKEND banner" width="100%" />

<br>

**`[ ACCESS GRANTED ]`** &nbsp; **`[ SYSTEM ONLINE ]`** &nbsp; **`[ DEV MODE ACTIVE ]`**

[![Python](https://img.shields.io/badge/PYTHON-BACKEND-00120a?style=for-the-badge&logo=python&logoColor=00ff9a&labelColor=072416&color=08b96b)](https://github.com/uzbcoding-Backend?tab=repositories)
[![Open Source](https://img.shields.io/badge/OPEN_SOURCE-PROJECTS-00120a?style=for-the-badge&logo=github&logoColor=00ff9a&labelColor=072416&color=08b96b)](https://github.com/uzbcoding-Backend?tab=repositories)
[![Terminal](https://img.shields.io/badge/MATRIX_MODE-ON-00120a?style=for-the-badge&logo=gnubash&logoColor=00ff9a&labelColor=072416&color=08b96b)](https://github.com/uzbcoding-Backend/blob/main/matrix_rain.py)

</div>

## `> INITIALIZE // DEVELOPER PROFILE`

<img src="./assets/matrix-console.svg" alt="Terminal console showing a green neon Matrix engine" width="100%" />

```console
dev@uzbcoding:~$ whoami
uzbcoding-Backend
dev@uzbcoding:~$ cat mission.txt
Learn. Build. Debug. Improve. Repeat.
dev@uzbcoding:~$ echo $CURRENT_STATUS
[ ONLINE ] [ PYTHON ] [ BACKEND ] [ WEB DEVELOPMENT ]
```

I'm **Mustafo**, an aspiring developer exploring **Python**, **backend engineering**, **web applications**, and creative tools. I enjoy building real projects, breaking down difficult ideas, and refining every new version.

## `> NAVIGATION // CYBER CONTROL PANEL`

<div align="center">

<a href="https://github.com/uzbcoding-Backend?tab=repositories"><img src="./assets/btn-repos.svg" alt="View all GitHub repositories" width="31%" /></a>
<a href="https://github.com/uzbcoding-Backend/test"><img src="./assets/btn-lab.svg" alt="Explore CodeForge project lab" width="31%" /></a>
<a href="https://github.com/uzbcoding-Backend"><img src="./assets/btn-follow.svg" alt="Visit GitHub profile to follow" width="31%" /></a>

</div>

## `> EXECUTE // THE MATRIX ENGINE`

**A real, runnable terminal animation, made with Python and the standard library.** No hacking, no external services — just moving green characters, flowing streams and terminal rendering.

```python
from dataclasses import dataclass
import random

@dataclass
class CodeStream:
    column: int
    head: float
    speed: float
    length: int

    def advance(self, delta: float, height: int) -> None:
        self.head += self.speed * delta
        if self.head - self.length > height:
            self.head = -random.randint(1, height)
            self.speed = random.uniform(8, 29)

def illuminate(column: int, head: int, length: int, height: int):
    """Yield visible characters from one moving stream."""
    glyphs = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&*"
    for tail in range(length):
        row = head - tail
        if 0 <= row < height:
            intensity = "HEAD" if tail == 0 else "GLOW" if tail < 3 else "DIM"
            yield row, column, random.choice(glyphs), intensity

print("[ MATRIX CORE ONLINE // BUILD SOMETHING GREAT ]")
```

<div align="center">

[![VIEW FULL SOURCE](https://img.shields.io/badge/%3E_VIEW_FULL_PYTHON_SOURCE-00db83?style=for-the-badge&logo=python&logoColor=001009&labelColor=062618)](./matrix_rain.py)

</div>

**Run the full animation locally:**

```bash
python matrix_rain.py --seconds 20 --fps 24 --density 0.58
```

> The SVG banner contains animated Matrix-style glyphs. Some GitHub viewers or reduced-motion settings may show a static frame instead.

## `> LOAD MODULES // TECH STACK`

<div align="center">

![Python](https://img.shields.io/badge/Python-06190f?style=for-the-badge&logo=python&logoColor=00ff99)
![Java](https://img.shields.io/badge/Java-Learning-06190f?style=for-the-badge&logo=openjdk&logoColor=00ff99)
![JavaScript](https://img.shields.io/badge/JavaScript-06190f?style=for-the-badge&logo=javascript&logoColor=00ff99)
![HTML5](https://img.shields.io/badge/HTML5-06190f?style=for-the-badge&logo=html5&logoColor=00ff99)
![CSS3](https://img.shields.io/badge/CSS3-06190f?style=for-the-badge&logo=css3&logoColor=00ff99)
![Git](https://img.shields.io/badge/Git-06190f?style=for-the-badge&logo=git&logoColor=00ff99)
![GitHub](https://img.shields.io/badge/GitHub-06190f?style=for-the-badge&logo=github&logoColor=00ff99)
![VS_Code](https://img.shields.io/badge/VS_Code-06190f?style=for-the-badge&logo=visualstudiocode&logoColor=00ff99)

</div>

## `> LS PROJECTS/ --ALL`

| Project | Mission | Source |
|:--|:--|:--:|
| **Java Mastery Course** | Java lessons, examples and quizzes | [OPEN](https://github.com/uzbcoding-Backend/Java-Mastery-Course) |
| **Study Planner Pro** | Organize subjects, tasks and deadlines | [OPEN](https://github.com/uzbcoding-Backend/Study-Planner-Pro) |
| **NOVA Shop** | Demo online shop with a functional cart | [OPEN](https://github.com/uzbcoding-Backend/NOVA-Shop) |
| **Urban Plate** | Restaurant menu and demo reservations | [OPEN](https://github.com/uzbcoding-Backend/Restuarant) |
| **Python Site** | Python practice and learning platform | [OPEN](https://github.com/uzbcoding-Backend/python-sayt) |
| **Game HTML** | Interactive browser game | [OPEN](https://github.com/uzbcoding-Backend/Game-HTML) |
| **CodeForge Lab** | Seven developer mini-projects | [OPEN](https://github.com/uzbcoding-Backend/test) |
| **VEXOR** | Frontend design experiments | [OPEN](https://github.com/uzbcoding-Backend/vexor) |

## `> MONITOR // LIVE SIGNALS`

<div align="center">

![Followers](https://img.shields.io/github/followers/uzbcoding-Backend?style=for-the-badge&logo=github&label=FOLLOWERS&labelColor=06150d&color=079658)
![Stars](https://img.shields.io/github/stars/uzbcoding-Backend?style=for-the-badge&logo=github&label=STARS&labelColor=06150d&color=079658)

**`sudo imagination --unlimited`**

<sub>⚡ Cyber visuals • Original code • Real projects • Always learning</sub>

</div>
