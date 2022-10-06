import logging
import os
import urllib.request

from tqdm import tqdm

logging.basicConfig(level=logging.INFO)


class DownloadProgressbar(tqdm):
    def update_to(self, block=1, block_size=1, total_size=None):
        if total_size is not None:
            self.total = total_size
        self.update(block * block_size - self.n)


def download_raw_data(url: str, path_to_data: str):
    with DownloadProgressbar(
        unit="B", unit_scale=True, miniters=1, desc=url.split("/")[-1]
    ) as t_bar:
        urllib.request.urlretrieve(url, filename=path_to_data, reporthook=t_bar.update_to)


def setup_raw_data(url: str, path_to_data: str, file_name: str):
    if os.path.isdir(path_to_data):
        if os.path.isfile(f"data/{file_name}"):
            logging.info("Found the correct data.")
            return
        else:
            logging.info(
                "Data folder found, but it does not contain the right data. Downloading..."
            )
    else:
        logging.info("Data folder not found. Downloading...")
        print("Data not found. Downloading...")

    os.makedirs(path_to_data, exist_ok=True)
    # Download raw data
    output_file = os.path.join(path_to_data, file_name)
    download_raw_data(url, output_file)

    # Check if all files are present
    logging.info("Checking if all files are present...")
    if os.path.isfile(f"data/{file_name}"):
        logging.info("All files are present")
    else:
        raise FileNotFoundError("Something went wrong. Please download the file manually. ")


def main():
    return ()


if __name__ == "__main__":
    main()
