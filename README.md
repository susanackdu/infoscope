# InfoScope

InfoScope is a Python-based utility designed to secure file access on Windows systems by setting advanced permissions and access controls. The program interacts with the Windows API to modify file permissions, ensuring that only authorized users have access to specific files.

## Features

- Modify file permissions using Windows API
- Set permissions for specific users
- Ensure secure access to sensitive files

## Requirements

- Windows OS
- Python 3.x
- Administrator privileges for modifying file permissions

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/InfoScope.git
   ```
2. Navigate to the project directory:
   ```bash
   cd InfoScope
   ```

## Usage

Run the `infoscope.py` script with the appropriate file path, username, and permission level. Modify the script to specify the user and permission level as needed.

```bash
python infoscope.py
```

### Example

Modify permissions for `example.txt` to give full control to a user:

```python
infoscope.set_file_permissions("example.txt", "username", "F")
```

## Permissions

- `F`: Full control
- `R`: Read
- `W`: Write
- `D`: Delete

## Note

- The current implementation serves as a basic demonstration of setting file permissions using the Windows API. It is important to handle security descriptors and access control lists (ACLs) carefully when dealing with production environments.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** Use this script at your own risk. The author is not responsible for any damage caused by the use or misuse of this script.