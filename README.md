# How to run

1. Clone or download this repo.
2. Open a terminal in the project folder.
3. Create a venv:

  On Windows:
    py -3.13 -m venv .venv
  On Linux/macOS:
    py3 -3.13 -m venv .venv
  
4. Activate the venv:
   
   On Windows:
     .venv\Scripts\activate
   On Linux/macOS:
     source .venv/bin/activate
   Note: if you're getting an error on Windows, do Set-ExecutionPolicy Unrestricted in PowerShell, and press A and enter.

   Now you should have a (.venv) prefix on the command line.

5. Install pygame:
  On Windows:
    pip install pygame
  On Linux/macOS:
    pip3 install pygame
6. Run it:
  On Windows:
    python main.py
  On Linux/macOS:
    python3 main.py
