import os
import shutil


def organize_jpg_files(source_folder):
    """
    Finds all JPG files in the source folder and moves them
    into an automatically created destination folder.
    """

    # Check whether source folder exists
    if not os.path.isdir(source_folder):
        print("\n❌ Error: Source folder does not exist.")
        return

    # Create destination folder automatically
    destination_folder = os.path.join(
        os.path.dirname(source_folder),
        "destination_folder"
    )

    os.makedirs(destination_folder, exist_ok=True)

    print("\n🔍 Searching for JPG files...")
    print("------------------------------------")

    moved_count = 0

    # Read files from source folder
    for filename in os.listdir(source_folder):

        source_path = os.path.join(source_folder, filename)

        # Process files only
        if not os.path.isfile(source_path):
            continue

        # Check for JPG/JPEG files
        if not filename.lower().endswith((".jpg", ".jpeg")):
            continue

        destination_path = os.path.join(
            destination_folder,
            filename
        )

        # Handle duplicate filenames
        if os.path.exists(destination_path):

            name, extension = os.path.splitext(filename)

            counter = 1

            while True:
                new_filename = f"{name}_{counter}{extension}"
                new_destination = os.path.join(
                    destination_folder,
                    new_filename
                )

                if not os.path.exists(new_destination):
                    destination_path = new_destination
                    filename = new_filename
                    break

                counter += 1

        try:
            # Move file
            shutil.move(source_path, destination_path)

            print(f"✅ Moved: {filename}")
            moved_count += 1

        except PermissionError:
            print(f"❌ Permission denied: {filename}")

        except OSError as error:
            print(f"❌ Could not move {filename}: {error}")

    print("------------------------------------")
    print("           TASK COMPLETED")
    print("------------------------------------")
    print(f"📸 JPG/JPEG files moved: {moved_count}")
    print(f"📁 Destination: {destination_folder}")
    print("------------------------------------")


def main():

    print("====================================")
    print("        JPG FILE ORGANIZER")
    print("====================================")
    print()
    print("This program automatically finds")
    print("JPG/JPEG images and moves them into")
    print("a destination folder.")
    print()

    # Ask user for source folder
    source_folder = input(
        "Enter source folder path: "
    ).strip().strip('"')

    # Run organizer
    organize_jpg_files(source_folder)


if __name__ == "__main__":
    main()