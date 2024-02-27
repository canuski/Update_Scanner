import win32com.client
from telegram_sender import send_telegram_msg
import asyncio
from datetime import datetime

# Function to check Windows updates


async def check_windows_updates():
    update_session = win32com.client.Dispatch('Microsoft.Update.Session')
    update_searcher = update_session.CreateUpdateSearcher()
    search_result = update_searcher.Search("IsInstalled=0")

    if search_result.Updates.Count == 0:
        pass
    else:
        message = "Windows updates available:\n"
        # Define a threshold date to filter out older updates
        threshold_date = datetime(2022, 1, 1)  # Example: January 1, 2022
        for update in search_result.Updates:
            # Convert LastDeploymentChangeTime to datetime
            last_change_time_str = str(update.LastDeploymentChangeTime)
            last_change_time_str = last_change_time_str.rsplit(
                '+', 1)[0]  # Remove timezone information
            last_change_time = datetime.strptime(
                last_change_time_str, "%Y-%m-%d %H:%M:%S")
            # Check if the update's release date is after the threshold date
            if last_change_time >= threshold_date:
                title = update.Title
                description = update.Description
                category = update.Categories[0].Name
                message += f"Title: {title}\nDescription: {description}\nCategory: {category}\n"

# Main function


async def main():
    await send_telegram_msg("Checking for Windows updates...")
    await check_windows_updates()

if __name__ == "__main__":
    asyncio.run(main())
