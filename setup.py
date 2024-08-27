import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]  # Replace "main.py" with your script's name

cx_Freeze.setup(
    name="LOL Tier1 startup",  # Your application's name
    version="0.1",  # Version number
    executables=executables,
)