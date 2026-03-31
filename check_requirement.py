import sys
import subprocess
import platform

REQUIRED_PACKAGES = {
    "cv2":"opencv-python",
    "pygame":"pygame",
    "pyttsx3":"pyttsx3",
    "pynput":"pynput",
}

PLATFORM_EXTRAS = {
    "win32":  ["pypiwin32"],
    "darwin": ["pyobjc"],
}


def install(package: str) -> bool:
    print(f"[INFO] Installation of '{package}'...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"[SUCCES] '{package}' installed.")
        return True
    else:
        print(f"[ERROR] installation of '{package}' :")
        print(f"    {result.stderr.strip()}")
        return False


def check_and_install_libraries() -> bool:
    print("[INFO] Checking for required libraries...")

    all_ok = True

    for import_name, package_name in REQUIRED_PACKAGES.items():
        try:
            __import__(import_name)
            print(f"[SUCCES] '{import_name}' already installed.")
        except ImportError:
            print(f"[ERROR] '{import_name}' is missing.")
            success = install(package_name)
            if not success:
                all_ok = False

    current_platform = sys.platform
    extras = PLATFORM_EXTRAS.get(current_platform, [])
    if extras:
        print(f"[INFO] Specific dependencies for '{platform.system()}' :")
        for package_name in extras:
            try:
                __import__(package_name.replace("-", "_"))
                print(f"[SUCCES] '{package_name}' already installed.")
            except ImportError:
                print(f"[INFO] '{package_name}' is missing.")
                success = install(package_name)
                if not success:
                    all_ok = False


    if all_ok:
        print("[SUCCES] All the bookshelves are ready...")
    else:
        print("[ERROR] Some installations failed. Check the errors listed above.")

    return all_ok