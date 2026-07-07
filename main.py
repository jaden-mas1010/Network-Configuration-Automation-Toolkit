"""
main.py

Entry point for the Network Configuration Automation Toolkit.
"""

from modes.interactive import interactive_mode
from modes.json_mode import json_mode
from modes.excel_mode import excel_mode


def display_menu() -> None:
    """
    Display the main menu.
    """

    print("\n" + "=" * 50)
    print(" Network Configuration Automation Toolkit")
    print("=" * 50)

    print("1. Interactive Mode")
    print("2. JSON Mode")
    print("3. Excel Mode")
    print("4. Exit")


def main() -> None:
    """
    Main application loop.
    """

    while True:

        display_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            interactive_mode()

        elif choice == "2":
            json_mode()

        elif choice == "3":
            excel_mode()

        elif choice == "4":
            print("\nThank you for using the toolkit.")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()