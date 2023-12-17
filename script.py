import requests
import zipfile
import os
import os
import shutil
import requests

version = input("Enter the version of the mod you want to download: ")
url = "https://mediafilez.forgecdn.net/files/4824/716/§4§l§o§kaaa§6§l§oCustomTotem§a" + version + "§4§l§o§kaaa.zip"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a directory for the extracted files
    directory = "Custom Totem"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the downloaded zip file
    zip_file_path = os.path.join(directory, 'Custom Totem.zip')
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)

    # Unzip the downloaded file to the specified directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(directory)

    os.remove(zip_file_path)

    username = input("Enter the username: ")
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    # Define the current directory
    current_directory = os.getcwd()

    if response.status_code == 200:
        # Get the ID from the response
        user_id = response.json()["id"]

        # Construct the URL for downloading the image
        import urllib.request

        image_url = f"https://mc-heads.net/skin/{user_id}"
        image_file_path = os.path.join(current_directory, 'skin.png')

        # Download the image file
        urllib.request.urlretrieve(image_url, image_file_path)

        # Send a GET request to the image URL
        image_response = requests.get(image_url)


    # Find the path of the skin.png file in the current directory
    current_directory = os.getcwd()
    skin_file_path = os.path.join(current_directory, 'skin.png')

    # Define the destination directory
    destination_directory = os.path.join(current_directory, 'Custom Totem', 'assets', 'minecraft', 'textures', 'item')

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Move the skin.png file to the destination directory and rename it to "Totem.png"
    new_skin_file_path = os.path.join(destination_directory, 'totem_of_undying.png')
    shutil.copy(skin_file_path, new_skin_file_path)


    # Rezip the Custom Totem folder
    new_zip_file_path = os.path.join(current_directory, 'Custom Totem.zip')
    with zipfile.ZipFile(new_zip_file_path, 'w') as zip_ref:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, directory))

    # Delete the Custom Totem folder
    shutil.rmtree(directory)

    # Delete the skin.png file
    os.remove(skin_file_path)

    





