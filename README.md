# Dangerous Writing App

A minimalist desktop writing application built with Python and Tkinter for macOS.

The idea is simple: keep writing or lose everything. If you stop typing for the selected amount of time, the text is automatically deleted.

## Features

- Minimal distraction-free writing interface
- Automatically deletes the current text after a period of inactivity
- Adjustable inactivity timer from 3 to 15 seconds
- Live word counter
- Save writing as a `.txt` file
- Save button becomes available after reaching 500 words
- Visual countdown progress bar
- Warning state when the timer is close to expiring
- "Text lost!" notification after the writing is deleted
- macOS-friendly interface using Tkinter and system fonts

## How It Works

1. Launch the application.
2. Start typing in the writing area.
3. Every keypress resets the inactivity timer.
4. The progress bar shows how much time remains.
5. If you stop typing for the selected time limit, the application deletes the text.
6. Once the text reaches 500 words, the Save button becomes available.
7. Choose a location to save the text as a `.txt` file.

The default inactivity limit is 5 seconds, but it can be changed using the slider.

## Technologies

- Python 3
- Tkinter
- `time`
- File dialogs
- ttk widgets

## Requirements

- Python 3
- macOS
- Tkinter

No external Python packages are required.

## Running the App

Clone the repository:

```bash
git clone https://github.com/maciek404/dangerous-writing-app.git
cd dangerous-writing-app
```

Run the application:

```bash
python3 main.py
```

Depending on your Python installation, you may need to use:

```bash
python main.py
```

## Project Structure

```text
dangerous-writing-app/
├── main.py
└── README.md
```

## Purpose

This project was created as a Python portfolio project to practice:

- Tkinter GUI development
- Event binding
- Timers and callbacks with `after()`
- Managing application state
- Working with Tkinter widgets
- File saving
- Basic user interface design

## Notes

The application intentionally makes writing risky. Once the inactivity timer expires, the current text is permanently cleared from the application window.

Saved `.txt` files are not affected.

## License

This project is available for personal and educational use.
