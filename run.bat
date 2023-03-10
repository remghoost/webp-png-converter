@echo off

rem Check if the run_config.txt file exists
if exist ".\run_config.txt" (
  rem If the file exists, read the script name from it
  set /p scriptName=<".\run_config.txt"
  goto startScript
) else (
  rem If the file does not exist, install the requirements and prompt the user to select an option
  echo Installing requirements from requirements.txt...
  pip install -r requirements.txt
  echo Running main script...
  echo Select option:
  echo 1. Run default script (main.py)
  echo 2. Specify custom script name
  set /p scriptOption=
  if "%scriptOption%" == "1" (
    set scriptName=main.py
  ) else (
    if "%scriptOption%" == "2" (
      set /p scriptName=Enter script name:
    )
  )
  rem Write the script name to the run_config.txt file
  echo %scriptName% > ".\run_config.txt"
)

:startScript
rem Run the script specified by the user (or main.py if the user selected that option)
echo Running %scriptName%...
python %scriptName%
echo Done!
