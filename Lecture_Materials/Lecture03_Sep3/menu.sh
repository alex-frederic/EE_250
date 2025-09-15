#!/bin/bash

while true; do
    clear
    echo "=============================="
    echo "   Simple Terminal Menu"
    echo "=============================="
    echo "1. Show current date and time"
    echo "2. Show calendar"
    echo "3. Show system uptime and load"
    echo "4. Show disk usage"
    echo "5. Quit"
    echo "=============================="
    read -p "Enter your choice [1-5]: " choice

    case $choice in
        1) 
            echo "Current date and time:"
            date
            ;;
        2)
            echo "Calendar:"
            cal
            ;;
        3)
            echo "System uptime and load:"
            uptime
            ;;
        4)
            echo "Disk usage:"
            df -h
            ;;
        5)
            echo "Exiting... Goodbye!"
            break
            ;;
        *)
            echo "Invalid choice. Please select 1–5."
            ;;
    esac
    echo
    read -p "Press Enter to return to menu..."
done
