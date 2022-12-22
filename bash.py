import subprocess


class Bash:
    """ Run bash commands easily. github.com/rideee"""

    command = None
    result = None
    stdout = None
    stderr = None
    rc = None


    @classmethod
    def run(cls, cmd, capture_output=True, text=True, check=True):
        cls.command = cmd
        cls.result = subprocess.run(
            cmd.split(),
            capture_output=capture_output,
            text=text,
            check=check
        )
        cls.stdout = cls.result.stdout
        cls.stderr = cls.stderr
        cls.rc = cls.result.returncode
