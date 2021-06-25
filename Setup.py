from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

from pathlib import Path
import shutil
import os

build_root_dir = 'build'

class BuildExt(build_ext):
    def run(self):
        build_ext.run(self)

        build_dir = self.build_lib
        lib_dir   = build_root_dir + "/Lib"

        for path, subdirs, files in os.walk(lib_dir):
            for name in files:
                filename, file_extension = os.path.splitext(os.path.basename(name))

                srcPath = os.path.join(build_dir, filename+'.pyd')
                destPath = os.path.relpath(path, build_root_dir)

                removePath = os.path.join(destPath, filename+'.pyc')
                if os.path.exists(removePath):
                    os.remove(removePath)

                removePath = os.path.join(destPath, filename+'.py')
                if os.path.exists(removePath):
                    os.remove(removePath)

                shutil.copy(srcPath, destPath)

        if os.path.isdir(build_root_dir):
            shutil.rmtree(build_root_dir)

        if os.path.isdir('Out'):
            shutil.rmtree('Out')

        if os.path.exists('.Utility'):
            os.remove('.Utility')

        if os.path.exists('.Switch'):
            os.remove('.Switch')

        if os.path.exists('run.bat'):
            os.remove('run.bat')

setup(
    name = 'aec-function-tester',
    cmdclass = dict(
        build_ext = BuildExt
    ),
    ext_modules=cythonize(
        [
           Extension("Lib/MCU/.*",      ["Lib/MCU/*.py"]),
           Extension("Lib/DSP/.*",      ["Lib/DSP/*.py"]),
           Extension("Lib/Utility/.*",  ["Lib/Utility/*.py"]),
           Extension("Lib/Switch/.*",   ["Lib/Switch/*.py"]),
           Extension("Lib/USB/.*",      ["Lib/USB/*.py"]),
           Extension("Lib/GTP/.*",      ["Lib/GTP/*.py"]),
        ],
        build_dir = build_root_dir,
        compiler_directives=dict(
        always_allow_keywords=True
        )),
)
