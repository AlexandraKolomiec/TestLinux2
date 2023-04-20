import subprocess

path_dir = '/home/user/tst'
path_arch = '/home/user/arx1.7z'


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True,
                            stdout=subprocess.PIPE, encoding='utf 8')
    print(result)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
