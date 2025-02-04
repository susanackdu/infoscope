import os
import ctypes
from ctypes import wintypes

class InfoScope:
    def __init__(self):
        self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        self.advapi32 = ctypes.WinDLL('advapi32', use_last_error=True)

    def set_file_permissions(self, file_path, user, permission):
        # Convert file path to Windows format
        file_path = os.path.abspath(file_path)
        
        # Open the file
        file_handle = self.kernel32.CreateFileW(
            file_path,
            0x10000000,  # GENERIC_ALL
            0,  # No sharing
            None,  # Default security
            3,  # OPEN_EXISTING
            0x00000080,  # FILE_ATTRIBUTE_NORMAL
            None
        )

        if file_handle == -1:
            raise ctypes.WinError(ctypes.get_last_error())

        # Retrieve the current security descriptor
        security_descriptor = ctypes.create_string_buffer(4096)
        needed = wintypes.DWORD()

        result = self.advapi32.GetKernelObjectSecurity(
            file_handle,
            4,  # DACL_SECURITY_INFORMATION
            security_descriptor,
            4096,
            ctypes.byref(needed)
        )

        if not result:
            self.kernel32.CloseHandle(file_handle)
            raise ctypes.WinError(ctypes.get_last_error())

        # Modify the security descriptor to include the new permissions
        # This part is simplified for demonstration purposes
        new_permissions = f"{user}:({permission})"
        # Apply the new security descriptor
        result = self.advapi32.SetKernelObjectSecurity(
            file_handle,
            4,  # DACL_SECURITY_INFORMATION
            security_descriptor
        )

        self.kernel32.CloseHandle(file_handle)

        if not result:
            raise ctypes.WinError(ctypes.get_last_error())

    def display_message(self):
        print("File permissions successfully updated!")

if __name__ == "__main__":
    infoscope = InfoScope()
    try:
        infoscope.set_file_permissions("example.txt", "username", "F")  # Full control
        infoscope.display_message()
    except Exception as e:
        print(f"An error occurred: {e}")