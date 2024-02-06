# Dynamic File Downloader

This project is a dynamic file downloader capable of efficiently downloading large files by utilizing multi-threading and segmented downloading. It allows users to specify the number of segments they want to divide the file into, enabling faster downloads through parallel downloading.

## Features

- **Segmented Downloading**: The downloader divides the file into multiple segments and downloads them simultaneously, increasing download speed.
- **Progress Tracking**: It provides a progress bar for each segment and an overall progress bar to track the download progress.
- **Faster Download**: It downloads the file blazingly fast due to its algorithm.
- **User Input Handling**: Accepts user inputs for the file URL, number of segments, and output file name to provide flexibility and customization.

## Algorithms Used

1. **Multi-threading**: Utilizes Python's `threading` module to implement multi-threading, allowing multiple segments of the file to be downloaded concurrently, thereby reducing download time.
2. **Segmented Downloading**: The file is divided into segments, and each segment is downloaded separately using a separate thread. This approach ensures efficient use of network bandwidth and resources.
3. **Progress Tracking**: Implements progress tracking using the `tqdm` library, which provides a visually appealing progress bar to monitor the download progress of each segment and the overall progress of the file download.

## Usage

1. **Download the Binary Executable**: Download the provided binary executable file (`dynamic_file_downloader`) suitable for your Linux environment.
2. **Run the Executable**: Execute the binary file in your terminal.
   ```bash
   $ ./dynamic_file_downloader
   ```
3. **Provide Inputs**: Enter the file URL, specify the number of segments, and provide the output file name as prompted.
4. **Monitor Progress**: Monitor the progress of the download with the provided progress bars.
5. **Completion**: Once the download is complete, the downloaded file will be available with the specified output file name.

## Additional Notes

- **Compatibility**: The binary executable (`dynamic_file_downloader`) is specifically built for Linux environments and may not work on other platforms.
- **Source Code**: The source code (`dynamic_file_downloader.py`) is provided for further customization or adaptation to different environments.

## Example

Suppose you want to download a large file from a URL `http://example.com/largefile.zip` with four segments and save it as `downloaded_file.zip`. You would execute the following command:

```bash
$ ./dynamic_file_downloader
```

You would then input:
- File URL: `http://example.com/largefile.zip`
- Number of Segments: `4`
- Output File Name: `downloaded_file.zip`

The downloader will then proceed to download the file, providing progress updates until completion.

---



