# Pomodoro

A small desktop Pomodoro timer built with Python and Tkinter. The app displays the current interval, a countdown, and completed-cycle marks.

## Features

- 25-minute work intervals.
- 5-minute short breaks.
- A 20-minute long break after four work intervals.
- The timer waits for you to press **Start** before beginning the next interval.
- **Reset** clears the countdown and cycle counter.

Interval lengths are configured by constants in `pomodoro/app.py`.

## Tkinter

The interface is built with Tkinter, Python's standard GUI toolkit. It uses `Tk` for the main window, `Label`, `Button`, and `Canvas` for interface elements, and `mainloop()` to process events.

The countdown is scheduled with `window.after()`. This lets Tkinter continue handling input and redrawing the window while the timer runs. Tkinter is usually included with standard Python installations, so no extra Python package is needed to run from source. On some Linux distributions, Tcl/Tk must be installed separately as a system package.

## Requirements

- Python 3
- Tkinter/Tcl-Tk

No third-party Python packages are required to run the source code.

To check whether Tkinter is available, run:

```bash
python -m tkinter
```

If a Tkinter test window opens, the environment is ready.

## Run from source

From the project root, run:

```bash
python main.py
```

On systems where `python` does not point to Python 3, use `python3 main.py`.

## Build for Windows

Build on Windows with Python and Tkinter installed:

```powershell
python -m pip install pyinstaller
pyinstaller main.spec
```

PyInstaller writes temporary files to `build/` and the finished executable to `dist/`. These directories can be deleted after the build; PyInstaller recreates them when needed. The `main.spec` configuration includes the tomato image in the bundle.

## Project structure

```text
.
├── assets/
│   └── tomato.png       # Image used by the interface
├── pomodoro/
│   ├── __init__.py
│   └── app.py           # Tkinter window and timer logic
├── main.py              # Entry point
├── main.spec            # PyInstaller configuration
├── pomodoro.exe         # Prebuilt Windows executable
└── README.md
```

The root-level `tomato.png` is kept for compatibility with the previously built `pomodoro.exe`; the Python application uses the image in `assets/`.
