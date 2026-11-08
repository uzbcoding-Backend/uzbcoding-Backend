#!/usr/bin/env python3
"""Matrix-style terminal rain. A harmless, offline visual demo."""

from __future__ import annotations

import argparse
import random
import shutil
import sys
import time
from dataclasses import dataclass

ESC = "\x1b["
RESET = ESC + "0m"
HEAD = ESC + "1;97m"
BRIGHT = ESC + "1;92m"
GREEN = ESC + "32m"
DIM = ESC + "2;32m"
GLYPHS = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&*+"


@dataclass
class Stream:
    column: int
    head: float
    speed: float
    length: int

    def tick(self, dt: float, height: int) -> None:
        self.head += self.speed * dt
        if self.head - self.length > height:
            self.head = -random.randrange(1, height + 1)
            self.speed = random.uniform(8, 29)
            self.length = random.randrange(5, max(6, height // 2 + 1))


class MatrixEngine:
    def __init__(self, fps: int = 24, density: float = 0.58) -> None:
        self.fps = fps
        self.density = density
        self.width, self.height = self.screen_size()
        self.streams = self.make_streams()

    @staticmethod
    def screen_size() -> tuple[int, int]:
        screen = shutil.get_terminal_size(fallback=(80, 24))
        return max(20, screen.columns), max(10, screen.lines - 2)

    def make_streams(self) -> list[Stream]:
        return [
            Stream(x, random.uniform(-self.height, self.height),
                   random.uniform(8, 29), random.randint(5, max(6, self.height // 2)))
            for x in range(self.width)
            if random.random() < self.density
        ]

    def draw(self, dt: float) -> str:
        width, height = self.screen_size()
        if (width, height) != (self.width, self.height):
            self.width, self.height = width, height
            self.streams = self.make_streams()
        cells = [[" " for _ in range(width)] for _ in range(height)]
        styles = [[GREEN for _ in range(width)] for _ in range(height)]
        for stream in self.streams:
            stream.tick(dt, height)
            for trail in range(stream.length):
                y = int(stream.head) - trail
                if 0 <= y < height:
                    cells[y][stream.column] = random.choice(GLYPHS)
                    styles[y][stream.column] = HEAD if trail == 0 else (BRIGHT if trail < 3 else DIM)
        label = "[ UZBCODING_BACKEND // MATRIX ENGINE ONLINE ]"
        if width >= len(label) + 4 and height > 6:
            y = height // 2
            x = (width - len(label)) // 2
            for j, ch in enumerate(label):
                cells[y][x + j] = ch
                styles[y][x + j] = HEAD
        lines = []
        for row, colors in zip(cells, styles):
            parts = []
            current = None
            for ch, color in zip(row, colors):
                if color != current:
                    parts.append(color)
                    current = color
                parts.append(ch)
            lines.append("".join(parts) + RESET)
        return ESC + "H" + "\n".join(lines)

    def run(self, seconds: float) -> None:
        if not sys.stdout.isatty():
            print("Run this program inside a terminal to see Matrix rain.")
            return
        start = time.monotonic()
        last = start
        sys.stdout.write(ESC + "?25l" + ESC + "2J")
        sys.stdout.flush()
        try:
            while seconds == 0 or time.monotonic() - start < seconds:
                now = time.monotonic()
                sys.stdout.write(self.draw(now - last))
                sys.stdout.flush()
                last = now
                time.sleep(1 / self.fps)
        except KeyboardInterrupt:
            pass
        finally:
            sys.stdout.write(RESET + ESC + "?25h" + ESC + "2J" + ESC + "H")
            sys.stdout.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline neon Matrix terminal animation")
    parser.add_argument("--seconds", type=float, default=20,
                        help="Duration in seconds (0 means until Ctrl+C)")
    parser.add_argument("--fps", type=int, default=24, help="Frames per second: 1..60")
    parser.add_argument("--density", type=float, default=0.58,
                        help="Stream density: 0.05..1.0")
    args = parser.parse_args()
    if args.seconds < 0 or not 1 <= args.fps <= 60 or not 0.05 <= args.density <= 1:
        parser.error("seconds must be >= 0, fps 1..60, density 0.05..1.0")
    MatrixEngine(args.fps, args.density).run(args.seconds)


if __name__ == "__main__":
    main()
