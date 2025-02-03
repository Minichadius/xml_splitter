import subprocess

# Команда для выполнения
command = [
    r"C:\Program Files\1cv8\8.3.24.1548\bin\1cv8.exe",  # Путь к 1cv8.exe
    "Config", 
    "/S", "Путь к серверной базе",  # Путь к серверной базе
    "/N", "Администратор",  # Имя пользователя
    "/ConfigurationRepositoryF", "Адрес базы",  # Путь к хранилищу конфигурации
    "/ConfigurationRepositoryN", "Имя пользователя",  # Имя репозитория конфигурации
    "/DumpConfigToFiles", r"Путь для выгрузки конфигурации",  # Путь для выгрузки конфигурации
    "-Format", "Hierarchical"  # Формат выгрузки
]

# Объединяем команду в строку
cmd_command = ' '.join(command)

# Запуск команды в новом консольном окне с автоматическим закрытием после завершения
subprocess.run(f'start /wait cmd /c "{cmd_command}"', shell=True)
