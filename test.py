import curses

def main(stdscr):
    # Turn off echoing of keys, and enter cbreak mode,
    # where keys are instantly available without waiting for Enter key
    curses.cbreak()
    stdscr.keypad(True)

    # Clear the screen
    stdscr.clear()

    # Initial options
    options = ["Test Option 1", "Test Option 2"]
    current_option = 0

    while True:
        stdscr.clear()

        # Display options
        for i, option in enumerate(options):
            if i == current_option:
                stdscr.addstr(i, 0, ">> " + option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, "   " + option)

        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_option = (current_option - 1) % len(options)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(options)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # If Enter key is pressed, go into sub-menu
            if current_option == 0:  # Test Option 1
                sub_menu(stdscr)

def sub_menu(stdscr):
    sub_options = ["Testing 1", "Testing 2", "Testing 3", "Testing 4"]
    selected = [False] * len(sub_options)
    current_option = 0

    while True:
        stdscr.clear()

        # Display sub-options with checkboxes
        for i, option in enumerate(sub_options):
            checkbox = "[X] " if selected[i] else "[ ] "
            if i == current_option:
                stdscr.addstr(i, 0, ">> " + checkbox + option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, "   " + checkbox + option)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_option = (current_option - 1) % len(sub_options)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(sub_options)
        elif key == ord(' '):  # Spacebar to toggle selection
            selected[current_option] = not selected[current_option]
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # If Enter key is pressed, confirm selections
            confirm_selections(stdscr, sub_options, selected)
            break
        elif key == curses.KEY_LEFT:
            # If left arrow key is pressed, return to main menu
            break

def confirm_selections(stdscr, sub_options, selected):
    stdscr.clear()
    stdscr.addstr(0, 0, "You selected:")
    for option, is_selected in zip(sub_options, selected):
        if is_selected:
            stdscr.addstr(1, 0, "- " + option)
            stdscr.refresh()
            stdscr.getch()  # Wait for a key press

if __name__ == "__main__":
    curses.wrapper(main)
