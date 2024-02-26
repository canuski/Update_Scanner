import win32com.client
import requests


def check_windows_updates():
    update_session = win32com.client.Dispatch('Microsoft.Update.Session')
    update_searcher = update_session.CreateUpdateSearcher()
    search_result = update_searcher.Search("IsInstalled=0")

    if search_result.Updates.Count == 0:
        print("No Windows updates available.")
    else:
        print("Windows updates available:")
        for update in search_result.Updates:
            print(update.Title)


def main():
    print("Checking for updates...")
    print("\nWindows Updates:")
    check_windows_updates()


if __name__ == "__main__":
    main()
